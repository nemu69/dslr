import pandas as pd
import sys
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import lib.math as lib


if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Error: no file data included")
		exit(-1)
	FILENAME = str(sys.argv[1])
	data = pd.read_csv(FILENAME, index_col=False)
	data.drop(['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand'], axis='columns', inplace=True)
    if ()