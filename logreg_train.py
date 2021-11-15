import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np
import lib.math as lib
import os

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Error: no file data included")
		exit(-1)
	FILENAME = str(sys.argv[1])
	data = pd.read_csv(FILENAME, index_col=False)
	data.drop(['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand',	'Arithmancy', 'Astronomy', 'Potions', 'Care of Magical Creatures'], axis='columns', inplace=True)
	if (lib.describe_count(data['Hogwarts House'].dropna()) == 0):
		print("Error: empty value")
		exit(-1)
	for i in range(lib.describe_unique(data['Hogwarts House'].dropna())):
		print(i)
	create_file = "value.csv"
	if not os.path.exists(create_file):
		with open(create_file, 'w+') as file:
			file.close()
	data.to_csv(
        create_file,
        index=False,
        sep=',',
    )
