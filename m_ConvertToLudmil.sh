#!/bin/bash

# converts mutation context text file into a format that can be read into Matlab

inFile=TARGET-SCMC-PCGP-R3_SNVs_Combined_MutSigSummaryG.wTcgaPcawg.txt 
exampleFile=/research/rgs01/project_space/PCGP/PCGP/common/sam/Shanghai/AssembleSignatures/V2_IOTA_FilteredPatients/SCMC_TrinucPrep.txt
outFile=Mega_TrinucPrep.txt

python ConvertToLudmilReal.py $inFile $exampleFile $outFile

