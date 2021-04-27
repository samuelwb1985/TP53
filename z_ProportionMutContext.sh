#!/bin/bash

inMutSigFile=TCGA_PCAWG_MutContext_SUMMARY_G.txt 
outFile=TCGA_PCAWG_MutContext_SUMMARY_G.proportion.txt

python ProportionMutContext.py $inMutSigFile $outFile

