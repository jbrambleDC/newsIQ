import nltk.data
import nltk

classifier = nltk.data.load("classifiers/test_data_sklearn.LinearSVC.pickle")
file = open("validate_data/thedailybell/Survey_Says_Americans_Trust_No_One.txt","rb")
words =[]
for line in file:
    line_words = nltk.word_tokenize(line)
    for word in line_words:
        words.append(word)

feats = dict([(word,True) for word in words])

print classifier.classify(feats)
