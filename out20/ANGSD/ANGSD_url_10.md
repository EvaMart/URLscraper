<-- http://www.popgen.dk/angsd/index.php/PCA-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
* 1 Genotype likelihood approach
* 1.2 NGS tools
* 2 single read sampling
# Genotype likelihood approach
Simulated low depth NGS data of 3 populations
For PCA analysis we would recommend using PCAngsd which is based on genotype likelihoods from variable sites. This works well for low/medium depth sequencing even with sequencing depth varies between samples.
You can generate the input files in ANGSD with the command
./angsd -GL 2 -out genolike -nThreads 10 -doGlf 2 -doMajorMinor 1 -SNP_pval 1e-6 -doMaf 1  -bam bam.filelist
which will output genotype likelihoods for variable sites in the beagle format. This file can then be used in PCAngsd.
ngsTools methods for doing PCA/Covariance based on genotype likelihoods files:
Fumagalli, M, Vieira, FG, Korneliussen, TS, Linderoth, T, Huerta-Sánchez, E, Albrechtsen, A, Nielsen, R (2013). Quantifying population genetic differentiation from next-generation sequencing data. Genetics, 195, 3:979-92.
This works even without the need to call SNPs or genotypes based on genotype likelihoods.
NB! If you have very different depths for the different samples, e.i. some very low and others medium and high, then you might want to use the PCAngsd or use single base sampling approach PCA_MDS
The main documentation for this is found here: https://github.com/mfumagalli/ngsTools and here https://github.com/mfumagalli/ngsTools#ngscovar
# single read sampling
Both PCA and MDS can be performed based on sampling of a single read at each site. This can work even with very low depth data e.g. <1X. This method can be found here:PCA_MDS. However, it requires low error rate and polymorphic sites need to be inferred (or provided by user based on for example reference data such as the 1000G for humans)
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
* This page was last modified on 7 February 2018, at 16:56.