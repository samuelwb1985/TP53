

import sys

inFile = open(sys.argv[1])
inFile1and5 = open(sys.argv[2])
outFile = open(sys.argv[3], "w")

# read inFile into a matrix
inMatrix = []

for line in inFile:
        lineList = line.rstrip("\n").rstrip("\r").split("\t")

        inMatrix.append(lineList)

# read other file into a matrix
inMatrix1and5 = []

for line in inFile1and5:
        lineList = line.rstrip("\n").rstrip("\r").split("\t")

        inMatrix1and5.append(lineList)

# check headers
if inMatrix[0] != inMatrix1and5[0]:
	sys.exit("ERROR: Unequal headers.")

# transpose
inMatrix = [list(a) for a in zip(*inMatrix)]
inMatrix1and5 = [list(a) for a in zip(*inMatrix1and5)]

# check headers
if inMatrix[0] != inMatrix1and5[0]:
        sys.exit("ERROR: Unequal headers.")

# if MMR-Thiop_Sig >= 100 and CosineSim >= 0.9, use the inFile1and5
for rowIndex in range(1, len(inMatrix)):
	mmrSigThio = int(inMatrix1and5[rowIndex][inMatrix[0].index("MMR-Thiop_Sig")])
        mmrSig26 = int(float(inMatrix1and5[rowIndex][inMatrix[0].index("Signature Subs-26")]))
        cosineVal = float(inMatrix1and5[rowIndex][inMatrix[0].index("CosineSim")])

        numMut = int(inMatrix1and5[rowIndex][inMatrix[0].index("NumMut")])
	
	if numMut == 0:
		numMut = 1

        mmrSigThio_Prop = float(mmrSigThio) / float(numMut)
        mmrSig26_Prop = float(mmrSig26) / float(numMut)

	# replace signature scores with those from the noCOSMIC1-5 run if conditions are met; could have done 1000 thresh for mmrSigThio except that we need to include TinN sample SJALL040471 which has only 164 mutations due to TinN
	if (mmrSigThio >= 100 and mmrSigThio_Prop >= 0.5 and cosineVal >= 0.9) or (mmrSig26 >= 1000 and mmrSig26_Prop >= 0.5 and cosineVal >= 0.9):
		print inMatrix[rowIndex][0]

		for colIndex in range(1, inMatrix[0].index("NumMut")):
			# switch values
			thisVal = inMatrix1and5[rowIndex][colIndex]
			inMatrix[rowIndex][colIndex] = thisVal
			
		inMatrix[rowIndex][inMatrix[0].index("CosineSim")] = str(cosineVal)
		inMatrix[rowIndex].append("Without_COSMIC1-5")
	else:
                inMatrix[rowIndex].append("Standard")

# write to outFile
inMatrix[0].append("Decision")

for line in inMatrix:
	outFile.write("\t".join(line) + "\n")

inFile.close()
outFile.close()

