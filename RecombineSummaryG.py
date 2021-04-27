
import sys

inFile = open(sys.argv[1])
outFile = open(sys.argv[2], "w")

# get list of files
fileList = inFile.read().split("\n")
fileList.pop()

# combine files into one
firstFile = True

outMatrix = []

for thisFile in fileList:
	inMatrix = []

	openFile = open(thisFile)

	for line in openFile:
		lineList = line.rstrip("\n").split("\t")
		inMatrix.append(lineList)

	openFile.close()

	if firstFile:
		firstFile = False

		for thisRow in inMatrix:
			outMatrix.append(thisRow)
	else:
		for colIndex in range(1, len(inMatrix[0])):
			for rowIndex in range(0, len(inMatrix)):
				outMatrix[rowIndex].append(inMatrix[rowIndex][colIndex])

# write to output file
for line in outMatrix:
	outFile.write("\t".join(line) + "\n")

inFile.close()
outFile.close()

