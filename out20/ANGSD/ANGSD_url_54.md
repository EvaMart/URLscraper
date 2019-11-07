<-- http://www.popgen.dk/angsd/index.php/Genotype_calling-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
We really don't recommend doing analysis based on called genotypes, but incorporate the uncertainty directly into the analysis you want to perform. But we recognise that many methods are still relying on called genotypes, and have therefore implemented a basic genotype caller into angsd.
Genotype calling in ANGSD is based on calculating the posterior probability of the genotypes. The **-doGeno** is therefore a simple wrapper around the **-doPost** along with some extra filtering options. See Allele Frequencies for more information.
* 1 Brief Overview
* 1.2.1 Allele frequency as prior
* 1.2.2 Sample allele frequency with SFS as prior
./angsd -dogeno         -> Wed Mar  2 12:39:19 2016
1: write major and minor
2: write the called genotype encoded as -1,0,1,2, -1=not called
4: write the called genotype directly: eg AA,AC etc 
8: write the posterior probability of all possible genotypes
16: write the posterior probability of called genotype
32: write the posterior probabilities of the 3 gentypes as binary
-> A combination of the above can be choosen by summing the values, EG write 0,1,2 types with majorminor as -doGeno 3
-postCutoff=0.333333 (Only genotype to missing if below this threshold)
-geno_minDepth=-1       (-1 indicates no cutof)
-geno_maxDepth=-1       (-1 indicates no cutof)
-geno_minMM=-1.000000   (minimum fraction af major-minor bases)
-minInd=0       (only keep sites if you call genotypes from this number of individuals)
NB When writing the posterior the -postCutoff is not used
NB geno_minDepth requires -doCounts
NB geno_maxDepth requires -doCounts
angsd can also use the full information of the sample allele frequencies for calling genotypes see SFS Estimation.
1: print out major minor
2: print the called genotype as -1,0,1,2
4: print the called genotype as AA, AC, AG, ...
8: print all 3 posts (major,major),(major,minor),(minor,minor)
16: print the posterior of the called genotype
32: somewhat different dumps the binary posterior for all samples, encoded as 3*nind double
Use the sum of the above to give the output you want. Forexample -doGeno 5 (1+4) prins the major and minor allele followed by the genotype (AA, AC ...) for each individual
1: estimate the posterior genotype probability based on the allele frequency as a prior
2: estimate the posterior genotype probability assuming a uniform prior
set genotypes to missing if the individual depth is less than [int]
set genotypes to missing if the individual depth is larger than [int]
set genotypes to missing if less than [float] of the bases are the major or minor (likely a triallic site). e.g. 0.1 means that less than 10% of reads in this individual is either the major or the minor
Call only a genotype with a posterior above this threshold.
NB if the raw posterior dump is requested the -postCutoff is not used
### Allele frequency as prior
./angsd -bam bam.filelist -GL 1 -out outfile -doMaf 2 -doMajorMinor 1 -SNP_pval 0.000001 -doGeno 5 -doPost 1 -postCutoff 0.95
gives a output like this:
1       14000202        G       A       GG      NN      NN      GA      NN      
1       14000873        G       A       GG      GG      GG      AA      GA      
1       14001018        T       C       NN      NN      NN      CC      NN      
1       14001867        A       G       NN      AA      AA      NN      NN      
1       14002342        C       T       CC      CC      CC      CC      CC      
1       14002422        A       T       AA      NN      NN      NN      NN      
1       14002474        T       C       TC      TT      TT      TT      TT      
1       14003581        C       T       CC      CC      NN      NN      CT      
1       14004623        T       C       TT      TT      TT      NN      TC      
1       14005069        A       G       AA      AA      AA      AA      AA
### Sample allele frequency with SFS as prior
1\. First get an estimate of the site frequency spectrum
./angsd -dosaf 1 -anc ../hg19ancNoChr.fa.gz -gl 1 -b list
2\. Now calculate diallelic genotype posterior probablity with
./angsd -dopost 3 -b list -gl 1 -domajorminor 1 -domaf 1 -pest angsdput.saf.idx.ml -dogeno 2 -r 1 -out angsdput2
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
* This page was last modified on 19 January 2018, at 14:59.