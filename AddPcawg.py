
import sys

inFile = open(sys.argv[1])
tcgaFile = open(sys.argv[2])
pcawgFile = open(sys.argv[3])
outFile = open(sys.argv[4], "w")

# read inFile into a matrix
outMatrix = []

for line in inFile:
	lineList = line.rstrip("\n").split("\t")

	outMatrix.append(lineList)

# add tcgaFile to outMatrix
rowIndex = 0

for line in tcgaFile:
        lineList = line.rstrip("\n").split("\t")

	rowHeader = outMatrix[rowIndex][0]
	rowHeaderThisLine = lineList[0]

	if rowHeader != rowHeaderThisLine:
		sys.exit("ERROR: Unequal row headers.")

	outMatrix[rowIndex].extend(lineList[1:])

	rowIndex += 1

# add pcawgFile to outMatrix
rowIndex = 0

for line in pcawgFile:
        lineList = line.rstrip("\n").split("\t")

        rowHeader = outMatrix[rowIndex][0]
        rowHeaderThisLine = lineList[0]

        if rowHeader != rowHeaderThisLine:
                sys.exit("ERROR: Unequal row headers.")

        outMatrix[rowIndex].extend(lineList[1:])

        rowIndex += 1

# write to outFile
for line in outMatrix:
	outFile.write("\t".join(line) + "\n")

inFile.close()
tcgaFile.close()
pcawgFile.close()
outFile.close()

