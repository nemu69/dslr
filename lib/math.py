from numpy import NaN
import math
import numpy as np

def describe_count(df):
	'''
	Return the count of the list
	'''
	return (len(df))

def describe_unique(df):
	'''
	Return the count of all different value
	'''
	unique = []
	for x in df:
		if x not in unique:
			unique.append(x)
	if len(df) == len(unique):
		return (NaN)
	return (len(unique))

def describe_top(df):
	'''
	Return the key of the value who appear the most
	'''
	l = []
	val = [NaN, 1]
	for x in df:
		l.append(x)
	top = [[x,l.count(x)] for x in set(l)]
	for x in top:
		if x[1] > val[1]:
			val = x
	return (val[0])

def describe_freq(df):
	'''
	Return the key of the number of time who the top appear
	'''
	l = []
	val = [NaN, 1]
	for x in df:
		l.append(x)
	top = [[x,l.count(x)] for x in set(l)]
	for x in top:
		if x[1] > val[1]:
			val = x
	if val[1] == 1:
		return (val[0])
	return (val[1])

def describe_mean(df):
	""""
	Mean of an array
	mean = sum(x) / len(x)
	"""
	l = []
	for x in df:
		if isinstance(x, float) or isinstance(x, int): 
			l.append(x)
	if not (len(l) == len(df)):
		return (NaN)
	if (len(l) == 0):
		return (NaN)
	return ((sum(l) / len(l)))

def describe_std(df):
	""""
	Standard deviation of an array
	std = sqrt(mean(x)), where x = abs(a - a.mean())**2.
	"""
	l = []
	for x in df:
		if isinstance(x, float) or isinstance(x, int): 
			l.append(x)
	if not (len(l) == len(df)):
		return (NaN)
	dif = df - describe_mean(df)
	mean = sum(np.abs(dif) ** 2) / (describe_count(df) - 1)
	x = abs(describe_count(df) - describe_mean(df))**2
	return (math.sqrt(mean))

def describe_min(df):
	'''
	Return the key of the min value in a dictionary
	'''
	min = 0
	check = False
	for x in df:
		if isinstance(x, float) or isinstance(x, int): 
			if not check or x <= min:
				check = True
				min = x
	if not (check):
		return (NaN)
	return (min)

def describe_p(df, percent):
	'''
	Take a ordered List with the rank in percent then return the percentile
	'''
	l = []
	for x in df:
		if isinstance(x, float) or isinstance(x, int):
			l.append(x)
	if not (len(l) == len(df)):
		return (NaN)
	if (len(l) == 0):
		return (NaN)
	k = (len(df) - 1) * percent / 100
	f = np.floor(k)
	c = np.ceil(k)
	if f == c:
		return df[int(k)]
	d0 = df[int(f)] * (c - k)
	d1 = df[int(c)] * (k - f)
	return d0 + d1

def describe_max(df):
	'''
	Return the key of the max value in a dictionary
	'''
	max = 0
	check = False
	for x in df:
		if isinstance(x, float) or isinstance(x, int): 
			if not check or x > max:
				check = True
				max = x
	if not (check):
		return (NaN)
	return (max) 

def     sigmoid(z):
    '''
    Sigmoid fonction
    '''
    return 1 / (1 + np.exp(-z))