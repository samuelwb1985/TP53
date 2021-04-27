
import sys

inFile = open(sys.argv[1])
outFile = open(sys.argv[2], "w")

# get header
header = inFile.readline().rstrip("\n").split("\t")
header2 = inFile.readline().rstrip("\n").split("\t")

# get columns with diagnosis samples ALL samples
goodCols = []
goodCols.append(0)

addedPatients = set()

sjTypeSet = set()
targetTypeSet = set()

for colIndex in range(1, len(header)):
        sample = header[colIndex]

	# skip non-ALL
	cancerType = header2[colIndex]

	if cancerType != "ALL":
		continue

	# figure out if diagnosis
	if sample.startswith("SJ"):
		patient, sampleType = sample.split("_")

		sjTypeSet.add(sampleType) # set(['R1', 'R3', 'S', 'R', 'D1', 'D'])

		if sampleType in ["D1","D"]:
			if patient in addedPatients:
				print("Skipping " + patient + " second diagnosis sample.")
			else:
				goodCols.append(colIndex)
	else: # TARGET samples
		sampleType = sample.split("-")[3][:2]
		patient = sample.split("-")[2]

		targetTypeSet.add(sampleType) # set(['03', '09', '40', '04'])

                if sampleType in ["03","09"]:
                        if patient in addedPatients:
                                print("Skipping " + patient + " second diagnosis sample.")
                        else:
                                goodCols.append(colIndex)

# write good columns
outFile.write("\t".join([header[i] for i in goodCols]) + "\n")

for line in inFile:
	lineList = line.rstrip("\n").split("\t")

	outFile.write("\t".join([lineList[i] for i in goodCols]) + "\n")

print("Kept " + str(len(goodCols)) + " diagnosis ALL samples.")


#print sjTypeSet
#print targetTypeSet

inFile.close()
outFile.close()

