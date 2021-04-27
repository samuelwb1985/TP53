#!/bin/bash

inFile=/research/rgs01/project_space/PCGP/PCGP/common/sam/TP53_BinBing/Nalm6_MutSig/snv-indel-post/FilterBlat/Nalm6_Tier1to3_SNV.goodblat.mutcontext.txt 
refGeneFile=refGene.txt
outFile=Nalm6_Tier1to3_SNV.goodblat.mutcontext.strand.txt

#python -u StrandBias.py $inFile $refGeneFile $outFile
bsub -J StrandBias -q standard -e stderr.err -o stdout.out -R rusage[mem=20000] python -u StrandBias.py $inFile $refGeneFile $outFile

