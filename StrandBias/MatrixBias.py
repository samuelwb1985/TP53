# Author: Samuel Brady

# Gets mutation context for each mutation, given a matrix
# of mutations. It adds the mutation context to the matrix
# and summarizes the number of mutations with each signature
# in each change pattern.

import sys

inFile = sys.argv[1] # matrix of mutations
outSummaryFile = sys.argv[2] # summary of mutation contexts for each change pattern in inFile

# ***********first define a function that gets the mutation context for a  mutation************
# This function returns the mutation context (1 base before, the base itself, and 1 base after)
# given an input chromosome and site on that chromosome; the folder containing chromosome
# fasta files (i.e. "17.fa", etc.) is also an input to the function

# Note that inputting the first or last base on a chromosome will break this function

import os

# read inFile into a matrix (inMatrix)
inMatrix = []

inputFile = open(inFile)
header = inputFile.readline().rstrip("\n").split("\t")
inMatrix.append(header)

for line in inputFile:
	lineList = line.rstrip("\n").split("\t")

	if lineList[1] == "NA":
		continue

	inMatrix.append(lineList)
	
inputFile.close()

# ********* now summarize mutation signatures for each change pattern; start by making a list of possible mutation contexts (there are 96 total and range from "C>A_ACA" to "T>G_TTT")
possibleContexts = [] # will contain all possible contexts
sixPossibleChanges = ["C>A", "C>G", "C>T", "T>A", "T>C", "T>G"] # for each of these 6 there will be 16 contexts, making 96 total
fourBases = ["A", "C", "G", "T"]

for thisChange in sixPossibleChanges: # this triple loop makes a list of all possible contexts - we start with the 6 possible changes
	for firstBase in fourBases: # then we loop through the possible first bases ("A", "T", "G", or "C")
		for lastBase in fourBases: # then we loop through the possible last bases
			mutationContextString = ""
			mutationContextString += thisChange + "_" # we start making the mutation context string by showing the change (i.e. "G>A_"
			mutationContextString += firstBase # then we add the first base - the base prior to the mutation
			mutationContextString += thisChange[0] # then we add the base itself, which we know to be the first character in the "thisChange" string
			mutationContextString += lastBase # then we add the last base - the base after the mutation

			transcribedString = mutationContextString + "|Transcribed"
                        untranscribedString = mutationContextString + "|Untranscribed"

			possibleContexts.append(transcribedString) # then we add this to the "possibleContexts" list
                        possibleContexts.append(untranscribedString) # then we add this to the "possibleContexts" list

# great! now we have the list of possible mutation contexts - now we need to make a matrix where columns are change patterns, rows are mutation contexts, and
# the data are the number of mutations with a specific mutation context for each change pattern
# we'll start by making the empty matrix of mutation context data
mutationContextMatrix = []
changePatternSet = set()

for rowIndex in range(1, len(inMatrix)): # go through each row in change pattern out matrix and add the change pattern to the first row of mutationContextMatrix
	changePattern = inMatrix[rowIndex][header.index("Sample")]
	changePatternSet.add(changePattern)

# add each change pattern as a column header in first row
firstRow = []
firstRow.append("MutationContext") # give the first column header first though

for changePatt in changePatternSet:
	firstRow.append(changePatt)

mutationContextMatrix.append(firstRow) # give the mutationContextMatrix its first row with headers indicating change patterns

for thisContext in possibleContexts: # now go through each possible mutation context and make them the row headers - fill in the data with zeros also
	nextRow = []
	nextRow.append(thisContext) # row header is the mutation context

	nextRow.extend([int("0") for chgPattern in changePatternSet]) # for every change pattern put a zero into the matrix for this row

	mutationContextMatrix.append(nextRow) # now add this row to the mutationContextMatrix

# now that we have the matrix set up, we just need to fill it up with numbers;
# to do this, we'll loop through inMatrix (our general data table), and every
# time we find a valid mutation context (non-indel) we add data to the mutationContextMatrix
for rowIndex in range(1, len(inMatrix)):
	# get mutation context and change pattern for this row
	mutationContext = inMatrix[rowIndex][header.index("CombinedAnno")]
	thisRowChangePattern = inMatrix[rowIndex][header.index("Sample")]

	if mutationContext != "NotApp-Indel" and mutationContext != "NA": # if this is a valid mutation context (i.e. not a "C>CA" type indel or other unusable case)
		# if this is not an "NA", find the row and column index in the numerical mutationContextMatrix (that counts occurrences of contexts for each change pattern)
		# and increment it by 1
		rowIndexInMutationContextMatrix = possibleContexts.index(mutationContext) + 1
		colIndexInMutationContextMatrix = mutationContextMatrix[0].index(thisRowChangePattern)

		mutationContextMatrix[rowIndexInMutationContextMatrix][colIndexInMutationContextMatrix] += 1 # increment by 1

# write to output file
outSummaryFile = open(outSummaryFile, "w")

for line in mutationContextMatrix:
	outSummaryFile.write("\t".join([str(a) for a in line]) + "\n")

outSummaryFile.close()
