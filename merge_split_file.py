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
