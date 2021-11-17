import os
from numpy import NaN
import math
import pandas as pd
import sys
import numpy as np
import lib.math as lib
 
if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Error: no file data included")
		exit(-1)
	FILENAME = str(sys.argv[1])
	if not os.path.exists(FILENAME):
		print("Error: file not found")
		exit(-1)
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
		print(" %*.0f" % (size, lib.describe_count(data[i].dropna())), end="")
		
	print("\n%-*s" % (size_title, "unique"), end="")
	for i in title:
		print(" %*.0f" % (size, lib.describe_unique(data[i].dropna())), end="")
		
	print("\n%-*s" % (size_title, "top"), end="")
	for i in title:
		print(" % *.*s" % (size, size, lib.describe_top(data[i].dropna())), end="")
		
	print("\n%-*s" % (size_title, "freq"), end="")
	for i in title:
		print(" %*.0f" % (size, lib.describe_freq(data[i].dropna())), end="")
		
	print("\n%-*s" % (size_title, "mean"), end="")
	for i in title:
		print(" %*f" % (size, lib.describe_mean(data[i].dropna())), end="")
		
	print("\n%-*s" % (size_title, "std"), end="")
	for i in title:
		print(" %*f" % (size, lib.describe_std(data[i].dropna())), end="")
		
	print("\n%-*s" % (size_title, "min"), end="")
	for i in title:
		print(" %*f" % (size, lib.describe_min(data[i].dropna())), end="")
		
	print("\n%-*s" % (size_title, "25%"), end="")
	for i in title:
		print(" %*f" % (size, lib.describe_p(data[i].dropna(), 25)), end="")
	   
	print("\n%-*s" % (size_title, "50%"), end="")
	for i in title:
		print(" %*f" % (size, lib.describe_p(data[i].dropna(), 50)), end="")
	   
	print("\n%-*s" % (size_title, "75%"), end="")
	for i in title:
		print(" %*f" % (size, lib.describe_p(data[i].dropna(), 75)), end="")
	   
	print("\n%-*s" % (size_title, "max"), end="")
	for i in title:
		print(" %*f" % (size, lib.describe_max(data[i].dropna())), end="")
	print()