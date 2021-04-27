
import sys

inFile = open(sys.argv[1])
outFile = open(sys.argv[2], "w")

# get list of VCF files
vcfList = inFile.read().split("\n")
vcfList.pop()

firstHeader = ""
firstFile = True

for thisVcf in vcfList:
	sjid = thisVcf.split("/")[-1].split("_")[0]
	sampleId = thisVcf.split("/")[-1].split(".")[0]

	openFile = open(thisVcf)

	header = ""

	for line in openFile:
		if line.startswith("##"):
			pass
		elif line.startswith("#CHROM"):
			header = line.rstrip("\n").split("\t")
			header[-1] = "ThisSampleInfo"
			header.insert(0, "Sample")

			# if it's the header line, get header and write to outFile (if first header) or ensure it's equal to first header
			if firstFile:
				firstFile = False
				firstHeader = []

				for thisVal in header:
					firstHeader.append(thisVal)

				outFile.write("\t".join(header) + "\n")
			else:
				if header != firstHeader:
					sys.exit("ERROR: Unequal headers.")
		else: # these are actual mutation lines which you can write to the output file
			lineList = line.rstrip("\n").split("\t")
			lineList.insert(0, sampleId)

			# convert hg38 to hg19 #  SampleCounts=1;HG19=10.308578.G.A;ANN=A|
			infoLine = lineList[header.index("INFO")]

			if "HG19" in infoLine:
				hg19_string = infoLine.split("HG19=")[1].split(";")[0]

				chrom, pos, ref, alt = hg19_string.split(".")

				lineList[header.index("#CHROM")] = chrom
				lineList[header.index("POS")] = pos
				lineList[header.index("REF")] = ref
				lineList[header.index("ALT")] = alt

				# cut INFO line if it's super long
				if len(infoLine) > 2000:
					infoLine = infoLine[:2000] + "|CUT-OFF-TOO-LONG"
					lineList[header.index("INFO")] = infoLine

				outFile.write("\t".join(lineList) + "\n")

	openFile.close()

inFile.close()
outFile.close()

