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
    """
    lexicon = {} # stocker le lexique dans un dictionnaire
    # parcourir le fichier conllu
    for line in conllufile:
        # ignorer les commentaires et les lignes vides
        if not line.startswith("#") or line.strip() == "":
            line = line.split("\t")
            if len(line) >= 4:  # verifie qu'on aura les éléments nécessaires selon les colonnes de conllu
                token = line[1]
                pos = line[3]
                entry = (token, pos) # tuple pour chaque entrée
                # ajouter une seule occurence de tuple au lexique si elle n'y est pas déjà
                if token in lexicon:
                    lexicon[token].add(entry)
                else:
                    lexicon[token] = {entry}
    # écrire le lexique en sortie dans un fichier tsv
    with open(output_path, 'w', encoding='utf-8', newline='') as tsvfile:
        for token, entries in lexicon.items():
            # pour chaque token écrire ses POS tags, un token peut avoir plusieurs POS tags dans une même ligne
            for entry in entries:
                tsvfile.write(f"{entry[0]}\t{entry[1]}\t")
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
	print(conlluToLexicon(fichier_conllu, "../train-treetagger/lexicon.tsv"))
	print(conlluToAnnotated(fichier_conllu, "../train-treetagger/annotated.tsv"))
	with open("../train-treetagger/tags.txt", "w", encoding="utf-8") as f:
		f.write(" ".join(tags))


