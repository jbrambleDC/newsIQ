from requests import get
from bs4 import BeautifulSoup as bs
import newspaper as ns
from nltk.corpus import brown, reuters
import os
import sys
import re

#construct builds of all segments on CNN
#save to folders
#build Trainer
urls =[]
for i in sys.argv:
  match = re.search("(https?://([-\w\.]+)+(:\d+)?(/([\w/_\.]*(\?\S+)?)?)?)",i)
  if match:
    urls.append(i)
print urls
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
            path ='test_data/' + url.split('.')[1] + '/' + article.title.replace(' ','_').replace(':','').replace("'",'').replace('/','').replace(',','').replace('-','_').replace('.','').replace(';','') +'.txt'
            print os.path.dirname(url.split('.')[1])
            ensure_dir('test_data/'+url.split('.')[1])
            f = open(path,'wb')
            f.write(unicode(article.text).encode("utf-8"))
            f.close()

