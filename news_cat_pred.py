import nltk.data
import nltk

classifier = nltk.data.load("classifiers/news_DecisionTree.pickle")
file = open("econ articles.txt","rb")
words =[]
for line in file:
    line_words = nltk.word_tokenize(line)
    for word in line_words:
        words.append(word)

feats = dict([(word,True) for word in words])

print classifier.classify(feats)
