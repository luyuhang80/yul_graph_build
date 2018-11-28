import numpy as np
import re

k = 8

def load_wl():
    f = open('../8_fre_graph/fre_>8_new.dic')
    con = f.read()
    word_list = eval(con)
    idx,lis = {},{}
    for i,w in enumerate(word_list):
        lis[w] = [w]
        idx[i] = w
    return idx,lis
def load_graph(filename):
    l = []
    for line in open(filename):
        l.append(line.strip().split())
    return l
idx,lis = load_wl()
co = load_graph('../8_fre_graph/cooccur_graph.txt')
kg = load_graph('../8_fre_graph/kg_graph.txt')
knn = load_graph('../8_fre_graph/knn_graph.txt')
merge = load_graph('../8_fre_graph/merge_graph.txt')
print(len(idx))
# file = open('../8_fre_graph/merge_knn_kg.txt','w+')
file = open('../8_fre_graph/example.txt','w+')
for i in range(len(kg)):
    s0 = set(merge[i])
    s1 = set(co[i])
    s2 = set(kg[i])
    s3 = set(knn[i])
    if len(s1 & s2 &s3 ) >1:
        print(merge[i])
        # l0 = [idx[i]] + [idx[int(q)] for q in s0]
        # l1 = [idx[i]] + [idx[int(q)] for q in s1]
        # l2 = [idx[i]] + [idx[int(q)] for q in s2]
        # l3 = [idx[i]] + [idx[int(q)] for q in s3]
        # file.writelines(' '.join(l0)+'\n')
        # file.writelines(' '.join(l1)+'\n')
        # file.writelines(' '.join(l2)+'\n')
        # file.writelines(' '.join(l3)+'\n\n')
        # print(l1,l2,l3)
#     tmp = list(set(co[i] + kg[i] + knn[i]))
#     tmp = list(set(kg[i] + knn[i]))
#     tmp = [str(q) for q in tmp]
#     file.writelines(str(i)+' '+' '.join(tmp)+'\n')
# file.close()

