#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 04:38:23 2019
Python version : 3.7.3

@author: dheeraj and madhumathi
"""

"""
A parallel sentence aligned corpus is given as input to this code.

SE_Input_file.txt : 
    This file consisting of english sentences 
SH_Input_file.txt :
    This file consisting of hindi sentences 
SE_Output_file.txt :
    Ouput file consisting of english sentences
    This will be created by the code and it consists of sentences which are properly combined according to puntuation marks 
    like "" , ( ) ,{ } , [ ] and ' '
SH_Output_file :
    The corresponding output file , consisting of hindi sentences
Description:
    Below code aligns the sentences properly within the puntuation marks given above.

Assumptions :
    1.Apostrophe comes between the letters of a word
        eg: It's and not Its'
    2.The parallel corpus must be sentence aligned 
      i.e. each sentence in E_input_file must have its corresponding translated sentence in the H_input_file
"""

import re

#This function is used to check whether a single quote must be paired with another single quote or it is an apostrophe.
def check(s):
    x=re.search(r'\w\'\w',s)
    if x:
        return False
    else:
        return True

#Initialising stack
stack=[]
final=[]
prev=""
c=0
yes=0

#A dictionary is used to store the line numbers which are merged so that corresponding line numbers must be merged in H_Input_file
combined={}
new_txt=open('<PATH> /SE_Ouptut_file.txt','a')
with open('<PATH>/SE_Input_file.txt','r') as fp:
    
    #Reading the file line by line
    line=fp.readline()
    c=1
    pres_root=-1
    
    #looping until the end of the file
    while line:
        #checking whether the given line is blank or not
        if len(line.strip()) >0:
            
            #storing the merged lines in the dictionary 
            if pres_root==-1:
                combined[c]=[c]
            else:
                combined[pres_root].append(c)
            
            #removing the new line charector from the line
            if line[len(line)-1]=='\n':
                line=line[:len(line)-1]
            s1=line
            
            #Traversing the entire line
            for j in range(len(s1)):
                
                #If we encounter a opening parenthesis or starting quote symbol of double quotes or single quotes(and checking whether it is apostrophe or not) push it into the stack
                #Or else if we encounter a closing puntuation mark and if there is corresponding symbol on the top of the stack then we are popping it out otherwise print corresponding error message
                
                if s1[j]=='[' or s1[j]=='(' or s1[j]=='{':
                    stack.append(s1[j])
                elif s1[j]=='"' or s1[j]=='”' or s1[j]=='“':
                    if len(stack)>0 and (stack[len(stack)-1]=='"' or stack[len(stack)-1]=='”' or stack[len(stack)-1]=='“'):
                        t=stack.pop()
                    else:
                        stack.append(s1[j])
                elif s1[j]=='\'':
                    can=0
                    if j!=0 and j!=len(line):
                        if check(s1[j-1:j+2]):
                            can=1
                    else:
                        can=1
                    if can==1:
                        if len(stack)>0 and stack[len(stack)-1]=='\'':
                            t=stack.pop()
                        else:
                            stack.append(s1[j])
                elif len(stack)>0:
                    if s1[j]==']' :
                        if stack[len(stack)-1]=='[':
                            t=stack.pop()
                        else:
                            print('Opening ] not found')
                    elif s1[j]=='}':
                        if stack[len(stack)-1]=='{':
                            t=stack.pop()
                        else:
                            print('Opening { not found')
                    elif s1[j]==')':
                        if stack[len(stack)-1]=='(':
                            t=stack.pop()
                        else:
                            print('Opening ( not found ')
            
            #Append a sentence to the outputfile if the stack is empty
            if len(stack)==0:
                final.append(prev+s1)
                new_txt.write(prev+s1+'\n')
                prev=""
                pres_root=-1
            else:
                if prev=="":
                    pres_root=c
                prev+=s1+" "
        line=fp.readline()
        c+=1
        
#printing the information which is not matched correctly and appending that to the output file
print(prev)
final.append(prev)
new_txt.write(prev+'\n')
new_txt.close()

#Now merging the same line numbers (which are combined in the E_Input_file ) in H_Input_file
new_txt_out=open('<PATH> /SH_Output_file.txt','a')
with open('<PATH> /SH_Input_file.txt','r') as fp:
    line=fp.readline()
    c=1
    prev=""
    pres_root=-1
    while line:
        if line[len(line)-1]=='\n':
            line=line[:len(line)-1]
        if c in combined.keys():
            l=combined[c]
            pres=line
            if len(l)==1:
                new_txt_out.write(pres)
                new_txt_out.write('\n')
                pres_root=-1
            else:
                prev+=line+' '
                pres_root=c
        elif pres_root!=-1:
            if c in combined[pres_root]:
                prev+=line+' '
            li=combined[pres_root]
            if c==li[len(li)-1]:
                new_txt_out.write(prev)
                new_txt_out.write('\n')
                pres_root=-1
                prev=""
                
        line=fp.readline()
        c+=1

new_txt_out.write('\n')
new_txt_out.close()
