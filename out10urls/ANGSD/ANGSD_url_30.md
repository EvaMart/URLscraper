<-- http://www.popgen.dk/angsd/index.php/NGSadmix-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
To estimate admixture proportions from sequencing data then you can use NGSadmix
NGSadmix has it's very own webpage, because we like it so much. NGSadmix webpage
You can generate input files for NGSadmix easily in ANGSD see Beagle_input.
./angsd -GL 1 -out genolike -nThreads 10 -doGlf 2 -doMajorMinor 1 -SNP_pval 1e-6 -doMaf 1  -bam bam.filelist
and then run NGSadmix (found in the mics folder in the angsd folder)
NGSadmix -likes input.gz -K 3 -P 4 -o myoutfiles -minMaf 0.05 
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
* This page was last modified on 7 February 2018, at 16:44.