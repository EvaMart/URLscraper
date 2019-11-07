<-- http://www.popgen.dk/angsd/index.php/Haploid_calling-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
Simple haploid output based on sampling or consensus. Latest github version of angsd has a small utility program in the misc folde that converts to plink output (tfam/tped).
# Major bug in version 0.911 (not in <0.911)
Use the developmental version github
* 1 Major bug in version 0.911 (not in <0.911)
* 2 Brief Overview
-> angsd version: 0.910-45-g2b2b4f0-dirty (htslib: 1.2.1-192-ge7e2b3d) build(Jan  3 2016 14:45:41)
-> Analysis helpbox/synopsis information:
./angsd -doHaploCall 	-> Sun Jan  3 15:18:15 2016
0:	 no haploid calling 
1:	 (Sample single base)
-doCounts	0	Must choose -doCount 1
-minMinor	0	Minimum observed minor alleles
-maxMis	-1	Maximum missing bases (per site)
This function outputs a base for each individual for each site
1; sample a random base 2; most frequent base. Random base for ties
use -doCounts 1 in order to count the bases at each sites after filters.
Minimum observed minor alleles; only prints sites with more than minMinor sampled alleles (across individuals).
maximum allowed missing alleles (accross individuals). -maxMis 0 means only sites without missing alleles are printed
Output: Each line represents site. chromsome name (Column 1), position (Column 2), major allele (Column 3). One column for each individual with the sampled allele.
Create a fasta file bases from a random samples of bases.
./angsd -bam bam.filelist -dohaplocall 1 -doCounts 1 -r 1: -minMinor 1
major allele (most common of the sampled alleles)
first individual - same order as in the input files
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
* This page was last modified on 10 August 2016, at 11:11.