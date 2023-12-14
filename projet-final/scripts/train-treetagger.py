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

path = "../corpus-lfg/pl_lfg-ud-train.conllu"
conllufile = readConll(path)
tags = conlluToTag(conllufile)


with open("../train-treetagger/tags.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(tags))

def conlluToAnnotated(conllufile, outputfile) : 
    with open(outputfile, "w") as of : 
        for line in conllufile : 
            if line != "" and line != "\n":
                if not line.startswith("#") : 
                    token = line.split("\t")[1]
                    tag = line.split("\t")[3]
                    of.write(token + "\t" + tag + "\n")

#print(conlluToAnnotated("../corpus-lfg/pl_lfg-ud-train.conllu", "../train-treetagger/pl_lfg-ud-train-treetagger.tsv"))
