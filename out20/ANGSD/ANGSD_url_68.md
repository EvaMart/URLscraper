<-- http://www.popgen.dk/angsd/index.php/Quick_Start-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
This page all contain some random examples that shows some aspect of the ANGSD program. We assume you will have SAMtools installed for general BAM/CRAM manipulation
Many of the examples in the individual subpages are based on this test data set. The examples below are just some random examples.
* 1 Download and prepare
* 1.1 BAM files from 1000genomes project
* 1.2 Ancestral fasta file for hg19
* 2.1 Calculate Allele frequencies
* 2.2 Generate Beagle Likelihood files
# Download and prepare
## BAM files from 1000genomes project
First download some test data of random small BAM files which contains some regions from different chromosomes for 10 samples from the 1000genomes project. The file size is around 100megabytes.
This has made a folder called **bams/**, which contains our 10 samples. Now download and install angsd you can follow the guidelines at the Installation page.
We will also index the BAM files in case we need to do random access, for this we will use SAMtools.
for i in bams/*.bam;do samtools index $i;done
We make a file containing a list of the locations of the 10 bamfiles
ls bams/*.bam > bam.filelist
## Ancestral fasta file for hg19
If you want to run the SFS examples on the wiki you should also download the ancestral states for the hg19 assembly of the human genome.
NB some have complained that the popgen.dk server is unstable, and we are therefore also hosting the compressed .fa file here: http://dna.ku.dk/~thorfinn/hg19ancNoChr.fa.gz
## Calculate Allele frequencies
Assuming you have a list of bamfiles in in file: 'bam.filelist' and you want the MAF using all reads and inferring the major and minor from the GL, we will use SAMtools genotype likelihoods, and will allow for 5 threads: See details on Allele Frequencies, Major Minor and Genotype Likelihoods.
./angsd -b bam.filelist -GL 1 -doMajorMinor 1 -doMaf 2 -P 5
./angsd -b bam.filelist -GL 1 -doMajorMinor 1 -doMaf 2 -P 5
-> angsd version: 0.574	 build(Jan 10 2014 17:44:41)
-> No '-out' argument given, output files will be called 'angsdput'
-> Parsing 10 number of samples 
-> Printing at chr: 20 pos:14095816 chunknumber 3500
-> Done reading data waiting for calculations to finish
-> Done waiting for threads
-> Fri Jan 10 17:46:15 2014
-> Arguments and parameters for all analysis are located in .arg file
[ALL done] cpu-time used =  130.67 sec
[ALL done] walltime used =  55.00 sec
The output is then located on angsdput.mafs.gz. We could have specified an different output file name with **-out**. Lets remove those reads that has a mapping quality below 30, and only use the bases with a score above 19. And to simply output we only print those sites with an allele frequency above 0.05.
./angsd -b bam.filelist -GL 1 -doMajorMinor 1 -doMaf 2 -P 5 -minMapQ 30 -minQ 20 -minMaf 0.05
./angsd -b bam.filelist -GL 1 -doMajorMinor 1 -doMaf 2 -P 5 -minMapQ 30 -minQ 20 -minMaf 0.05 
-> angsd version: 0.574	 build(Jan 10 2014 17:44:41)
-> No '-out' argument given, output files will be called 'angsdput'
-> Parsing 10 number of samples 
-> Printing at chr: 20 pos:14085533 chunknumber 2800
-> Done reading data waiting for calculations to finish
-> Done waiting for threads
-> Fri Jan 10 17:57:55 2014
-> Arguments and parameters for all analysis are located in .arg file
[ALL done] cpu-time used =  123.48 sec
[ALL done] walltime used =  51.00 sec
And lets look at the output:
gunzip -c angsdput.mafs.gz |head
We have 10 samples, lets only look at the sites where we have information from at least 8 individuals.
./angsd -b bam.filelist -GL 1 -doMajorMinor 1 -doMaf 2 -P 5 -minMapQ 30 -minQ 20 -minMaf 0.05 -minInd 8
./angsd -b bam.filelist -GL 1 -doMajorMinor 1 -doMaf 2 -P 5 -minMapQ 30 -minQ 20 -minMaf 0.05 -minInd 8
-> angsd version: 0.574	 build(Jan 10 2014 17:44:41)
-> No '-out' argument given, output files will be called 'angsdput'
-> Parsing 10 number of samples 
-> Printing at chr: 20 pos:14085533 chunknumber 2800
-> Done reading data waiting for calculations to finish
-> Done waiting for threads
-> Fri Jan 10 18:11:09 2014
-> Arguments and parameters for all analysis are located in .arg file
[ALL done] cpu-time used =  36.64 sec
[ALL done] walltime used =  30.00 sec
And look at the output:
gunzip -c angsdput.mafs.gz |head
## Generate Beagle Likelihood files
For diploid samples we have 10 possible genotypes. but we would only expect to observe two different alleles at most sites. We can infer the major and minor allele and output the 3 possible genotypes in beagle genotype likelihood format. Furthermore we are only interested in variable sites, so let us use the LRT statistic for filtering out the sites that are very likely to be polymorphic with a p-value less than 10^-6. We need to allele frequency in order to test if a site is polymorphic.
./angsd -GL 2 -doGlf 2 -b bam.filelist -doMajorMinor 1 -SNP_pval 1e-6 -doMaf 1
./angsd -GL 2 -doGlf 2 -b bam.filelist -doMajorMinor 1 -SNP_pval 1e-6 -doMaf 1 
-> angsd version: 0.574	 build(Jan 10 2014 17:44:41)
-> No '-out' argument given, output files will be called 'angsdput'
-> Parsing 10 number of samples 
-> Printing at chr: 20 pos:14095816 chunknumber 3500
-> Done reading data waiting for calculations to finish
-> Done waiting for threads
-> Fri Jan 10 18:26:56 2014
-> Arguments and parameters for all analysis are located in .arg file
[ALL done] cpu-time used =  27.24 sec
[ALL done] walltime used =  27.00 sec
Let us look at the generated output file: angsdput.beagle.gz. We only look at the data for the first 2 individuals.
gunzip -c angsdput.beagle.gz | less -S
marker allele1 allele2 Ind0 Ind0 Ind0 Ind1 Ind1 Ind1
1_14000202 2 0 0.000532 0.999468 0.000000 0.333333 0.333333 0.333333
1_14000873 2 0 0.000000 0.030324 0.969676 0.663107 0.333333 0.003560
1_14001018 3 1 0.000000 0.015429 0.984571 0.799823 0.200177 0.000000
1_14001867 0 2 0.000056 0.333333 0.666611 0.888793 0.111207 0.000000
1_14002342 1 3 0.941072 0.058928 0.000000 0.888806 0.111194 0.000000
1_14002422 0 3 0.000000 0.111147 0.888853 0.799777 0.200223 0.000000
1_14002474 3 1 0.969662 0.030338 0.000000 0.799810 0.200190 0.000000
1_14003581 1 3 0.000000 0.200027 0.799973 0.984577 0.015423 0.000000
1_14004623 3 1 0.000000 0.200035 0.799965 0.984501 0.015499 0.000000
Notice that the 'marker' contains the genomic position, encoded by using underscore as separator.
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
* This page was last modified on 4 December 2015, at 14:58.