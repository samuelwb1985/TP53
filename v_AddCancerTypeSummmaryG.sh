#!/bin/bash

inFile=TARGET-SCMC-PCGP-R3_SNVs_Combined_MutSigSummaryG.txt
targetMetaFiles=Bayes/TARGET_FileList.txt
pcgpLookup=Bayes/PCGP_CancerTypes.txt
outFile=TARGET-SCMC-PCGP-R3_SNVs_Combined_MutSigSummaryG.cancerType.txt

python AddCancerTypeSummaryG.py $inFile $targetMetaFiles $pcgpLookup $outFile

