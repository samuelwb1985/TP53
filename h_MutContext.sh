#!/bin/bash

# This bash script can be executed on the output file from step j to add a column to
# your VAF txt file that indicates the trinucleotide mutation context of each SNV. It
# also summarizes the number of mutations in each mutation cluster (each change pattern)
# with each mutation context (96 possible mutation contexts).

# This data can be used as input to deconstructSigs to perform mutation signature analysis.
# Please see documentation for deconstructSigs or contact Samuel Brady (Samuel.Brady@utah.edu)
# for more information on how to interface this output with deconstructSigs.

chromFastaFolder=/research/rgs01/resgen/prod/tartan/index/reference/Homo_sapiens/GRCh37-lite/FASTA/chromosomes  
for inFile in SmallMutList_NonClust_Split_*1.txt
do
	outFile=${inFile/txt/mutcontext.txt} 
	mutSigSummaryFile=${inFile/.txt/_MutSigSummaryG.txt}

	bsub -J MutContext -q standard -e stderr.err -o stdout.out -R rusage[mem=2000] "python -u MutContext.py $inFile $chromFastaFolder $outFile $mutSigSummaryFile"
done

