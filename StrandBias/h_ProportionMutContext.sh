#!/bin/bash

inFile=Nalm6_Tier1to3_SNV.goodblat.mutcontext.strand.summary.rna.anno.G.txt
outFile=Nalm6_Tier1to3_SNV.goodblat.mutcontext.strand.summary.rna.anno.G.prop.txt

python ProportionMutContext.py $inFile $outFile

