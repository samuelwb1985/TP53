#!/bin/bash

inFile=Nalm6_Tier1to3_SNV.goodblat.mutcontext.strand.summary.rna.txt 
tpmThresh=69.45 # 75th percentile of expression
outFile=Nalm6_Tier1to3_SNV.goodblat.mutcontext.strand.summary.rna.anno.txt

python AnnoExpr.py $inFile $tpmThresh $outFile

