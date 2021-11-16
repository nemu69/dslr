# scatter plot of the data 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import lib.math as lib

def normalize(x):
	return (x - min(x)) / (max(x) - min(x))

def draw():
	ax = plt.subplot(len(title), len(title), k * len(title) + j + 1)
	if (j == 0):
		ax.set_ylabel(title[i], color='#ff5010')
	if (k == 0):
		ax.set_title(title[j], color='#2497C0')
	if (j != i):
		ax.scatter(g[title[i]], g[title[j]], color='#EC493C', label="Gryffindor")
		ax.scatter(r[title[i]], r[title[j]], color='#125E9F', label="Ravenclaw")
		ax.scatter(s[title[i]], s[title[j]], color='#24C070', label="Slytherin")
		ax.scatter(h[title[i]], h[title[j]], color='#F8FC05', label="Hufflepuff")
	else:	
		ax.hist(g[title[i]], bins='auto', density=True, alpha=0.75, histtype='stepfilled', color='#EC493C', label="Gryffindor")
		ax.hist(r[title[i]], bins='auto', density=True, alpha=0.75, histtype='stepfilled', color='#125E9F', label="Ravenclaw")
		ax.hist(s[title[i]], bins='auto', density=True, alpha=0.75, histtype='stepfilled', color='#24C070', label="Slytherin")
		ax.hist(h[title[i]], bins='auto', density=True, alpha=0.75, histtype='stepfilled', color='#F8FC05', label="Hufflepuff")

def get_size_to_draw():
	ncol = size
	if len(title) < size:
		ncol = len(title)
	nrow = (len(title))
	if (ncol == 0 or nrow == 0):
		print("Error: no line data")
		exit(-1)
	return ([nrow, ncol])

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Usage: scatter_plot.py <data_file>')
		sys.exit(1)
	# read the data
	data = pd.read_csv(sys.argv[1])
	if (lib.describe_count(data['Hogwarts House'].dropna()) == 0):
		print("Error: empty value")
		exit(-1)
	# drop the data
	data.drop(['Index','First Name', 'Last Name', 'Birthday', 'Best Hand'], axis='columns', inplace=True)
	g = data.loc[data['Hogwarts House'] == "Gryffindor"]
	r = data.loc[data['Hogwarts House'] == "Ravenclaw"]
	s = data.loc[data['Hogwarts House'] == "Slytherin"]
	h = data.loc[data['Hogwarts House'] == "Hufflepuff"]
	data.drop(['Hogwarts House'], axis='columns', inplace=True)
	title = list(data.columns)
	size = len(title)
	nb = get_size_to_draw()
	fig = plt.figure(figsize=(nb[1] , nb[0]))
	plt.style.use('seaborn')
	fig.set_size_inches(18.5, 15.5)
	for i in range(len(title)):
		k = i
		for j in range(len(title)):
			draw()

	colors = ['red', 'tan', 'lime']
	fig.tight_layout(pad=2, w_pad=2)
	fig.savefig('img/pair_plot.png', dpi=100)
	plt.show()
