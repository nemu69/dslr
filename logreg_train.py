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

def draw_cost():
	fig, ax = plt.subplots(facecolor=(.18, .31, .31))
	plt.tick_params(labelcolor='tab:orange')
	x_cost = np.linspace(0.001, 0.999, 100)
	y_cost0 = [-np.log(1 - x) for x in x_cost]
	y_cost1 = [-np.log(x) for x in x_cost]
	plt.title('cost function', color='cornflowerblue')
	ax.plot(x_cost, y_cost0, label='$y = 0, -\log(1 - h_θ(x))$', color='royalblue')
	ax.plot(x_cost, y_cost1, label='$y = 1, -\log(h_θ(x))$', color='crimson')
	plt.legend()
	plt.grid()
	plt.tight_layout()
	plt.savefig("img/log/cost.png")
	plt.show()

def draw_signoide():
	fig, ax = plt.subplots(facecolor=(.18, .31, .31))
	plt.tick_params(labelcolor='tab:orange')
	X_sig = np.linspace(-10, 10, 100)
	Y_sig = lib.sigmoid(X_sig)
	plt.title('Sigmoid function', color='cornflowerblue')
	ax.plot(X_sig, Y_sig, label=r'$g(z) = \frac{1}{1 + e^{-z}}$', color='darkviolet')
	plt.yticks([0, 0.5, 1])
	plt.legend()
	plt.grid()
	plt.tight_layout()
	plt.savefig("img/log/sigmoid.png")
	plt.show()

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Error: no file data included")
		exit(-1)
	FILENAME = str(sys.argv[1])
	iteration = check_arg(sys.argv)
	data = pd.read_csv(FILENAME, index_col=False)
	data = data.fillna(0)
	data = data.dropna()
	data.drop(['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand',	'Arithmancy', 'Astronomy', 'Potions', 'Care of Magical Creatures', 'Transfiguration'], axis='columns', inplace=True)
	if (lib.describe_count(data['Hogwarts House'].dropna()) == 0):
		print("Error: empty value")
		exit(-1)
	m = len(data['Hogwarts House'])
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
		Y = T(np.array([int(y == house) for y in df], ndmin=2))
		theta = np.zeros((9, 1))
		for i in range(iteration):
			theta = lib.stochastic_gradient_descent(theta, X, Y, m, alpha=0.5)
		print(house)
		print(theta)
		save[house] = theta
	save_file(save)
	draw_signoide()
	draw_cost()