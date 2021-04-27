#!/bin/bash

targetFile=panCGI_filter_rescued_tier123.txt
scmcFile=XmaSuperSnv.NoSplit.txt
r3Files=SJALL040467-R3_Tier1to3_SNV.goodblat.txt,SJBALL013787-R3_Tier1to3_SNV.goodblat.rename.txt 
pcgpFile=PCGP_SNVs.txt
outFile=TARGET-SCMC-PCGP-R3_SNVs_Combined.txt

python CombineVars.py $targetFile $scmcFile $r3Files $pcgpFile $outFile

