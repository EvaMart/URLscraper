<-- http://www.popgen.dk/angsd/index.php/Change_log-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
* 3 0.589 to 599
* 4 <0.570 and <0.588
* 7 <0.5 and <0.570
Odd versions are github versions...
* 0.608 not super usefull but we now compile with knetfile, so users can use remote .fa files. I really recommend that users download the fasta instead.
* 0.607 changed name of all abstract base classes to the more reasonable abc*.cpp. Included contamination and the iCounts format. Added a templated class so users can see how to access the internal datastructures.
* 0.606 added more info in the thetaStat subprogram renamed all analysis classes to abc*.cpp.
* 0.605 continued updating the Eunjung code
* 0.604 added a 'job' array for the analysis classes which should greatly reduce the number of needed function call. I doubt that will make any noticeable speed difference. Has copied and modified some code from Eunjung (from jnovembre lab) for a banded approach in the saf calculation. This is not working yet -doSaf 2
* 0.603 1) fixed wrong branching if users used simfiles. 2) fixed 2 bugs in the inbreeeded angsd_realSFS.cpp. Very small changes
* 0.602 1) programs output the actual chromosome, if there is a mismatch between the fasta and bamheader 2) added a check that the index files (fa vs fai,bam vs bai) is newer than the index. 3) Program now validates that the .so and include files used are the same.
* 0.601 1) started the move to includeflags/discardflags, outcommented in this version 2) validates that data has been generted for the different samples by looking at difference between values, instead of comparing againts -0.0. 3) MAF estimates now skips estimation for a site if the updated GL shows that GLs are noninformative.
* 0.600 fixed a change in default FLAGS when using bam files. If you hadn't removed the unmapped reads from your bamfiles these would have been included in the analysis.
# 0.589 to 599
* 0.589 removed soap/sim/glf/glfclean(bin and text) and tglf.
* 0.590 added text mpileup as new input format. Very useful
* 0.591 refactored the file reading, moved the arguments to multi reader, such that all file reading is done from multi reader. FREEZE version. We will only allow bug fixes in the next many versions.
* 0.592 -pest output in angsd_realSFS.cpp. smartcounts. fixed a bug in hetplas. edited the printout msg for 'if you really want angsd to exit' -pest output in angsd_realSFS.cpp. smartcounts. fixed a bug in hetplas. edited the printout msg for 'if you really want angsd to exit'. Maybe fixed an unknown bug. line 2 in .arg or screen output is now commandline used, and some other visual stuff. Program didn't complain if -doMaf but no -domajorminor. if chromosomesome name contained ':" it wouldn't work strchr->strrchr
* 0.593 fixed a strange bug, where the program would crash if, no analysis was chosen. fixed the 'shouldbeone' bug.
* 0.596 fixed a bug in persite depth counter (double count of C alleles). fixed a bug in smartcount subprogram.
* 0.597 treemix input file generation from smart counts
* 0.598 fixed a wrong compile flag in one of the utility programs 'smartCount'
* 0.599 many much more informative information if users forgot to add -fai argument. Fixed a bug in parsing of arguments with -doSaf 4.
# <0.570 and <0.588
* 0.571 removed bf's from maf classs, negative values of -domaf disabled dumping of files, inbreeding has been added
* 0.572 Some funky new approach for the makefile is now being used, minor bug fixes (minDepth -> setMinDepth, extra header column in thetas.gz has been fixed)
* 0.573 added better info barfiles have different header. Added check if length of supplied reference/ancestral doesn't match bamheader. autosize in emOptim2 for 2dsfs. Fixed subtle issue if very large coverage between bamfiles, now the 'biggests(file size)' is used to select region instead of the first baffle. Netaccess is now deprecated.
* 0.574 modifed emOptim2 so now compiles on mac
* 0.575 smaller fixes to the inbreeding parsing, added p-value in analysisMaf instead of the raw llh.
* .0.576 -doSNP and -minLRT now deprecated, please use -SNP_pval instead
* 0.577 bugfix for -SNP_pval if value was one 1. doHWE now called -HWE_pval and can be used for filtering.
* 0.578 speedup in hew stuff
* 0.579 fixed an extremely rare assertion error (program was working, assertion was off). Redid all strcmp to strcasecom. Fixed a bug in -doMaf 2 with -snp_pval
* 0.581 if trimming has been enabled, N's will be plugged in instead of the bases. A number of small changes.
* 0.583 1) changed bugfix when using counts based estimator for major/minor 2) keepsites is now using the effecive number of samples in all cases 3) changed output of maf to a 'nicer' format
* 0.584 updated internal testing scripts.
* 0.585 1) fixed 'baq complains even though -ref was supplied' 2) fixed -doMajorMinor 4 and doMajorMinor 5 (sites not discarded) 3) added trumendounsly better information for the -sites 4) added some check for -doPost 5) program can now exit uncleanly if ctrl+c is pressed 3 times. 6) added an else to catch wrong arg in theteStat.
* 0.586 1) fixed parsing of pars if input is -sim1 2) fixed a bug in -doFasta 3 (the ebd one) 3) fixed a printout problem in -doFasta
* 0.587 1) fixed a number of minor instances where memory wasn't being freed/delete (mostly for keeping valgring silent) 2) fixed a memleak if -sites files contained 4 columns but -doMajorMinor not 3. 3) fixed a memory leak that could occur if -doPost 2 and -doMaf 0.
* 0.588 1) fixed small printout error that could cause segfaults in rare cases. 2) change stderr to pos+1 3) changed some checks of user supplied pars 4) fixed a stack overflow if a very long -rf file was supplied.
* 0.16 Is now bundled with SAMtools-0.1.17 and the mpileup (and friends) command be used for passing data to dirty.
* 0.17 added extra options -minInd and -minMaf, for only printing and using sites above a threshold
* 0.18 added option to pass reference and ancestral allele as fasta files.(using faidx format) (doMaf is now encoded internally as a MAF_(UN)KNOWN_TYPE)
* 0.19 added support for tglf inputfiles, -tglf -posfile see runexamples, also added the likeratio test for snp calling
* 0.20 Added the check for missing data, before the major/minor. included -realSFS, changed the deallocation of the -doMAF results, such that its proper cleaned up.
* 0.21 refactored pml.cpp into pml_estError_genLikes.cpp and pml_freq_asso.cpp (fixed a bug that preventede -samglf and samglfclean from working)
* 0.22 Well this update was a mixture of edits from user:albrecht and BGI so its difficult to give a concise description
* .0.23 Program can now read simulated files (single pop only) An example can be seen in "full example ... sfs" and input types.
* 0.24 added the tajima estimator. This should go in tandem with some R scripts. Had to modify parseargs, shared, and pml_freq_asso
* 0.25 the depth is now being populated when using mpileup -g. The program can now get the counts from mpileup
* 0.01.a - 0.01.b The bfgs now supports threading, maybe anders implemented a heteorzygosity estimator.
* 0.01.c A problem if we didn't observe any llh, caused the MAF estimator to 'nan'.
* 0.02 Fixed small bug in bfgs optimization of sfs optimization. When choosing a region bigger than what was covered by the .sfs file the program would hang. Added genotypecaller, added -sfsEst to the realSFS part of the program.
* 0.03 added and documented genotypecaller, can dump counts,-realSFS 1 dumps positions, -realSFS 2 is deprecated,S,pi and tajima has been added to sfstools along with possibility to do prior
* 0.3 clean version with less features. The lost features will be reintroduced later.
* 0.43 first very clean version, everything should be included
* 0.441 rewrote the SOAPsnp GL model, -L and -maxQ is not needed anymore. Also added an option to choose an output dir for the recalibration matrix
* 0.4471 error estimation is now working, the fasta reading is now threadsafe. all GLs are now likeratios.
* 0.512 After 0.500 we have changed the internal structure such that each chunk is enforced to be on the same chr. version c) fixes a problem of hardclipping
* 0.515 Alot of legacy code has been removed from mUppile.cpp. Program can now use remote files, build on code from SAMtools
* 0.520 Alot more legacy code has been removed from mUpPile.cpp. Program now does baq and adjustment of mapQ similar to -C in samtools. Also compiles on osx, but this is not supported
* 0.535 Bug in internal representation of mapQ's (only problematic for mapQ>128), we now use the flag to determine if a read has mapped. calcstat is now deprecated, users should use the bgid program now.
* 0.538 changed position output in association part. Fixed incorrect assert assumption in mUpPile.cpp. Added some downsampling options for errorEst and changed internal buffering when reading beagle files to allow for >10k individuals.
* 0.549 to many changes to remember
# <0.5 and <0.570
* 0.551 tajima paper is now published, so the emOptim2 and bgid has now been properly documented. plink output is now supported and some snp filters can be outputted.
* 0.552 minor bug when calling genotypes without defining postcutoff -> missingness couldnt occur. removed the optimSFS and emOptim from the default compilelist
* 0.553 uint removed from code.
* 0.554 plugged in sfstools functionality into main angsd, (ability to output log posts)
* 0.555 anders added some concensus stuff
* 0.556 updated the filtering (if binary rep of keep file is incomplete it is removed again. It checks timestamps to see if file has been updated), folded spectra analysis should now be working
* 0.557 There was a bug in the realsfs part of the code, that was created in the 0.556 version. 0.557 is simply a fix of this, and the removal of a warning compiler flag in the msToGlf subprogram. We only observed the problematic compiler flag on a osx machine
* 0.558 tempversion,from this version bgid is now called thetaStat
* 0.560 analysisCount.cpp has been updated to the nice standard of the wiki
* 0.561 program now compiles on clang, many small compiler warnings has been fixed.
* 0.562 Merge of forked versions, abba-baba fasta.
* 0.563 minQ filter has been moved to a much earlier step. Previously it was downstream classes that checked this. Now a base will be set to 'n' if it is below the threshold
* 0.564 cleaned up funky pars maf/asso such that all results are in ->extras[]
* 0.565 moved file reading stuff from shared to analysisFunction in namespace ail::
* 0.566 cleaned up small things, added a newer version of hetplas
* 0.567 cleaned up small things again. Started to add single pars e.g. -P -b
* 0.568 refactored compile order in general.cpp
* 0.569 added saf genotype calling, changed name from -realsfs to -doSaf
* 0.570 modified emOptim2 to estimate nSites and tell how much memory it will use, fixed empty -bam file
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
* This page was last modified on 26 August 2019, at 12:10.