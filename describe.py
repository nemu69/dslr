from numpy import NaN
import math
import pandas as pd
import sys
import numpy as np

def describe_count(df):
	return (len(df))

def describe_unique(df):
	unique = []
	for x in df:
		if x not in unique:
			unique.append(x)
	if len(df) == len(unique):
		return (NaN)
	return (len(unique))

def describe_top(df):
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
	mean = sum(x) / len(x)
	"""
	l = []
	for x in df:
		if isinstance(x, float) or isinstance(x, int): 
			l.append(x)
	if not (len(l) == len(df)):
		return (NaN)
	return ((sum(l) / len(l)))

def describe_std(df):
	""""
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
	l = []
	for x in df:
		if isinstance(x, float) or isinstance(x, int):
			l.append(x)
	if not (len(l) == len(df)):
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
 
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Error: no file data included")
		exit(-1)
	FILENAME = str(sys.argv[1])
	data = pd.read_csv(FILENAME)
	#print(data.describe(include='all'))
	title = list(data.columns)
	data = data.transform(np.sort)
	size = 13
	size_title = 6

	print("%-*s" % (size_title, ""), end="")
	for i in title:
		print(" %*.*s" % (size, size, i), end="")

	print("\n%-*s" % (size_title, "count"), end="")
	for i in title:
		print(" %*.0f" % (size, describe_count(data[i].dropna())), end="")
		
	print("\n%-*s" % (size_title, "unique"), end="")
	for i in title:
		print(" %*.0f" % (size, describe_unique(data[i].dropna())), end="")
		
	print("\n%-*s" % (size_title, "top"), end="")
	for i in title:
		print(" % *.*s" % (size, size, describe_top(data[i].dropna())), end="")
		
	print("\n%-*s" % (size_title, "freq"), end="")
	for i in title:
		print(" %*.0f" % (size, describe_freq(data[i].dropna())), end="")
		
	print("\n%-*s" % (size_title, "mean"), end="")
	for i in title:
		print(" %*f" % (size, describe_mean(data[i].dropna())), end="")
		
	print("\n%-*s" % (size_title, "std"), end="")
	for i in title:
		print(" %*f" % (size, describe_std(data[i].dropna())), end="")
		
	print("\n%-*s" % (size_title, "min"), end="")
	for i in title:
		print(" %*f" % (size, describe_min(data[i].dropna())), end="")
		
	print("\n%-*s" % (size_title, "25%"), end="")
	for i in title:
		print(" %*f" % (size, describe_p(data[i].dropna(), 25)), end="")
	   
	print("\n%-*s" % (size_title, "50%"), end="")
	for i in title:
		print(" %*f" % (size, describe_p(data[i].dropna(), 50)), end="")
	   
	print("\n%-*s" % (size_title, "75%"), end="")
	for i in title:
		print(" %*f" % (size, describe_p(data[i].dropna(), 75)), end="")
	   
	print("\n%-*s" % (size_title, "max"), end="")
	for i in title:
		print(" %*f" % (size, describe_max(data[i].dropna())), end="")
	print()