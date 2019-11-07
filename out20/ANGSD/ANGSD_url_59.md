<-- http://www.popgen.dk/angsd/index.php/Heterozygosity-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
The heterozygosity is the proportion of heterozygous genotypes. This is in some sense encapsulated in the theta estimates. And this page will just serve as a quick short example which is also written elsewhere on the wiki.
An important aspect with this approach is that we **DO NOT** require to fix the major and minor, or make any other apriori assumptions other than supplying the ancestral state.
The heterozygosity can either be a global estimate or a local estimate.
For diploid single samples the hetereo zygosity is simply second value in the SFS/AFS. By fixing the ancestral we loop over the 3 possible derived alleles, or we can use the reference as the ancestral and fold the spectrum.
This is simply the SFS Estimation for single samples. A short example is:
./angsd -i my.bam -anc ancestral.fa -dosaf 1 -gl 1
./angsd -i my.bam -anc ref.fa -dosaf 1 -fold 1
#followed by the actual estimation
The heterozygosity is then:
Things to consider is:
1\. Add -C 50 -ref ref.fa -minQ 20 -minmapq 30 to the angsd parameters to weed out the worst reads and bases.
2\. The output file could be very big. One might argue that we just need a reasonable large subset of the genome to estimate the one samples SFS (is is only 2 free parameters). So you could limit the analysis to a single chromosome by adding -r chr1. to the angsd part. Or you could add -nSites to the _realSFS_ function.
3\. if you work with ancient data. You can discard transition by adding -noTrans 1, to the angsd part of the code.
This is the single sample version of the theta estimation.
1\. We need to have a prior of the global heterozygosity as estimated from the example above 'est.ml' Then we generate persite thetas.
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
* This page was last modified on 24 January 2017, at 13:51.