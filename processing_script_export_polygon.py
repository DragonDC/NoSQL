import sys
import os.path

if (os.path.exists(sys.argv[1])):
	#1. Delete all blank lines from file
	file = sys.argv[1]
	with open(file,"r") as fin:
	    lines=fin.readlines()
	with open(file,"w") as fin:  
	    [fin.write(line) for line in lines if line.strip() ]

	#2. Delete last line
	with open(file, 'r') as fin:
	    data = fin.read().splitlines(True)
	with open(file, 'w') as fin:
	    fin.writelines(data[:-1])

	#3. Insert line at the beginning 
	f = open(file, "r")
	data = f.readlines()
	f.close()
	data.insert(0, "{\n \"type\": \"FeatureCollection\",\n \"features\": \n")

	#4. Add polygon
	f = open(file, "w")
	data = "".join(data)
	polygon = ("},\n{\n \"type\":\n \"Feature\",\n \"geometry\": {\n \"type\": \"Polygon\",\n \"coordinates\": " + 
			  "[[[ -102.077029, 41.052873 ], [ -95.236718, 37.044054 ], [ -99.447158, 32.029309 ], " + 
			  " [ -104.222035, 32.065320], [-109.057755, 37.023279], [ -102.077029, 41.052873 ]]]},\n " + 
			  "\"properties\": {\"value\": \"query field\"} \n} \n]}")
	f.write(data+polygon)
	f.close()
	print("OK")	
else:
	print("ERROR, couldn't find appropriate file")








