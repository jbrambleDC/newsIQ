from requests import get
from bs4 import BeautifulSoup as bs
import newspaper as ns
from nltk.corpus import brown, reuters
import os
import sys

#print reuters.categories()
#print brown.categories()

#construct builds of all segments on CNN
#save to folders
#build Trainer
urls =['http://www.thenation.com']
#cnn_paper = ns.build('http://cnn.com')
#medium = ns.build('http://medium.com')

#urls = [url for url in cnn_paper.category_urls()]
def ensure_dir(f):
    d = os.path.dirname(f)
    print d
    if not os.path.exists(f):
        print "done"
        os.makedirs(f)


for url in urls:
    print url
    paper = ns.build(url)
    print len(paper.articles)
    if len(paper.articles) >= 1:
        for article in paper.articles:
            article.download()
            article.parse()
            print article.text
            print url.split('.')[1] + '/' + article.title.replace(' ','_') +'.txt'
            path ='news/' + url.split('.')[1] + '/' + article.title.replace(' ','_').replace("'",'').replace('/','').replace(',','').replace('-','_').replace('.','') +'.txt'
            print os.path.dirname(url.split('.')[1])
            ensure_dir('news/'+url.split('.')[1])
            f = open(path,'wb')
            f.write(unicode(article.text).encode("utf-8"))
            f.close()




#for category in medium.category_urls():
#    print category
#print "done"
#for category in cnn_paper.category_urls():
    #print category

#for article in cnn_paper.articles:
    #print article.url

#curr_article = cnn_paper.articles[0]
#curr_article.download()
#curr_article.parse()
#curr_article.nlp()
#print curr_article.keywords
