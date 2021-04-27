#!/bin/bash

# get row and column names

inFile=Mega_SingSampleOutput_Cosmic60.txt
sampleNames=SAMPLE_NAMES_Mega_SingSampleOutput_Cosmic60.txt
headerFile=SIG_NAMES_Mega_SingSampleOutput_Cosmic60.txt
outFile=Header_Mega_SingSampleOutput_Cosmic60.txt

python AddHeaderRowAndColumn.py $inFile $sampleNames $headerFile $outFile 

