
import sys

inFile = open(sys.argv[1])
idFile = open(sys.argv[2])
outFile = open(sys.argv[3], "w")

# get dict where uuid -> tcga id
idDict = {}

header = idFile.readline().rstrip("\n").split("\t")

for line in idFile:
	lineList = line.rstrip("\n").split("\t")

        uuid = lineList[header.index("Object ID")]
	tcgaId = lineList[header.index("TcgaBarcode")]

	idDict[uuid] = tcgaId

# convert to TCGA ID
header = inFile.readline().rstrip("\n").split("\t")

for index in range(1, len(header)):
	tcgaId = idDict[header[index]]

	header[index] = tcgaId

outFile.write("\t".join(header) + "\n")

for line in inFile:
	outFile.write(line)

inFile.close()
idFile.close()
outFile.close()

