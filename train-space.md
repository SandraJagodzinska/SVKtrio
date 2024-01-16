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

```python
train-spacy/spacy_model2/model-best
news
(0.9516865776528461, 0.8772357723577235)
fiction
(0.9430827438723475, 0.8580952380952381)
(media)
(0.9384615384615385, 0.8571428571428571)
social
(0.9595959595959596, 0.8823529411764706)
(conversational)
(0.9229122055674518, 0.7045454545454546)
nonfiction
(0.9266375545851528, 0.8427947598253275)
(prepared)
(0.9680851063829787, 0.8285714285714286)
legal
(1.0, 1.0)
blog
(0.9565217391304348, 0.9259259259259259)
academic
(0.9090909090909091, 0.6666666666666666)

              precision    recall  f1-score   support

         ADJ       0.91      0.90      0.91       830
         ADP       0.97      0.99      0.98      1097
         ADV       0.90      0.95      0.93       589
         AUX       0.92      0.56      0.69       429
       CCONJ       0.89      0.99      0.94       354
         DET       0.95      0.90      0.92       324
        INTJ       0.50      0.33      0.40         6
        NOUN       0.92      0.94      0.93      2457
         NUM       0.94      0.91      0.93        90
        PART       0.97      0.95      0.96       597
        PRON       0.97      0.98      0.98       986
       PROPN       0.89      0.86      0.88       470
       PUNCT       1.00      1.00      1.00      2555
       SCONJ       0.92      0.99      0.96       141
        VERB       0.95      0.96      0.96      2187

    accuracy                           0.95     13112
   macro avg       0.91      0.88      0.89     13112
weighted avg       0.95      0.95      0.95     13112

pl_core_news_sm
news
(0.9567814476458187, 0.9219512195121952)
fiction
(0.9416022372100674, 0.9057142857142857)
(media)
(0.9384615384615385, 1.0)
social
(0.9528619528619529, 0.9607843137254902)
(conversational)
(0.9357601713062098, 0.8409090909090909)
nonfiction
(0.9362445414847161, 0.9170305676855895)
(prepared)
(0.976063829787234, 0.9142857142857143)
legal
(1.0, 1.0)
blog
(0.9565217391304348, 0.8888888888888888)
academic
(0.9090909090909091, 1.0)

              precision    recall  f1-score   support

         ADJ       0.95      0.96      0.95       830
         ADP       0.99      0.99      0.99      1097
         ADV       0.93      0.93      0.93       589
         AUX       0.79      0.53      0.64       429
       CCONJ       0.95      0.95      0.95       354
         DET       0.97      0.95      0.96       324
        INTJ       0.40      0.33      0.36         6
        NOUN       0.94      0.96      0.95      2457
         NUM       0.99      0.94      0.97        90
        PART       0.93      0.93      0.93       597
        PRON       0.98      0.99      0.98       986
       PROPN       0.81      0.87      0.84       470
       PUNCT       1.00      1.00      1.00      2555
       SCONJ       0.87      0.99      0.92       141
        VERB       0.96      0.94      0.95      2187
           X       0.00      0.00      0.00         0

    accuracy                           0.95     13112
   macro avg       0.84      0.83      0.83     13112
weighted avg       0.95      0.95      0.95     13112

pl_core_news_md
news
(0.9634574841883345, 0.9390243902439024)
fiction
(0.9485112683007073, 0.9352380952380952)
(media)
(0.9384615384615385, 1.0)
social
(0.9663299663299664, 0.9803921568627451)
(conversational)
(0.9357601713062098, 0.8636363636363636)
nonfiction
(0.9423580786026201, 0.9170305676855895)
(prepared)
(0.976063829787234, 1.0)
legal
(1.0, 1.0)
blog
(0.9304347826086956, 0.8518518518518519)
academic
(0.7272727272727273, 0.6666666666666666)

              precision    recall  f1-score   support

         ADJ       0.94      0.96      0.95       830
         ADP       0.99      0.99      0.99      1097
         ADV       0.95      0.92      0.93       589
         AUX       0.79      0.55      0.64       429
       CCONJ       0.96      0.95      0.96       354
         DET       0.96      0.95      0.96       324
        INTJ       0.75      0.50      0.60         6
        NOUN       0.96      0.97      0.97      2457
         NUM       0.98      0.99      0.98        90
        PART       0.93      0.95      0.94       597
        PRON       0.96      0.99      0.97       986
       PROPN       0.87      0.90      0.89       470
       PUNCT       1.00      1.00      1.00      2555
       SCONJ       0.87      0.99      0.92       141
        VERB       0.98      0.96      0.97      2187
           X       0.00      0.00      0.00         0

    accuracy                           0.96     13112
   macro avg       0.87      0.85      0.85     13112
weighted avg       0.96      0.96      0.96     13112

pl_core_news_lg
news
(0.9660927617709065, 0.9479674796747968)
fiction
(0.9506497779240006, 0.9361904761904762)
(media)
(0.9384615384615385, 1.0)
social
(0.9562289562289562, 0.9803921568627451)
(conversational)
(0.9400428265524625, 0.8863636363636364)
nonfiction
(0.9475982532751092, 0.9301310043668122)
(prepared)
(0.9787234042553191, 0.9714285714285714)
legal
(1.0, 1.0)
blog
(0.9478260869565217, 0.8518518518518519)
academic
(0.7272727272727273, 0.6666666666666666)

              precision    recall  f1-score   support

         ADJ       0.95      0.97      0.96       830
         ADP       0.99      0.99      0.99      1097
         ADV       0.94      0.93      0.94       589
         AUX       0.78      0.54      0.64       429
       CCONJ       0.97      0.97      0.97       354
         DET       0.97      0.96      0.96       324
        INTJ       0.40      0.33      0.36         6
        NOUN       0.96      0.97      0.97      2457
         NUM       0.98      0.98      0.98        90
        PART       0.95      0.94      0.94       597
        PRON       0.98      0.99      0.98       986
       PROPN       0.83      0.91      0.87       470
       PUNCT       1.00      1.00      1.00      2555
       SCONJ       0.87      0.99      0.93       141
        VERB       0.98      0.96      0.97      2187
           X       0.00      0.00      0.00         0

    accuracy                           0.96     13112
   macro avg       0.85      0.84      0.84     13112
weighted avg       0.96      0.96      0.96     13112
```

## Matrices de confusion

