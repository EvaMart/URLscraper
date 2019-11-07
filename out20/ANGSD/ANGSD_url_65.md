<-- http://www.popgen.dk/angsd/index.php/Citing_angsd-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
There is an overall angsd paper with bibtex below.
title = {{ANGSD}: Analysis of Next Generation Sequencing Data},
abstract = {High-throughput {DNA} sequencing technologies are generating vast amounts of data. Fast, flexible and memory efficient implementations are needed in order to facilitate analyses of thousands of samples simultaneously.},
journal = {{BMC} Bioinformatics},
author = {Korneliussen, Thorfinn S. and Albrechtsen, Anders and Nielsen, Rasmus},
* 1.1 Maf estimation from counts of alleles
* 1.2 Allele estimation
* 1.3 SNP calling
* 1.4 Genotype likelihoods
* 1.6 SFS estimation
* 1.7 Neutrality tests (eg Tajima)
* 1.9 Error rates method 1
* 1.10 Error rates method 2
### Maf estimation from counts of alleles
allele estimation from genotype likelihoods
SNP calling based on genotype likelihoods
same as in samtools Li2011
same as in gatk
same as in soapSNP
same as in kim2011
using score statistic Skotte2012
-doAsso 1 or 3
using allele frequencies kim2011
Estimating the site frequency spectrum Nielsen2012
### Neutrality tests (eg Tajima)
### Error rates method 1
joint GL and error estimation kim2011
### Error rates method 2
based on a high quality genome orlando2013
from X chromosome Rasmussen2011
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
* This page was last modified on 31 August 2015, at 10:08.