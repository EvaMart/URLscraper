<-- http://www.popgen.dk/angsd/index.php/Plink-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
From version 0.549 we now support plink output files. Currently we only support the transposed **.tfam/.tped** files. But we are working on a native **.bed/.bim/.fam** output.
There are 3 approaches for making plink file. First is based on calling genotypes with angsd and outputting the results as a .tped file. The second approach is a based on doing a pseudohaploid call for sites for a list of individuals followed by a subprogram for converting this into a .tped file. Final approach is based on generating a fasta file (which also contains the pseudo haploid concensus) for each individual followed by a subprogram that extract the reference bases for specific sites and is then merged into a tped file.
This method is essentially a wrapper around the existing genotype caller, and all options for the genotype caller can therefore be used for the plink formated output file.
See Genotype calling for options relating to calling genotypes. For dumping the plink file you should supply:
* 1 Brief Overview
* 3 Output files
1: binary fam/bim/bed format (still beta, not really working)
NB This is a wrapper around -doGeno see more information for that option
A full example commandline is given below:
./angsd -bam bam.filelist -out outnames -doPlink 2 -doGeno -4 -doPost 1 -doMajorMinor 1 -GL 1 -doCounts 1 -doMaf 2 -postCutoff 0.99  -SNP_pval 1e-6 -geno_minDepth 4
Notice the extra minus in the **-dogeno -4** argument, this will suppress the -doGeno output.
The above commands will generate a **.tfam/.tped** files
1 1 0 0 0 -9
2 1 0 0 0 -9
3 1 0 0 0 -9
4 1 0 0 0 -9
5 1 0 0 0 -9
6 1 0 0 0 -9
7 1 0 0 0 -9
8 1 0 0 0 -9
9 1 0 0 0 -9
10 1 0 0 0 -9
11 1 0 0 0 -9
12 1 0 0 0 -9
13 1 0 0 0 -9
14 1 0 0 0 -9
15 1 0 0 0 -9
1 1_14000202 0 14000202 G G     G G     G G     G A     G G     G G     G A     G A     G A     G G     G G     G A     G G     G G     G A     G A     G G     G G     G G     G A     G G     G G     G A     G G     G G     G G     G G     G G     G A     G G     G A     G A     G G
1 1_14000873 0 14000873 G G     G G     G G     A A     G A     G G     G G     G G     G A     G G     G A     G G     G A     G G     G G     A A     G G     G A     G G     G A     G A     G G     G A     G G     G G     A A     A A     G G     G A     G G     G A     G G     G G
1 1_14001018 0 14001018 T T     T T     T T     C C     T C     T T     T T     T T     T C     T T     T C     T T     T T     T T     T T     C C     T T     T C     T T     T T     T C     T T     T T     T C     T T     T C     T C     T T     T C     T T     T C     T T     T T
1 1_14001867 0 14001867 A A     A A     A A     A G     A G     A A     A A     A A     A G     A A     A G     A A     A G     A A     A A     G G     A A     A G     A A     A G     A G     A A     A G     A G     A A     A G     G G     A A     A G     A A     A G     A A     A A
Notice that the family id simply an incrementing integer, and that the SNPid is the genomic position.
We highly recommand that users, don't perform analysis on called genotypes unless you have high depth, since calling genotypes is likely to cause bias in the downstream analysis.
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
* This page was last modified on 30 April 2019, at 17:26.