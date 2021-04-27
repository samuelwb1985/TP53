#!/bin/bash

ls SmallMutList_NonClust_Split_*MutSigSummaryG.txt > SummaryList.txt 

inFile=SummaryList.txt
outFile=TARGET-SCMC-PCGP-R3_SNVs_Combined_MutSigSummaryG.txt

python RecombineSummaryG.py $inFile $outFile

