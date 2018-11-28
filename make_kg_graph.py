import numpy as np
import re
from gensim.models import Word2Vec

k = 8

def load_wl():
    f = open('fre_>10_new.dic')
    con = f.read()
    word_list = eval(con)
    idx,lis = {},{}
    for i,w in enumerate(word_list):
        lis[w] = [w]
        idx[w] = i
    return idx,lis

idx,lis = load_wl()
word2sen = dict()
sents = []
for line in open('kg_complete_new.txt'):
    words = line.strip().split()
    if len(words)>1:
        node = words[0]
        nbs = words[1:]
        if node in idx:
            for n in nbs:
                if n in idx and n!=node:
                    lis[node].append(n)
                    
file = open('kg_graph.txt','w+')
for i,w in enumerate(lis):
    tmp = [str(idx[i]) for i in lis[w]]
    file.writelines(' '.join(tmp)+'\n')
file.close()

