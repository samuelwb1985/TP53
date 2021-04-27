
import sys

inFile = open(sys.argv[1])
exampleFile = open(sys.argv[2])
outFile = open(sys.argv[3], "w")

# read inFile into a matrix
inMatrix = []

for line in inFile:
	lineList = line.rstrip("\n").rstrip("\r").split("\t")

	inMatrix.append(lineList)

# get example file header
exampleMatrix = []

exampleMatrix.append(exampleFile.readline().rstrip("\n").rstrip("\r").split("\t"))
exampleMatrix.append(exampleFile.readline().rstrip("\n").rstrip("\r").split("\t"))
exampleMatrix.append(exampleFile.readline().rstrip("\n").rstrip("\r").split("\t"))

# create outMatrix
outMatrix = []
outMatrix.append(exampleMatrix[0])
outMatrix.append(exampleMatrix[1])
outMatrix.append(exampleMatrix[2])

nextRow = []

for colIndex in range(1, len(inMatrix[0])):
	thisSample = inMatrix[0][colIndex]

	nextRow.append(thisSample)

outMatrix.append(nextRow)

for colIndex in range(0, len(outMatrix[1])):
	thisMutation = outMatrix[1][colIndex]
	thisMutationSubtype = outMatrix[2][colIndex]

	context = thisMutation + "_" + thisMutationSubtype

	# find row in inMatrix with this context
	whichRow = ""

	for rowIndex in range(1, len(inMatrix)):
		if inMatrix[rowIndex][0] == context:
			whichRow = rowIndex
			break

	outRow = inMatrix[whichRow][1:]

	outMatrix.append(outRow)

# write to output file
for line in outMatrix:
	outFile.write("\t".join(line) + "\n")

inFile.close()
outFile.close()

