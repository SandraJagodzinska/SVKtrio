# Re-entrainement de Treetagger - (travail en groupe)

Pour se faire, nous avons suivie le guide su git : `https://gite.lirmm.fr/advanse/sentiment-analysis-webpage/-/tree/master/resources_on_server/TreeTagger` 


/!\ Se positionner dans le répértoire parent du projet /!\

## Corpus Polonais (même que spacy)

Corpus conllu pl-lfg_ud (train, dev et test)

## Installation de treetagger

`https://www.cis.uni-muenchen.de/~schmid/tools/TreeTagger/`

## Entrainement

Pour entrainer treetagger nous avons besoin de trois fichiers

### Fichier 1 : lexicon.txt

Construire un lexicon (mots formes + tag)

```python
dictionnaire : {
            "Token1" : [("Token", TAG)("Token",TAG)],
			"Token2" : [("Token2", TAG),("Token2",TAG)],
            ...
            }
```

### Fichier 2 : tags.txt

À partir d'un des corpus UD récupére tous les tags :

```python
	La \t a \t PRON \t la \t DET
```

### Fichier 3 : annotated.txt

Extraite tous les tokens du corpus avec leurs étiquettes :

```python
		Pierre \t NP
		a \t V
		la \t DET
```

## Entrainement

Lancement de l'entrainement avec la commande : `bin/train-tree-tagger -st PUNCT train-treetagger/lexicon.txt train-treetagger/tags.txt train-treetagger/annotated.txt train-treetagger/model`

(-st PUNCT' permet d'unifier avec spacy)

### Résultats

```python
569	    dig	            569
lat	    subst:pl:gen:m3	rok
temu	prep:acc	    temu
spalono	imps:perf	    spalić
na	    prep:loc	    na
stosie	subst:sg:loc:m3	stos
Joannę	subst:sg:acc:f	Joanna
D'Arc	subst:sg:nom:f	<unknown>
.	interp:sent	.
6	dig	6
```

### Observations

- Cas des NP : les mêmes formes mais pas les même lemmes.
- Tokenisation
  - Spacy :
  ```python
  [('To', 'AUX'), ('jest', 'AUX'), ('11', 'ADJ'), ('-', 'ADJ'), ('letnia', 'ADJ'), ('serdako', 'ADJ'), ('-', 'PUNCT'), ('sukienka', 'NOUN'), ('na', 'ADP'), ('ul', 'X'), ('.', 'PUNCT'), ('czerstwej', 'ADJ')]
  ```
  - Treetagger :
  ```python
  11-letnia ADJ
  serdako-sukienka NOUN
  Ul. NOUN
  ```

### Solutions

Calculer la F-mesure au lieu de l'accuracy

## Test
Récupérer le texte de test depuis pl_lfg-ud --> on s'est trompé, le fichier ne devait pas être un bloc de texte mais de tokens (1 par ligne).

**Altérnative :** récupérer la tokenization de spacy afin d'éviter les potentielles incohérences.
PS : le but n'est pas l'évaluation des tokens.

`bin/tree-tagger train-treetagger/model-name train-treetagger/text4TT.txt train-treetagger/annotation_treetagger.txt -token`

## Évaluation

## Matrices de confusion
### Tree-Tagger-polonais
![Matrice Tree-Tagger-polonais](projet-final/train-treetagger/tt_pl_original.png "Matrice Tree-Tagger-polonais")

### Tree-Tagger-polonais-entrainé
![Matrice Tree-Tagger-polonais-entrainé](projet-final/train-treetagger/tt_pl_entraine.png "Matrice Tree-Tagger-polonais-entrainé")

