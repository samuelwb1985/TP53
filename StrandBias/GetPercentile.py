
import sys
import numpy as np

inFile = open(sys.argv[1])

# get percentile
rnaMatrix = []
firstLine = True

percentileList = []

for line in inFile:
        lineList = line.rstrip("\n").split("\t")

        if firstLine:
                firstLine = False

                lineList.append("Nalm6_Mean")
                rnaMatrix.append(lineList)
        else:
                firstVal = float(lineList[-2])
                secondVal = float(lineList[-1])

                meanTpm = (firstVal + secondVal) / 2.0

		percentileList.append(meanTpm)

                lineList.append(meanTpm)
                rnaMatrix.append(lineList)


percentileVal = np.percentile(percentileList, 75)

print("75th percentile of Nalm6 expression is " + str(percentileVal) + " TPM.")

inFile.close()

