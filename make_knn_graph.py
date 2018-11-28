import numpy as np
import re
from gensim.models import Word2Vec

k = 8

def load_wl():
    f = open('fre_>10_new.dic')
    con = f.read()
    word_list = eval(con)
    new = {}
    for i,w in enumerate(word_list):
        new[w] = i
    return new

word_list = load_wl()
word2sen = dict()
sents = []
with open("./seqs_for_train.txt", "r") as text_input_file:
    buf = text_input_file.readlines()
    for index, line in enumerate(buf):
        sentence, label = line.strip().split("\t")
        punc = '[,.!\'%*+-/=><]'
        sentence = re.sub(punc, '', sentence)
        print(index, sentence, label)
        sents.append(sentence.split())

model = Word2Vec(sents, size=50, window=5, min_count=1, workers=4)
model.save("word2vec.model")
file = open('knn_graph.txt','w+')
for i,w in enumerate(word_list):
    print(i,'/',len(word_list))
    tmp = [str(i)]
    try:
        nbs = [i[0] for i in model.most_similar(w,topn=k)]
        # print(nbs)
        for nb in nbs:
            if nb in word_list:
                tmp.append(str(word_list[nb]))
        print(tmp)
    except Exception as e:
        print(e)
        
    file.writelines(' '.join(tmp)+'\n')

