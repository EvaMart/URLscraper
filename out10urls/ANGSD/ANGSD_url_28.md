<-- http://www.popgen.dk/angsd/index.php/Direct_Ancestry-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
Based on the 2dsfs for two individuals it is possible to estimate the direct ancestry
angsd -i ind1.bam -gl 1 -anc ancestral.fasta -dosaf 1 -out ind1
angsd -i ind2.bam -gl 1 -anc ancestral.fasta -dosaf 1 -out ind2
realSFS ind1.saf.idx ind2.saf.idx -P 32 >2dsfs
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
* This page was last modified on 8 November 2016, at 22:33.