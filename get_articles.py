from requests import get
import newspaper as ns
import os
import sys
import re

urls =[]
for i in sys.argv:
  match = re.search("(https?://([-\w\.]+)+(:\d+)?(/([\w/_\.]*(\?\S+)?)?)?)",i)
  if match:
    urls.append(i)
print urls
def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(f):
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
            path ='news/' + url.split('.')[1] + '/' + article.title.replace(' ','_').replace(':','').replace("'",'').replace('/','').replace(',','').replace('-','_').replace('.','').replace(';','') +'.txt'
            print os.path.dirname(url.split('.')[1])
            ensure_dir('news/'+url.split('.')[1])
            f = open(path,'wb')
            f.write(unicode(article.text).encode("utf-8"))
            f.close()

