import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem.porter import PorterStemmer

import sys
import re

##allow to take a directory
def get_files():
    files =[]
    for i in sys.argv:
        match = re.match(".*\.txt$", i)
        if match:
            files.append(i)
    return files

def freq_dist(files):
    pstm = PorterStemmer()
    words = []
    for f in files:
        with open(f,"rb") as curr_file:
            data = word_tokenize(curr_file.read().replace('\n', ''))
            words += [pstm.stem(d) for d in data]
    return FreqDist(w.lower() for w in words)

def main():
    freq_dist(get_files()).plot().show()

main()
