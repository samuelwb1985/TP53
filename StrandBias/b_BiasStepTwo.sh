#!/bin/bash

inFile=Nalm6_Tier1to3_SNV.goodblat.mutcontext.strand.txt 
outFile=Nalm6_Tier1to3_SNV.goodblat.mutcontext.strand.summary.txt

python BiasStepTwo.py $inFile $outFile

