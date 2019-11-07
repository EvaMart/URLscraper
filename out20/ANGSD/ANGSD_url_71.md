<-- http://www.popgen.dk/angsd/index.php/Depth-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
This method will find depth distribution for every sample and for all samples jointly.
which requires -doCounts 1.
Defaults to 100. Sites with more than maxDepth reads are counted as having 100 reads.
Find the depth for chromsome 7 for the first 5 samples in bam.filelist
angsd -bam bam.filelist -doDepth 1 -out all -doCounts 1 -r 7: -nInd 5
Same as above but only using reads with a mapping quality above 30 and a nucleotide qscore above 20.
angsd -bam bam.filelist -doDepth 1 -out strict -doCounts 1 -r 7: -nInd 5 -minMapQ 30 -minQ 20
This file contains nInd number of lines. Column1 is the number sites that has sequencing depth=0,Column2 is the number of sites that has sequencing depth=1 etc
The sequencing depth for all samples.
Here are the results the all data
1147 	4240 	8357 	13017 	16077 	15481 	12871 	10738 	7288 	4537 	2998 	1638 	889 	451 	211 	92 	50     14 	
1831 	6725 	12572 	17090 	17451 	15359 	11588 	8274 	4538 	2551 	1199 	545 	209 	83 	20 	33 	13 	9 	
12749 	23974 	25261 	18900 	10294 	5388 	2326 	850 	241 	83 	28 	2 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 
15366 	25983 	24257 	16854 	9152 	4832 	2585 	791 	214 	42 	20 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	
13131 	24070 	25347 	18949 	10514 	5090 	1991 	688 	213 	82 	21 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 
150500 	21708 	39928 	65820 	87290 	97337 	105127 	115961 	123207 	126721 	129377 	127351 	125596 	118588 	107096 	93171 	78612 	66905 	53952 	43224 	34777 25672 	19393 	14431 	9771 	6958 	4837 	3149 	2027 	1362 	919 	471 	308 	198 	79 	48 	41 	8 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0
6391 	11709 	16031 	17921 	16209 	12232 	8424 	5352 	2913 	1552 	814 	348 	129 	53 	15 	3 	0 	0 	0 	
7735 	17432 	20843 	19832 	14877 	9459 	5334 	2679 	1139 	468 	185 	63 	26 	11 	9 	2 	2 	0 	0 	0 	0 
25931 	30865 	23189 	12260 	5217 	1860 	579 	152 	35 	8 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0
21104 	29568 	23802 	13951 	7090 	3028 	1157 	327 	52 	16 	1 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 
25971 	30627 	23572 	12355 	5041 	1775 	561 	149 	32 	9 	4 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0
182709 	73098 	106362 	134201 	153550 	161615 	163108 	161384 	155021 	139328 	124616 	106576 	87303 	68862 	53696 	40599 	29287 	20417 	14767 	9702 	6299 	3833 	2415 	1435 	827 	457 	260 	108 	35 	25 	19 	1 	5 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0 	0
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
* This page was last modified on 3 January 2014, at 13:16.