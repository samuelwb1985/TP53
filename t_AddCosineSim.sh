#!/bin/bash

# add the cosine similarity - how well each sample
# was explained by the signatures

inFile=Header_Mega_SingSampleOutput_Cosmic60.numMut.txt
cosineFile=Cosine_stdout.out
outFile=Header_Mega_SingSampleOutput_Cosmic60-novSigs-mmrThio.numMut.cosine.txt

python AddCosineSim.py $inFile $cosineFile $outFile

