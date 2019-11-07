<-- http://www.popgen.dk/angsd/index.php/Alleles_counts-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
(Redirected from Alleles counts)
Jump to: navigation, search
* 1 Brief Overview
* 2.2 output summary
* 3 Output formats
* 3.1 Printing Counts per site
* 3.2 qscore Distribution
* 3.3 Depth Distribution
Sometimes we want or need the frequency of the different bases. This is what -doCounts does.
You can refine which bases to be included using the filter parameters **-minMapQ/-minQ/-trim**. Based on the total depth for each you can discard sites for further analysis if the total depth is below/above some threshold **-setMaxDepth/setMinDepth**, and you can discard a site if the effective sample size is below some threshold **-minInd**.
You can output summary statistics such as Q score distribution **-doQsDist**, depth distribution **-doDepth**, or various per site counts **-dumpCounts**. All output files has a nice header which should make the interpretation straightforward.
-> angsd version: 0.560	 build(Dec  4 2013 13:27:02)
-> Analysis helpbox/synopsis information:
-doCounts	0	(Count the number A,C,G,T. All sites, All samples)
-minQ		13	(remove bases with qscore<minQ)
-minQfile	(null)	 file with individuals quality score threshold)
-setMaxDepth	-1	(If total depth is larger then site is removed from analysis.
-1 indicates no filtering)
-setMinDepth	-1	(If total depth is smaller then site is removed from analysis.
-1 indicates no filtering)
-trim		0	(trim ends of reads)
-minInd		0	(Discard site if effective sample size below value.
0 indicates no filtering)
-doDepth	0	(dump distribution of seqdepth)	.depthSample,.depthGlobal
-maxDepth	100	(bin together high depths)
-doQsDist	0	(dump distribution of qscores)	.qs
1: total seqdepth for site	.pos.gz
3: A,C,G,T sum all samples	.pos.gz,.counts.gz
4: A,C,G,T sum every sample	.pos.gz,.counts.gz
Default 13, Discard bases with a qscore below this threshold.
Default 0. Trim [int] bases at both ends of the reads. Useful for ancient DNA.
Default -1. If the total depth is below this value, the site is discarded
Default -1. If the total depth is above this value, the site is discarded
Default NULL. File with individual base quality score. This should be a file with the number of rows matching the number of individuals and the number of columns should either be 1 or 4. If four columns are given then a separate quality threshold is used for each base (A C G T). Both space and tab is acceptable as delimiters.
Default 0. See examples below. Output files are called **.pos,.counts.gz**.
Default 0. Output the distribution of scores. Output files are called **.qs**.
Default 0. Output the distribution of sequencing depths. Sites with depth above> **-maxDepth**, will be binned. Output files are called **.depthSample,depthGlobal'**.
Default 100. See **-doDepth** parameter.
## Printing Counts per site
1: Print overall depth in the .pos file. This depth is the sum of reads covering a sites for all individuals. The first column is the chromosome, the second it the position the third is the total depth.
2: prints the depth of each individual. Example of the depth of 10 individuals. Each line corresponce to the same line in the postion file.
3: Prints the depth for each of the four bases across all individuals. Each line corresponce to the same line in the postion file.
totA    totC    totG    totT
1       0       0       0
0       0       1       0
0       1       0       0
0       0       0       2
2       0       0       0
0       2       0       0
0       0       0       2
0       2       0       0
0       0       2       0
0       0       2       0
0       0       2       0
2       0       0       0
0       0       2       0
4: Prints the depth for each of the four bases for each indivial for each site. Example with the first four column belonging to the first individuals the counts of the number of A C G and Ts. Only two indivduals are shown. Each line corresponce to the same line in the postion file.
ind0_A ind0_C ind0_G ind0_T ind1_A ind1_C ind1_G ind1_T ind2_A ind2_C ind2_G ind2_T 
0 1 0 0 0 0 0 0 0 0 0 0 
0 0 1 0 0 0 0 0 0 0 0 0 
1 0 0 0 0 0 0 0 0 0 0 0 
0 0 1 0 0 0 0 0 0 0 0 0 
1 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 1 0 0 0 0 0 0 0 0 
0 0 0 1 0 0 0 0 0 0 0 1 
0 0 1 0 0 0 0 0 0 0 1 0 
0 1 0 0 0 0 0 0 0 0 0 0 
Print the individuals depth from bam files
./angsd -out out -doCounts 1 -dumpCounts 2 -bam bam.filelist
Print the individuals depth from bam files but filter away low quality bases
./angsd -out out -doCounts 1 -dumpCounts 2 -bam bam.filelist -minQ 20
Print the individuals depth from bam files but filter away low quality bases based on different threshold per individuals and base type
./angsd -out out -doCounts 1 -dumpCounts 2 -bam bam.filelist -minQ 20 -minQfile qThres.txt
20 23 23 20
30 34 34 30
30 34 34 30
30 34 34 30
30 34 34 30
20 23 23 20
30 34 34 30
30 34 34 30
20 30 30 20
20 23 23 20
The above analysis removes A and T bases with a Q score less then 20 for individual 1. The other individuals uses different thresholds
Column 1 is the qscore value, and column 2 are the corresponding count.
Column1 in the **.depthSample,.depthGlobal** contains the number of sites with sequencing depth of 1. Column2 is the number of sites with a sequencing depth of 2, etc.
The **.depthSample** contains depth per sample. Line one corresponds to individual 1. Column2 corresponds to individual 2 etc.
The **.depthGlobal** file contains the depth distribution across all individuals.
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
* This page was last modified on 26 February 2014, at 14:17.