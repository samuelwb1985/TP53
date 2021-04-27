# From mutation signature summary data, calculates the percentage of each mutation
# from the absolute numbers of mutations

import sys

inFile = sys.argv[1]
outFile = sys.argv[2]

# read input file into matrix
inMatrix = []

inputFile = open(inFile)

for line in inputFile:
	inMatrix.append(line.rstrip("\n").split("\t"))

inputFile.close()

# go through each column and change to percent
for colIndex in range(1, len(inMatrix[0])):
	# get column sum
	columnSum = 0

	for rowIndex in range(1, len(inMatrix)):
		columnSum += int(inMatrix[rowIndex][colIndex])

	# go through each value and convert to percentage		
	for rowIndex in range(1, len(inMatrix)):
                newValue = ""

		if columnSum == 0:
                        newValue = 0
                else:
                        newValue = float(inMatrix[rowIndex][colIndex]) / float(columnSum)

                inMatrix[rowIndex][colIndex] = newValue


# change format of mutation context from C>A_ACT to C[C>T]T
for rowIndex in range(1, len(inMatrix)):
	thisContext = inMatrix[rowIndex][0]

	conversion, context = thisContext.split("_")

	newContextName = context[0] + "[" + conversion + "]" + context[2]

	inMatrix[rowIndex][0] = newContextName

# output modified inMatrix to outFile
outputFile = open(outFile, "w")

for line in inMatrix:
	outputFile.write("\t".join([str(a) for a in line]) + "\n")

outputFile.close()

