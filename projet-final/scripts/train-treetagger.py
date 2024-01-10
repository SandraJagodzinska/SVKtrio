#usr/bin/python3
# -*- coding: utf-8 -*-

def readConll(path):
    """
    Lit un fichier CoNLL-U et retourne son contenu sous forme de liste de lignes.

    Args:
        path (str): Le chemin du fichier CoNLL-U.

    Returns:
        list: Une liste de lignes du fichier CoNLL-U.
    """
    with open(path, "r", encoding="utf-8") as f: 
        conllufile = f.readlines()
    return conllufile

def conlluToLexicon(conllufile, output_path):
    """
    Prend un fichier conllu et donne un lexique dans un fichier tsv
    le lexicon a la forme : tokenX POSTokenX1 lemmaTokenX1 POSTokenX2 lemmaTokenX2
    """
    lexicon = {} # stocker le lexique dans un dictionnaire
    # parcourir le fichier conllu
    for line in conllufile:
        # ignorer les commentaires et les lignes vides
        if not line.startswith("#") or line.strip() == "":
            line = line.split("\t")
            if len(line) >= 4:  # verifie qu'on aura les éléments nécessaires selon les colonnes de conllu
                token = line[1]
                lemma = line[2]
                pos = line[3]
                entry = {pos : lemma} # liste pour chaque entrée
                # ajouter une seule occurence de liste au lexique si elle n'y est pas déjà
                if token not in lexicon:
                    lexicon[token] = entry
                else:
                    if pos not in lexicon[token] : 
                        lexicon[token][pos] = lemma
    print(lexicon["Stanisława"])
    print(lexicon["wczoraj"])
    print(lexicon["temu"])
    # écrire le lexique en sortie dans un fichier tsv
    with open(output_path, 'w', encoding='utf-8', newline='') as tsvfile:
        for token, entries in lexicon.items():
            # pour chaque token écrire ses POS tags et lemmes, un token peut avoir plusieurs entrées dans une même ligne
            tsvfile.write(f"{token}\t")
            if len(entries) > 1 :
            	for i in range(len(entries)-1):
            		lst = list(entries.items())
            		pos, lemma = lst[i]
            		tsvfile.write(f"{pos} {lemma} ")
            	pos, lemma = lst[-1]
            	tsvfile.write(f"{pos} {lemma}")
            else : 
            	pos, lemma = list(entries.items())[0]
            	tsvfile.write(f"{pos} {lemma}")
            tsvfile.write('\n') # sauter une ligne entre chaque entrée

# Tester
#inputconllu = readConll("corpus_pl-ud/corpus-lfg/pl_lfg-ud-train.conllu")
#lexicon = conlluToLexicon(inputconllu, "../train-treetagger/lexique_pl_lfg-ud-train-treetagger.tsv")

def conlluToTag(conllufile):
    """
    Extrait les éléments de la colonne 4 (index 3) de chaque ligne du fichier CoNLL-U.

    Args:
        conllufile (list): Une liste de lignes du fichier CoNLL-U.

    Returns:
        list: Une liste des tags extraits de la colonne 4.
    """
    tags = []
    for line in conllufile:
        if line.startswith("#"): # Si la ligne commence par un # (commentaire) on l'ignore
            continue
        else:
            columns = line.split("\t") # Sépare les colonnes par une tabulation
            if len(columns) >= 4: # Si la ligne contient au moins 4 colonnes
                if columns[3] not in tags: # Si le tag n'est pas déjà dans la liste
                    tags.append(columns[3]) # Ajoute le tag à la liste
    return tags

# path = "../corpus-lfg/pl_lfg-ud-train.conllu"
# conllufile = readConll(path)
# 


def conlluToAnnotated(conllufile, outputfile) : 
	"""
	Prend un fichier connllu et rend un fichier token - tag ligne par ligne
	"""
	with open(outputfile, "w") as of : 
		for line in conllufile : 
			if line != "" and line != "\n":
				if not line.startswith("#") : 
					token = line.split("\t")[1]
					tag = line.split("\t")[3]
					of.write(token + "\t" + tag + "\n")

if __name__ == "__main__" : 
	fichier_conllu = readConll("../corpus-lfg/pl_lfg-ud-train.conllu")
	tags = conlluToTag(fichier_conllu)
	print(conlluToLexicon(fichier_conllu, "../train-treetagger/lexicon.txt"))
	print(conlluToAnnotated(fichier_conllu, "../train-treetagger/annotated.tsv"))
	with open("../train-treetagger/tags.txt", "w", encoding="utf-8") as f:
		f.write(" ".join(tags))


