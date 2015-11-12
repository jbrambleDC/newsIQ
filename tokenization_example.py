from nltk.tokenize import PunktSentenceTokenizer
from nltk.collocations import *
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

txt = "I was in the room in Los Angeles in 1988, about 200 feet from Michael Dukakis, when Bernard Shaw asked him what he'd do if his wife were raped. Now that really was a sucker punch of a question. I was on the other side of the arena, in Cleveland, when Donald Trump bared his teeth (metaphorically speaking) at Megyn Kelly."

pst = PunktSentenceTokenizer()
sents = pst.sentences_from_text(txt.encode('utf-8').replace('\n',''))
print sents
bigrams = ngrams(word_tokenize(sents[1].replace('.','')),2)
print bigrams
