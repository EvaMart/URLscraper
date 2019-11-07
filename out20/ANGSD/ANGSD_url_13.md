<-- http://www.popgen.dk/angsd/index.php/SnpFilters-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
Angsd has different snpfilters/snpstats.
* SB1 strand bias1
* SB2 strand bias2
* SB3 strand bias3
* deviation from HWE 
* Wilcox rank sum test for qscore bias
* hetbias filter (based on reads of the genotypes that are called to be heterozygotes. This therefore requires -doGeno option)
The 3 strand bias filters are described here: http://www.biomedcentral.com/1471-2164/13/666
The deviation from HWE is described in http://www.ncbi.nlm.nih.gov/pubmed/23950147
The wilcox rank sum test is not described anywhere
These statistics will be calculated and reported and written into a file called **PREFIX.snpStat.gz**
./angsd -b list -domaf 1 -domajorminor 1 -gl 1 -snp_pval 1e-2  -P 5 -dosnpstat 1 
Please notice that **-doSnpStat 1** does not filter out sites, but will only report stats. In the above command we therefore limit the analysis and output to the sites that are likely to be truly variable (-snp_pval 1e-2).
You filter by supply pvalue cutoffs. Some examples are
Sites with pvalue in the interval (0-cutoff) will be discarded.
hromo  Position        +Major +Minor -Major -Minor     SB1:SB2:SB3     HWE_LRT:HWE_pval        baseQ_Z:baseQ_pval
1       14000023        45 0 22 4       -2.730769:0.163031:0.015386     0.060143:8.062706e-01   -1.882799:5.972750e-02
1       14000072        58 0 43 1       -2.318182:0.022952:0.431373     -0.000006:1.000000e+00  -1.647226:9.951167e-02
1       14000202        33 0 24 15      -1.846154:0.485830:0.000023     -0.000021:1.000000e+00  -2.114540:3.446902e-02
1       14000873        41 20 56 21     0.185598:0.339238:0.574272      1.973686:1.600571e-01   -3.496682:4.711723e-04
1       14001018        37 14 32 11     0.070296:0.278303:1.000000      1.759127:1.847334e-01   -3.037824:2.383068e-03
1       14001501        80 1 66 1       -0.190897:0.014943:1.000000     -0.000002:1.000000e+00  -0.357063:7.210450e-01
1       14001867        46 21 52 13     0.440386:0.337740:0.165207      0.288166:5.913983e-01   -1.961795:4.978620e-02
1       14002342        52 1 53 3       -0.945670:0.054563:0.618547     0.659996:4.165614e-01   -0.161165:8.719638e-01
1       14002422        41 17 29 20     -0.332741:0.441037:0.228091     6.478374:1.091948e-02   -0.822001:4.110760e-01
1       14002474        66 6 46 5       -0.164439:0.098696:0.761125     -0.000012:1.000000e+00  -1.763711:7.778050e-02
1       14002970        47 0 50 4       -1.870370:0.077129:0.121143     -0.000094:1.000000e+00  -2.411706:1.587805e-02
1       14003581        59 22 53 18     0.068718:0.275157:0.854787      0.870476:3.508235e-01   -1.033482:3.013785e-01
1       14004473        57 2 59 1       0.683522:0.034195:0.618617      -0.000022:1.000000e+00  -1.067950:2.855431e-01
1       14004623        57 21 56 34     -0.331562:0.410438:0.142272     0.616781:4.322460e-01   -1.788061:7.376604e-02
1       14005069        73 4 77 1       1.212954:0.052991:0.209619      -0.000002:1.000000e+00  -1.002612:3.160481e-01
# Example run with hetfilter
./angsd -dosnpstat 1 -b list -domajorminor 1 -gl 1 -snp_pval 1e-6 -domaf 1 -dogeno 3 -dopost 2 -out to -hetbias_pval 0.05
gunzip -c to.snpStat.gz |head
Chromo	Position	+Major +Minor -Major -Minor	SB1:SB2:SB3	HWE_LRT:HWE_pval	baseQ_Z:baseQ_pval	mapQ_Z:mapQ_pval	edge_z:edge_pval	+MajorHet +MinorHet -MajorHet -MinorHet nHet	hetStat:hetStat_pval
1	14000202	33 0 24 15	-1.846154:0.485830:0.000023	4.123488:4.229181e-02	-2.114540:3.446902e-02	-2.225467:2.604981e-02	-1.303389:1.924422e-01	17 0 5 13 35	2.314286:1.281902e-01	
1	14000873	41 20 56 21	0.185598:0.339238:0.574272	2.011470:1.561140e-01	-3.496682:4.711723e-04	-0.272559:7.851920e-01	-0.442618:6.580421e-01	9 9 14 7 39	1.256410:2.623317e-01	
1	14001018	37 14 32 11	0.070296:0.278303:1.000000	1.980987:1.592864e-01	-3.037824:2.383068e-03	-0.273832:7.842138e-01	-0.179702:8.573863e-01	6 2 7 5 20	1.800000:1.797125e-01	
1	14001867	46 21 52 13	0.440386:0.337740:0.165207	0.300249:5.837261e-01	-1.961795:4.978620e-02	-0.772750:4.396705e-01	-0.502157:6.155570e-01	11 10 11 5 37	1.324324:2.498174e-01	
1	14002342	52 1 53 3	-0.945670:0.054563:0.618547	3.058305:8.032542e-02	-0.161165:8.719638e-01	-1.950092:5.116507e-02	-1.418248:1.561184e-01	0 0 0 0 0	nan:nan	
1	14002422	41 17 29 20	-0.332741:0.441037:0.228091	6.975560:8.263036e-03	-0.822001:4.110760e-01	-0.160470:8.725105e-01	-1.375461:1.689888e-01	4 5 1 5 15	1.666667:1.967056e-01	
1	14002474	66 6 46 5	-0.164439:0.098696:0.761125	0.227889:6.330933e-01	-1.763711:7.778050e-02	-1.316136:1.881284e-01	-0.868561:3.850870e-01	3 6 3 5 17	1.470588:2.252529e-01	
1	14003581	59 22 53 18	0.068718:0.275157:0.854787	0.882506:3.475164e-01	-1.033482:3.013785e-01	-1.179927:2.380295e-01	-0.269877:7.872551e-01	12 11 10 7 40	0.400000:5.270893e-01	
1	14004623	57 21 56 34	-0.331562:0.410438:0.142272	0.621479:4.304982e-01	-1.788061:7.376604e-02	-1.226968:2.198347e-01	-0.655735:5.119945e-01	18 10 13 24 65	0.138462:7.098153e-01
The last columns are the counts of major/minor over +/- strand along with the test statistic and the corresponding pvalue.
The source code can be found here: https://github.com/ANGSD/angsd/blob/master/abcFilterSNP.cpp
NB please use latest dev version for these options
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
* This page was last modified on 27 June 2017, at 21:24.