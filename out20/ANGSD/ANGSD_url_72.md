<-- http://www.popgen.dk/angsd/index.php/Inferring_Major_and_Minor_alleles-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
(Redirected from Inferring Major and Minor alleles)
Jump to: navigation, search
Many method assume that polymorphic sites are diallelic. For these methods one needs to define what is the major and minor allele. We allow the major and minor to be determined from either the counts of nucleotides, based on genotype likelihoods, specified by the ancestral/reference or even force both major minor to specific bases, which can be useful if you compare with HapMap data etc.
* 1 Brief Overview
* 2.1 From genotype likelihood data
* 2.2 From counts of data
* 2.3 Pre specified Major and Minor
* 2.4 Pre specified Major using a reference
* 2.5 Pre specified Major using the ancestral state
-> angsd version: 0.910-19-g8b9b43a-dirty (htslib: 1.2.1-251-g2072527) build(Dec  4 2015 11:37:02)
-> Analysis helpbox/synopsis information:
./angsd -domajorminor 	-> Fri Dec  4 13:56:10 2015
1: Infer major and minor from GL
2: Infer major and minor from allele counts
3: use major and minor from a file (requires -sites file.txt)
4: Use reference allele as major (requires -ref)
5: Use ancestral allele as major (requires -anc)
-rmTrans: remove transitions 0
## From genotype likelihood data
From input for either sequencing data like bam files or from genotype likelihood data like glfv3 the major and minor allele can be inferred directly from likelihoods. We use a maximum likelihood approach to choose the major and minor alleles. Details of the method can be found in the theory section of this page and for citation use this publication Skotte2012 and is briefly described here.
## From counts of data
If you input sequencing data like the bam format you can choose to infer the major and minor allele by picking the two most frequently observed bases across individuals. This is the approach from here: citation.
## Pre specified Major and Minor
Using the -sites option the major and minor allele can be predefined for the desired sites. The is very useful when comparing with other data sources e.g. SNP chips where the major and minor allele is known.
-doMajorMinor 3 -sites [filename]
## Pre specified Major using a reference
You can force the major allele according to the reference states if you have defined those **-ref**. The minor allele will be inferred based on the genotype likelihood (see do major minor 1). This is the approach used by both GATK and Samtools
-doMajorMinor 4 -ref [fasta.fa]
## Pre specified Major using the ancestral state
You can force the major allelel according to your ancestral states if you have defined those **-anc**. The minor allele will be inferred based on the genotype likelihood (see do major minor 1)
-doMajorMinor 5 -anc [fasta.fa]
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
* This page was last modified on 4 December 2015, at 14:56.