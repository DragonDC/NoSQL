import sys
import os.path

if (os.path.exists(sys.argv[1])):
	#1. Delete all blank lines from file
	file = sys.argv[1]
	with open(file,"r") as fin:
	    lines=fin.readlines()
	with open(file,"w") as fin:  
	    [fin.write(line) for line in lines if line.strip() ]
	
	#2. Insert lines at the beginning
	f = open(file, "r")
	data = f.readlines()
	f.close()
	data.insert(0, "{\n \"type\": \"FeatureCollection\",\n \"features\": \n")
	
	#3. Add at the end of file '}'	
	f = open(file, "w")
	data = "".join(data)
	f.write(data+'}')
	f.close()
	print("OK")	
else:
	print("ERROR, couldn't find appropriate file")
