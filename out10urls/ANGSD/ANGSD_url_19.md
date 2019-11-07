<-- http://www.popgen.dk/angsd/index.php/Download_and_installation-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
(Redirected from Download and installation)
Jump to: navigation, search
There has been some confusion about the versions of ANGSD.
* Even versions are freezes from the last odd giversion
* Odd versions are git versions. Once there has been enough commits we will increment and make a release.
* 1 Download and Installation
* 3 Install from github
* 4 Systemwide installation of htslib?
# Download and Installation
To download and use ANGSD you need to download the htslib and the angsd source folder
You can either download the angsd0.930.tar.gz which contains both. [1]
Or you can use github for the latest version of both htslib and angsd
Earlier versions from here: http://popgen.dk/software/download/angsd/ And here: https://github.com/ANGSD/angsd/releases
Download and unpack the tarball, enter the directory and type make. Users on a mac computer, can use curl instead of wget.
The software can be compiled using make.
The executable then located in **angsd/angsd**.
# Install from github
To install CRAM support you also need to install htslib and can be done using the following commands
git clone https://github.com/ANGSD/angsd.git 
cd htslib;make;cd ../angsd ;make HTSSRC=../htslib
# Systemwide installation of htslib?
Then you just type make in the angsd directory
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
* This page was last modified on 26 August 2019, at 12:12.