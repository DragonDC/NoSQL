#1. Delete all blank lines from file
file = sys.argv[1]
with open(file,"r") as fin:
    lines=fin.readlines()
with open(file,"w") as fin:  
    [fin.write(line) for line in lines if line.strip() ]

#2. Delete first three lines and the last one
with open(file, 'r') as fin:
    data = fin.read().splitlines(True)
with open(file, 'w') as fin:
    fin.writelines(data[3:-1])

#3. Add at the beginning of file '['	
f = open(file, "r")
data = f.readlines()
f.close()
data.insert(0, '[\n')

f = open(file, "w")
data = "".join(data)
f.write(data)
f.close()	
