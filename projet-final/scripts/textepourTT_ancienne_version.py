import re

with open('pl_lfg-ud-test.conllu', 'r') as input_file:
    with open('texte_pourTTancienne_version.txt', 'w') as output_file:
        result = ""
        for line in input_file:
            line = line.strip()
            if line.startswith("# text"):
                line = re.sub(r'# text = ', '', line)
                #print(line)
                result += line + ' ' # car on ne veut pas de passage à la ligne entre les différents textes du corpus
        output_file.write(result)

