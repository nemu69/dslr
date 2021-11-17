import pandas as pd
import numpy as np
import lib.math as lib
import time

import pandas as pd
import sys
import numpy as np
from lib.math import sigmoid
import lib.math as lib
import os
import random


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

def prediction(theta, X):
	predict = sigmoid(X.dot(theta))
	array_predict = []
	# Get the max column index of each row of predict
	for i in range(len(predict)):
		array_predict.append(housesName[np.argmax(predict[i])])
	return array_predict

def inputHat(str):
	x = 0
	boole = True
	while boole:
		tmp = input("Magic Hat \N{top hat} :  What\'s your grade in " + str + " ? ")
		try:
			x = float(tmp)
			boole = False
		except:
			print("ERROR: put a float value")
	return x 

if __name__ == '__main__':

	WEIGHTNAME = "value.csv"
	DATANAME = "datasets/dataset_train.csv"
	if not os.path.exists(WEIGHTNAME) or not os.path.exists(DATANAME):
		print("Error: no file data included")
		exit(-1)
	datatest = pd.read_csv(DATANAME, index_col=False)
	weight = pd.read_csv(WEIGHTNAME, index_col=False)

	if weight.shape != (9, 4):
		print("Error: weight file not correct")
		exit(-1)

	datatest = datatest.fillna(0)
	datatest = datatest.dropna()
	weight = weight.fillna(0)
	weight = weight.dropna()
	datatest.drop(['Index' ,'Hogwarts House','First Name','Last Name','Birthday', 'Best Hand', 'Arithmancy', 'Astronomy', 'Potions', 'Care of Magical Creatures', 'Transfiguration'], axis='columns', inplace=True)
	if weight.shape != (9, 4):
		print("Error: weight file not correct")
		exit(-1)
	print('Magic Hat \N{top hat} : ', 'Welcome student !')
	time.sleep(1)
	print('Magic Hat \N{top hat} : ','Which house do you belong to ?')
	time.sleep(1)
	print('Magic Hat \N{top hat} : ','Please fill in the following information')
	c = ['Herbology','Defense Against the Dark Arts','Divination','Muggle Studies','Ancient Runes','History of Magic','Charms','Flying']
	save = pd.DataFrame()
	for i in c:
		save[i] = [inputHat(i)]
	datatest = pd.concat([datatest,save], ignore_index = True, axis=0)
	X = np.concatenate(
		(
			np.ones((datatest.shape[0], 1)),
			standarize_X(datatest),
		),
		axis=1
	)
	housesName = weight.columns.values
	pred = prediction(weight, X)
	hard = ['Difficult, very difficult...', 'Um, it\'s not easy It\'s actually very difficult...', 'Not so obvious...', 'Hmm, difficult. VERY difficult.']
	qualities = ['I see a lot of courage and intellectual qualities too.','There is talent, oh yes, and a great desire to prove oneself.',
	'Intellectual qualities, too, there is talent and... ho! ho! my boy, you are eager to prove yourself, that is interesting... ', 'Plenty of courage, I see.']
	choice = ['So where shall I put you?','Let\'s see, where shall I put you?']
	for i in range(5):
		print('Magic Hat \N{top hat} :  ', end='')
		if (i == 0):
			print(hard[random.randint(0, len(hard) - 1)])
		elif (i == 2):
			print(qualities[random.randint(0, len(qualities) - 1)])
		elif (i == 4):
			print(choice[random.randint(0, len(choice) - 1)])
		else:
			print('...')
		time.sleep(1)
	print('Magic Hat \N{top hat} : ','You are in the house of ' , pred[datatest.shape[0] - 1])

