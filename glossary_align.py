#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 04:47:23 2019

@author: dheeraj
"""
'''
prerequisites : flair (pip install flair)
translate the hindi text into english or viceversa

E_sentences - glossary file of english text book
H_sentences_eng - translated glossary file of hindi text book


'''


from flair.embeddings import WordEmbeddings, FlairEmbeddings, DocumentPoolEmbeddings, Sentence

document_embeddings = DocumentPoolEmbeddings([
                                        WordEmbeddings('glove'), 
                                        FlairEmbeddings('news-forward'), 
                                        FlairEmbeddings('news-backward'),
                                       ])

#opening english file and embedding each sentence
eng=open('<PATH> /E_sentences.txt','r')
#vec_eng=open('/home/dheeraj/Desktop/IIITH-Intern/Major-TH-Tool/glossary/E_vecs.txt','a')
line=eng.readline()
eng_vecs=[]
while(line):
    sentence=Sentence(line)
    document_embeddings.embed(sentence)
    li=sentence.get_embedding()
    li=li.tolist()
    eng_vecs.append(li)
    line=eng.readline()
eng.close()

#opening hindi file and embedding each hindi sentence
hin=open('<PATH> /H_sentences_eng.txt','r')
line=hin.readline()
hin_vecs=[]
while(line):
    sentence=Sentence(line)
    document_embeddings.embed(sentence)
    li=sentence.get_embedding()
    li=li.tolist()
    hin_vecs.append(li)
    line=hin.readline()
hin.close()

#dictionary to make note of which sentences got aligned 
#similarity between two sentences is found out by using cosine similarity function 
d={}
from scipy import spatial
for i in range(len(eng_vecs)):
    data1=eng_vecs[i]
    ans=[]
    
    #picking the sentence which has greatest simialarity
    for j in range(len(hin_vecs)):
        data2=hin_vecs[j]
        x=1-spatial.distance.cosine(data1,data2)
        ans.append((x,j))
    ans.sort(reverse=True)
    d[i]=ans[0][1]
    #print(ans)

#to get know about unassigned english and hindi words
l=[]
un_h=[]
for i in d.values():
    yes=0
    if i in l:
        yes=1
        print(i)
        un_h.append(i)
    else:
        l.append(i)

un=[]
for i in d.keys():
    if d[i] in un_h:
        un.append([i,d[i]])
