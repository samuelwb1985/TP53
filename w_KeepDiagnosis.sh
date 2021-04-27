#!/bin/bash

inFile=TARGET-SCMC-PCGP-R3_SNVs_Combined_MutSigSummaryG.cancerType.txt
outFile=TARGET-SCMC-PCGP-R3_SNVs_Combined_MutSigSummaryG.cancerType.diagALL.txt

python KeepDiagnosisALL.py $inFile $outFile

