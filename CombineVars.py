
import sys

targetFile = open(sys.argv[1])  # panCGI_filter_rescued_tier123.txt
scmcFile = open(sys.argv[2]) # XmaSuperSnv.NoSplit.txt
r3Files = sys.argv[3].split(",") # SJALL040467-R3_Tier1to3_SNV.goodblat.txt
pcgpFile = open(sys.argv[4]) # PCGP_SNVs.txt
outFile = open(sys.argv[5], "w") 

# get TARGET data
#annovar_index   annovar_type    annovar_gene    annovar_class   annovar_aachange        annovar_cdna    annovar_isoform TARGET_CASE_ID  Trio    Hugo_Symbol     Variant_Classification  VariantType     dbSNP_RS        Mutation_Status PFAM_DOMAIN     Somatic_Score   Somatic_Rank    Somatic_quality Tumor_ReadCount_Alt     Tumor_ReadCount_Ref     Tumor_ReadCount_Total   Normal_ReadC
#4.128743955.A.G snv     HSPA4L  missense        K615R   c.A1844G        NM_014278       10-PAIXPH               HSPA4L  MISSENSE        SNP             Somatic PFAM:PF00012:HSP70      -1      0.161   SQHIGH  11      18      29      1       40      41              Cosmic_Gene     A       A       G       A       A       TARGET-10-PAIXPH-03A-01D  
header = targetFile.readline().rstrip("\n").rstrip("\r").split("\t")

for line in targetFile:
	lineList = line.rstrip("\n").rstrip("\r").split("\t")

        sample = lineList[header.index("Tumor_Sample_Barcode")]
        chrom = lineList[header.index("Chromosome")].replace("chr", "")
        site = lineList[header.index("Start_position")]
        ref = lineList[header.index("Reference_Allele")]
        alt = lineList[header.index("TumorSeq_Allele2")]

	outFile.write("\t".join([sample, chrom, site, ref, alt, "TARGET"]) + "\n")

# SCMC data
# no header
#SJALL018365_D1  chr1    16475118        G       A
#SJALL018365_R1  chr1    16475118        G       A
for line in scmcFile:
        lineList = line.rstrip("\n").rstrip("\r").split("\t")
	
	lineList[1] = lineList[1].replace("chr", "")

	lineList.append("SCMC")
        outFile.write("\t".join(lineList) + "\n")

# R3 data
#Sample  Mutation        MinD    TinD    MinN    TinN
#SJALL040467_R3_G1       chr10.122438387.T.C     5       27      0       33
#SJALL040467_R3_G1       chr10.34311495.G.T      8       24      0       25
for aFile in r3Files:
	r3File = open(aFile)

	header = r3File.readline().rstrip("\n").rstrip("\r").split("\t")

	for line in r3File:
		lineList = line.rstrip("\n").rstrip("\r").split("\t")

		sample = lineList[0].replace("_G1", "")
		chrom, pos, ref, alt = lineList[1].split(".")
		chrom = chrom.replace("chr", "")

		outFile.write("\t".join([sample, chrom, pos, ref, alt, "SCMC-R3"]) + "\n")

	r3File.close()

# PCGP file
#Sample  #CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  ThisSampleInfo
#SJBALL011_D     10      308578  .       G       A       .       .       SampleCounts=1;HG19=1
header = pcgpFile.readline().rstrip("\n").rstrip("\r").split("\t")

for line in pcgpFile:
        lineList = line.rstrip("\n").rstrip("\r").split("\t")

        sample = lineList[header.index("Sample")]
        chrom = lineList[header.index("#CHROM")].replace("chr", "")
        site = lineList[header.index("POS")]
        ref = lineList[header.index("REF")]
        alt = lineList[header.index("ALT")]

        outFile.write("\t".join([sample, chrom, site, ref, alt, "PCGP"]) + "\n")

targetFile.close()
scmcFile.close()
pcgpFile.close()
outFile.close()

