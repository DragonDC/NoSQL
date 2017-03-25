import sys
#python processing_script_export.py wynik3.geojson

#1. Delete all blank lines from file
file = sys.argv[1]
with open(file,"r") as fin:
    lines=fin.readlines()
with open(file,"w") as fin:  
    [fin.write(line) for line in lines if line.strip() ]
	
f = open(file, "r")
data = f.readlines()
f.close()

data.insert(0, "{\n \"type\": \"FeatureCollection\",\n \"features\": \n")

f = open(file, "w")
data = "".join(data)
f.write(data+'}')
f.close()		