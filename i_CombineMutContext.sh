#!/bin/bash

ls SmallMutList_NonClust_Split_*mutcontext.txt > FileList.txt

inFile=FileList.txt
outFile=TARGET-SCMC-PCGP-R3_SNVs_Combined.mutcontext.txt

bsub -J CombineMut -q standard -e stderr.err -o stdout.out -R rusage[mem=2000] "python -u CombineMutContext.py $inFile $outFile"

