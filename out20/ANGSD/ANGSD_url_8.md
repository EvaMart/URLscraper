<-- http://www.popgen.dk/angsd/index.php/Filters-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
We allow for filtering at many different levels.
1. Read level, MapQ, unique mapped reads etc
2. Base level, qscore
4. Regions (using BAM indexing (active lookup))
5. Single sites (passive lookup, also allows for forcing major and minor) -sites
6. Filtering based on downstream analysis. minimum MAF, LRT for SNP calling etc.
7. Trimming out the ends of the reads
It follows that some filters will select a subset of data, and some of the filters will discard certain sites. If multiple filters has been chosen, the analysis will be limited to the chain of filters.
* 1 Filters for reads in Bam files
* 2 Selected Sites
* 3 Allele frequencies
* 4 Polymorphic sites
* 5 Number of non missing individuals
# Filters for reads in Bam files
We allow for filtering and manipulation a the read level. These filters include minimum mapping and base qualtity, paired reads and others. Additionally specific regions can be analysed. All of the filters for bam files are described in Input#BAM_files.
For analysing specfic regions see Input#BAM_files. If you are interested in running your analysis at individual sites that are distributed throughout the entire genome, it might be faster to simply to loop over the entire data, but only analyse the data at specific positions. This can be done by supplying the -sites argument. With this approach we also allows for the forcing of major/minor alleles using external information.
only work with sites with a maf above [float]
only work with sites with a p-value less than [float]
# Number of non missing individuals
Only keep sites with at least minIndDepth (default is 1) from at least [int] individuals
Only works with the -minInd filter. Change the minimum depth the individuals must have in order to keep the site. Default is 1.
Discard site if total sequencing depth (all individuals added together) is below [int]. Requires  -doCounts
Discard site if total sequencing depth (all individuals added together) is above [int]  -doCounts
Discard individual if sequencing depth for an individual is below [int]. This filter is only applied to analysis which are based on counts of alleles i.e. analysis that uses  -doCounts
Discard individual if sequencing depth for an individual is above [int] This filter is only applied to analysis which are based on counts of alleles i.e. analysis that uses  -doCounts
Only call genotypes if the depth is as least [int] for that individuals
This requires  -doCounts and -doGeno
First we do a run with no filters
./angsd  -doMaf 2 -doMajorMinor 1 -out TSK -bam bam.filelist -GL 1 -r 1:
gunzip -c TSK.mafs.gz | head
Now we do a filter with MAF cutoff of 1\%
./angsd -doMaf 2 -doMajorMinor 1 -out TSK -bam bam.filelist -GL 1 -r 1: -minMaf 0.01
gunzip -c TSK.mafs.gz | head
Similar if we only want sites with information for atleast 5 samples
./angsd -doMaf 2 -doMajorMinor 1 -out TSK -bam bam.filelist -GL 1 -r 1: -minInd 5
gunzip -c TSK.mafs.gz | head
If we are interested in all sites with a p-value of 10^(-6) of being variable
./angsd -doMaf 2 -doMajorMinor 1 -out TSK -bam bam.filelist -GL 1 -r 1: -SNP_pval 1e-6
gunzip -c TSK.mafs.gz | head
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
* This page was last modified on 3 March 2017, at 12:16.