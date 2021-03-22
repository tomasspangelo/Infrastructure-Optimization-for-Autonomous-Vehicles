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
#maxSize = nCore-1
nSubsets=0
cities = np.arange(1, nCities + 1)

f = open("subsets.txt", "w")
f.write("Subsets: [\n")
for i in range(2,maxSize+1):
    subsets=(list(itertools.combinations(cities, i)))
    for set in subsets:
        nSubsets+=1
        line=""
        for c in cities:
            if c in set:
                line+=str(1)+"\t"
            else: line += str(0)+"\t"
        f.writelines(line+"\n")
f.writelines("] \n")
f.writelines("nSubsets: "+str(nSubsets))

f.close()