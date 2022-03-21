# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 02:48:36 2022

@author: lisha
"""

from nltk.corpus.reader import PlaintextCorpusReader
source_dir = "creditcard/Mar 11/" #Lifeismoney/Feb 14/
pcr = PlaintextCorpusReader(root=source_dir, fileids=".*\.txt")

from nltk.probability import FreqDist
fd = FreqDist(samples=pcr.words())
print(fd.most_common(n=250))

from gensim.models import Word2Vec
from gensim.models.word2vec import PathLineSentences
corpus = PathLineSentences(source_dir)
model = Word2Vec(sentences=corpus, vector_size=200, window=5, min_count=1, workers=4)

print(model.wv.most_similar(positive=["銀行","回饋"], negative=["信用卡"]))
