%% Example for running SigProfilerSingleSample 
%% The example examines 10 biliary adenocarcinoma whole-genomes from ICGC Mega and
%% assigns mutational signatures using upcoming release of Mega mutational signatures
%% Clearing all data
close all;
clearvars;
clc;
addpath('/research/rgs01/project_space/PCGP/PCGP/common/sam/Osteosarcoma/LudmilMatlabApr2018/tools/SigProfilerSingleSample/source/');

%% Starting the default cluster
if ( ~isempty(gcp('nocreate')) )
    delete(gcp);
end
c = parcluster;
job = parpool(c);

%% Analysis of all signatures in individual samples
tic
    analysis_individual_samples('/research/rgs01/project_space/PCGP/PCGP/common/sam/TP53_BinBing/Nalm6_MutSig/snv-indel-post/FilterBlat/COSMIC60_ReadyFormatted_PLUS-NOVEL_PlusNalm6.mat', ... % set of signatures
                                'Mega_TrinucPrep_UnnecessaryUnknowns.mat', ... % set of signatures in samples
                                'Mega_TrinucPrep_Plus.mat', ... % set of individual samples for examination
                                'output/', ... % output folder
                                'Mega_SingSampleOutput_Cosmic60.mat', ... % output file
                                0, ... % boolean variable indicating whether to use rules or not (1==use rules; 0==do not use rules)
                                [1 5], ... % IDs of signatures to be included in all samples regardless of rules or sparsity  
                                {[2 17], [7 8 9 10], [13 14], [21 22]}); % connected signatures (e.g., signatures SBS-2 and SBS-13)
toc
