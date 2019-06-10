
***
This code splits the hindi and english glossary into words and sentences and places them in different files.

***
eng=open('<PATH>/english_glossary.txt','r')
hin=open('<PATH> /hindi_glossary.txt','r')
new_eng1=open('<PATH> /E_words.txt','a')
new_eng2=open('<PATH> /E_sentences.txt','a')
new_hin1=open('<PATH> /H_words.txt','a')
new_hin2=open('<PATH> /H_sentences.txt','a')

l=hin.readline()
while(l):
    x=l.split(":")
    if(len(x)==1):
        print(x)
    new_hin1.write(x[0]+'\n')
    new_hin2.write(x[1])
    l=hin.readline()
hin.close();
new_hin1.close()
new_hin2.close()


l=eng.readline()
while(l):
    x=l.split(":")
    if(len(x)==1):
        print(x)
    new_eng1.write(x[0]+'\n')
    new_eng2.write(x[1])
    l=hin.readline()
eng.close();
new_eng1.close()
new_eng2.close()
