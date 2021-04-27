#!/bin/bash

# detect signatures using SigProfiler

module load matlab

mkdir -p temp
mkdir -p output

bsub -J ParNonClust -q compbio -e stderr.err -o stdout.out -R rusage[mem=10000] "matlab -r SamSigProfilerSingleSample_RealSamples" 

