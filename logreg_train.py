import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np
import lib.math as lib
import os

def T(array):
    '''
    Transpose of an array:
    '''
    array_T = np.zeros((array.shape[::-1]), dtype=array.dtype)
    for i in range(array.shape[1]):
        for j in range(array.shape[0]):
            array_T[i][j] = array[j][i]
    return array_T

def ft_standardized(myList):
    '''
    Standarize a list of data
    '''
    mean = lib.describe_mean(myList)
    std = lib.describe_std(myList)
    Z = []
    for value in myList:
        Z.append((value - mean) / std)
    return np.array(Z)

def standarize_X(df_matrice):
    '''
    Standarize the matrice by standarize each column
    '''
    std_matrice = []
    for col in df_matrice.columns:
        std_matrice.append(
            ft_standardized(df_matrice[col])
        )
    return T(np.array(std_matrice))

def atoi(str):
    resultant = 0
    for i in range(len(str)):
        resultant = resultant * 10 + (ord(str[i]) - ord('0'))        #It is ASCII substraction 
    return resultant

def save_file(df):
	create_file = "value.csv"
	if not os.path.exists(create_file):
		with open(create_file, 'w+') as file:
			file.close()
	df.to_csv(
		create_file,
		index=False,
		sep=',',
	)

def check_arg(arg):
	iteration = 20
	for i in range(len(arg)):
		if (arg[i] == "iteration"):
			if (i + 1 < len(arg)):
				iteration = atoi(arg[i + 1])
	return (iteration)

def draw_coef_derter(cost, name):
    plt.title("Courbe d'apprentisage " + name)
    plt.tick_params(labelcolor='tab:orange')
    plt.plot(range(len(cost)), cost, color='tab:red')
    plt.tight_layout()
    plt.savefig("img/log/learning_" + name + ".png")
    # plt.show()

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Error: no file data included")
		exit(-1)
	FILENAME = str(sys.argv[1])
	iteration = check_arg(sys.argv)
	data = pd.read_csv(FILENAME, index_col=False)
	data = data.dropna()
	data.drop(['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand',	'Arithmancy', 'Astronomy', 'Potions', 'Care of Magical Creatures', 'Transfiguration'], axis='columns', inplace=True)
	if (lib.describe_count(data['Hogwarts House'].dropna()) == 0):
		print("Error: empty value")
		exit(-1)
	m = len(data['Hogwarts House'])
	cost_values = []
	trained_parameters = []
	X = np.concatenate(
        (
            np.ones((data.shape[0], 1)),
            standarize_X(data.iloc[:, 1:]),
        ),
        axis=1
    )
	df = data['Hogwarts House']
	save = pd.DataFrame()
	for house in lib.describe_unique_list_name(data['Hogwarts House'].dropna()):
		cost_list = []
		Y = np.array([int(y == house) for y in df], ndmin=2)
		theta = np.zeros((9, 1))
		for i in range(iteration):
			theta = lib.stochastic_gradient_descent(theta, X, T(Y), m, cost_list, alpha=0.5)
		print(house)
		print(theta)
		save[house] = theta
		cost_values.append([cost_list, house])
	for cost in cost_values:
		draw_coef_derter(cost[0], cost[1])
	save_file(save)