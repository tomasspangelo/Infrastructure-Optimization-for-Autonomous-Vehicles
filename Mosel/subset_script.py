import itertools
import numpy as np
import sys
nCities = 0
nCore = 0
print("hello")
print("__________________")
print("__________________")
print("__________________")
f = open("AutonomaxData.txt","r")
line = f.readline()
while line:
    line = str(line)
    if "nCities" in line:
        nCities = int(line.split(":")[-1].strip())
    elif "nCore" in line:
        nCore = int(line.split(":")[-1].strip())
    line = f.readline()

f.close()

maxSize=int(np.floor(nCore/2))

cities = np.arange(1, nCities + 1)

f = open("subsets.txt", "w")
for i in range(2,maxSize+1):
    f.write("Subset"+str(i)+":[\n")
    subset=(list(itertools.combinations(cities, i)))
    for set in subset:
        line=""
        for c in set:
            line+=str(c)+"\t"
        f.writelines(line+"\n")
    f.writelines("]\n")

f.close()


