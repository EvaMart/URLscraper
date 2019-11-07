<-- http://www.popgen.dk/angsd/index.php/Tajima-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
This method will estimate different thetas (population scaled mutation rate) and can based on these thetas calculate Tajima's D and various other neutrality test statistics. Method is described in Korneliussen2013.
* NB Information on this website is for version 0.917-33-g6d2aec8 or higher.
* NB The Korneliussen2013 covers two methods, 
1. using an ML method 
2. using the emperical Bayes (EB) method. The information on this page relates to the EB method.
For performing the ML method, you should the use the SFS Estimation method and define the region af interest.
* 1 Quick Example
* 1.1 Full command list for below examples
* 1.2 Step 1: Finding a 'global estimate' of the SFS
* 1.3 Step 2: Calculate the thetas for each site
* 1.4 Step 3a: Estimate Tajimas D and other statistics
* 1.5 Step 3b: Sliding Window example
* 2 Example Output
* 2.1 ./thetaStat print angsdput.thetas.idx
* 3 Unknown ancestral state (folded sfs)
Below is a chain of commands used for caculating statistics. These are based on the test files that can be dowloaded on the Quick Start  page.
Its a 3 step procedure
1. Estimate an site frequency spectrum. Output is **out.sfs** file. This is what is being used as the **-pest ** argument in step2.
2. Calculate per-site thetas. Output is a **.thetas.idx/.thetas.gz** files. This contains the binary persite estimates of the thetas.
3. Calculate neutrality tests statistics. Output is a **.thetas.idx.pestPG file.**
## Full command list for below examples
Here is the chain of commands required to do estimate the thetas, and perform neutrality test statistics. These different commands are described in great detail in the following **step 1,... step 3b** sub sections.
./angsd -bam bam.filelist -doSaf 1 -anc chimpHg19.fa -GL 1 -P 24 -out out 
./misc/realSFS out.saf.idx -P 24 > out.sfs
./angsd -bam bam.filelist -out out -doThetas 1 -doSaf 1 -pest out.sfs -anc chimpHg19.fa -GL 1
#Estimate for every Chromosome/scaffold
#Do a sliding window analysis based on the output from the make_bed command.
./misc/thetaStat do_stat out.thetas.idx -win 50000 -step 10000  -outnames theta.thetasWindow.gz
## Step 1: Finding a 'global estimate' of the SFS
First estimate the site allele frequency likelihood
./angsd -bam bam.filelist -doSaf 1 -anc chimpHg19.fa -GL 1 -P 24 -out out
-> Reading fasta: chimpHg19.fa
-> Parsing 10 number of samples 
-> Printing at chr: 20 pos:14095817 chunknumber 3500
-> Done reading data waiting for calculations to finish
-> Done waiting for threads
-> Mon Jun 30 12:02:58 2014
-> Arguments and parameters for all analysis are located in .arg file
[ALL done] cpu-time used =  47.19 sec
[ALL done] walltime used =  43.00 sec
Obtain the maximum likelihood estimate of the SFS using the **realSFS** program found in the misc subfolder. (See more here realSFS)
./misc/realSFS out.saf.idx -P 24 > out.sfs
To plot the SFS in R :
## Step 2: Calculate the thetas for each site
./angsd -bam bam.filelist -out out -doThetas 1 -doSaf 1 -pest out.sfs -anc chimpHg19.fa -GL 1
The output from the above command are two files out.thetas.gz and out.thetas.idx. A formal description of these files can be found in the doc/formats.pdf in the angsd package. It is possible to extract the logscale persite thetas using the ./thetaStat print program.
thetaStat print out.thetas.idx 2>/dev/null |head
Per default the print command will also output the contents of the index file to the stderr.
## Step 3a: Estimate Tajimas D and other statistics
## thetaStat VERSION: 0.01 build:(Jun 30 2014,12:06:12)
#(indexStart,indexStop)(firstPos_withData,lastPos_withData)(WinStart,WinStop)   Chr     WinCenter       tW      tP      tF      tH      tL      Tajima  fuf     fud     fayh    zeng    nSites
(0,98316)(14000032,14100082)(0,14100082)        1       7050041 51.002623       46.171402       64.683834       51.290955       48.731178       -0.392892       -0.647071       -0.595302       -0.099654       -0.048444       98316
(0,98474)(13999910,14100060)(0,14100060)        2       7050030 92.689100       88.806005       101.768262      122.422498      105.614255      -0.174701       -0.252477       -0.220588       -0.360944       0.152373        98474
(0,93269)(14000529,14100095)(0,14100095)        3       7050047 70.757874       76.248087       75.447438       68.354514       72.301301       0.322902        0.020330        -0.148419       0.110921        0.023794        93269
(0,96339)(13999912,14100064)(0,14100064)        4       7050032 99.748624       107.898618      94.265208       130.283528      119.091076      0.340878        0.247030        0.123956        -0.223386       0.211971        96339
(0,99659)(13999926,14100063)(0,14100063)        5       7050031 120.941697      132.667821      86.726667       163.908351      148.288088      0.404945        0.688320        0.639821        -0.257254       0.247395        99659
(0,99541)(13999918,14100103)(0,14100103)        6       7050051 96.666344       112.146685      69.740992       143.403712      127.775201      0.667988        0.792499        0.627735        -0.321842       0.351730        99541
(0,99786)(13999926,14100047)(0,14100047)        7       7050023 93.164548       92.023886       92.742574       142.413716      117.218807      -0.051058       -0.013928       0.010201        -0.538288       0.282133        99786
(0,98759)(13999923,14100082)(0,14100082)        8       7050041 133.567125      177.157879      72.197498       204.069028      190.613463      1.363708        1.425567        1.040517        -0.200700       0.467490        98759
(0,97855)(14001686,14100094)(0,14100094)        9       7050047 88.777475       102.853333      64.660948       104.749694      103.801516      0.660983        0.776148        0.611265        -0.021256       0.184875        97855
(0,98031)(13999906,14100096)(0,14100096)        10      7050048 129.583334      134.877160      88.135115       213.231615      174.054390      0.170681        0.654145        0.724072        -0.602284       0.375595        98031
(0,99220)(13999900,14100060)(0,14100060)        11      7050030 66.349155       79.423643       60.194045       68.903312       74.163477       0.819589        0.520022        0.207421        0.157614        0.128409        99220
(0,99861)(13999913,14100078)(0,14100078)        12      7050039 86.461303       81.630083       96.156392       110.974922      96.302507       -0.232902       -0.302980       -0.252190       -0.337701       0.124323        99861
(0,98258)(13999943,14100097)(0,14100097)        16      7050048 83.191170       99.392421       77.561510       106.148748      102.770584      0.811500        0.472922        0.152079        -0.080798       0.257008        98258
(0,99428)(13999902,14100095)(0,14100095)        17      7050047 90.254620       99.816352       65.610351       113.328929      106.572638      0.441707        0.683942        0.614609        -0.148988       0.197530        99428
(0,97118)(13999898,14100071)(0,14100071)        18      7050035 79.843256       75.282296       86.844252       67.720321       71.501308       -0.237958       -0.260778       -0.196888       0.094212        -0.114062       97118
(0,93783)(13999895,14100089)(0,14100089)        19      7050044 54.311523       49.839190       64.913940       72.868913       61.354048       -0.341795       -0.495649       -0.434079       -0.421111       0.141133        93783
(0,98938)(13999916,14100091)(0,14100091)        20      7050045 68.148147       63.323800       78.463736       56.040370       59.682084       -0.294508       -0.398845       -0.338673       0.106250        -0.135474       98938
## Step 3b: Sliding Window example
We can easily do a sliding window analysis by adding -win/-step arguments to the last command.  thetaStat
thetaStat do_stat out.thetas.idx -win 50000 -step 10000  -outnames theta.thetasWindow.gz
This will calculate the test statistic using a window size of 50kb and a step size of 10kb.
- Output in the ./thetaStat print thetas.idx are the log scaled per site estimates of the thetas
- Output in the pestPG file are the sum of the per site estimates for a region
## ./thetaStat print angsdput.thetas.idx
#Chromo Pos     Watterson       Pairwise        thetaSingleton  thetaH  thetaL
1       14000032        -9.457420       -10.372069      -8.319252       -13.025778      -10.997194
1       14000033        -9.463637       -10.379368      -8.324414       -13.035780      -11.004670
1       14000034        -9.463740       -10.379488      -8.324500       -13.035942      -11.004793
1       14000035        -9.463603       -10.379328      -8.324386       -13.035725      -11.004629
1       14000036        -9.323246       -10.218453      -8.204848       -12.826627      -10.840519
1       14000037        -9.179270       -10.048883      -8.086425       -12.596436      -10.666670
1       14000038        -9.004664       -9.845473       -7.941453       -12.328274      -10.458416
1       14000039        -9.327033       -10.222983      -8.207914       -12.833007      -10.845176
1       14000040        -9.621554       -10.557563      -8.461745       -13.262415      -11.185971
1       14000041        -9.617449       -10.552869      -8.458225       -13.256257      -11.181185
1       14000042        -7.337841       -8.161756       -204.045433     -5.457443       -6.085818
1       14000043        -9.570405       -10.502160      -8.415195       -13.197596      -11.129976
1       14000044        -9.511097       -10.434558      -8.364249       -13.110037      -11.061100
1       14000045        -9.563664       -10.494371      -8.409489       -13.187203      -11.122022
1       14000046        -9.617690       -10.555402      -8.456395       -13.265004      -11.184107
1       14000047        -9.563722       -10.494438      -8.409538       -13.187292      -11.122090
1       14000048        -9.856578       -10.819096      -8.669691       -13.587898      -11.451396
4\. ThetaD (nucleotide diversity)
5\. Theta? (singleton category)
The .pestPG file is a 14 column file (tab seperated). The first column contains information about the region. The second and third column is the reference name and the center of the window.
We then have 5 different estimators of theta, these are: Watterson, pairwise, FuLi, fayH, L. And we have 5 different neutrality test statistics: Tajima's D, Fu&Li F's, Fu&Li's D, Fay's H, Zeng's E. The final column is the effetive number of sites with data in the window.
## thetaStat VERSION: 0.01 build:(Jun 30 2014,12:06:12)
#(indexStart,indexStop)(firstPos_withData,lastPos_withData)(WinStart,WinStop)   Chr     WinCenter       tW      tP      tF      tH      tL      Tajima  fuf     fud     fayh    zeng    nSites
(0,98316)(14000032,14100082)(0,14100082)        1       7050041 51.002623       46.171402       64.683834       51.290955       48.731178       -0.392892       -0.647071       -0.595302       -0.099654       -0.048444       98316
(0,98474)(13999910,14100060)(0,14100060)        2       7050030 92.689100       88.806005       101.768262      122.422498      105.614255      -0.174701       -0.252477       -0.220588       -0.360944       0.152373        98474
(0,93269)(14000529,14100095)(0,14100095)        3       7050047 70.757874       76.248087       75.447438       68.354514       72.301301       0.322902        0.020330        -0.148419       0.110921        0.023794        93269
(0,96339)(13999912,14100064)(0,14100064)        4       7050032 99.748624       107.898618      94.265208       130.283528      119.091076      0.340878        0.247030        0.123956        -0.223386       0.211971        96339
(0,99659)(13999926,14100063)(0,14100063)        5       7050031 120.941697      132.667821      86.726667       163.908351      148.288088      0.404945        0.688320        0.639821        -0.257254       0.247395        99659
(0,99541)(13999918,14100103)(0,14100103)        6       7050051 96.666344       112.146685      69.740992       143.403712      127.775201      0.667988        0.792499        0.627735        -0.321842       0.351730        99541
(0,99786)(13999926,14100047)(0,14100047)        7       7050023 93.164548       92.023886       92.742574       142.413716      117.218807      -0.051058       -0.013928       0.010201        -0.538288       0.282133        99786
(0,98759)(13999923,14100082)(0,14100082)        8       7050041 133.567125      177.157879      72.197498       204.069028      190.613463      1.363708        1.425567        1.040517        -0.200700       0.467490        98759
` (indexStart,indexStop)(posStart,posStop)(regStat,regStop) chrname wincenter tW tP tF tH tL tajD fulif fuliD fayH zengsE numSites `
Most likely you are just interest in the wincenter (column 3) and the column 9 which is the Tajima's D statistic.
The first 3 columns relates to the region. The next 5 columns are 5 different estimators of theta, and the next 5 columns are neutrality test statistics. The final column is the number of sites with data in the region.
The first **()()()** er mainly used for debugging the sliding window program. The interpretation is:
* The posStart and posStop is the first physical position, and last physical postion of sites included in the analysis.
* The regStat and regStop is the physical region for which the analysis is performed. Therefore the posStat and posStop is always included within the regStart and regStop
* The indexStart and IndexStop is the position within the internal array.
# Unknown ancestral state (folded sfs)
* Below is for version 0.556 and above
If you don't have the ancestral states, you can still calculate the Watterson and Tajima theta, which means you can perform the Tajima's D neutrality test statistic. But this requires you to use the folded sfs. The output files will have the same format, but only the thetaW and thetaD, and tajimas D is meaningful.
Below is an example based on the earlier example where we now base our analysis on the folded spectrum. Notice the -fold 1
First estimate the folded site allele frequency likelihood
./angsd -bam bam.filelist -doSaf 1 -anc hg19.fa -GL 1 -P 24 -out outFold -fold 1
Obtain the maximum likelihood estimate of the SFS
misc/realSFS outFold.saf.idx -P 24 > outFold.sfs
Calculate the thetas (remember to fold)
./angsd -bam bam.filelist -out outFold -doThetas 1 -doSaf 1 -pest outFold.sfs -anc hg19.fa -GL 1 -fold 1
thetaStat do_stat outFold.thetas.idx -nChr 10
Retrieved from "http://www.popgen.dk/angsd/index.php?title=Thetas,Tajima,Neutr ality_tests&oldid=2940"
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
* This page was last modified on 29 May 2017, at 21:53.