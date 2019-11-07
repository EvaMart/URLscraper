<-- http://www.popgen.dk/angsd/index.php/Genotype_Distribution-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
Works from version 0.913 and above. The latest developmental version can be found here github
This method allow for estimation of the expected genotype count or fractions for one or two individuals based on genotype likelihoods. This can be very usefull for a number of population genetic statistics including Relatedness and Heterozygosity.
Examples of genotypes fraction for a single individual
all 10 possible genotypes
pAA  pAC  pAG  pAT  pCC  pCG  pCT  pGG  pGT  pTT
0.293  9.3e-05  0.000331  7.3e-05  0.2  7.7e-05  0.000411  0.204  7e-05  0.302
number of derived alleles (use  SFS method )
pAA  pAD  pDD
0.9986  0.0003168  0.001127
or homozygoes vs. heterogoes
For two individuals it could be the full 10x10 possible genotype combination
Example of 10x10 genotype probability
AA     AC     AG     AT     CC     CG     CT     GG     GT     TT
AA 0.0420 0.0130 0.0200 0.0170 0.0160 0.0170 0.0150 0.0240 0.0042 0.0500
AC 0.0030 0.0034 0.0071 0.0067 0.0074 0.0071 0.0065 0.0074 0.0032 0.0038
AG 0.0030 0.0033 0.0068 0.0064 0.0070 0.0068 0.0061 0.0070 0.0028 0.0034
AT 0.0071 0.0084 0.0110 0.0110 0.0110 0.0110 0.0100 0.0120 0.0072 0.0084
CC 0.0180 0.0045 0.0110 0.0100 0.0092 0.0100 0.0089 0.0140 0.0016 0.0240
CG 0.0015 0.0018 0.0061 0.0061 0.0067 0.0063 0.0060 0.0067 0.0019 0.0015
CT 0.0029 0.0032 0.0068 0.0064 0.0070 0.0067 0.0060 0.0069 0.0027 0.0033
GG 0.0180 0.0054 0.0110 0.0096 0.0088 0.0094 0.0085 0.0120 0.0012 0.0200
GT 0.0029 0.0033 0.0069 0.0066 0.0072 0.0070 0.0062 0.0071 0.0027 0.0031
TT 0.0400 0.0130 0.0200 0.0170 0.0150 0.0170 0.0150 0.0240 0.0038 0.0480
or the number of derived alleles (use  2D SFS method  for this)
ind1  pAA  pAD  pDD
or the heterozygoes and homozygoes
HO HO  HO HE  HE HO  HE HE  HO altHO
0.6562  0.1476  0.1476  0.0324  0.0162
* 1 Brief Overview
-nInd/-n	nubmer of individuals in GLF file:
-maxSites/-m	maximum sites to analyze:
-model		ibs model:0 all 10 genotypes, 1 HO/HE
A binary GLF fileName that contains 10 genotype likelihoods per sites per individual as specified  in ANGSD -doGLF 1.
prefix for the output file names. Default in the glf input filename
number of individuals in GLF file. This is needed if you have more than one individual in the GLF file.
If you dont want to analysis all individuals then you can specify a single individual to analyze. an integer 0-(nInd-1). The first individuals is individuals 0
if you only want to analyse a single pair of individuals then you can specify ind1 and ind2 an integer 0-(nInd-1). The first individuals is individuals 0
use -allPairs 1 to analyse all pairs of individuals
maximum sites to analyze. This is usefull if you don't have enough RAM for the whole genome
model:0 all 10 genotypes, 1 HO/HE
If you analyse each individuals seperately (-allpair 0 )
Example of output *.ibs
Example of output *.ibspair
First generate genotype likelihood file for chromosome 1
./angsd -GL 1 -out genolike -doGlf 1 -bam bam.filelist -r 1:
Estimate all 10 genotype fractions for the second (same order as the bam.filelist) individual (-ind1 1)
misc/ibs -f genolike.glf.gz -nInd 10 -ind1 1
The output file is genolike.glf.gz.ibs
Estimate all 10 genotype fractions for each of the 10 individuals
misc/ibs -f genolike.glf.gz -nInd 10 -o all
The output file is all.ibs
Estimate the 10x10 genotype fraction matrix the first (-ind1 0) and the fourth (ind2 3) individual (same order as the bam.filelist)
misc/ibs -f genolike.glf.gz -nInd 10 -ind1 0 -ind 3
Estimate the 10x10 genotype fraction matrix for all pairs (very slow)
misc/ibs -f genolike.glf.gz -nInd 10 -allpairs 1 -o all
The output file is all.ibspair
* (Multi) SFS Estimation
* Population branch statistics (pbs)
* PCA (sampling approach)
* HWE and inbreeding with ngsF
* Create Fasta file
### SNPs and genotypes
* Major and Minor
* Genotype likelihood files
* overview of class
* accessing core data
* custom data containers
* What links here
* This page was last modified on 14 July 2016, at 11:16.