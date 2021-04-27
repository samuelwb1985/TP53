#!/bin/bash

# add the number of mutations per sample

inFile=Header_Mega_SingSampleOutput_Cosmic60.txt
mutFile=TARGET-SCMC-PCGP-R3_SNVs_Combined_MutSigSummaryG.wTcgaPcawg.txt 
outFile=Header_Mega_SingSampleOutput_Cosmic60.numMut.txt

python AddNumMutations.py $inFile $mutFile $outFile

