<p align="center">
    <img alt="42-lyon" src="https://user-images.githubusercontent.com/45235527/106354618-6ec65a00-62f3-11eb-8688-ba9e0f4e77de.jpg" />
</p>

# dslr

<!-- <img alt="Note" src="https://user-images.githubusercontent.com/45235527/104627073-dc894980-5696-11eb-999d-e53798ea9ae4.png" width="250" height="200" /> -->

### <strong>Description</strong>

Sujet proposé par l'association 42AI. Découvrez la Data Science à travers ce projet dans la reconstitution du Choixpeau Magique de Poudlard ! Attention, ceci n'est pas un sujet sur les appareils photos.

> *Project en collaboration avec <a href="https://github.com/nemu69">Nemuel Page Léonie</a> (<a href="https://profile.intra.42.fr/users/nepage-l">nepage-l</a>).*

# Partie Obligatoire 

## V.1 Data Analysis

Avant toutes choses, jetez un oeil aux données disponibles. Regardez sous quel formatelles sont enregistrées, s’il y a divers types de données, les différentes fourchettes, etc. Il est important de se faire une idée de votre matière première avant de commencer à travailler. Plus vous travaillerez sur des données et plus vous développerez une intuition sur comment vous allez pouvoir vous en servir.

Dans cette partie, le professeur McGonagall vous demande de produire un programme nommé describe.[extension]. Ce programme prendra un dataset en paramètre. Il devra ni plus ni moins afficher les informations sur toutes les features numériques comme l’exemple qui suit :

![exemple 1](https://user-images.githubusercontent.com/45235527/140956374-bd39ca97-3633-44b2-b493-32e194b6c4dd.PNG)

## V.2  Data Visualization

La visualisation des données est un outil puissant pour le datascientist. Cela vous permet d’acquérir une intuition sur comment les données sont connectées les unes aux autres. Visualiser vos données vous permet aussi de déceler plusieurs défauts.

Dans cette section, il vous est demandé de répondre à une question en créant un script pour chacune des questions qui affichera une visualisation particulière. Il n’y a pas forcèment une seule réponse valable à la question.

## V.2.1  Histogram

Faites un script nommé histogram.[extension] qui affiche un histogram répondant à la question suivante :

Quel cours de Poudlard a une répartition des notes homogènes entre les quatres maisons ?

## V.2.2  Scatter plot

Faites un script nommé scatter_plot.[extension] qui affiche un scatter plot répondant à la question suivante :

Quelles sont les deux features qui sont semblables ?

## V.2.3  Pair plot

Faites un script nommé pair_plot.[extension] qui affiche un pair plot ou scatter plot matrix (selon la librairie graphique que vous utiliserez).

À partir de cette visualisation, quelles caractéristiques allez-vous utiliser pour entraîner votre prochaine régression logistique ?

## V.3  Logistic Regression

Vous arrivez à la dernière partie : coder votre Choixpeau magique. Pour ce faire, il vous est demandé de réaliser un multi-classifieur en utilisant une régression logistique en one-vs-all.

Vous devrez rendre deux programmes :

- un premier qui va train vos modèles, il se nomme logreg_train.[extension]. Il prend en paramètre dataset_train.csv. Pour la partie obligatoire, vous devez utilisez la technique du gradient descent pour minimiser l’erreur. Le programme génère un fichier contenant les poids qui seront réutilisés pour la prédiction.

- un second qui se nomme logreg_predict.[extension]. Il prend en paramètre dataset_test.csv et un fichier contenant les poids entraînés au préalable. Afin d’évaluer les performances de votre classifieur ce second programme devra génèrer un fichier de prédictions houses.csv formatté strictement de la manière suivante:

![exemple 2](https://user-images.githubusercontent.com/45235527/140956376-a3c95194-5fc6-45c6-a6c3-bb0c549b71b7.PNG)

# Requirements

- python3.10 min
- lib:
    - pip3 install pandas
    - pip3 install matplotlib

# Results

 `python ./histogram.py DATA`

<img alt="histo" src="https://github.com/AcensJJ/dslr/blob/main/img/histogram.png">

`python ./scatter_plot.py DATA`
 
<img alt="scatter" src="https://github.com/AcensJJ/dslr/blob/main/img/all_scatter_plot.png">

<img alt="scatter line" src="https://github.com/AcensJJ/dslr/blob/main/img/result_scatter_plot.png">

`python ./pair_plot.py DATA`

<img alt="pair" src="https://github.com/AcensJJ/dslr/blob/main/img/pair_plot.png">
