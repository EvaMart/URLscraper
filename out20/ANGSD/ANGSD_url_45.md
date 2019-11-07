<-- http://www.popgen.dk/angsd/index.php/Angsd_structure-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
This page contains a short description of the overall structure of angsd.
It can be divided into:
We allow for many different input formats, many of these are deprecated and have little use, but we have decided to keep these.
2. soap alignment files
4. glfv3 (Binary and text)
The data for the different input formats are encapsulated in a struct 'funkyPars', and this struct is sent to the 'analysis' classes, which will do analysis and populate the struct with results (eg based on the sequencing data we calculate genotype likelihoods and attach this to the struct).
Depending on the input format the information in the struct will span different regions. For the Beagle files the region size is defined by **-chunkSize**. The region size for BAM input can very quite alot since this is dependent on number of reads in the different BAM files. A thorough description of the BAM reading can be found in BAM reading details
We have defined the following **abstract base class** called general.h
static aHead *header;//contains the header of a single bam;
static std::map<char *,int,ltstr> *revMap;
//  virtuel general()
virtual void run(funkyPars *f)=0;
virtual void print( funkyPars *f)=0;
//  virtual void printArg(const char *fname)=0; <-maybe include
virtual void clean(funkyPars *f)=0;
Angsd started back in 2009 as a simple program for estimating allele frequency, based on this we incrementally added new functionality. A rough timeline can be found in the AUTHORS file in the program bundle
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
* This page was last modified on 4 December 2013, at 20:03.