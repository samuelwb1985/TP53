
import sys

inFile = open(sys.argv[1])
tcgaMetaFile = open(sys.argv[2])
pcawgMetaFile = open(sys.argv[3])
targetMetaFiles = open(sys.argv[4])
pcgpFile = open(sys.argv[5])
outFile = open(sys.argv[6], "w")

# get dict where sample -> cancer type from TCGA
cancerDict = {}

header = tcgaMetaFile.readline().rstrip("\n").split("\t")

for line in tcgaMetaFile:
        lineList = line.rstrip("\n").split("\t")

        sample = lineList[header.index("TcgaBarcode")]
        cancer = lineList[header.index("CancerType")]

        cancerDict[sample] = cancer

# get cancer type for PCAWG samples
pcawgHeader = pcawgMetaFile.readline().rstrip("\n").split("\t")

for line in pcawgMetaFile:
        lineList = line.rstrip("\n").split("\t")

        patient = lineList[pcawgHeader.index("donor_id/donor_count")]
        cancerType = lineList[pcawgHeader.index("project_id/project_count")].split("-")[0]

        cancerDict[patient] = cancerType

# get dict where PCGP prefix -> cancer type
pcgpDict = {}

for line in pcgpFile:
	lineList = line.rstrip("\n").split("\t")

	pcgpDict[lineList[0]] = lineList[1]

# get cancer type for TARGET samples
cancerList = targetMetaFiles.read().split("\n")
cancerList.pop()

for thisFile in cancerList:
        cancerType = thisFile.split("/")[-1].split(".")[1].split("_")[0].upper()

        openFile = open(thisFile)
        openFile.readline()

        for line in openFile:
                thisSample = line.split("\t")[0]
		thisSampleCut = thisSample.split("-")[2]

                cancerDict[thisSampleCut] = cancerType

        openFile.close()

# add cancer type
header = inFile.readline().rstrip("\n").split("\t")
cancerLine = []
cancerLine.append("CancerType")

outFile.write("\t".join(header) + "\n")

for colIndex in range(1, len(header)):
        sample = header[colIndex]

	# get cancer type
	cancerType = "Unknown"

	if sample.startswith("SJALL"):
		cancerType = "ALL"
	elif sample.startswith("SJ"):
                # get the prefix of the SJID
                sjid = sample
                preFix = ""

                if sjid.startswith("SJE2A"):
                        preFix = "SJE2A"
                else:
                        for index in range(0, len(sjid)):
                                thisChar = sjid[index]

                                if not thisChar.isdigit():
                                        preFix += thisChar
                                else:
                                        break

                # get cancer type from prefix
                cancerType = pcgpDict[preFix]
	elif sample.startswith("DO") or sample.startswith("TCGA"):
                cancerType = cancerDict[sample]
	else: # TARGET samples
		cancerType = cancerDict[sample.split("-")[2]]

	if cancerType == "Unknown":
		sys.exit("ERROR: Couldn't find cancer type.")

	cancerLine.append(cancerType)

# write output
outFile.write("\t".join(cancerLine) + "\n")

for line in inFile:
	outFile.write(line)

inFile.close()
tcgaMetaFile.close()
pcawgMetaFile.close()
targetMetaFiles.close()
outFile.close()

