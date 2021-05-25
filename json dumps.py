import json
Valus1=["neelam","programer","24","2400"]
key=["name","Designation","age","salary"]
emp1={}
emp2={}
emp3={}
emp4={}
pihu1={}
i=0
while i<len(Valus1):
    key1=key[i]
    j=0
    while j<len(Valus1):
        emp1[key[j]]=Valus1[i]
        j=j+1
    i=i+1
pihu1["emp1"]=emp1
Valus2=["komal","trainer","24","20000"]
key=["name","Designation","age","salary"]
p=0
while p<len(Valus2):
    key1=key[p]
    b=0
    while b<len(Valus2):
        emp2[key[b]]=Valus2[p]
        b=b+1
    p=p+1
pihu1["emp2"]=emp2
Valus3=["anuradha","HR","25","40000"]
key=["name","Designation","age","salary"]
t=0
while t<len(Valus3):
    key1=key[t]
    r=0
    while r<len(Valus3):
        emp3[key[r]]=Valus3[t]
        r=r+1
    t=t+1
pihu1["emp3"]=emp3
Valus4=["Abhishek","manager","29","63000"]  
key=["name","Designation","age","salary"]
u=0
while u<len(Valus4):
    key1=key[u]
    o=0
    while o<len(Valus4):
        emp4[key[o]]=Valus4[u]
        o=o+1
    u=u+1
pihu1["emp4"]=emp4

import json
out_file= open("myfile.json", "w")
json.dump(pihu1,out_file,
indent = 6)
out_file.close() 

 



    


        
