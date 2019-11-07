<-- http://www.popgen.dk/angsd/index.php/Relatedness-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
* 1 NGSrelate - estimation of IBD probabilities
* 2 IBS/genotype distribution
* 2.1 How to get the IBS pattern
* 2.2 Rcode to get expectations
## NGSrelate - estimation of IBD probabilities
In order to estimate kinship coefficient then population allele frequencies are needed. These can be estimated from data if you can multiple individuals. For some individuals, for example most human populations, there are publicly available data. If you can obtain population allele frequencies or have a many samples from your population then we recommend that you use NGSrelate has works with ANGSD output. From the estimated IBD probabilities you can then infer the relationship. Below is a table of the expected IBD sharing probabilities assuming no inbreeding
NGSrelate has its very own website http://www.popgen.dk/software/index.php/NgsRelate
If you do not have population allele frequencies the you cannot estimate kinship coefficients. However, you can still make some claims about the relationship of your samples based on IBS patterns. Below is an example of IBS patterns between two individuals where we ignore the allele types. G is the genotype that counts for example the number of derived or non-reference alleles. Basically it is the 2D SFS where the is just 1 individual in each of the two populations The full decription of the method can be seen here: IBSrelate
Here are some usefull ratio of IBS that can be used to say something about relatedness. Here we assume no inbreeding.
Relationship  Expected ratio  Expected ratio (R1)  Expected ratio (R1)
### How to get the IBS pattern
You can get the estimate by using the  2D SFS method or you can use the genotype distribution method both in ANGSD.
The two methods are very similar but with a very small difference. The SFS method uses ancestral information or a reference in order to infer the 2 alleles for each position. The genotype distribution does not infer either the major or the minor allele but uses all 10 possible genotype likelihoods.
### Rcode to get expectations
# R code go get expected IBS pattern
## k is the 3 IBD sharing probabities
## f is the allele frequency 
[,1]  [,2]   [,3]
[1,] 0.0625 0.125 0.0625
[2,] 0.1250 0.250 0.1250
[3,] 0.0625 0.125 0.0625
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
* This page was last modified on 29 August 2019, at 09:21.