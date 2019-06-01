#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 20:12:18 2019

@author: dheeraj and madhumathi
"""

"""
This code is for:
Before running the champollian for parallel hindi and english corpus we remove newlines in the corpus and make it as paragraphs.
"""
eng=open('<PATH> / english_1','r')
hin=open('<PATH>/hindi_1','r')
new=open('<PATH>/new_eng','a')
l=eng.readline()
while l:
    if l[0]=='\n':
        new.write('\n')
    else:
        new.write(l[:len(l)-1])
    l=eng.readline()
eng.close()
new.close()

new=open('<PATH> /new_hin','a')
l=hin.readline()
i=1
while l:
    if l[0]=='\n':
        new.write('\n')
    else:
        new.write(l[:len(l)-1])
    l=hin.readline()
    print(i)
    i+=1
hin.close()
new.close()
