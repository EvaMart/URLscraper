<-- http://www.popgen.dk/angsd/index.php/Fst-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
Our program can estimate fst between populations. And has been generalized to give all pairwise fst estimates if you supply the command with multiple populations.
if you supply 3 populations, the program will also output the pbs statistic.
NB we have removed the very unusefull unweighted fst estimator in the output, and have included a header. The output example below will be updated at some point.
\- Use angsd for calculating **saf** files for each population
\- Use realSFS to calculate 2d sfs for each pair
\- Use the above calculated 2dsfs as priors jointly with all **safs** from step1 to calculate **fst** binary files
\- Use realSFS to extract the the fst values from the **fst**
NB; In the latest github version there is a different fst estimator which should be preferable for small sample sizes. Feel free to try that out with
./realSFS fst index [saf.idx's] -whichFst 1
* 1 Note about fst for folded spectra
* 2 Two Populations real data
* 3 3 Populations real data
* 3.1 Sliding Window output
* 3.2 Relative window positions?
* 4 realSFS fst print
# Note about fst for folded spectra
* Earlier versions of angsd/realSFS could output folded 1d sample allele frequencies which would be usefull for 1population neutrality test like Tajima. This is however not appropriate to use for calculating fst since the folding was done within population.
* We have therefore added a proper folding procedure for the optimization based on the UNFOLDED .saf.idx files generated by -doSaf. These are the ones that should be used for calculating fst.
Therefore please remember to add -fold 1 if you want angsd (the realSFS subfunction) to perform fst and pbs estimation using the folded spectra.
# Two Populations real data
#this is with 2pops
#first calculate per pop saf for each populatoin
../angsd -b list1  -anc hg19ancNoChr.fa -out pop1 -dosaf 1 -gl 1
../angsd -b list2  -anc hg19ancNoChr.fa -out pop2 -dosaf 1 -gl 1
#calculate the 2dsfs prior
../misc/realSFS pop1.saf.idx pop2.saf.idx >pop1.pop2.ml
#prepare the fst for easy window analysis etc
../misc/realSFS fst index pop1.saf.idx pop2.saf.idx -sfs pop1.pop2.ml -fstout here
#get the global estimate
../misc/realSFS fst stats here.fst.idx 
#below is not tested that much, but seems to work
../misc/realSFS fst stats2 here.fst.idx -win 50000 -step 10000 >slidingwindow
# 3 Populations real data
In commands below im using 24 threads, because this is what I have. Adjust accordingly
#this is with 2pops
#first calculate per pop saf for each populatoin
./angsd -b list10  -anc hg19ancNoChr.fa -out pop1 -dosaf 1 -gl 1
./angsd -b list11  -anc hg19ancNoChr.fa -out pop2 -dosaf 1 -gl 1
./angsd -b list12  -anc hg19ancNoChr.fa -out pop3 -dosaf 1 -gl 1
#calculate all pairwise 2dsfs's
./misc/realSFS pop1.saf.idx pop2.saf.idx -P 24 >pop1.pop2.ml
./misc/realSFS pop1.saf.idx pop3.saf.idx -P 24 >pop1.pop3.ml
./misc/realSFS pop2.saf.idx pop3.saf.idx -P 24 >pop2.pop3.ml
#prepare the fst for easy analysis etc
./misc/realSFS fst index pop1.saf.idx pop2.saf.idx pop3.saf.idx -sfs pop1.pop2.ml -sfs pop1.pop3.ml -sfs pop2.pop3.ml -fstout here
#get the global estimate
-> Assuming .fst.gz file: here.fst.gz
#below is not tested that much, but seems to work
../misc/realSFS fst stats2 here.fst.idx -win 50000 -step 10000 >slidingwindow
In the presence of 3 populations, the program will also calculate the population branch statistics
## Sliding Window output
The sliding window seems to work so we have documented it here:
Second column is chromosome, third is center of window followed by
fst.unweight(pop1,pop2) fst.weight(pop1,pop2) fst.unweight(pop1,pop3) fst.weight(pop1,pop3) fst.unweight(pop2,pop3) fst.weight(pop2,pop3)
The last 3 columns are the populations branch statistic for population1, popultion2 and population3
## Relative window positions?
We allow for 3 different ways of defining window positions, these are chosen with the **-type** argument in realSFS
-type 2 Use pos=1 as the leftmost position of first window. Even though there isn't any data.
-type 1 Use first position with data, as leftmost position for the first window.
-type 0 Split out the genome into blocks. And use the first window that have data for the entire window. Then we will have the same windowcenters across datasets.
# realSFS fst print
You can print out the precalculated A and B with
_./realSFS fst print pop1.pop2.fst.idx_
Assuming we have pop1.saf.idx, pop2.saf.idx.
./realSFS pop1.saf.idx pop2.saf.idx >pop1.pop2.saf.idx.ml
./realSFS fst index pop1.saf.idx pop2.saf.idx -fstout pop1.pop2 -sfs pop1.pop2.saf.idx.ml
./realSFS fst print pop1.pop2.fst.idx
The weighted fst for a region is the ratio between the sum of As and the sum of B. The unweighted is the mean of the persite ratios.
A is the alpha from the reynolds 1983 (or Bhatia) and B is the alpha + beta.
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
* This page was last modified on 17 August 2019, at 03:38.