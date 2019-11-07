<-- http://www.popgen.dk/angsd/index.php/SFS_Estimation-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
Latest version can now do bootstrapping.
* 1 Quick Start
* 3 Brief Overview
* 5 Output file
* 6 Interpretation of the output file
* 7 Folded spectra
* 8 Posterior of the per-site distributions of the sample allele frequency
* 9 Format specification of binary .saf* files
* 11 How to plot
* 12 Which genotype likelihood model should I choose ?
* 13.1 -doSaf 1
* 13.2 -doSaf 2
* 14 safv3 comparison
* 15 Using NGStools
The process of estimating the SFS and multidimensional has improved a lot in the newer versions.
Assuming you have a bam/cram file list in the file 'file.list' and you have your ancestral state in ancestral.fasta, then the process is:
./angsd -gl 1 -anc ancestral -dosaf 1
#or alot of filtering
./angsd -gl 1 -anc ancestral -dosaf 1 -baq 1 -C 50 -minMapQ 30 -minQ 20
#this will generate 3 files
1) angsdput.saf.idx 2) angsdput.saf.pos.gz 3) angsdput.saf.gz
#these are binary files that are formally defined in https://github.com/ANGSD/angsd/blob/newsaf/doc/formats.pdf
#To find the global SFS based on the run from above simply do
##or only use chromosome 22
./realSFS angsdput.saf.idx -r 22
## or specific regions
./realSFS angsdput.saf.idx -r 22:100000-150000000
##or limit to a fixed number of sites
./realSFS angsdput.saf.idx -r 17 -nSites 10000000
##or you can find the 2dim sf by
##NB the program will find the intersect internally. No need for multiple runs with angsd main program.
##or you can find the 3dim sf by
./realSFS ceu.saf.idx yri.saf.idx MEX.saf.idx
This method will estimate the site frequency spectrum, the method is described in Nielsen2012. The theory behind the model is briefly described here
This is a 2 step procedure first generate a ".saf" file (site allele frequency likelihood), followed by an optimization of the .saf file which will estimate the Site frequency spectrum (SFS).
For the optimization we have implemented 2 different approaches both found in the misc folder. The diagram below shows the how the method goes from raw bam files to the SFS.
You can also estimate a  2dsfs or even higher if you want to.
* NB the ancestral state needs to be supplied for the full SFS, but you can use the -fold 1 to estimate the folded SFS and then use the reference as ancestral.
* NB the output from the -doSaf 2 are not sample allele frequency likelihoods but sample alle posteriors.
And applying the realSFS to this output is therefore NOT the ML estimate of the SFS as described in the Nielsen 2012 paper,
but the 'Incorporating deviations from Hardy-Weinberg Equilibrium (HWE)' section of that paper.
-> angsd version: 0.910-76-gad32889 (htslib: 1.3-32-gecdc348) build(Mar  2 2016 12:38:33)
-> Analysis helpbox/synopsis information:
./angsd -doSaf  -> Wed Mar  2 12:47:13 2016
-doSaf          0
1: perform multisample GL estimation
2: use an inbreeding version
3: calculate genotype probabilities (use -doPost 3 instead)
4: Assume genotype posteriors as input (still beta) 
-doThetas               0 (calculate thetas)
-underFlowProtect       0
-fold                   0 (deprecated)
-anc                    (null) (ancestral fasta)
-noTrans                0 (remove transitions)
-pest                   (null) (prior SFS)
-isHap                  0 (is haploid beta!)
-doPost                 0 (doPost 3,used for accesing saf based variables)
If -pest is supplied in addition to -doSaf then the output will then be posterior probability of the sample allelefrequency for each site
./realSFS afile.saf.idx [-start FNAME -P nThreads -tole tole -maxIter  -nSites ]
For information and parameters concerning the realSFS subprogram go here: realSFS
Calculate the Site allele frequency likelihood based on individual genotype likelihoods assuming HWE
(version above 0.503) Calculate per site posterior probabilities of the site allele frequencies based on individual genotype likelihoods while taking into account individual inbreeding coefficients. This is implemented by Filipe G. Vieira. You need to supply a file containing all the inbreeding coefficients. -indF. Consider if you want to either get the MAP estimate by using all sites, or get the standardized values by conditioning on the called snpsites. See bottom of this page for examples.
Calculate the genotype posterior probabilities for all samples forall sites, using an estimate of the sfs (sample allele frequency distribution). This needs a prior distribution of the SFS (which can be obtained from -doSaf 1/realSFS).
Calculate the posterior probabilities of the sample allele frequency distribution for each site based on genotype probabilities. The genotype probabilities should be provided by the using using the -beagle options. Often the genotype probabilities will be obtained by haplotype imputation. 
0: (default) no underflow protection. 1: use underflow protection. For large data sets (large number of individuals) underflow projection is needed.
The output file from the _-doSaf_ is described in detail in angsd/doc/formats.pdf. These binary annoying files can be printed with
realSFS print mayflies.saf.idx -r chr1:10000-20000
A full example is shown below where we use the test data that can be found on the quick start page. In this example we use GATK genotype likelihoods.
first generate .saf file with 4 threads
./angsd -bam bam.filelist -doSaf 1 -out small -anc  chimpHg19.fa -GL 2 -P 4
We always recommend that you filter out the bad qscore bases and meaningless mapQ reads. eg **-minMapQ 1 -minQ 20**. So the above analysis with these filters can be written as:
./angsd -bam bam.filelist -doSaf 1 -out small -anc chimpHg19.fa -GL 2 -P 4 -minMapQ 1 -minQ 20
Obtain a maximum likelihood estimate of the SFS using EM algorithm
misc/realSFS small.saf.idx -maxIter 100 -P 4 >small.sfs
A plot of this figure are seen on the right. The jaggedness is due to the very low number of sites in this small dataset.
# Interpretation of the output file
Each row is a region of the genome (see below). Each row is the expected values of the SFS.
The generation of the .saf file contains a saf for each site, whereas the optimization requires information for a region of the genome. The optimization will therefore use large amounts of memory.
If you don't have the ancestral state, you can instead estimate the folded SFS. This is done by supplying the -anc with the reference genome and also supply -fold 1.
The above example would then be
#first generate .saf file
./angsd -bam bam.filelist -doSaf 1 -out smallFolded -anc  chimpHg19.fa -GL 2 -fold 1
#now try the EM optimization with 4 threads
misc/realSFS smallFolded.saf.idx -maxIter 100 -P 4 >smallFolded.sfs
# Posterior of the per-site distributions of the sample allele frequency
If you supply a prior for the SFS (which can be obtained from the -doSaf/realSFS analysis), the output of the .saf file will no longer be site allele frequency likelihoods but instead will be the log posterior probability of the sample allele frequency for each site in logspace.
# Format specification of binary .saf* files
This can be found in the angsd/doc/formats.pdf
* If the -fold 1 has been set, then the dimension is no longer 2*nInd+1 but nInd+1
* If the -pest parameter has been supplied the output is no longer likelihoods but log posterior site allele frequencies
We have recently added the possibility to bootstrap the SFS. Which can be very usefull for getting confidence intervals of the estimated SFS.
This is done by:
realSFS pop.saf.idx -bootstrap 100 -P number_of_cores
The program will then get you 100 estimates of SFS, based on data that has been subsampled with replacement.
# How to plot
Assuming the we have obtained a single global sfs(only one line in the output) from **realSFS** program, and this is located in **file.saf.sfs**, then we can plot the results simply like:
sfs<-(scan("small.sfs")) #read in the log sfs
barplot(sfs[-c(1,length(sfs))]) #plot variable sites 
We can make it more fancy like below:
norm <- function(x) x/sum(x)
#the variability as percentile
#the variable categories of the sfs
If your output from **realSFS** contains more than one line, it is because you have estimated multiple local SFS's. Then you can't use the above commands directly but should first pick a specific row.
# Which genotype likelihood model should I choose ?
It depends on the data. As shown on this example Glcomparison, there was a huge difference between **-GL 1** and **-GL 2** for older 1000genomes BAM files, but little difference for newer bam files.
The validation is based on the pre 0.900 version
./supersim -outfiles test -npop 1 -nind 12 -pvar 0.9 -nsites 50000
echo testchr1 100000 >test.fai
../angsd -fai test.fai -glf test.glf.gz -nind 12 -doSaf 1 -issim 1
./realSFS angsdput.saf 24 2>/dev/null >res
31465.429798 4938.453115 2568.586388 1661.227445 1168.891114 975.302535 794.727537 632.691896 648.223566 546.293853 487.936192 417.178505 396.200026 409.813797 308.434836 371.699254 245.585920 322.293532 282.980046 292.584975 212.845183 196.682483 221.802128 236.221205 197.914673
$ngsSim  -npop 1 -nind 24 -nsites 1000000 -depth 4 -F 0.0 -outfiles testF0.0
$ngsSim  -npop 1 -nind 24 -nsites 1000000 -depth 4 -F 0.9 -outfiles testF0.9
for i in `seq 24`;do echo 0.9;done >indF
echo testchr1 250000000 >test.fai
$angsd -fai test.fai -issim 1 -glf testF0.0.glf.gz -nind 24 -out noF -dosaf 1
$angsd -fai test.fai -issim 1 -glf testF0.9.glf.gz -nind 24 -out withF -dosaf 2 -domajorminor 1 -domaf 1 -indF indF
$angsd -fai test.fai -issim 1 -glf testF0.9.glf.gz -nind 24 -out withFsnp -dosaf 2 -domajorminor 1 -domaf 1 -indF indF -snp_pval 1e-4
$realSFS noF.saf 48 >noF.sfs
$realSFS withF.saf 48 >withF.sfs
barplot(rbind(trueNoF,estNoF)[,-1],main="true vs est SFS F=0 (ML) (all sites)",be=T,col=1:2)
barplot(rbind(trueWithF,estWithF)[,-1],main='true vs est sfs=0.9 (MAP) (all sites)',be=T,col=1:2)
barplot(rbind(trueWithF,colMeans(m))[,-1],main='true vs est sfs F=0.9 (colmean of site pp) (all sites)',be=T,col=1:2)
##m contains SFS for absolute frequencies
##m now contains a corrected estimate containing the zero category
barplot(rbind(trueWithF,norm(m))[,-1],main='true vs est sfs F=0.9 (colmean of site pp) (called snp sites)',be=T,col=1:2)
See results from above here:http://www.popgen.dk/angsd/sfsFcomparison.pdf
Between 0.800 and 0.900 i decided to move to a better format than the raw sad files. This new format takes up half the storage and allows for easy random access and generalizes to unto 5dimensional sfs. A comparison can be found here: safv3
See realSFS for how to convert the new safformat to the old safformat if you use NGStools.
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
* This page was last modified on 24 March 2016, at 09:17.