<p align="center">
    <img alt="42-lyon" src="https://user-images.githubusercontent.com/45235527/106354618-6ec65a00-62f3-11eb-8688-ba9e0f4e77de.jpg" />
</p>

# dslr

<!-- <img alt="Note" src="https://user-images.githubusercontent.com/45235527/104627073-dc894980-5696-11eb-999d-e53798ea9ae4.png" width="250" height="200" /> -->

### <strong>Description</strong>

Subject created by the 42AI association. Discover Data Science in the projects where you re-constitute Poudlard’s Sorting Hat. Warning: this is not a subject on cameras.

> *Project en collaboration avec <a href="https://github.com/AcensJJ">Jean Jacques Acens</a> (<a href="https://profile.intra.42.fr/users/jacens">jacens</a>).*

# Mandatory part 

## V.1 Data Analysis

First of all, take a look at the available data. look in what format it is presented, if there are various types of data, the different ranges, and so on.
It is important to make an idea of your raw material before starting. The more you work on data - the more you develop an intuition about how you will be able to use it.

In this part, Professor McGonagall asks you to produce a program called describe.[extension].
This program will take a dataset as a parameter. All it has to do is to display information for all numerical features like in the example:

![exemple 1](https://user-images.githubusercontent.com/45235527/140956374-bd39ca97-3633-44b2-b493-32e194b6c4dd.PNG)

## V.2  Data Visualization

Data visualization is a powerful tool for a data scientist. It allows you to make insights and develop an intuition of what your data looks like.
Visualizing your data also allows you to detect defects or anomalies..

In this section, you are asked to create a set of scripts, each using a particular visualization method to answer a question. There is not necessarily a single answer to the question.


## V.2.1  Histogram

Make a script called histogram.[extension] which displays a histogram answering the next question :

Which Hogwarts course has a homogeneous score distribution between all four houses ?

## V.2.2  Scatter plot

Make a script called scatter_plot.[extension] which displays a scatter plot answering the next question :

What are the two features that are similar ?

## V.2.3  Pair plot

Make a script called pair_plot.[extension] which displays a pair plot or scatter plot matrix (according to the library that you are using).

From this visualization, what features are you going to use for your logistic regression ?

## V.3  Logistic Regression

You arrive at the last part: code your Magic Hat. To do this, you have to perform a multi-classifier using a logistic regression one-vs-all.

You will have to make two programs :

- First one will train your models, it’s called logreg_train.[extension]. It takes as a parameter dataset_train.csv. . For the mandatory part, you must use the technique of gradient descent to minimize the error. The program generates a file containing the weights that will be used for the prediction.

- A second has to be named logreg_predict.[extension]. It takes as a parameter
dataset_test.csv and a file containing the weights trained by previous program.

In order to evaluate the performance of your classifier this second program will have
to generate a prediction file houses.csv formatted exactly as follows:

![exemple 2](https://user-images.githubusercontent.com/45235527/140956376-a3c95194-5fc6-45c6-a6c3-bb0c549b71b7.PNG)

# Partie bonus

It is possible to make a lot of interesting bonuses for this subject. Here are some suggestions :
- Add more fields for describe.[extension]
- Implement a stochastic gradient descent
- Implement other optimization algorithms (Batch GD/mini-batch GD/ you name it)
- ...

# Requirements

- python3.10
- lib:
    - pip3 install pandas
    - pip3 install matplotlib

# doc

<a href="https://sdsclub.com/stochastic-gradient-descent-vs-gradient-descent-a-head-to-head-comparison/">gradient vs stochastic gradient</a>

# Results

## Tools

 `python ./histogram.py DATA`

<img alt="histo" src="https://github.com/AcensJJ/dslr/blob/main/img/histogram.png">

`python ./scatter_plot.py DATA`
 
<img alt="scatter" src="https://github.com/AcensJJ/dslr/blob/main/img/all_scatter_plot.png">

<img alt="scatter line" src="https://github.com/AcensJJ/dslr/blob/main/img/result_scatter_plot.png">

`python ./pair_plot.py DATA`

<img alt="pair" src="https://github.com/AcensJJ/dslr/blob/main/img/pair_plot.png">

## IA

`python ./logreg_train.py DATA`

### Sigmoid function (Logistic Function)

<img alt="pair" src="https://github.com/AcensJJ/dslr/blob/main/img/log/sigmoid.png">

### Cost function

<img alt="pair" src="https://github.com/AcensJJ/dslr/blob/main/img/log/cost.png">
