
import sys

inFile = open(sys.argv[1])
sampleFile = open(sys.argv[2])
headerFile = open(sys.argv[3])
outFile = open(sys.argv[4], "w")

# get sample names
sampleNames = sampleFile.read().split("\n")
sampleNames.pop()

# get header
header = headerFile.read().split("\n")

# create output matrix
outMatrix = []

# get inFile
index = 1

for line in inFile:
	lineList = line.rstrip("\n").split("\t")

	lineList.insert(0, header[index])

	outMatrix.append(lineList)

	index += 1

# add output header
outHeader = []
outHeader.append("Sig")
outHeader.extend(sampleNames[1:])
outMatrix.insert(0, outHeader)

# write to output file
for line in outMatrix:
	outFile.write("\t".join(line) + "\n")

inFile.close()
headerFile.close()
outFile.close()

