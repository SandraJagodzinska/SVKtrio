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


