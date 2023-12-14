def conlluToAnnotated(conllufile, outputfile) : 
    with open(conllufile, "r") as cf, open(outputfile, "w") as of : 
        for line in cf : 
            if line != "" and line != "\n":
                if not line.startswith("#") : 
                    token = line.split("\t")[1]
                    tag = line.split("\t")[3]
                    of.write(token + "\t" + tag + "\n")

#print(conlluToAnnotated("../corpus-lfg/pl_lfg-ud-train.conllu", "../train-treetagger/pl_lfg-ud-train-treetagger.tsv"))