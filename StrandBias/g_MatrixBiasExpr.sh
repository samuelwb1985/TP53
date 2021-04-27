#!/bin/bash

inFile=Nalm6_Tier1to3_SNV.goodblat.mutcontext.strand.summary.rna.anno.txt 
outFile=Nalm6_Tier1to3_SNV.goodblat.mutcontext.strand.summary.rna.anno.G.txt

python MatrixBias.py $inFile $outFile

