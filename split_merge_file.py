#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:51:15 2019

@author: dheeraj and madhumathi
"""

"""
M_Merge_file:
    This is the input file 
HM_output_file :
    Hindi file which is produced as output
EM_output_file :
    English file which is produced as output
Description:
    This code will split a merged file (output of champollian) into two files 
    -> one contains all the english sentences
    -> another contains all the hindi sentences
"""

eng=open('<PATH> /EM_output_file ','a')
hin=open('<PATH> /HM_output_file','a')
i=0
with open('<PATH> /M_Merge_file') as fp:
    t=fp.readline()
    while t:
        if(t[len(t)-1]=='\n'):
            t=t[:len(t)-1]
        [english,hindi]=t.split('<=>')
        t=fp.readline()
        eng.write(english+'\n')
        hin.write(hindi+'\n')
eng.close()
hin.close()

#Merging both of the files
eng=open('<PATH> /E_file','r')
hin=open('<PATH> /H_file','r')
out=open('<PATH> /Output_merged_file','a')
i=0
e=eng.readline()
h=hin.readline()
while e and h:
    out.write(e+' <=> '+h+'\n')
    e=eng.readline()
    h=hin.readline()
eng.close()
hin.close()
