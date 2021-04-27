
import sys

inFile = open(sys.argv[1])
outFile = open(sys.argv[2], "w")

# get header
header = inFile.readline().rstrip("\n").split("\t")

header.append("Strand")
header.append("CombinedAnno")
outFile.write("\t".join(header) + "\n")

# go through each line and establish strand bias
skippedMultiDir = 0
usedOnes = 0

for line in inFile:
	lineList = line.rstrip("\n").split("\t")

	biasInfo = lineList[-1]

	if biasInfo == "NA":
		lineList.append("NA")
		lineList.append("NA")

		outFile.write("\t".join(lineList) + "\n")
		continue

	biasList = biasInfo.split("|")

	firstDir = ""
	differentDir = False

	for thisEntry in biasList:
		aChrom, aDir, aStart, aEnd, aGene = thisEntry.split("$")
		
		if firstDir == "":
			firstDir = aDir
		else:
			if firstDir != aDir: # multiple genes going different directions; enter NA
				differentDir = True

	if differentDir:
		skippedMultiDir += 1

		lineList.append("NA")
		lineList.append("NA")
		outFile.write("\t".join(lineList) +"\n")
	else: # figure out strandedness
		#Sample  Mutation        MutContext      Annotation
		#TCGA-AP-A0LE-01A-11D-A127-09    1.52176.T.G     T>G_CTA NA
		chrom, pos, mutRef, mutAlt = lineList[1].split(".")
		#mutRef = lineList[3]
		#mutAlt = lineList[4]

		transcribedOrNo = ""

		if mutRef == "G" or mutRef == "A":
			if firstDir == "+":
				transcribedOrNo = "Transcribed"
			elif firstDir == "-":
				transcribedOrNo = "Untranscribed"
			else:
				sys.exit("ERROR: Invalid directionality.")
		else:
                        if firstDir == "+":
                                transcribedOrNo = "Untranscribed"
                        elif firstDir == "-":
                                transcribedOrNo = "Transcribed"
                        else:
                                sys.exit("ERROR: Invalid directionality.")

		lineList.append(transcribedOrNo)

		mutContext = lineList[header.index("MutContext")]
		finalAnno = mutContext + "|" + transcribedOrNo
		lineList.append(finalAnno)

                outFile.write("\t".join(lineList) +"\n")

inFile.close()
outFile.close()

