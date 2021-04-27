#!/bin/bash

inFile=Header_Mega_SingSampleOutput_Cosmic60-novSigs-mmrThio.numMut.cosine.txt
noCosm15=NoRequire_COSMIC1or5/Header_Mega_SingSampleOutput_Cosmic60-novSigs-mmrThio.noReqCOSM1or5.numMut.cosine.txt
outFile=Mega_TP53_NonClustered_Cosmic60_mmrThio.IntegrateNo1-5.newR3.txt

python IntegrateMutSig.py $inFile $noCosm15 $outFile

