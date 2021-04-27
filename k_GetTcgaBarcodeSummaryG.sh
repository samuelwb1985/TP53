#!/bin/bash

inFile=TCGA_PCAWG_MutContext_SUMMARY_G.txt
idFile=/research/rgs01/project_space/PCGP/PCGP/common/sam/Shanghai/AssembleSignatures/TCGA_PCAWG/ConvertUUIDStoTcgaBarcode/TCGA-PCAWG_ConvertList-REAL.filtered.txt
outFile=TCGA_PCAWG_MutContext_SUMMARY_G.tcgaBarcode.txt

python GetTcgaBarcodeSummaryG.py $inFile $idFile $outFile

