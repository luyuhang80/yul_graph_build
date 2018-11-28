import numpy as np
import re

k = 8
path = '../10_fre_graph/'
def load_wl(path):
    f = open(path+'fre_>10_new.dic')
    con = f.read()
    word_list = eval(con)
    idx,lis = {},{}
    for i,w in enumerate(word_list):
        lis[w] = [w]
        idx[w] = i
    return idx,lis
def load_graph(path,filename):
    l = []
    for line in open(path+filename):
        l.append(line.strip().split())
    return l
idx,lis = load_wl(path)
co = load_graph(path,'cooccur_graph.txt')
knn = load_graph(path,'knn_graph.txt')
file = open(path+'merge_knn_co.txt','w+')
for i in range(len(co)):
    tmp = list(set(co[i] + knn[i]))
    tmp = [str(q) for q in tmp]
    file.writelines(str(i)+' '+' '.join(tmp)+'\n')
file.close()

