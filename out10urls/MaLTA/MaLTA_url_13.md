<-- http://alan.cs.gsu.edu/NGS/?q=content/pyrosequencing-error-correction-algorithm-->

* Funded Research Projects
* Request new password
You are hereSoftware / Pyrosequencing error correction algorithm
# Pyrosequencing error correction algorithm
**11/28/2012 **The new version of KEC is available. The algorithm for error threshold finding based on fitting of Poisson distribution to k-counts distribution was added. Special thanks for helping to Bram Vrancken and Alex Artyomenko
**02/27/2013 **The new version of KEC is available. The user interface was updated and cross-paltform functionality was added. Special thanks to Alex Artyomenko
**04/12/2013** The new version of KEC is available. An option allowing to use Muscle instead of Clustal for additional correction procedure was added. Special thanks to Alex Artyomenko
KEC is distributed under the GNU General Public License (http://www.gnu.org/copyleft/gpl.html)
**Running instructions for KEC**
• Download the java archive KEC.jar from KEC
• Download the implementation of the adaptive mean shift based clustering algorithm from http://coewww.rutgers.edu/riul/research/code/AMS/fams_pc.zip Create the folder with the name “fams” at the same folder, as ErrorCorrection.jar. Put the executable file “fams.exe” to the folder “fams”
• Download ClustalW2 from http://ftp.ebi.ac.uk/pub/software/clustalw2/  Create a folder with the name “ClustalW2” at the same folder as ErrorCorrection.jar. Put the executable file with the name “clustalw2.exe” to the folder “ClustalW2”
Download Muscle from http://www.drive5.com/muscle/ Create a folder with the name "Muscle" at the same folder as ErrorCorrection.jar. Put the executable file with the name “muscle.exe” to the folder “Muscle”
• Download the archive lib.rar from http://alan.cs.gsu.edu/~skumsp/lib.rar and extract it at the same folder as ErrorCorrection.jar
java -jar ErrorCorrection.jar [-h] [-k k] [-i i] [-cl | -mus] [-l l] [-dg dg] [-dpp dpp] filename
* filename is the name of file containing reads to be corrected;
* k is the size of k-mers. Default: k=25
* i is the number of iterations of the algorithm. Default: i=3
* -cl Enable using of CLustalW for multiple and pairwise sequence alignment for additional correction procedure. Default: do not align
* -mus Enable using of Muscle for multiple and pairwise sequence alignment for additional correction procedure. Default: do not align
* l is responsible for an error threshold finding. If l = 0, then the algorithm based on fitting of Poisson distribution to k-counts distribution is used. If l > 0, then the region of l consecutive zeros in the k-counts distribution is used to find the error threshold. Default: l =0
* dg is the parameter for haplotypes postprocessing using multiple alignment (see parameter alpha, Algorithm 2, step 3)). Default: dg = 30
* dpp is the parameter for postprocessing of haplotypes using pairwise alignment of neigbor leaves of neighbor joining tree (see parameter alpha, Algorithm 2, step 4). Default: dpp = 30
* -h - help
java -jar ErrorCorrection.jar -k 25 -i 3 -cl -l 25 test.fas
java -jar ErrorCorrection.jar test.fas
java -jar ErrorCorrection.fas -mus -l 1 -dg 15 -dpp 15 test.fas
java -jar ErrorCorrection.jar -h
The output contains several files. The most important are:
1) filename_corrected.fas_corrected.fas – corrected reads
2) filename_corrected.fas_haplotypes.fas - haplotypes found after the first stage of the algorithm (without allignment stage)
_PostprocPair.fas - haplotypes found after the second stage of the algorithm using allignment (available only with -a)
Data sets used in the paper are available at
1) sequencing results (fasta files, sff files)
2) haplotypes found by KEC
3) HVR1 clones used to create data sets (original and reverse complemented sequences)
**Running instructions for ET**
** **Will be here soon
P. Skums, Z. Dimitrova, D. S. Campo, G. Vaughan, L. Rossi, J. C. Forbi, J. Yokosawa, A. Zelikovsky, Y. Khudyakov, “Efficient error correction for next- generation sequencing of viral amplicons,”_ __BMC Bioinformatics _13 (Suppl10): S6 2012**, publisher url**
Georgia State University NGS Research Group