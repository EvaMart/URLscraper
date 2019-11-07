<-- http://www.popgen.dk/angsd/index.php/Genotype_likelihoods#Output_genotype_likelihoods-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
(Redirected from Genotype likelihoods)
Jump to: navigation, search
Many methods in ANGSD are based on genotype likelihoods, and ANGSD has 4 different genotype likelihood models implemented.
Genotype likelihoods and the four models are described in the  Bottom.
The SOAPsnp requires that a reference is supplied. Preferably the recalibration should only be performed on non-variable sites, so we recommend that the reference fasta should be modified such that all snp sites have an 'N'.
We also allow for output of the calculated genotype likelihoods in various formats that might be handy for some users.
NB the GATK model described and implemented in this program are the one described in the first GATK paper. This might be drastically different from the one used in the newer version of GATK.
* 1 Brief Overview
* 3.2 SYK (Kim et al.)
* 4 Output genotype likelihoods
* 4.2 Beagle format
* 4.3 Simple Text Format
* 5 Which genotype likelihood model should I choose ?
* 6.1 GATK genotype likelihoods
* 6.2 SAMtools genotype likelihoods
* 6.3 SOAPsnp genotype likelihoods
* 6.4 SYK genotype likelihoods
-> angsd version: 0.567	 build(Dec  7 2013 14:56:25)
-> Analysis helpbox/synopsis information:
-trim		0		(zero means no trimming)
-minInd		0		(0 indicates no filtering)
1: binary glf (10 log likes)	.glf.gz
2: beagle likelihood file	.beagle.gz
3: binary 3 times likelihood	.glf.gz
4: text version (10 log likes)	.glf.gz
If your input is sequencing file you can estimate genotype likelhoods from the mapped reads. Four different methods are available.
When estimating GL with soapSNP we need to generate a calibration matrix. This is done automaticly if these doesn't exist. These are located in angsd_tmpdir/basenameNUM.count,angsd_tmpdir/basenameNUM.qual, and the read length is not allowed to exceed 256 base pairs.
This will discards [int] bases at both ends of the reads when calculating the genotype likelihoods.
default is `angsd_tmpdir`. SOAPsnp generates a mismatch matrix for each BAM file and based on this mismatch matrix it calculates the type specific errors for each position in the read. So for each BAM file it generates two files, to avoid cluttering up the working directory you can specify a folder that should be used. SOAPsnp assumes that all reads have the same length, if this is not the case this model might not be suited (also true for other recalibration tools).
SYK model requires a file containing the type specific errors, as estimated from  -doError 1.
Discard the sites where we don't have data from **-minInd** individuals. If you have 100 individuals, and you only want to base your downstream analysis on the sites where you have data for at least half your samples then set **-minInd 50**.
See Input#BAM_files for Bam specific filters.
SAMtools and GATK likelihood are chosen simply with
./angsd -GL 1 #SAMtools
./angsd -GL 2 #GATK
SOAPsnp and SYK requires some extra arguments as shown below.
First run through the bam files ones to generate the calibration matrix
./angsd -bam bam.filelist -GL 3 -out outfile -ref hg19.fa -minQ 0
#NB important to set -minQ to zero, ANGSD defaults to minQ 13
This first loop doesn't estimate anything else than the calibration matrix.
After this run the we can estimate the genotype likelihoods and any other further analysis we desire.
./angsd -bam bam.filelist -GL 3 -out outfile -doGlf 1
## SYK (Kim et al.)
./angsd -bam bam.filelist -GL 4 -out outfile -errors error.file -doCounts 1
This model is based on counts of bases and therefore needs Alleles_counts "-doCounts 1". The error file is one line of 16 values as outputted from -doError
# Output genotype likelihoods
Output the log genotype likelihoods to a file
0\. don't output the genotype likelihoods (default)
1\. binary all 10 log genotype likelihood
2\. beagle genotype likelihood format (use directly for imputation)
4\. textoutput of all 10 log genotype likelihoods.
Glf file in binary doubles. All 10 genotype likelihoods are printed to a file. For each printed site there are 10*N doubles where N is the number of individuals. The order of the 10 genotypes are alphabetical AA AC AG AT CC CG CT GG GT TT. These are log scaled likelihood ratios to the most likely.
Pseudocode for parsing these files in **c/c++**.
FILE *fp = fopen(genotypelikelihood.bin,"r")
ind nInd = 5;
Beagle haplotype imputation and be performed directly on genotype likelhoods. To generate beagle input file use
In order to make this file the major and minor allele has the be inferred -doMajorMinor. It is also a good idea to only use the polymorphic sites.
In this example our input files are bam files. We use the samtools genotype likelihood methods. We use 10 threads. We infer the major and minor allele from the likelihoods and estimate the allele frequencies. We test for polymorphic sites and only outbut the ones with are likelhood ratio test statistic of minimum 24 (ca. p-value<1e-6).
./angsd -GL 1 -out genolike -nThreads 10 -doGlf 2 -doMajorMinor 1  -doMaf 2 -SNP_pval 2e-6 -bam bam.filelist
The above command generates the file genolike.beagle.gz that can be use as input for the beagle software
marker  allele1 allele2 Ind0    Ind0    Ind0    Ind1    Ind1    Ind1    Ind2    Ind2    Ind2    Ind3    Ind3    Ind3 
1_14000023      1       0       0.941177        0.058822        0.000001        0.799685        0.199918        0.000397        0.666316        0.333155        0.000529 
1_14000072      2       3       0.709983        0.177493        0.112525        0.941178        0.058822        0.000000        0.665554        0.332774        0.001672
1_14000113      0       2       0.855993        0.106996        0.037010        0.333333        0.333333        0.333333        0.799971        0.199989        0.000040 
1_14000202      2       0       0.835380        0.104420        0.060201        0.799685        0.199918        0.000397        0.333333        0.333333        0.333333
Note that the above values sum to one per sites for each individuals. This is just a normalization of the genotype likelihoods in order to avoid underflow problems in the beagle software it does not mean that they are genotype probabilities.
the chromosome and position
column 2 (allele 1)
the major allele codes as 0=A, 1=C, 2=G, 3=T
column 3 (allele 2)
the minor allele codes as 0=A, 1=C, 2=G, 3=T
Genotype likelihood for the major/major genotype for the first individual
Genotype likelihood for the major/minor genotype for the first individual
Genotype likelihood for the minor/minor genotype for the first individual
Genotype likelihood for the major/major genotype for the second individual ...
## Simple Text Format
./angsd -GL 1 -bam bam.filelist -doGlf 4 -nInd 1
We use SAMtools genotype likelihoods from the first sample (**-nInd 1**) in the file list called **bam.filelist**.
Generates **angsdput.glf.gz**, which looks like:
1 13999965 -2.072327 -0.693156 -2.072327 -2.072327 0.000000 -0.693156 -0.693156 -2.072327 -2.072327 -2.072327
1 13999966 -2.072327 -2.072327 -0.693156 -2.072327 -2.072327 -0.693156 -2.072327 0.000000 -0.693156 -2.072327
1 13999967 0.000000 -0.693156 -0.693156 -0.693156 -2.072327 -2.072327 -2.072327 -2.072327 -2.072327 -2.072327
1 13999968 -2.072327 -2.072327 -0.693156 -2.072327 -2.072327 -0.693156 -2.072327 0.000000 -0.693156 -2.072327
1 13999969 0.000000 -0.693156 -0.693156 -0.693156 -2.072327 -2.072327 -2.072327 -2.072327 -2.072327 -2.072327
1 13999970 -2.072327 -2.072327 -2.072327 -0.693156 -2.072327 -2.072327 -0.693156 -2.072327 -0.693156 0.000000
First 2 columns are the genomic positions, and the final 10 values are the genotype likelihoods in the usual ordering.
# Which genotype likelihood model should I choose ?
It depends on the data. As shown on this example Glcomparison, there was a huge difference between **-GL 1** and **-GL 2** for older 1000genomes BAM files, but little difference for newer bam files.
Genotype likelihoods are in this context the likelihood the data given a genotype. This is to be understood as we take all the information from our data for a specific position for a single individual, and we use this information to calculate the likelihood for our different genotypes. Since we assume diploid individuals it follows that we have 10 different genotypes.
And we write the genotype likelihood as
## GATK genotype likelihoods
In angsd we use the direct method of the first version of GATK (dragon). This is simply
where M is the sequencing depth  is the observed base in read _i, e_ is the probability of error calculated from the phredscaled qscore e.g.
## SAMtools genotype likelihoods
This subsection with SAMtools gl are preliminary
## SOAPsnp genotype likelihoods
## SYK genotype likelihoods
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
* This page was last modified on 18 May 2018, at 14:14.