import itertools
import numpy as np
import sys

nCities = int(sys.argv[1])
nCores = int(sys.argv[2])
maxSize=int(np.floor(nCores/2))

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


