# titanic-ml-pipeline

## Objectif
Ce projet prédit si un passager du Titanic a survécu ou non, à partir de quatre 
caractéristiques : sa classe (Pclass), son sexe, son âge et la taille de sa famille 
à bord (FamilySize).
## Dataset
Les données proviennent du dataset Titanic classique, chargé depuis un fichier CSV 
en ligne. Il contient 891 passagers avec des colonnes comme l'âge, le sexe, la classe, 
le port d'embarquement, le tarif du billet, et la variable cible Survived (0 = décédé, 
1 = survécu).
## Méthodologie
1. Chargement des données
2. Nettoyage des données (valeurs manquantes, doublons)
3. Feature engineering (FamilySize, Title)
4. Visualisation des données
5. Encodage des variables catégorielles
6. Entraînement et comparaison de deux modèles (Logistic Regression, Random Forest)
7. ## Résultats
| Modèle | Accuracy |
|---|---|
| Logistic Regression (baseline) | 0.80 |
| Random Forest | 0.82 |

Le Random Forest obtient une meilleure accuracy que la régression logistique, 
ce qui est cohérent : en combinant plusieurs arbres de décision, il capture 
mieux les interactions complexes entre les variables.
## Utilisation
1. Cloner le dépôt : `git clone https://github.com/kaneserignembacke260-beep/titanic-ml-pipeline.git`
2. Ouvrir un notebook dans Google Colab ou Jupyter
3. Exécuter les cellules dans l'ordre
tu peux tester par ici :https://titanic-survie-serigne.streamlit.app/
