# TALA540A - 2023/2024

Cet ensemble Git assure le suivi et la bonne marche du projet TALA540.

## INFORMATIONS UTILES

### Groupe : SVKtrio

Sandra, Valentina, Kenza.

### Langue

Ce projet traitera principalement du polonais.

### Outils à évaluer

L'outil spacy VS l'outil treetager et polyglot si le temps le permet.

### Données

- Pour l'évaluation de SpaCy, nous utiliserons le corpus annoté de la langue polonaise disponible sur [Universal Dependencies](https://universaldependencies.org,), téléchargeable depuis [github](https://github.com/UniversalDependencies/UD_Polish-PDB/).
- Pour l'évaluation de Treetagger, nous utiliserons le corpus annoté de la langue polonaise disponible sur ...

## DÉROULEMENT DU PROJET

## 1. **Évaluation de l'outil spacy**

### Position

Se positionner dans le dossier projet-eval afin de tester les scripts.

### Étape 1 : Préparation du corpus

- [x] Télécharger le corpus conllu (train, dev et test). --> corpus pl-lfg_ud
- [x] Convertir le corpus en corpus d'entrainement.

### Étape 2 : configuration de la pipeline

- [x] Configurer un modéle pour le polonais, morphologizer et optimisé vitesse 'efficiency'. (tagger ne fonctionne pas trés bien)
- [x] Télécharger le base_config.cfg.
- [x] Créer le fichier config.cfg :

> Commande :

`python3 -m spacy init fill-config config-pl/base_config.cfg config-pl/config.cfg`.

- [ ] Modifier base.cfg (si besoin).

### Étape 3 : entrainement

- [x] Transformation du corpus conllu en corpus d'entrainement spacy.

> Commandes :

`python3 -m spacy convert corpus_pl-ud/corpus-lfg/pl_lfg-ud-train.conllu corpus_pl-ud/corpus-ent`

`python3 -m spacy convert corpus_pl-ud/corpus-lfg/pl_lfg-ud-dev.conllu corpus_pl-ud/corpus-ent`

`python3 -m spacy convert corpus_pl-ud/corpus-lfg/pl_lfg-ud-test.conllu corpus_pl-ud/corpus-ent`

- [ ] Entrainer le modèle sur le corpus d'entrainement.

> Commande :

`python3 -m spacy train ./config-pl/config.cfg --output ./spacy_model2/ --paths.train ./corpus_pl-ud/corpus-ent/pl_lfg-ud-train.spacy --paths.dev ./corpus_pl-ud/corpus-ent/pl_lfg-ud-dev.spacy`

> Résultats :

## Étape 4 : évaluation

- [ ] Évaluer le modèle sur le corpus de test.

> Commande :
> `python3 scripts/evaluation.py`

> Résultats :
