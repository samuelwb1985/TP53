#!/bin/bash

inFile=TARGET-SCMC-PCGP-R3_SNVs_Combined_MutSigSummaryG.txt
tcgaFile=TCGA_PCAWG_MutContext_SUMMARY_G.tcgaBarcode.txt 
pcawgFile=PCAWG_MutContext_SUMMARY_G.txt
outFile=TARGET-SCMC-PCGP-R3_SNVs_Combined_MutSigSummaryG.wTcgaPcawg.txt

python AddPcawg.py $inFile $tcgaFile $pcawgFile $outFile

