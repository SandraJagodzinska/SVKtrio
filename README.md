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

### **Évaluation de l'outil spacy**

### Étape 1 : Préparation du corpus pour l'

- [ ] Télécharger le corpus conllu (train, dev et test).
- [ ] Convertir le corpus en corpus d'entrainement.

### Étape 2 :

## Étape 2 : configuration de la pipeline

- [ ] Configurer un modéle pour le polonais, uniquement un tagger et optimisé vitesse 'efficiency'.
- [ ] Télécharger le base_config.cfg.
- [ ] Télécharger la commande : `python -m spacy init fill-config base_config.cfg config.cfg`.
- [ ] Modifier base.cfg (si besoin).

## Étape 3 : entrainement

- [ ] Entrainer le modèle sur le corpus d'entrainement.

  > Commande : `python3 -m spacy train config/config.cfg --output ./spacy_model2/ --paths.train corpus/CORPUS/CORPUS-train.spacy --paths.dev corpus/CORPUS/CORPUS-dev.spacy`

> Résultats :

## Étape 4 : évaluation

- [ ] Évaluer le modèle sur le corpus de test.

> Résultats :
