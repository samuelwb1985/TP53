#!/bin/bash

inFile=Nalm6_Tier1to3_SNV.goodblat.mutcontext.strand.summary.txt 
rnaFile=NALM6_mRNA_TPM.txt #/research/rgs01/project_space/PCGP/PCGP/common/sam/YanglingNBL/TCGA_Tim_Sig18/ForStrandBias/merge.TPM_sampleID.dnaRnaOverlap.TPM.rmdup.geneSymbol.sum.recalcTpm.txt 
outFile=Nalm6_Tier1to3_SNV.goodblat.mutcontext.strand.summary.rna.txt

bsub -J GetExpr -q standard -e stderr.err -o stdout.out -R rusage[mem=20000] "python -u AddGeneExpression.py $inFile $rnaFile $outFile"

