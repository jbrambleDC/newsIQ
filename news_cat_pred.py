import nltk.data
import nltk
from nltk.tokenize import PunktSentenceTokenizer
import sys
import re

#classifier = nltk.data.load("classifiers/test_data_sklearn.LinearSVC.pickle")
#file = open("validate_data/thedailybell/Survey_Says_Americans_Trust_No_One.txt","rb")
classifier = nltk.data.load("classifiers/test_data_sklearn.LinearSVC.pickle")
pst = PunktSentenceTokenizer()
files =[]
words = []
##allow to take a directory
for i in sys.argv:
  match = re.match(".*\.txt$", i)
  if match:
    files.append(i)

print 'file_name' + '\t' + 'politcal_stance'

for f in files:
  with open(f,"rb") as class_file:
    if sys.argv[1] == '--sents':
      data = class_file.read().replace('\n', '')
      sents = pst.sentences_from_text(data)
      for sent in sents:
        sent_words = nltk.word_tokenize(sent)
        for word in sent_words:
          words.append(word)
      feats = dict([(word, True) for word in words])

    else:
      for line in class_file:
        line_words = nltk.word_tokenize(line)
        for word in line_words:
          words.append(word)
      feats = dict([(word, True) for word in words])

    print f + '\t' + classifier.classify(feats)
