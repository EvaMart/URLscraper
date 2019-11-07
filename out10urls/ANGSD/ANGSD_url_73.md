<-- http://www.popgen.dk/angsd/index.php/Special:Random-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
* This program will estimate the (multi) SFS based on a .saf file generated from the **./angsd [options] -doSaf **.
* It can also textoutput the saf files.
* It can also convert to the old format.
* You can also specify regions of analysis using -r chromoname:start-stop
* you can also estimate fst and pbs with realSFS see Fst PCA.
* You can also supply -sites directly to the realSFS subprogram for choosing a subset of sites. This could be useful if you are interested in the spectra for differenct functional categories.
* You can also merge saf files. Then you can run angsd on the separate chromosomes and merge afterwars
See also SFS Estimation and 2d SFS Estimation.
* 1 Brief overview
* 2.1 Estimating SFS
* 2.2 Printing the SAF
* 3 Estimating 1d SFS
* 4 Estimating 2dsfs
* 8 Using NGStools/NGSpopgen
* 9 Merge SAF files
-> EXAMPLES FOR ESTIMATING THE (MULTI) SFS:
-> Estimate the SFS for entire genome??
-> ./realSFS afile.saf.idx 
-> 1) Estimate the SFS for entire chromosome 22 ??
-> ./realSFS afile.saf.idx -r chr22 
-> 2) Estimate the 2d-SFS for entire chromosome 22 ??
-> ./realSFS afile1.saf.idx  afile2.saf.idx -r chr22 
-> 3) Estimate the SFS for the first 500megabases (this will span multiple chromosomes) ??
-> ./realSFS afile.saf.idx -nSites 500000000 
-> 4) Estimate the SFS around a gene ??
-> ./realSFS afile.saf.idx -r chr2:135000000-140000000 
-> Other options [-P nthreads -tole tolerence_for_breaking_EM -maxIter max_nr_iterations -bootstrap number_of_replications]
-> See realSFS print for possible print options
-> Use realSFS print_header for printing the header
-> NB: Output is now counts of sites instead of log probs!!
-> NB: You can print data with ./realSFS print afile.saf.idx !!
-> NB: Higher order SFS's can be estimated by simply supplying multiple .saf.idx files!!
-> NB: Program uses accelerated EM, to use standard EM supply -m 0 
./realSFS afile.saf.idx [-start FNAME -P nThreads -tole tole -maxIter  -nSites  ]
./realSFS pop1.saf.idx pop2.saf.idx [-start FNAME -P nThreads -tole tole -maxIter  -nSites]
./realSFS pop1.saf.idx pop2.saf.idx pop3.saf.idx [-start FNAME -P nThreads -tole tole -maxIter  -nSites]
The saf files are generated using  ./angsd -doSaf.
-start is a file containing a log scaled estimate of the SFS that can be used as the start point for the EM optimisation. -tole When the difference in successive likelihood values in the EM algorithm gets below this value the optimisation will stop -P number of threads to allocate to program -nSites Limit the optimisation to a region of this size. If nothing is supplied the program will use the entire saf file -maxIter maximum number of iterations in the EM algorithm
You can also specify a region to use for estimating the SFS
./realSFS pop1.saf.idx pop2.saf.idx -r chr22:10000000-20000000
## Printing the SAF
./realSFS print pop1.saf.idx pop2.saf.idx
#two populations chr2 from 100mb to 110mb
./realSFS print pop1.saf.idx pop2.saf.idx -r chr2:100000000-110000000
And you can convert to the old <0.800 format using -oldout 1.
# Estimating 1d SFS
realSFS sfstest.saf.idx -P 4 >sfs.em
The **realSFS** program will read in a block of the genome (from the .saf) file, and for this region it will estimate the SFS.
The size of the block can be choosen using -nSites argument, otherwise it will try to read in the entire saf file.
If you have .saf file larger than -nSites (you can check the number of sites in the .saf.pos file), then the program will loop over the genome and output the results for each block. So each line in your Whit.saf.ml, is an SFS for a region.
./realSFS pop1.saf.idx pop2.saf.idx[-start FNAME -P nThreads -tole tole -maxIter  -nSites  ]
Main results are printed to the stdout. These are the expected values. For 2dsfs the results is a single line, assuming we have n categories in population1 and m categories in population2, then the first m values will be the SFS for the first category in population1, etc.
Use as many sites as possible, for more reliable estimates.
The -nSites is used for choosing a max number of sites that should be used for the optimization. Using more sites will give you more reliable estimates. If you dont specify anything it will try to load all sites into memory.
The software from Matteo Fumagalli [1] expects the old format saf files, and these can be generated using realSFS
#example using three pops
realSFS print pop1.saf.idx pop2.saf.idx pop3.saf.idx -oldout 1
#example using two pops
realSFS print pop1.saf.idx pop2.saf.idx -oldout 1
This will then generate a single **shared.pos.gz** file, and a **.saf** file for each saf file. The output will only be generated for the sites that exists in all populations.
# Merge SAF files
-> This will cat together .saf files from angsd
-> regions has to be disjoint between saf files. This WONT be checked (alot) !
-> This has only been tested on safs for different chrs !
-> outnames: '(null)' number of safe:0
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
* This page was last modified on 15 July 2016, at 13:11.