<-- http://www.popgen.dk/angsd/index.php/Fasta-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
This option creates a fasta.gz file from a sequencing data file (BAM file). The function uses genome information in the BAM header to determine the length and chromosome names. For the sites without data an "N" is written.
This can be used as input for the ANGSD analysis:
The iupac output code was kindly provided by Kristian Ullrich.
* 1 Brief Overview
./angsd -dofasta 	-> Tue Sep 26 17:02:07 2017
1: use a random (non N) base (needs -doCounts 1)
2: use the most common (non N) base (needs -doCounts 1)
3: use the base with highest ebd (under development) 
4: output iupac codes (under development) 
-basesPerLine	50	(Number of bases perline in output file)
-explode	0	 print chromosome where we have no data (0:no,1:yes)
-rmTrans	0	 remove transitions as different from -ref bases (0:no,1:yes)
-ref	(null)	 reference fasta, only used with -rmTrans 1
-seed	0	 use non random seed of value 1
This function will dump a fasta file, the full header information from the SAM/BAM file will be used. This means that a fasta will be generated for the entire chromosome even if '-r/-rf -sites' is used.
sample a random base at each position. N's or filtered based are ignored. The "-doCounts 1" options for allele counts is needed in order to determine the most common base. If multiple individuals are used the four bases are counted across individuals. 
use the most common base. In the case of ties a random base is chosen among the bases with the same maximum counts. N's or filtered based are ignored. The "-doCounts 1" options for allele counts is needed in order to determine the most common base. If multiple individuals are used the four bases are counted across individuals. 
use the base with thie highest effective depth (EBD). This only works for one individual
Number of bases perline in output fasta file (default is 50)
0 (default) only output chromosomes with data. 1: write out all chromosomes
0 (default) all sites are used. 1: Remove transition. Here transitions are determined using a fasta file such as a reference genome.
a fasta file used to determine if a site is a transitions (needed when using -rmTrans 1 is used)
Use a seed in order to replicate results
For filters see Filters
Output is a fasta file, a normal looking fast file. Nothing special about this. For -doFasta 1, sometimes its big letters sometime small letters. This is due to the results being copied directly from the sequencing data. So small/big letters correspond to which strand for the original data. For the consensus fasta all letters are capital letters.
Create a fasta file bases from a random samples of bases.
./angsd -i bams/smallNA07056.mapped.ILLUMINA.bwa.CEU.low_coverage.20111114.bam -doFasta 1
For four bases we have 4 different EBD, each EBD is the product of the mapping quality and scores for the base under consideration. The EBD is the effective base depth, as defined by [1]:
where  is a certain base,  is the number of reads with base
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
* This page was last modified on 26 September 2017, at 18:09.