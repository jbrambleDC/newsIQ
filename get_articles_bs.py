from bs4 import BeautifulSoup
from requests import get
import newspaper as ns
from newspaper import Article
from nltk.corpus import brown, reuters
import os
import sys
import xml.etree.ElementTree as ET

#<div class="cnn_relpostn">
#<div class="cnn_mtt1img">
#file = open("newsspace200.xml")
#soup = BeautifulSoup(file,"xml")
#print soup.contents[0]
#print soup.title

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(f):
        os.makedirs(f)

tree = ET.parse('newsspace200.xml')
root = tree.getroot()
urls = []
cats = []
desc = []
for a in root.findall('./url'):
    urls.append(a.text)
for a in root.findall('./category'):
    cats.append(a.text)
for b in root.findall('./description'):
    desc.append(b.text)

print urls[0], cats[0], desc[0]
print len(urls), len(cats), len(desc)

for i in range(0,len(urls)-1):
    if cats[i] != "Business" and cats[i] != "Sci/Tech" and desc[i] is not None:
        print cats[i]
        url = urls[i]
        a = Article(url,language='en')
        a.download()
        a.parse()
        if cats[i] is None:
            cats[i] = cats[i-1]
        if desc[i] is None:
            desc[i] = desc[i-1].split(' ')[1] + ' ' + desc[i-1].split(' ')[-1]
        #check if path already exists and then add
        path ='news/'+cats[i].split('/')[0]+'/'+ desc[i].split(' ')[0]+desc[i].split(' ')[1] +'.txt'

        ensure_dir('news/'+unicode(cats[i].split('/')[0]).encode("utf-8"))
        if len(a.text) > 0:
            f = open(path,'wb')
            f.write(unicode(a.text).encode("utf-8"))
            f.close()
        print 'next'
