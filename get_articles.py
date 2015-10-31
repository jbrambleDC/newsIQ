from requests import get
import newspaper as ns
import os
import sys
import re
import logging

def get_urls():
  urls =[]
  for i in sys.argv:
    match = re.search("(https?://([-\w\.]+)+(:\d+)?(/([\w/_\.]*(\?\S+)?)?)?)",i)
    if match:
      urls.append(i)
  return urls

def ensure_dir(f):
    #d = os.path.dirname(f)
  if not os.path.exists(f):
    os.makedirs(f)

def main(urls):
  for url in urls:
    logging.info('fetching from %s', url)
    paper = ns.build(url)
    logging.info('sourcing %s articles', len(paper.articles))

    if len(paper.articles) >= 1:
      for article in paper.articles:
        article.download()
        article.parse()
        path ='news/' + url.split('.')[1] + '/' + article.title.replace(' ','_').replace(':','').replace("'",'').replace('/','').replace(',','').replace('-','_').replace('.','').replace(';','') +'.txt'
        ensure_dir('news/'+url.split('.')[1])
        logging.info('writing %s', path)
        f = open(path,'wb')
        f.write(unicode(article.text).encode("utf-8"))
        f.close()

    else:
      logging.warning('paper sourced from %s is empty', url)

main(get_urls())

