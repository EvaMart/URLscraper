<-- http://www.popgen.dk/angsd/index.php?title=ANGSD&action=edit-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
# View source for ANGSD
Jump to: navigation, search
You do not have permission to edit this page, for the following reason:
The action you have requested is limited to users in the group: Users.
You can view and copy the source of this page.
ANGSD is a software for analyzing next generation sequencing data. The software can handle a number of different input types from mapped reads to imputed genotype probabilities. Most methods take genotype uncertainty into account instead of basing the analysis on called genotypes. This is especially useful for low and medium depth data. The software is written in C++ and has been used on large sample sizes. This program is not for manipulating BAM/CRAM files, but solely a tool to perform various kinds of analysis. We recommend the excellent program [http://samtools.sourceforge.net/ SAMtools] for outputting and modifying bamfiles. ANGSD is also on github: https://github.com/ANGSD/angsd <!-- ** ==Overview of input and intermediary data== The input and intermediary data structures of angsd. <classdiagram type="dir:LR"> [sequence data]->[genotype;likelihoods] [genotype;likelihoods]->[genotype;probabilities] [sequence files|bam files;SOAP files{bg:orange}]->[sequence data] [glf files|glfv3;soapSNP{bg:orange}]->[genotype;likelihoods] [genotype prob|beagle output{bg:orange}]->[genotype;probabilities] </classdiagram> ==Analysis from sequencing data== <classdiagram> // [input|bam files;SOAP files{bg:orange}]->[sequence data] [sequence data]->[output|summary stats;phat estimates;error estimates{bg:blue}] </classdiagram> ==Analysis from genotype likelihoods== <classdiagram> //[input data|glf files{bg:orange}]->[genotype;likelihoods] [genotype;likelihoods]->[output|glf files;beagle files;MAF estimates;MAF associations;SNP Calling;realSFS;error estimates;Inbreeding{bg:blue}] </classdiagram> ==Analysis from genotype probabilities== <classdiagram> //[input data|beagle output{bg:orange}]->[genotype;probabilities] [genotype;probabilities]->[output|genotype calling;MAF estimates;associations;SFS{bg:blue}] </classdiagram> \--> =Synopsis= <code lang=sh> ./angsd [OPTIONS] </code> example of allele frequency estimated from genotype likelihoods with bam files as input using 10 threads <code lang=sh> ./angsd -out outFileName -bam bam.filelist -GL 1 -doMaf 1 -doMajorMinor 1 -nThreads 10 </code> =Platform= The program is developed on tested on a Linux system with gcc compiler. It compiles on OSX with clang, but OSX is not really that tested.
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