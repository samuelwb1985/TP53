#!/bin/bash

ls /research/rgs01/project_space/PCGP/PCGP/common/sam/Osteosarcoma/Archive/MutSig/CompareToPecan/PCGP_vcf_scott/PCGP_vcf/single_sample_vcf/*vcf > VcfListPcgp.txt

inFile=VcfListPcgp.txt
outFile=PCGP_SNVs.txt

python GetPcgp.py $inFile $outFile

#cp /research/rgs01/project_space/PCGP/PCGP/common/sam/Osteosarcoma/Archive/MutSig/OsteoAutopsy/SJOS001101/SNV/SamAnalysis/PeCan_CisplatinSig/PeCan_Mut_Mat.txt ./

