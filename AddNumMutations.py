
import sys

inFile = open(sys.argv[1])
mutFile = open(sys.argv[2])
outFile = open(sys.argv[3], "w")

# get number of mutations for each sample and store in dict
mutDict = {} # dict where sample -> number of mutations

mutMatrix = []

for line in mutFile:
	lineList = line.rstrip("\n").rstrip("\r").split("\t")
	mutMatrix.append(lineList)

for colIndex in range(1, len(mutMatrix[0])):
	sample = mutMatrix[0][colIndex]

	# get sum of mutations
	mutSum = 0

	for rowIndex in range(1, len(mutMatrix)):
		mutSum += int(mutMatrix[rowIndex][colIndex])

	mutDict[sample] = mutSum

# read inFile into matrix
inMatrix = []

for line in inFile:
	lineList = line.rstrip("\n").rstrip("\r").split("\t")

	inMatrix.append(lineList)

# add last row with number of mutations
lastRow = []
lastRow.append("NumMut")

for colIndex in range(1, len(inMatrix[0])):
	thisSample = inMatrix[0][colIndex]

	numMutThisSample = mutDict[thisSample]
	lastRow.append(str(numMutThisSample))

inMatrix.append(lastRow)

# write to output file
for line in inMatrix:
	outFile.write("\t".join(line) + "\n")

inFile.close()
mutFile.close()
outFile.close()

