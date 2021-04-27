
%%%%%%%% Prepare the raw data for this sample %%%%%%%%%%%

%% load signature data
%%sigData = load('res_all_mut_matrix_full_signatures_3.mat');
%%sigData = load('PCGP_ReAnalyze_TrinucPrep.mat')
sigData = load('Mega_TrinucPrep.mat')

%% get number of signatures
sizeVec = size(sigData.originalGenomes);
numSamples = sizeVec(2);

%% sequencing type
seqType = cell(numSamples,1);
for i=1:numSamples; seqType{i} = 'WGS'; end

[sigData(:).seqType] = seqType;

% cancer type
thisType = 'Relapsed ALL'; %%sigData.input.cancerType;

cancerType = cell(numSamples,1);
for i=1:numSamples; cancerType{i} = thisType; end

[sigData(:).cancerType] = cancerType;

save('Mega_TrinucPrep_Plus.mat', '-struct', 'sigData');

%%%%%%%% Prepare the pre-prepared data that we actually don't know %%%%%%%%%%%
sigs60plusNovel = load('/research/rgs01/project_space/PCGP/PCGP/common/sam/TP53_BinBing/Nalm6_MutSig/snv-indel-post/FilterBlat/COSMIC60_ReadyFormatted_PLUS-NOVEL_PlusNalm6.mat')  %Consensus_subs_mutational_signatures_PLUS-NOVEL.mat');

sigsToTestSize = size(sigs60plusNovel.signatureNames);
numSigsCosmic = sigsToTestSize(1);

verTwo = sigData;

[verTwo(:).cancerTypes] = {'Relapsed ALL'};
[verTwo(:).sampleCancerTypes] = sigData.cancerType;
[verTwo(:).sigNames] = sigs60plusNovel.signatureNames;
[verTwo(:).signaturesInSamples] = zeros(numSigsCosmic, numSamples); %% don't tell it to look for specific signatures yet - use all zeros %% char.empty(numSigs,0);

%% cancer type
[verTwo(:).sampleCancerTypes] = cancerType;


%% add in signatures to test
[verTwo(:).signaturesInCancerTypes] = char.empty(numSamples,0);
[verTwo(:).signaturesInCancerTypes] = zeros(1, numSigsCosmic) + 1; % test all signatures (+ 1 part)
%verTwo.signaturesInCancerTypes(1,1) = 1;
%verTwo.signaturesInCancerTypes(1,2) = 1;
%verTwo.signaturesInCancerTypes(1,3) = 1;
%verTwo.signaturesInCancerTypes(1,5) = 1;
%verTwo.signaturesInCancerTypes(1,17) = 1;
%verTwo.signaturesInCancerTypes(1,23) = 1;
%verTwo.signaturesInCancerTypes(1,36) = 1;

save('Mega_TrinucPrep_UnnecessaryUnknowns.mat', '-struct', 'verTwo');
quit()

