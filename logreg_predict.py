import pandas as pd
import sys
import numpy as np
from lib.math import sigmoid
import lib.math as lib
import os

housesName = []

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
		resultant = resultant * 10 + (ord(str[i]) - ord('0'))		#It is ASCII substraction 
	return resultant

def save_file(df):
	create_file = "houses.csv"
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

def prediction(theta, X):
	predict = sigmoid(X.dot(theta))
	array_predict = []
	# Get the max column index of each row of predict
	for i in range(len(predict)):
		array_predict.append(housesName[np.argmax(predict[i])])
	return array_predict

if __name__ == "__main__":

	if (len(sys.argv) < 3):
		print("Error: no file data included")
		exit(-1)

	DATANAME = str(sys.argv[1])
	WEIGHTNAME = str(sys.argv[2])
	datatest = pd.read_csv(DATANAME, index_col=False)
	weight = pd.read_csv(WEIGHTNAME, index_col=False)

	if weight.shape != (9, 4):
		print("Error: weight file not correct")
		exit(-1)

	datatest = datatest.fillna(0)
	datatest = datatest.dropna()
	weight = weight.fillna(0)
	weight = weight.dropna()
	datatest.drop(['Birthday', 'Best Hand', 'Arithmancy', 'Astronomy', 'Potions', 'Care of Magical Creatures', 'Transfiguration'], axis='columns', inplace=True)

	X = np.concatenate(
		(
			np.ones((datatest.shape[0], 1)),
			standarize_X(datatest.iloc[:, 4:]),
		),
		axis=1
	)
	housesName = weight.columns.values
	houses = {
		'Index' : list(datatest['Index']),
		'Hogwarts House': prediction(weight, X)
	}
	save = pd.DataFrame(houses)
	save_file(save)