<-- http://www.popgen.dk/angsd/index.php?title=ANGSD&printable=yes-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
ANGSD is a software for analyzing next generation sequencing data. The software can handle a number of different input types from mapped reads to imputed genotype probabilities. Most methods take genotype uncertainty into account instead of basing the analysis on called genotypes. This is especially useful for low and medium depth data. The software is written in C++ and has been used on large sample sizes.
This program is not for manipulating BAM/CRAM files, but solely a tool to perform various kinds of analysis. We recommend the excellent program SAMtools for outputting and modifying bamfiles.
ANGSD is also on github: https://github.com/ANGSD/angsd
` ./angsd [OPTIONS] `
example of allele frequency estimated from genotype likelihoods with bam files as input using 10 threads
` ./angsd -out outFileName -bam bam.filelist -GL 1 -doMaf 1 -doMajorMinor 1 -nThreads 10 `
The program is developed on tested on a Linux system with gcc compiler. It compiles on OSX with clang, but OSX is not really that tested.
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
* This page was last modified on 4 December 2015, at 15:07.