
import json
filename='data.txt'
pihu1={}
with open("data.tex") as fh:
    for line in fh:
        command, description=line.strip().split(None,1)
        pihu1[command]=description.strip()
out_file=open("test1.json","w")
json.dump(pihu1,out_file,indent=4,sort_keys=False)
out_file.close()
