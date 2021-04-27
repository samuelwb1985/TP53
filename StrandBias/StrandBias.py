
import sys

inFile = open(sys.argv[1])
refGeneFile = open(sys.argv[2])
outFile = open(sys.argv[3], "w")

# read inFile into a matrix
inMatrix = []

for line in inFile:
	lineList = line.rstrip("\n").split("\t")
	inMatrix.append(lineList)

# get dict for each chromosome
goodChroms = [i for i in range(1, 23)]
goodChromsString = [str(a) for a in goodChroms]

geneDict = {}

for i in goodChroms:
	geneDict[i] = set()

for line in refGeneFile:
	lineList = line.rstrip("\n").split("\t")

	chrom = lineList[2].replace("chr", "")
	direction = lineList[3]
	startPos = int(lineList[4])
	endPos = int(lineList[5])

	gene = lineList[12]

	#if gene.endswith("-AS1"):
	#	continue

	if chrom not in goodChromsString:
		continue

	geneDict[int(chrom)].add("$".join([chrom, direction, str(startPos), str(endPos), gene]))

# go through each mutation and see if it's in a coding region and if so, add strand info
#Sample  Chrom   Pos     Ref     Alt     MutContext
#SJALL018365_D1  chr1    16475118        G       A       C>T_TCC

counter = 0

for rowIndex in range(1, len(inMatrix)):
	if counter % 1000 == 0:
		print("On " + str(counter))
	counter += 1

	#Sample  Mutation        MutContext
	#1cceb0f8-3cd4-5f1f-b390-611270d57b18    1.673983.C.A    C>A_TCA

	chrom, pos, ref, alt = inMatrix[rowIndex][1].split(".") # = inMatrix[rowIndex][1].replace("chr", "")
	chrom = chrom.replace("chr", "")
	pos = int(pos)
	#pos = int(inMatrix[rowIndex][2])
	#ref = inMatrix[rowIndex][3]
	#alt = inMatrix[rowIndex][4]

	outList = []

	if chrom in goodChromsString:
		chrom = int(chrom)

		# check whether in any gene
		for thisEntry in geneDict[chrom]:
			aChrom, aDir, aStart, aEnd, aGene = thisEntry.split("$")

			aStart = int(aStart)
			aEnd = int(aEnd)

			if pos >= aStart and pos <= aEnd:
				outList.append(thisEntry)

	outString = ""

	if outList == []:
		outString = "NA"
	else:
		outString = "|".join(outList)

	inMatrix[rowIndex].append(outString)

inMatrix[0].append("Annotation")

# write to output file
for line in inMatrix:
	outFile.write("\t".join([str(a) for a in line]) + "\n")

inFile.close()
refGeneFile.close()
outFile.close()

