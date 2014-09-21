newsIQ
======

Just starting out, building NaiveBayes and DecisionTree Classifiers for news articles
This is a Work in Progress. So forgive the suboptimal documentation.

after pulling this repo locally:
1. pip install nltk-trainer
2. mkdir news
3. change get_articles_bs.py to remove the if cats[i] != "Business" and cats[i] != "Sci/Tech" conditions for now.
4. run get_articles_bs.py on the shortnews.xml, by changing the the file parameter in get_articles_bs.py
5. Look over the nltk-trainer documentation and use the command line tool for building classifiers, to make a classifier on the data contained in the news directory.
6. make sure news_cat_pred.py has the correct pickle classifier imported.
7. import the text of a news article of your choice in news_cat_pred.py
8. run python news_cat_pred.py to classify that article

I am building a more user friendly framework out of this so that anyone can build and use classifiers on news articles.
