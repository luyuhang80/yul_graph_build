import numpy as np
import re


# dic = {}
# dic['x'] = 1
# dic['t'] = 5
# dic['w'] = 4
# print(top_k[:10])

# threshold = 5
# top_k 
k = 10
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
        sent = set(sentence.split())
        sents.append(sent)
out = open('cooccur_graph.txt','w+')
for i,w in enumerate(word_list):
    print(i,'/',len(word_list))
    dic = {}
    for sen in sents:
        if w in sen:
            for s in sen:
                if s != w and s in word_list:
                    if s in dic:
                        dic[s] += 1
                    else:
                        dic[s] = 1
    tmp = [str(i)]
    top_k = [str(word_list[i[0]]) for i in sorted(dic.items(), key=lambda d: d[0])]
    tmp += top_k[:k]
    out.writelines(' '.join(tmp)+'\n')

