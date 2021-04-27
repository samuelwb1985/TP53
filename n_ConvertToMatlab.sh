#!/bin/bash

# converts mutation context data to Matlab format

module load matlab

bsub -J Convert -q standard -e stderr.err -o stdout.out -R rusage[mem=10000] "(echo filename=\'Mega_TrinucPrep.txt\'; cat get.mat.from.txt.m) | matlab"

