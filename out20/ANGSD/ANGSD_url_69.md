<-- http://www.popgen.dk/angsd/index.php/Authors-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
Fililpe Vieira has been implementing changes to the frequency estimator. analysisMaf.cpp -> analysisMaf.inbreed.cpp some changes in angsd_realSFS.cpp And the analysisHWE.cpp
Matteo has been implementing the Fst and PCA which uses output from angsd.
Some code is very 'inspired' by SAMtools (bamfile reading GL -1). The code for the SOAPsnp GL estimator is also very inspired by SOAPsnp
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
* This page was last modified on 28 June 2013, at 13:50.