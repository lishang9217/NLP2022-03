# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 02:48:36 2022

@author: lisha
"""
import urllib
from string import printable
file = urllib.request.urlopen(url="https://github.com/stopwords-iso/stopwords-zh/blob/master/stopwords-zh.txt")
stopwords = file.read().decode("utf8").split()

from nltk.corpus.reader import PlaintextCorpusReader
from nltk.probability import FreqDist

creditcard_dir = "creditcard/Mar 11/" #Lifeismoney/Feb 14/
pcr = PlaintextCorpusReader(root=creditcard_dir, fileids=".*\.txt")
fd = FreqDist(samples=pcr.words())
creditcard_words = [word for word,freq in fd.most_common(n=300) if word not in stopwords and word[0] not in printable]

Lifeismoney_dir = "Lifeismoney/Feb 14/"
pcr = PlaintextCorpusReader(root=Lifeismoney_dir, fileids=".*\.txt")
fd = FreqDist(samples=pcr.words())
Lifeismoney_words = [word for word,freq in fd.most_common(n=300) if word not in stopwords and word[0] not in printable]

print(creditcard_dir)
print([word for word in creditcard_words if word not in Lifeismoney_words])

print(Lifeismoney_dir)
print([word for word in Lifeismoney_words if word not in creditcard_words])

from gensim.models import Word2Vec
from gensim.models.word2vec import PathLineSentences

corpus = PathLineSentences(creditcard_dir)
mode = Word2Vec(sentences=corpus, vector_size=100, window=5, min_count=1, workers=4)
print(mode.wv.most_similar(positive=["銀行","回饋"], negative=["信用卡"]))#優惠 商品 折扣

corpus2 = PathLineSentences(Lifeismoney_dir)
mode = Word2Vec(sentences=corpus2, vector_size=100, window=5, min_count=1, workers=4)
print(mode.wv.most_similar(positive=["優惠","折扣"], negative=["商品"]))