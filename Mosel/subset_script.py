import itertools
import numpy as np

nCities = 0
nCore = 0
Z = 0

# Read number of cities from AutonomaxData.txt
f = open("AutonomaxData.txt", "r")
line = f.readline()
while line:
    line = str(line)
    if "nCities" in line:
        nCities = int(line.split(":")[-1].strip())
        break
f.close()

# Read number of cities in core net and cyclic/path from mosel parameter environment
f = open("autonomax.mos", "r")
line = f.readline()
while line:
    line = str(line)
    if "NC" in line:
        nCore = int(line.split(";")[0].split("=")[-1].strip())
    elif "Z" in line:
        Z = int(line.split(";")[0].split("=")[-1].strip())
        break
    line = f.readline()

f.close()

# maxSize of subsets is dependent on whether the core net is cyclic or not
if Z == 1:
    maxSize = int(np.floor(nCore / 2))
if Z == 0:
    maxSize = nCore - 1

nSubsets = 0
cities = np.arange(1, nCities + 1)  # Array containing 1, 2 ... nCities

# Creates subsets and writes to subsets.txt
f = open("subsets.txt", "w")
f.write("Subsets: [\n")
for i in range(2, maxSize + 1):
    subsets = (list(itertools.combinations(cities, i)))
    for set in subsets:
        nSubsets += 1
        line = ""
        for c in cities:
            if c in set:
                line += str(1) + "\t"
            else:
                line += str(0) + "\t"
        f.writelines(line + "\n")
f.writelines("] \n")
f.writelines("nSubsets: " + str(nSubsets))

f.close()
