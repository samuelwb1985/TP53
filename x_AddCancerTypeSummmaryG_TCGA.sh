#!/bin/bash

inFile=TARGET-SCMC-PCGP-R3_SNVs_Combined_MutSigSummaryG.wTcgaPcawg.txt 
tcgaMetaFile=/research/rgs01/project_space/PCGP/PCGP/common/sam/Shanghai/AssembleSignatures/TCGA_PCAWG/ConvertUUIDStoTcgaBarcode/TCGA-PCAWG_ConvertList-REAL.filtered.cancerType.txt
pcawgMetaFile=/research/rgs01/project_space/PCGP/PCGP/common/sam/Shanghai/AssembleSignatures/PCAWG/manifest.aws-virginia.1532035756354.tsv
targetMetaFiles=Bayes/TARGET_FileList.txt
pcgpLookup=Bayes/PCGP_CancerTypes.txt
outFile=TARGET-SCMC-PCGP-R3_SNVs_Combined_MutSigSummaryG.wTcgaPcawg.cancerType.txt

python AddCancerTypeSummaryG_TCGA.py $inFile $tcgaMetaFile $pcawgMetaFile $targetMetaFiles $pcgpLookup $outFile

