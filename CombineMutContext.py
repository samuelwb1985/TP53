
import sys

inFile = open(sys.argv[1])
outFile = open(sys.argv[2], "w")

# get file list
fileList = inFile.read().split("\n")
fileList.pop()

# combine files
firstFile = True
firstHeader = ""

counter = 1

for thisFile in fileList:
	print counter
	counter += 1

	openFile = open(thisFile)

	if firstFile:
		firstHeader = openFile.readline().rstrip("\n").split("\t")

		outFile.write("\t".join(firstHeader) + "\n")

		for line in openFile:
			outFile.write(line)

		firstFile = False
	else:
                header = openFile.readline().rstrip("\n").split("\t")

		if header != firstHeader:
			print header
			print firstHeader
			sys.exit("ERROR: Unequal headers.")

                for line in openFile:
                        outFile.write(line)

	openFile.close()

inFile.close()
outFile.close()

