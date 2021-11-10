import pandas as pd
import sys
import matplotlib.pyplot as plt

def draw():
    ax = plt.subplot2grid(shape=(nb[0], nb[1]), loc=(y, i - y * size))
    ax.set_title(title[i])
    ax.set_ylabel('Frequency')
    ax.set_xlabel('Score')
    ax.hist(g[title[i]], bins=30, density=True, alpha=0.75, histtype='stepfilled', color='#EC493C', label="Gryffindor")
    ax.hist(r[title[i]], bins=30, density=True, alpha=0.75, histtype='stepfilled', color='#125E9F', label="Ravenclaw")
    ax.hist(s[title[i]], bins=30, density=True, alpha=0.75, histtype='stepfilled', color='#24C070', label="Slytherin")
    ax.hist(h[title[i]], bins=30, density=True, alpha=0.75, histtype='stepfilled', color='#F8FC05', label="Hufflepuff")
    ax.legend()

def get_size_to_draw():
    ncol = size
    if len(title) < size:
        ncol = len(title)
    nrow = int((len(title)) / size) + 1
    if ((len(title)) % size == 0):
        nrow -= 1
    if (ncol == 0 or nrow == 0):
        print("Error: no line data")
        exit(-1)
    return ([nrow, ncol])

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Error: no file data included")
        exit(-1)
    FILENAME = str(sys.argv[1])
    data = pd.read_csv(FILENAME, index_col=False)
    data.drop(['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand'], axis='columns', inplace=True)
    g = data.loc[data['Hogwarts House'] == "Gryffindor"]
    r = data.loc[data['Hogwarts House'] == "Ravenclaw"]
    s = data.loc[data['Hogwarts House'] == "Slytherin"]
    h = data.loc[data['Hogwarts House'] == "Hufflepuff"]
    data.drop(['Hogwarts House'], axis='columns', inplace=True)
    title = list(data.columns)
    size = 4
    nb = get_size_to_draw()
    fig = plt.figure(figsize=(nb[0] * 2, nb[1] * 2))
    plt.style.use('seaborn')
    fig.set_size_inches(18.5, 10.5)
    
    y = -1
    for i in range(len(title)):
        if (i % size == 0):
            y += 1
        draw()
    colors = ['red', 'tan', 'lime']
    fig.tight_layout()
    fig.savefig('img/histogram.png', dpi=100)
    plt.show()