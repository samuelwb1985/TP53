#!/bin/bash

inFile=NALM6_mRNA_fpkm.txt 
outFile=NALM6_mRNA_TPM.txt

python ConvertToTpm.py $inFile $outFile 

