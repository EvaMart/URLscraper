<-- http://www.popgen.dk/angsd/index.php/HWE_test-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
Test for Hardy Weinberg equilibrium based on genotype likelihoods. This class works both as a filter for all other classes and outputs the results in a file.
This function has been updated to allow for all kinds of deviations not just F>0. This approach works from version **0.912** and in the latest developmental version from github
If you want to estimate inbreeding for individuals or include inbreeding information in your analysis try HWE_and_Inbreeding_estimates.
* 3 Use as a filter
Estimate the divination from HWE for each site
Method only works for diallelic sites. There choose a methods for selecting the major and minor allele (see Inferring_Major_and_Minor_alleles)
Remove sites with a pvalue below this threshold i.e. only use with that does not violate HWE
Remove sites with a pvalue above this threshold. E.g. -maxHWEpval 1e-3 print only sites that violates HWE with a pvalue of less than 0.001
angsd -bam bam.filelist  -doHWE 1 -domajorminor 1 -GL 1 
most of the time it only makes sense to do for the variable site e.g.
angsd -bam bam.filelist  -doHWE 1 -domajorminor 1 -GL 1 -doMaf 1 -SNP_pval 1e-6
## Use as a filter
see snpFilters, -minHWEpval or -maxHWEpval
This function will also print the results of the selected sites.
Example of output *.hwe.gz
Chromo  Position        Major   Minor   hweFreq Freq    F       LRT     p-value
1       14000873        G       A       0.282473        0.263594        0.674624        3.140936e+00    7.634997e-02
1       14015890        A       G       0.283119        0.300032        0.999762        8.207572e+00    4.171594e-03
1       14018430        A       C       0.276112        0.299817        0.675018        2.780118e+00    9.544113e-02
1       14033343        A       G       0.295368        0.299442        0.999762        6.473824e+00    1.094747e-02
1       14037881        T       A       0.306003        0.341598        -0.518384       3.178415e+00    7.461710e-02
1       14038946        T       C       0.329113        0.333424        0.999775        6.925424e+00    8.497884e-03
**Chromo** is the chromosome 
**Position** is the position **Major** is the major allele 
**Minor** is the minor allele 
**hweFreq** is the allele frequency assuming HWE (same as -doMaf 1) 
**Freq** is the allele frequency without HWE assumption 
**F** is the scale departure from HWE (inbreeding coefficient - see model) 
**LRT** is the likelihood ratio statistic 
**p-value** is the p-value based on a likelihood ratio test 
Probability of genotypes without assumption of HWE
total number of individuals X
all sequencing data for a site f
true unobserved genotype 
* NB! we allow for negative values of F in order to be able to detect any divination from HWE.
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
* This page was last modified on 23 October 2017, at 15:32.