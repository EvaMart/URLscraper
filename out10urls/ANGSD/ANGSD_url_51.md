<-- http://www.popgen.dk/angsd/index.php/Allele_Frequency_estimation-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
(Redirected from Allele Frequency estimation)
Jump to: navigation, search
-domaf,-domaf,-domaf,-domaf,-domaf, domaf, domaf, domaf, domaf, domaf, domaf, dopost, SNP_pval 
The allele frequency is the relative frequency of an allele for a site. This can be polarized according to the major/minor, reference/non-refernce or ancestral/derived. .Therefore the choice of allele frequency estimator is closely related to choosing which alleles are segregating (see Inferring_Major_and_Minor_alleles).
We allow for frequency estimation from different input data:
2. Genotype posterior probabilities
3. Counts of bases
The allele frequency estimator from genotype likelihoods are from this publication, and the base counts method is from this publication.
For the case of the genotype likelihood based methods we allow for deviations from Hardy-Weinberg, namely we allow for users to supply a file containing inbreeding coefficients for each individual.
* 1 Brief Overview
* 2 Allele Frequency estimation
* 3.1 From genotype likelihood
* 3.2 From genotype probabilities
* 3.3 Estimator from base counts
* 4 Output data
-> angsd version: 0.910-76-gad32889 (htslib: 1.3-32-gecdc348) build(Mar  2 2016 12:38:33)
-> Analysis helpbox/synopsis information:
./angsd -doMaf  -> Wed Mar  2 12:45:40 2016
-doMaf  0 (Calculate persite frequencies '.mafs.gz')
1: Frequency (fixed major and minor)
2: Frequency (fixed major unknown minor)
4: Frequency from genotype probabilities
8: AlleleCounts based method (known major minor)
NB. Filedumping is supressed if value is negative
-doPost 0       (Calculate posterior prob 3xgprob)
1: Using frequency as prior
2: Using uniform prior
3: Using SFS as prior (still in development)
-minMaf         -1.000000       (Remove sites with MAF below)
-SNP_pval       1.000000        (Remove sites with a pvalue larger)
-rmTriallelic   0.000000        (Remove sites with a pvalue lower)
-ref    (null)  (Filename for fasta reference)
-anc    (null)  (Filename for fasta ancestral)
-eps    0.001000 [Only used for -doMaf &8]
-beagleProb     0 (Dump beagle style postprobs)
-indFname       (null) (file containing individual inbreedcoeficients)
NB These frequency estimators requires major/minor -doMajorMinor
# Allele Frequency estimation
The major and minor allele is first inferred from the data or given by the user (see Inferring_Major_and_Minor_alleles). This includes information from both major and minor allele, a reference genome (for major) or an ancestral genome.
1: Known major, and Known minor. Here both the major and minor allele is assumed to be known (inferred or given by user). The allele frequency is the obtained using based on the genotype likelihoods. The allele frequency estimator from genotype likelihoods are from this  publication but using the EM algorithm and is briefly described here.
2: Known major, Unknown minor. Here the major allele is assumed to be known (inferred or given by user) however the minor allele is not determined. Instead we sum over the 3 possible minor alleles weighted by their probabilities. The allele frequency estimator from genotype likelihoods are from this  publication but using the EM algorithm and is briefly described here. .
4: frequency based on genotype posterior probabilities. If genotype probabilities are used as input to ANGSD the allele frequency is estimated directly on these by summing over the probabitlies.
8: frequency based on base counts. This method does not rely on genotype likelihood or probabilities but instead infers the allele frequency directly on the base counts. The base counts method is from this publication.
Multiple estimators can be used simultaniusly be summing up the above numbers. Thus -doMaf 7 (1+2+4) will use the first three estimators. If the allele frequencies are estimated from the genotype likelihoods then you need to infer the major and minor allele (-doMajorMinor)
NB using -doMaf 4 is only supported if the posteriors are supplied as external files. Since the estimation of genotype posteriors in itself requires a maf estimator.
## From genotype likelihood
Example for estimating the allele frequencies both while assuming known major and minor allele but also while taking the uncertaincy of the minor allele inference into account. The inference of the major and minor allele is done directly from the genotype likelihood
./angsd -out out -doMajorMinor 1 -doMaf 3 -bam bam.filelist -GL 1
## From genotype probabilities
Example of the use of a genotype probability file for example from the output from beagle.
./angsd -out out -doMaf 4 -beagle beagle.file.gz
## Estimator from base counts
The allele frequencies can be infered directy from the sequencing data citation. This works by using "counts" of alleles, and should be invoked like
./angsd -out out -doMajorMinor 2 -doMaf 8 -bam bam.filelist -doCounts 1
21      9719788 T       A       0.000001        -0.000012       3
21      9719789 G       A       0.000000        -0.000001       3
21      9719790 A       C       0.000000        -0.000004       3
21      9719791 G       A       0.000000        -0.000001       3
21      9719792 G       A       0.000000        -0.000002       3
21      9719793 G       T       0.498277        41.932766       3
21      9719794 T       A       0.000000        -0.000001       3
21      9719795 T       A       0.000000        -0.000001       3
frequency using -doMaf 1
frequency using -doMaf 2
frequency using -doMaf 8
is the number of individuals with data
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
* This page was last modified on 2 April 2018, at 11:53.