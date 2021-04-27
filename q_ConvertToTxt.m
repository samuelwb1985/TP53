

Data = load('/research/rgs01/project_space/PCGP/PCGP/common/sam/TP53_BinBing/Parallel_MegaReRun/NonClustered/output/Mega_SingSampleOutput_Cosmic60.mat')
dlmwrite('Mega_SingSampleOutput_Cosmic60.txt', Data.exposuresNew, 'delimiter', '\t')

T = table(Data.sigNames)
writetable(T,'SIG_NAMES_Mega_SingSampleOutput_Cosmic60.txt')

Q = table(Data.input.sampleNames)
writetable(Q,'SAMPLE_NAMES_Mega_SingSampleOutput_Cosmic60.txt')

quit()

