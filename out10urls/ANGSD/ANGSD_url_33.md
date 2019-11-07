<-- http://www.popgen.dk/angsd/index.php/MsToGlf-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
For the Korneliussen2013 paper, we simulated data according to genotypes simulated from ms/msms output. For this we used the msToGlf program found in the 'misc/' subfolder of the angsd source directory.
This program assumes diploid samples.
* 1 Brief Overview
* 2 Output format
* 3.1 Standard neutral model
* 3.2 With Selection
* 3.3 Two populations
Probs with args, supply -in -out
also -err -depth -depthFile -singleOut -regLen -nind
-in ms/msms outputfilename -out prefix output filename -regLen [int] Number of base pairs the ms/msms output is supposed to represent. This is for each repetition. -singleOut [zero or one] ms/msms can generate multiple replicates of the same scenario '-singleOut 1' will generate a single output file -depth average sequencing depth -nind Number of individuals in the ms/msms file (only needed in combination with -depthfile) -err errorrate, a value 0.005 corresponds to a 0.5% errorrate. -depthFile filename, This is useful if you want to force a different mean depth between individuals, remember to also use -nind if you use this option. -pileup [int] 0 print GLF, 1 print mpileup format that can be read my ANGSD using the -pileup option -Nsites [int] 0 normal ms output, 1 msms -N [INT] output
The program will dump a binary compressed file. It will calculate all 10 possible genotype likelihoods for each individual for all sites. The genotypes are in the order AA,AC,AG,AT,CC,CG,CT,GG,GT,TT. These are encoded as ctype 'double'. So the size requirements for a single site for N individuals are 'N*10*sizeof(double)'.
## Standard neutral model
This ms/msms command will generate haplotypes assuming human recombination/mutation rates for a 1mb region. We will make 50 haplotypes (25 diploids) and do 14 repetitions.
msms -ms 50 14 -t 900 -r 400 -oTPi 0.05 0.05 -oAFS >msoutput
Now we will simulate genotype likelihoods assuming an errorate of 1.5% and a sequencing depth of 8x, but only for the variable/informative sites contained in the msoutputfile
./msToGlf -in msoutput -out msoutputNoInvar.gl -err 0.015 -depth 8 -nind 25 -singleOut 1
The output is single, very small file called 'msoutputNoInvar.gl.glf.gz'.
Now lets do a more realistic example, where we don't limit ourselves to the informative sites but also simulate all the invariable sites for our 1mb region.
./msToGlf -in msoutput -out msoutputWithInvar.gl -err 0.015 -depth 8 -nind 25 -singleOut 1 -regLen 1000000
These can be feed into angsd using -glf argument as input
../angsd -glf msoutputNoInvar.gl.glf.gz -nind 25 -doMajorMinor 1 -doMaf 1 -fai hg19.fai -isSim 1
If you do sample allele frequency based analysis '-doSaf' then the ancestral states are assumed to be 'A'.
The below command will generate 100 replicates of a scenario with strong positive selection in the center of 1mb region, assuming 25 diploids.
msms -ms 50 100 -t 900 -r 400 -SAA 1000 -SaA 500 -N 10000 -SF 0 -Sp .5 -oTPi 0.05 0.05 -oAFS >msoutput
And lets generate genotype likelihoods corresponding to the above command. This will take some time and fill up considerable amounts of diskspace. Because its the full data for a 100mb region for 25 samples. We here assume 2x data with 0.5% errors.
./msToGlf -in msoutput -out withselection.gl -err 0.005 -depth 2 -nind 25 -singleOut 0 -regLen 1000000
This will generate msoutput for 20 diploids in total doing 10 repetitions each based on a 1mb region. Using human mutaiton/recombination rates. These parameters are supposed to mimic the population bottleneck followed by rapid expansion similar to europeans and african populations. We have 12 individuals i population1 and 8 individuals form population2.
Not really sure where I got this command.
msms -ms 40 10 -t 930 -r 400 -I 2 24 16 0 -g 1 9.70406 -n 1 2 -n 2 1 -ma x 0.0 0.0 x -ej 0.07142857 2 1  >msoutput
Let's run the mstoglf command:
./msToGlf -in msoutput -out raw -singleOut 1 -regLen 0 -depth 6 -err 0.005
We here specify a mean sequencing depth of 6, and an error rate of 0.5%. We only generate genotype likelihoods for the informative sites (-regLen 0), and generate a single output file.
We now slice out the two populations into seperate files:
angsd/misc/splitgl raw.glf.gz 20 1 12 >pop1.glf.gz 
angsd/misc/splitgl raw.glf.gz 20 13 20 >pop2.glf.gz 
And we run -doSaf 1 on both files
./angsd -glf pop1.glf.gz -nInd 12 -doSaf 1 -out pop1 -fai hg19.fai -isSim 1
./angsd -glf pop2.glf.gz -nInd 8 -doSaf 1 -out pop2 -fai hg19.fai -isSim 1
And finally lets estimate the 2dsfs using the full ML method included in **realSFS**:
realSFS 2dsfs pop1.saf pop2.saf 24 16 -P 4 >pop.em.ml
The output is 25x17 matrix You can then read in the data in R and barplot the marginals
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
* This page was last modified on 5 February 2016, at 17:44.