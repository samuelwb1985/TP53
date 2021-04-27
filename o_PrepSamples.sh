#!/bin/bash

# prepares samples for signature detection by creating files telling whether there
# is any a priori knowledge of signatures in the samples being analyzed; in this
# case we assume no foreknowledge and so create dummy files

module load matlab

bsub -J PrepMat -q standard -e stderr.err -o stdout.out -R rusage[mem=10000] "matlab -r PrepForSingleSample_RealSamples"

