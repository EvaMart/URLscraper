<-- http://www.popgen.dk/angsd/index.php/Error_estimation-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
ANGSD currently has 2 different methods for estimating error rates.
1. A method that will estimate the joint typespecific errorrates for multiple samples. This method is using the minor allele frequency as prior, and therefore this method can not be used for single samples.
1. A method that that uses an outgroup and an 'errorfree' individual. Useful for single samples.
The type specific errorrates is an  matrix, with the error rates of observing base e.g. **A** when in reality the true base is e.g. **C**.
* 1 Error estimation from polymorphic sites
* 1.1 Brief Overview
* 2 Error estimation using an outgroup and an error free individual
* 2.1 Brief Overview
* 3 Mismatch rates
# Error estimation from polymorphic sites
The method for estimating type specific errors is described in Kim2011, and is based on the _counts_ of the 4 different nucleotides. This method should be applied to the sites that are variable and the measure for variability is the simple MAF estimator that is described in Li2010. The idea of the method is briefly described here
NB The analysis will use at least a prespecified number of sites (-minSites) for that analysis. If you do not have this number of variable sites, then the analysis will not be performed.
-> angsd version: 0.564  build(Dec  6 2013 12:52:55)
-> Analysis helpbox/synopsis information:
-doError        0
1: SYK method, joint typespecific errors (Multisample)
-minSites       10000
-errors         (null)  (Filename for starterrors)
-emIter         100
-minPhat        0.005000        (Minimum phat)
-eps            0.001000        (Estimate of errorrate)
NB this method requires -doMajorMinor 2
default 10000. This is the minimum number of sites we used in the analysis. Every time this number of variable sites is read the error rates are estimated. This means that multiple error rates are estimated if the number of variable sites in you data exceeds the minimum number of sites.
default 0.005. This means we only run the error estimation on sites with a MAF>0.005. This should be modified according to the number of samples in the dataset.
default 0.001.This is a guess of the error rate in the sample, this is used for the simple MAF estimator
This file should contain a start guess of the type specific errors.
To further refine what data should be used please see alleles counts and input#Bam_files.
The simplest example is:
./angsd -bam bam.filelist -doCounts 1 -out test  -doError 1 -doMajorMinor 2 -nThreads 5 -minSites 1000 -r 1:
Or a more elaborate example where we only want to estimate the typespecific errors for the "good" data:
./angsd -bam bam.filelist -doCounts 1 -out test2  -doError 1 -doMajorMinor 2 -nThreads 5 -minSites 1000 -minQ 20 -minMapQ 30 -r 1:
The output for this analysis is a file suffixed with ***.error.chunkunordered**.
Notice that we for the more stringent test2 dataset have somewhat lower error rates. But we should really choose a much larger number of sites to do this analysis. Each line has 16 entries corresponding to the type specific errors for a region of **-minSites**.
NB Currently the ordering of each line, can not be interpreted as the error rates along the genome, due to the threading. If no threading is used the order is preserved. This will likely change in future versions.
We can visualise this easily in R, see figures on right side (These are not the values from the above)
names(a) <- as.vector((sapply(1:4,function(x) paste(DNA[x],DNA,sep="->"))))
# Error estimation using an outgroup and an error free individual
The estimated rates can roughly be interpreted as relative error rates. That is excess of derived alleles in your sample compare to the derived alleles in the an error free indviduals The idea is the your sample and the error free individuals should have the same expected number of derived alleles and the extra observed derived alleles in you sample are due to the excess error. For each individual we sample a single base from the reads at each position. We use only positions were there are coverage for both the outgroup, the sample and the error free individual. Some more details about the method is described here.
If you work with human data mapped to hg19 we have a fasta file containing the ancestral states (actually the chimp mapped to hg19).
-> angsd version: 0.580	 build(Feb 26 2014 10:11:49)
-> Analysis helpbox/synopsis information:
0:	 no error estimation 
1:	 (Use all bases)
2:	 (Sample single base)
3:	 (Sample first base)
-ref	(null)	(fastafile containg 'perfect' sample)
NB: the -ref should be a fasta for a sample where you assume no errors.
We measure the difference between the outgroup and your -ref sample.
The statistic is then the excess of substitutions between your BAM file and outgroup, compared to the perfect sample. After the ANGSD run use:  Rscript R/estError.R file=angsdput.ancerror
**To make matters explicit:** For this analysis, the **-ref** should not be your reference, but a fasta file containing the consensus of a 'perfect' sample. The method will calculate the difference between the **-ref** and **-anc**, and the difference between the supplied BAM files, and interpret the excess of difference as an error. You can generate a consensus fasta with  -doFasta. 
Use -doAncError to use this analysis. 0: No error estimation
1: Use all reads
2: Sample only one base per site
3: Use first read per site (the reads are order with position start)
To further refine what data should be used please see alleles counts and  read filters.
fasta file with the ancestral alleles
fasta file of an error free individual. ]
- angsd -doAncError 1 -anc chimpHg19.fa -ref hg19perfect.fa -out results -bam bam.filelist
- Rscript R/estError.R file=results.ancError
Typing Rscript R/estError.R will give you additional options for plotting the results.
The command for plotting the figure on the right was given as:
Rscript R/estError.R file=output/smallBamMicsAncq30Q20.ancError main="Errorrate using outgroup (CHIMP) and a perfect MAN" doPng=TRUE
NB the script will generate an empty Rplots.pdf file. This is expected. Sorry about this. The reason is that we haven't figured out how to change the R command called palette without generating a Rplots.pdf file (stupid R 3.+ color palette).
1. The output from the angsd cprogram is in a horrible format. Those are 2 files suffixed with ***.ancError** and ***.ancErrorChr**.
For each individual we allocate a integer vector with 125 entries. Each entry represents the counts of combinations of the outgroup,perfect,sample alleles. The offset is given by: outgroup*25+perfect*5+bam;With the bases encoded as a=0,c=1,g=2,t=3,n=4
1. The Rscript will output the type specific errors and the overall errors. It will also produce two figures. One will the type specific errors and one with the overall errors. If a lot of individuals are included in the analysis the figure will need to be modified. The output is 3 files: 2) figures called **errorEst/errorEstOverall**. And a text file containing the values used for generating the figures. Example below
"C -> A"	"G -> A"	"T -> A"	"A -> C"	"G -> C"	"T -> C"	"A -> G"	"C -> G"	"T -> G"	"A -> T"	"C -> T"	"G -> T"
Type, strand, read position specific mismatch rates can be obtain using the soapSNP genotype likelihood method. Use a reference genome with known variations removed to reduce the bias of this method
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
* This page was last modified on 12 January 2017, at 13:57.