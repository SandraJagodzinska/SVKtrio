from typing import List, Union, Dict, Set, Optional, Tuple
from pathlib import Path
from dataclasses import dataclass

from spacy import Language as SpacyPipeline
from spacy.tokens import Token as SpacyToken, Doc as SpacyDoc
import spacy

from pyJoules.energy_meter import measure_energy

from sklearn.metrics import classification_report, ConfusionMatrixDisplay, confusion_matrix
from matplotlib import pyplot as plt

@dataclass
class Token:
    form: str
    tag: str
    is_oov: bool


@dataclass
class Sentence:
    sent_id: str
    tokens: List[Token]


@dataclass
class Corpus:
    sentences: List[Sentence]


def read_conll(path: Path, vocabulaire: Optional[Set[str]] = None) -> Corpus:
	lst_cat = []
	sentences: List[Sentence] = []
	tokens: List[Token] = []
	sid = ""
	with open(path) as f :
		for line in f:
			line = line.strip()
			if line.startswith("# genre =" ):
				sid = line.split(" ")[-1]
				if sid not in lst_cat : 
					lst_cat.append(sid)
			if not line.startswith("#"):
				if line == "":
					sentences.append(Sentence(sent_id=sid, tokens=tokens))
					tokens = []
				else:
					fields = line.split("\t")
					form, tag = fields[1], fields[3]
					if not "-" in fields[0]:  # éviter les contractions type "du"
						if vocabulaire is None:
							is_oov = True
						else:
							is_oov = not form in vocabulaire
						tokens.append(Token(form, tag, is_oov))
	return lst_cat, Corpus(sentences)


def build_vocabulaire(corpus: Corpus) -> Set[str]:
    return {tok.form for sent in corpus.sentences for tok in sent.tokens}


def sentence_to_doc(sentence: Sentence, vocab) -> SpacyDoc:
    words = [tok.form for tok in sentence.tokens]
    return SpacyDoc(vocab, words=words)


def doc_to_sentence(doc: SpacyDoc, origin: Sentence) -> Sentence:
    tokens = []
    for tok, origin_token in zip(doc, origin.tokens):
        tag = tok.pos_ 
        if len(tag) == 0 :
            tag = tok.tag_
        tokens.append(Token(tok.text, tag, is_oov=origin_token.is_oov))
    return Sentence(origin.sent_id, tokens)

# @measure_energy
def tag_corpus_spacy(corpus: Corpus, model_spacy: SpacyPipeline) -> Corpus:
    sentences = []
    for sentence in corpus.sentences:
        doc = sentence_to_doc(sentence, model_spacy.vocab)
        doc = model_spacy(doc)
        sentences.append(doc_to_sentence(doc, sentence))
    return Corpus(sentences)


def compute_accuracy(corpus_gold: Corpus, corpus_test: Corpus, subcorpus: Optional[str] = None) -> Tuple[float, float]:
    nb_ok = 0
    nb_total = 0
    oov_ok = 0
    oov_total = 0
    for sentence_gold, sentence_test in zip(
        corpus_gold.sentences, corpus_test.sentences
    ):
        if subcorpus is None or subcorpus in sentence_gold.sent_id: 
            for token_gold, token_test in zip(sentence_gold.tokens, sentence_test.tokens):
                assert token_gold.form == token_test.form
                if token_gold.tag == token_test.tag:
                    nb_ok += 1
                nb_total += 1
                if token_gold.is_oov:
                    oov_total += 1
                    if token_gold.tag == token_test.tag:
                        oov_ok += 1
    
    return nb_ok / nb_total, oov_ok / oov_total
    
def reconstituer_le_text_pour_treetagger(corpus_gold: Corpus, output_file) :
	"""Cette fonction prend en argument un corpus gold obtenu depuis la lecture du fichier conll
	ensuite extrait les tokens de ce corpus pour les mettre dans le fichier qui va être annoté par Treetagger"""
	with open(output_file, "w") as f : 
		for sentence_gold in corpus_gold.sentences:
			for token_gold in sentence_gold.tokens:
				f.write(f"{token_gold.form}\n")

def annotation_treetagger_to_corpus(corpus: Corpus, annotation_file, tagSet_complex) :
	"""c'est une fonction qui prend en argument le corpus gold constitue à partir de conllu et remplace les étiquettes
	associés par le treetagger à chaque token et renvoie un nouveau corpus étiquetté"""
	sentences = []
	tokens = []
	i = 0
	lst_annotated = get_annotation(annotation_file, tagSet_complex)
# 	print(lst_annotated)
	for sentence in corpus.sentences:
		for token_origin in sentence.tokens:
			token_tag_annotated = lst_annotated[i]
			form_annotated, tag_annotated = token_tag_annotated[0], token_tag_annotated[1]
			#print(token_origin.form, "-->", token_origin.tag, "////", form_annotated, "-->", tag_annotated)
			i+=1
			tokens.append(Token(token_origin.form, tag_annotated, is_oov=token_origin.is_oov))
		sentence_form = Sentence(sentence.sent_id, tokens)
		sentences.append(sentence_form)
		tokens = []
	return Corpus(sentences)
			


def get_annotation(annotation_file, tagSet_complexe):
	"""C'est une fonction qui prend en entrée un fichier avec annotation de TreeTagger - un token-tag par ligne, 
	et le rassemble dans une liste de tuples (token, tag)"""
	lst_tuples = []
	with open(annotation_file, "r") as annotation : 
		for line in annotation : 
			line = line.strip()
			token, tag = line.split("\t")[0], line.split("\t")[1]
			if tagSet_complexe: 
# 				print("complexe tag", token, tag)
				tag = dico_étiquettes_treeTagger(tag)
# 				print("nouveau tag", tag)
			pair = (token,tag)
			lst_tuples.append(pair)
	return lst_tuples
	
def dico_étiquettes_treeTagger(tag_complexe) : 
	"""c'est une fonction qui prend tag d'annotation de TreeTagger pré-entrainé et renvoie une étiquette unifié avec notre tagset"""
	étiquettes = {"subst" : "NOUN",
					"depr" : "NOUN",
					"num" : "NUM",
					"numcol" : "NUM",
					"dig" : "NUM",
					"adj" : "ADJ",
					"adja" : "ADJ",
					"adjp" : "ADJ",
					"adjc" : "ADJ",
					"adv" : "ADV",
					"part" : "PART",
					"ppron12" : "PRON",
					"ppron3" : "PRON",
					"siebie" : "VERB",
					"fin" : "VERB",
					"bedzie" : "VERB",
					"aglt" : "VERB",
					"praet" : "VERB",
					"impt" : "VERB",
					"imps" : "VERB",
					"inf" : "VERB",
					"pcon" : "VERB",
					"pant" : "VERB",
					"ger" : "VERB",
					"pact" : "VERB",
					"ppas" : "VERB",
					"winien" : "VERB",
					"pred" : "VERB",
					"prep" : "ADP",
					"conj" : "CONJ",
					"comp" : "CONJ",
					"qub" : "PART",
					"brev" : "X", #L'étiquette qui est pas traduisable
					"burk" : "INTJ", #mais pas sur à revoir
					"interj" : "INTJ",
					"interp" : "PUNCT",
					"xxx" : "X", #alien
					"xxs" : "X", #alien
					"xxp" : "X", #alien
					"ign" : "X" #ignoré
	}
	tag_complexe = tag_complexe.split(":")[0]
	if tag_complexe in étiquettes : 
		tag_propre = étiquettes[tag_complexe]
	else:
		tag_propre = "X"
	return tag_propre
			

def print_report(corpus_gold: Corpus, corpus_test: Corpus):
    ref = [tok.tag for sent in corpus_test.sentences for tok in sent.tokens]
    test = [tok.tag for sent in corpus_gold.sentences for tok in sent.tokens]
    print(classification_report(ref, test))

def matrix(corpus_gold: Corpus, corpus_test: Corpus):
    ref = [tok.tag for sent in corpus_test.sentences for tok in sent.tokens]
    test = [tok.tag for sent in corpus_gold.sentences for tok in sent.tokens]
    labels = sorted(set(ref + test))  
    cm = confusion_matrix(ref, test, labels=labels)
    
    # Plot the confusion matrix
    cm_display = ConfusionMatrixDisplay(cm, display_labels=labels)
    cm_display.plot(cmap=plt.cm.PuRd, values_format=".2f") 
    plt.show()  # Display the plot

    return cm_display

def main():
    lst_cat_train, corpus_train = read_conll("../corpus-lfg/pl_lfg-ud-train.conllu")
    vocab_train = build_vocabulaire(corpus_train)
    lst_cat_gold, corpus_gold = read_conll("../corpus-lfg/pl_lfg-ud-test.conllu", vocabulaire=vocab_train)
    # for model_name in ("../train-spacy/spacy_model2/model-best", "pl_core_news_sm", "pl_core_news_md", "pl_core_news_lg"):
#         print(model_name)
#         model_spacy = spacy.load(model_name)
#         lst_cat_gold, corpus_gold = read_conll("../corpus-lfg/pl_lfg-ud-test.conllu", vocabulaire=vocab_train)
#         corpus_test = tag_corpus_spacy(corpus_gold, model_spacy)
#         print(model_name)
#         print(compute_accuracy(corpus_gold, corpus_test))
#         for subcorpus in lst_cat_gold:
#             print(subcorpus)
#             print(compute_accuracy(corpus_gold, corpus_test, subcorpus))
#         print_report(corpus_gold, corpus_test)
    reconstituer_le_text_pour_treetagger(corpus_gold, "../text4TT.txt")
    corpus_test_treeTagger_notre = annotation_treetagger_to_corpus(corpus_gold, "../annotation_treeTagger.txt", False)
    corpus_test_treeTagger = annotation_treetagger_to_corpus(corpus_gold, "../annotation_treeTagger_original.txt", True)
    print("TREE-TAGGER RESULTS ENTRAINE")
    for subcorpus in lst_cat_gold:
        print(subcorpus)
        print(compute_accuracy(corpus_gold, corpus_test_treeTagger_notre, subcorpus))
    print_report(corpus_gold, corpus_test_treeTagger_notre)
    print("TREE-TAGGER RESULTS ORIGINAL")
    for subcorpus in lst_cat_gold:
        print(subcorpus)
        print(compute_accuracy(corpus_gold, corpus_test_treeTagger, subcorpus))
    print_report(corpus_gold, corpus_test_treeTagger)

    matrix(corpus_gold, corpus_test)


if __name__ == "__main__":
    main()
