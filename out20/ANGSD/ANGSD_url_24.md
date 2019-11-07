<-- http://www.popgen.dk/angsd/index.php/Base_quality-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
Counts the number of bases for each quality score. Need the -doCount option to be invoked
default 0. The minimum allowed base quality score.
default 0. Remove sites were less than 'minInd' individuals have at least one read
Print the number of
./angsd -out out -doCounts 1 -doQsDist 1 -bam bam.filelist
First coloums is the quality score the second one the number of bases with this score.
0       3113
1       15619
2       97044
3       68369
4       117163
5       12149
6       15016
7       17982
8       21897
9       26471
10      31854
11      36491
12      41649
13      47400
14      53778
15      61933
16      73120
17      87034
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
* This page was last modified on 30 September 2013, at 09:17.