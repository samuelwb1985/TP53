
import sys

inFile = open(sys.argv[1])
cosineFile = open(sys.argv[2])
outFile = open(sys.argv[3], "w")

# get cosine for each sample and store in dict
cosineDict = {} # dict where sample -> cosine similarity

for line in cosineFile:
	# looking for line like this:
	# Sample #208: Relapsed ALL SJTALL013798_D1 with 2 signatures and an accuracy of 0.94
	if line.startswith("Sample #") and "signatures and an accuracy of" in line:
		lineList = line.rstrip("\n").split(" ")
		sample = lineList[4]
		cosine = lineList[-1]

		cosineDict[sample] = cosine

# read inFile into matrix
inMatrix = []

for line in inFile:
	lineList = line.rstrip("\n").split("\t")

	inMatrix.append(lineList)

# add last row with cosine
lastRow = []
lastRow.append("CosineSim")

for colIndex in range(1, len(inMatrix[0])):
	thisSample = inMatrix[0][colIndex]

	cosineThisSample = cosineDict[thisSample]
	lastRow.append(str(cosineThisSample))

inMatrix.append(lastRow)

# write to output file
for line in inMatrix:
	outFile.write("\t".join(line) + "\n")

inFile.close()
cosineFile.close()
outFile.close()

