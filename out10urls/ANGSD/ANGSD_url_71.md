<-- http://www.popgen.dk/angsd/index.php/ThetaStat-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
Small program to do window statistics.
Here is what the program is supposed to do.
1) define a positionstart pS, as from the first position(on the genome) with data.
2) find a positionstep pE, which is pS+winsize. If pE is after the last position(on the genome) with data exit.
3) calculate statistics using the region that is spanned by pS and pE.
4) increment pS with stepsize, goto step 2). 
For a description of the type. See the information regarding the fst window analysis here:
'./thetaStat': a program to do neutrality test statistics using thetas.idx output from angsd
1) ./thetaStat print angsdput.thetas.idx
2) ./thetaStat do_stat angsdput.thetas.idx -win 5000 -step 1000
Type './thetaStat do_stat' or './thetaStat print' for more information
./thetaStat print angsdput.thetas.idx [-r chrName]
2)./thetaStat print angsdput.thetas.idx -r chr2
./thetaStat do_stat .thetas.idx [-win INT -step INT -r chrName -type [0,1,2] -outnames outputprefix]
2)./thetaStat do_stat angsdput.thetas.idx -win 5000 -step 1000
3)./thetaStat do_stat angsdput.thetas.idx -win 5000 -step 1000 -r chr1
4)./thetaStat do_stat angsdput.thetas.idx -win 5000 -step 1000 -r chr1 -nChr 20 -outnames newoutputname
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
* This page was last modified on 20 April 2018, at 11:10.