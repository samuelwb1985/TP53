#!/bin/bash

inFile=TARGET-SCMC-PCGP-R3_SNVs_Combined.txt 
numPatients=10
outBase=SmallMutList_NonClust_Split

bsub -J Split -q standard -e stderr.err -o stdout.out -R rusage[mem=4000] "python SplitBeforeMutContext.py $inFile $numPatients $outBase"

