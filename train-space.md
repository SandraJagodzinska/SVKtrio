# Ré-entrainement de Spacy - (travail individuel pendant les TP)

/!\ Se positionner dans le répértoire parent /!\

## Corpus Polonais

Corpus conllu pl-lfg_ud (train, dev et test)

## Conversion du corpus conllu en spacy

`python3 -m spacy convert corpus-lfg-conllu/pl_lfg-ud-train.conllu train-spacy/corpus-lfg-spacy`

`python3 -m spacy convert corpus-lfg-conllu/pl_lfg-ud-dev.conllu train-spacy/corpus-lfg-spacy`

`python3 -m spacy convert corpus-lfg-conllu/pl_lfg-ud-test.conllu train-spacy/corpus-lfg-spacy`

## 1.1. Configuration de la pipeline : Morphologizer - Offiency

`python3 -m spacy init fill-config ./train-spacy/config-spacy/base_config.cfg .train-spacy/config-spacy`

### Entrainement

`python3 -m spacy train ./train-spacy/config-spacy/config.cfg --output ./train-spacy/spacy_model2/ --paths.train ./train-spacy/corpus-lfg-spacy/pl_lfg-ud-train.spacy --paths.dev ./train-spacy/corpus-lfg-spacy/pl_lfg-ud-dev.spacy`

### Résultats de l'entrainement

```python
✔ Created output directory: train-spacy/spacy_model2
ℹ Saving to output directory: train-spacy/spacy_model2
ℹ Using CPU

======================= Initializing pipeline ======================
✔ Initialized pipeline
======================== Training pipeline ==========================
ℹ Pipeline: ['tok2vec', 'morphologizer']
ℹ Initial learn rate: 0.001
E    #       LOSS TOK2VEC  LOSS MORPH...  POS_ACC  MORPH_ACC  SCORE
---  ------  ------------  -------------  -------  ---------  ------
  0       0          0.00          89.26    35.94      23.52    0.30
  0     200        265.81       12244.41    76.92      56.51    0.67
  0     400        573.08       10735.36    86.92      69.39    0.78
  ...
 28    4400        955.57        2663.25    94.63      84.88    0.90
 30    4600        938.47        2531.77    94.67      84.88    0.90
 32    4800        927.07        2457.63    94.61      84.76    0.90
✔ Saved pipeline to output directory
train-spacy/spacy_model2/model-last
```

## Évaluation

`python3 scripts/train-spacy.py`

### Résultats de l'évaluation



## Matrices de confusion

