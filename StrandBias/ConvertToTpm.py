
import sys

inFile = open(sys.argv[1])
outFile = open(sys.argv[2], "w")

# read inFile into matrix
inMatrix = []

for line in inFile:
	lineList = line.rstrip("\n").rstrip("\r").split("\t")

	lineCut = []
	lineCut.append(lineList[1])
	lineCut.extend(lineList[6:])
	inMatrix.append(lineCut)

# convert to TPM
for colIndex in range(1, len(inMatrix[0])):
	# get column sum
	colSum = 0

	for rowIndex in range(1, len(inMatrix)):
		colSum += float(inMatrix[rowIndex][colIndex])

	# divide by column sum
	for rowIndex in range(1, len(inMatrix)):
		thisVal = float(inMatrix[rowIndex][colIndex])
		thisValNew = 1000000 * thisVal / float(colSum)

		inMatrix[rowIndex][colIndex] = str(thisValNew)

# write to output file
for line in inMatrix:
	outFile.write("\t".join(line) + "\n")

inFile.close()
outFile.close()

