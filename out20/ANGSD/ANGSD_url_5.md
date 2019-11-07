<-- http://www.popgen.dk/angsd/index.php/Supersim-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
Small program to simulate genotype likelihoods.
-outfiles PREFIX	 PREFIX.seq PREFIX.glf PREFIX.frq PREFIX.arg
-npop	Number of populations. This MUST be set before -nind [1]
-nind	Number of diploid individuals for each population [10]
-nsites	Number of sites [500000]
-errate	The sequencing error rate [0.0075]
-depth	Mean sequencing depth [5]
-pvar	Probability that a site is variable in the population [0.015]
-mfreq	Minimum population frequency [0.0001]
-F	inbreeding coefficient for each population [0]
-model	0=fixed errate 1=variable errate [1]
-base_freq	Background allele frequencies for A,C,G,T [0.25 0.25 0.25 0.25]
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
* This page was last modified on 4 December 2015, at 16:18.