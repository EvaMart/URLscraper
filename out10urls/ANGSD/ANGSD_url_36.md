<-- http://www.popgen.dk/angsd/index.php/Contamination-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
Angsd can estimate contamination, but only for chromosomes that exists in one genecopy (eg chrX for males). This method requires a list of polymorphic sites along with their frequency and we also recommend to discard regions with low mappability.
We have included a mappability and HapMap files for chrX these are found in the **RES** subfolder of the angsd source package (using hg19). So if you are working with humans, and your sample is a male then you can estimate the contamination with the follow two commands.
* First we generate a binary count file for chrX for a single BAM file (ANGSD cprogram)
* Then we do a Fisher's exact test for finding a p-value, and jackknife to get an estimate of contamination (Rprogram)
An example are found below:
./angsd -i my.bam -r X:5000000-154900000 -doCounts 1  -iCounts 1 -minMapQ 30 -minQ 20
#do jackKnife in R
Rscript R/contamination.R mapFile="RES/map100.chrX.gz" hapFile="RES/hapMapCeuXlift.map.gz" countFile="angsdput.icnts.gz" mc.cores=24
#or use the command below for a newer version of the resourcefiles.
Rscript R/contamination.R mapFile="RES/chrX.unique.gz" hapFile="RES/HapMapChrX.gz" countFile="angsdput.icnts.gz" mc.cores=24
##or the fancy fast new c++ program
misc/contamination -a angsdput.icnts.gz -h RES/HapMapChrX.gz 
The **contamination.R** program is found in the **R/** subfolder, and the resource files are found in the **RES** folder. The jackknive procedure can be quite slow, so we allocate 24 cores for this analysis **mc.cores=24**.
The output from the above command is shown below
* 1.1 Interpretation of output
Loading required package: parallel
->  Needed arguments:
countFile : Count file 
->  Optional arguments (defaults):
mapFile  ( NA ) : Mappability file 
minDepth  ( 2 ) : Minimum depth 
maxDepth  ( 20 ) : Maximium depth 
mc.cores  ( 10 ) : Number of cores 
fixed  ( TRUE ) : Use fixed version of likelihood 
jack  ( TRUE ) : Jacknive to get confidence intervals 
minmaf  ( 0.05 ) : minimum maf 
startPos  ( 5e+06 ) : start position 
stopPos  ( 154900000 ) : stop position 
seed  ( NA ) : set a seed (supply int value) 
Rscript ../R/contamination.R mapFile="map100.chrX.bz2" hapFile="hapMapCeuXlift.map.bz2" countFile="angsdput.icnts.gz" mc.cores=24
Loading required package: parallel
Doing Fisher exact test for Method1:
SNP site adjacent site
minor base      616          3554
major base   198492       1589087
Fisher's Exact Test for Count Data
alternative hypothesis: true odds ratio is not equal to 1
95 percent confidence interval:
Doing Fisher exact test for Method2:
SNP site adjacent site
minor base      114           654
major base    37983        304122
Fisher's Exact Test for Count Data
alternative hypothesis: true odds ratio is not equal to 1
95 percent confidence interval:
major and minor bases - Method1:
-4     -3     -2     -1 SNP site      1      2      3      4
minor base    427    417    475    437      616    486    439    427    446
major base 198651 198715 198656 198645   198492 198500 198681 198693 198546
major and minor bases - Method2:
-4    -3    -2    -1 SNP site     1     2     3     4
minor base    75    76    96    73      114    86    79    80    89
major base 38022 38021 38001 38024    37983 38011 38018 38017 38008
Running jackknife for Method1 (could be slow)
Running jackknife for Method2 (could be slow)
Method1     Method2    
Contamination 0.03837625  0.03380983 
llh           1034.078    483.5145   
SE            0.002630455 0.003900376
## Interpretation of output
Both methods shows a highly significant pvalue, and estimate the level of contamination to be approx 3%.
Later versions of angsd gives a much nice output format. Below is based on a different file from above.
-> Must supply -h hapmapfile -a angsd.icnts.gz file
-> Other options: -m minaf -b startpos -c stoppos -d mindepth -e maxdepth -f skiptrans -p nthreads -s seed -j maxjackknife
misc/contamination -a angsdput.icnts.gz -h RES/HapMapChrX.gz -p 100 -s 100
hapmap:RES/HapMapChrX.gz counts:angsdput.icnts.gz minMaf:0.050000 startPos:5000000 stopPos:154900000 minDepth:2 maxDepth:200 skiptrans:0 nthreads:100 seed:100
Method2 is subject to fluctuations due to random sampling
Seed value of 0 (zero) will use time as seed
[readhap] We now have: 58190 snpSites after filtering based on hapMapfile
[readicnts] fname:angsdput.icnts.gz minDepth:2 maxDepth:200
[readicnts] Has read:70325301 sites,  28883428 sites (after depfilter) from ANGSD icnts file
After removing SNP sites with no data in 5bp surrounding region`
We have nSNP sites: 9809, with flanking: 88281
MAIN RESULTS: Fisher exact test:
Method	 n11 n12 n21 n22 prob left right twotail
Method1: old_llh Version: MoM:0.020657 SE(MoM):1.898369e-03 ML:0.020983 SE(ML):1.847108e-03
Method1: new_llh Version: MoM:0.020538 SE(MoM):1.908704e-03 ML:0.020909 SE(ML):1.839107e-03
Method2: old_llh Version: MoM:0.018192 SE(MoM):2.877245e-03 ML:0.018908 SE(ML):2.799355e-03
Method2: new_llh Version: MoM:0.018087 SE(MoM):2.892190e-03 ML:0.018832 SE(ML):2.787229e-03
The method is described in the supplementary of Rasmussen2011
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
* This page was last modified on 11 July 2015, at 15:51.