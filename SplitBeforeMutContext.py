
import sys
from operator import itemgetter

inFile = open(sys.argv[1])
numPatients = int(sys.argv[2])
outBase = sys.argv[3]

# read inFile into a matrix and sort
inMatrix = []

for line in inFile:
	lineList = line.rstrip("\n").split("\t")

	inMatrix.append(lineList)

inMatrix = sorted(inMatrix, key = itemgetter(0))

# inFile format:
#Sample  Chr     Pos     Chr_Allele      Alternative_Allele      Source  MutContext
#TARGET-10-PAIXPH-03A-01D        4       128743955       A       G       TARGET  T>C_TTT
#TARGET-10-PAIXPH-03A-01D        5       31317500        G       T       TARGET  C>A_GCA
#TARGET-10-PAIXPH-03A-01D        7       6731767 T       C       TARGET  T>C_ATA
#TARGET-10-PAIXPH-03A-01D        7       146536993       C       T       TARGET  C>T_TCT

#Sample  Mutation
#DO46416 1.1230448.G.A
#DO46416 1.1609723.C.T

whichPatient = 0
whichFile = 0

firstTime = True
lastPatient = ""

openFile = open(outBase + "_1.txt", "w")

for rowIndex in range(0, len(inMatrix)):
	lineList = inMatrix[rowIndex]
        line = "\t".join(lineList) + "\n"

	thisPatient = lineList[0]

	if firstTime: # if first line, just write to first open file
		lastPatient = thisPatient
		openFile.write(line)

		firstTime = False
	else: # if not first line...
		if thisPatient == lastPatient: # if it's the same patient as the last patient, just write to output file
			openFile.write(line)
		else: # but if it's a new patient, we need to check whether we've hit the limit
			whichPatient += 1 # increment the patient

			if whichPatient % numPatients == 0: # if the new patient increment filled up our last file, start a new file
				whichFile += 1
				openFile.close()

				openFile = open(outBase + "_" + str(whichPatient + 1) + ".txt", "w")

				print("Writing to file " + outBase + "_" + str(whichPatient + 1) + ".txt")

				openFile.write(line)
		
				lastPatient = thisPatient
			else:
				openFile.write(line)
				lastPatient = thisPatient

inFile.close()

