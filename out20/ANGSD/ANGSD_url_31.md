<-- http://www.popgen.dk/angsd/index.php/Beagle_input-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
NBNB: The information on this page refers to version 3 of beagle.
Beagle haplotype imputation can be performed directly on genotype likelihoods. To generate beagle input file use
In order to make this file the major and minor allele has the be inferred (-doMajorMinor) and genotype likelihoods need to be estimated  (-GL) . It is also a good idea to only use the polymorphic sites, see Filters and SNP_calling.
In this example our input files are bam files. We use the samtools genotype likelihood methods. We use 10 threads. We infer the major and minor allele from the likelihoods and estimate the allele frequencies. We test for polymorphic sites and only output the ones with are likelhood ratio test p-value<1e-6.
./angsd -GL 1 -out genolike -nThreads 10 -doGlf 2 -doMajorMinor 1 -SNP_pval 1e-6 -doMaf 1  -bam bam.filelist
The above command generates the file genolike.beagle.gz that can be use as input for the beagle software
marker  allele1 allele2 Ind0    Ind0    Ind0    Ind1    Ind1    Ind1    Ind2    Ind2    Ind2    Ind3    Ind3    Ind3 
1_14000023      1       0       0.941177        0.058822        0.000001        0.799685        0.199918        0.000397        0.666316        0.333155        0.000529 
1_14000072      2       3       0.709983        0.177493        0.112525        0.941178        0.058822        0.000000        0.665554        0.332774        0.001672
1_14000113      0       2       0.855993        0.106996        0.037010        0.333333        0.333333        0.333333        0.799971        0.199989        0.000040 
1_14000202      2       0       0.835380        0.104420        0.060201        0.799685        0.199918        0.000397        0.333333        0.333333        0.333333
Note that the above values sum to one per site for each individuals. This is just a normalization of the genotype likelihoods in order to avoid underflow problems in the beagle software it does not mean that they are genotype probabilities.
The imputation can be done in beagle using the command
java -Xmx15000m -jar beagle.jar like=genolike.beagle.gz out=beagleOutName
Beagle outputs phasing and genotype probabilities. These can be using in ANGSD for downstream analysis such as MAF estimation and  Association testing
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
* This page was last modified on 6 November 2017, at 18:53.