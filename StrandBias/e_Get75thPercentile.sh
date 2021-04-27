#!/bin/bash

module load python/2.7.12

inFile=NALM6_mRNA_TPM.txt 

python GetPercentile.py $inFile  

