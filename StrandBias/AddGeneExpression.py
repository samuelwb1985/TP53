
import sys

inFile = open(sys.argv[1])
rnaFile = open(sys.argv[2])
outFile = open(sys.argv[3], "w")

# read inFile into inMatrix
inMatrix = []

for line in inFile:
	lineList = line.rstrip("\n").split("\t")
	inMatrix.append(lineList)

# read rnaFile into rnaMatrix and get mean of two Nalm6 experiments
rnaMatrix = []
firstLine = True

for line in rnaFile:
        lineList = line.rstrip("\n").split("\t")
        
	if firstLine:
		firstLine = False

		lineList.append("Nalm6_Mean")
		rnaMatrix.append(lineList)
	else:
		firstVal = float(lineList[-2])
                secondVal = float(lineList[-1])

		meanTpm = (firstVal + secondVal) / 2.0

		lineList.append(meanTpm)
                rnaMatrix.append(lineList)

# get vector of gene locations
geneList = []

for rowIndex in range(0, len(rnaMatrix)):
	geneList.append(rnaMatrix[rowIndex][0])

# add RNA expression to inMatrix
for rowIndex in range(1, len(inMatrix)):
	# Sample  Chrom   Pos     Ref     Alt     MutContext      Annotation      Strand  CombinedAnno
	#SJALL018365_D1  chr1    16475118        G       A       C>T_TCC 1$-$16450831$16482604$EPHA2     Untranscribed   C>T_TCC|Untranscribed
	#SJALL018365_R1  chr1    16475118        G       A       C>T_TCC 1$-$16450831$16482604$EPHA2     Untranscribed   C>T_TCC|Untranscribed

	if rowIndex % 10000 == 0:
		print("On " + str(rowIndex))

	thisSample = inMatrix[rowIndex][inMatrix[0].index("Sample")]
        thisAnno = inMatrix[rowIndex][inMatrix[0].index("Annotation")]
        thisStrand = inMatrix[rowIndex][inMatrix[0].index("Strand")]
	
	if thisStrand not in ["Transcribed", "Untranscribed"]:
		inMatrix[rowIndex].append("NA")
		continue

	thisGene = thisAnno.split("|")[0].split("$")[-1]

	thisSampleCut = "-".join(thisSample.split("-")[:4])  # TCGA-AP-A0LE-01A-11D-A127-09

	if thisGene in geneList:
		thisGeneRow = geneList.index(thisGene)
		
		thisSampleCol = rnaMatrix[0].index("Nalm6_Mean")
		thisGeneExpr = rnaMatrix[thisGeneRow][thisSampleCol]

		inMatrix[rowIndex].append(thisGeneExpr)
	else: # gene must be in rnaMatrix; otherwise it's NA
                inMatrix[rowIndex].append("NA")

	#if rowIndex > 25000: # remove later
#		break

# write to output file
inMatrix[0].append("RNA_TPM")

for line in inMatrix:
	outFile.write("\t".join([str(a) for a in line]) + "\n")

inFile.close()
rnaFile.close()
outFile.close()

