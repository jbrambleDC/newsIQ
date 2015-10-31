import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

import plotly.plotly as ply
import plotly.graph_objs as go

import sys
import re

import logging

reload(sys)
sys.setdefaultencoding('utf-8')

##allow to take a directory
def get_files():
  files =[]
  for i in sys.argv:
    match = re.match(".*\.txt$", i)
    if match:
      files.append(i)
  logging.info("found %s files to parse", len(files))
  return files

def freq_dist(files):
  pstm = PorterStemmer()
  words = []
  if files.count > 0:
    for f in files:
      with open(f,"rb") as curr_file:
        data = word_tokenize(curr_file.read().replace('\n', ''))
        words += [pstm.stem(d) for d in data if d.lower() not in stopwords.words('english') and len(d) > 5]
    return dict(FreqDist(w.encode('utf-8').lower() for w in words).items()[0:100])
  else:
    logging.error("no files to process")

def main():
  terms = freq_dist(get_files())
  data = [go.Bar(x=terms.keys(),y=terms.values())]
  plot_url = ply.plot(data, filename='word_hist_lib')

main()
