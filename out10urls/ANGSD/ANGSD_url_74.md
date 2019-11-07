<-- http://www.popgen.dk/angsd/index.php/SNP_calling-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
* 1 SNP Calling
* 1.1 Likelihood ratio test
## Likelihood ratio test
SNPs are called based on their allele frequencies. If a site has a minor allele frequency significantly different from 0 a site is called as polymorphic. The MAF estimate(s) given by -doMaf (see Allele_Frequency_estimation), will be used for a like ratio test by using a chi-square distribution with one degree of freedom for -doMaf 1 and -doMaf 2.
The p-value used for calling snaps. see Allele_Frequency_estimation for additional options
In this example we analyse data from bam files (-bam bam.files), calculate the genotype likelihood using the samtools method (-GL 1), infer the major and minor alleles (-doMajorMinor 1), estimate the allele frequencies assuming known minor (-doMAF 2) and only keep those sites that have a p-value less than 1e-6 of for being variable.
./angsd -bam bam.filelist -GL 1 -out outfile -doMaf 2 -SNP_pval 1e-6 -doMajorMinor 1
the results are given in the file outfile.mafs.gz:
chromo  position        major   minor   unknownEM       pu-EM   nInd
1       14000873        G       A       0.282476        0.000000e+00    10
1       14001018        T       C       0.259890        7.494005e-14    9
1       14001867        A       G       0.272099        6.361578e-14    10
1       14002422        A       T       0.377890        0.000000e+00    9
1       14003581        C       T       0.194393        5.551115e-16    9
1       14004623        T       C       0.259172        2.424727e-13    10
1       14007493        A       G       0.297176        5.114086e-07    9
1       14007558        C       T       0.381770        0.000000e+00    8
1       14007649        G       A       0.220547        1.054967e-11    9
1       14008734        T       A       0.242852        0.000000e+00    10
1       14009723        G       C       0.255063        2.470836e-07    10
1       14010597        G       A       0.315430        0.000000e+00    10
1       14010851        C       A       0.276936        0.000000e+00    10
1       14012240        C       T       0.297956        0.000000e+00    10
The columns are the chromosome, the position, the major allele, the minor allele, the minor allele estimate, the allele frequency, the p-value and the number of individuals with information.
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
* This page was last modified on 5 March 2014, at 18:54.