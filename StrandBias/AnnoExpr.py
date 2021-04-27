
import sys

inFile = open(sys.argv[1])
rnaThresh = float(sys.argv[2])
outFile = open(sys.argv[3], "w")

# get header
header = inFile.readline().rstrip("\n").split("\t")
outFile.write("\t".join(header) + "\n")

# annotate and keep as needed
for line in inFile:
	lineList = line.rstrip("\n").split("\t")

	# Sample  Chrom   Pos     Ref     Alt     MutContext      Annotation      Strand  CombinedAnno    RNA_TPM
	# SJALL018365_D1  chr1    16475118        G       A       C>T_TCC 1$-$16450831$16482604$EPHA2     Untranscribed   C>T_TCC|Untranscribed   NA
	tpmVal = lineList[-1]

	if tpmVal == "NA":
		continue

	tpmVal = float(tpmVal)

	if tpmVal >= rnaThresh:
		lineList[0] += "_HighTpm"
	else:
		lineList[0] += "_LowTpm"

	outFile.write("\t".join(lineList) + "\n")

inFile.close()
outFile.close()

