<-- http://alan.cs.gsu.edu/NGS/?q=content/kgem-->

* Funded Research Projects
* Request new password
You are hereSoftware / kGEM: k-Genotype Expectation Maximization algorithm for Reconstructing a Viral population from Single-Amplicon reads.
# kGEM: k-Genotype Expectation Maximization algorithm for Reconstructing a Viral population from Single-Amplicon reads.
kGEM tool finds haplotypes for Single-amplicon sequencing data. This tool requires aligned reads in special internal format and auxiliary program B2W could help to convert reads in this format either from fasta (unaligned) format or from SAM (pairwise alignment) format.
To run both kGEM Java Runtime Environment is necessary (http://java.com/en/download/index.jsp)
After reads_aligned.fas file obtained run KGEM using following comand:
` java -jar <path_to_KGEM-v.jar>  <path_to_reads>/aligned_reads.fas <k> -o <output_directory>`
where <k> is a number of initial haplotypes for estimation (this number should be higher than actual number of haplotypes in population or for clustering more <k> could be reduced). This parameter is positive integer number
aligned_reads.fas reads obtained on previous step and <output_directory> (default: current) will contains two files after prograram will be finished. The file haplotypes.fa will contain haplotypes in fasta format and their frequencies in description (example:
means that this haplotype has frequency 38%)
and second file will contain these haplotypes but instead of frequencies in description program just copy them proportionally to the frequencies. This file will contain the same number of entries as initial file with reads.
* **Note: **result files reads.fa and haplotypes.fa may contain dashes '-' which were used for alignment, hence to get pure sequences file should be cleaned via any txt editor with command Repalce all '-' '' or in linux machines with command:
sed -e 's/\-//g' haplotypes.fa > haplotypes_cleaned.fa
Assuming ERIF.jar KGEM.jar sample_data.fa and reference.fa are in current directory. Then first run following command:
`java -jar ERIF.jar -g reference.fa -i sample_data.fa -o test_`
**Alternatively!** you could use SAM file instead of fasta. (reads.sam)** **
`java -jar ERIF.jar -g reference.fa -sam reads.sam -o test_`
After that in this folder will appear output file **test_reads.sam_ext.txt**
`java -jar KGEM-0.3.1.jar test_reads.sam_ext.txt 100 `
After completion of kGEM the two files will appear in current directory: haplotypes.fa and reads.fa
For linux users to clean dashes from output following command is available:
` sed -e 's/\\-//g' haplotypes.fa > haplotypes_cleaned.fa`
And as a result haplotypes with their frequencies will be stored in haplotypes_cleaned.fa file.
##  **For developers: **
source code available on git repository KGEM_on_github.
Programming Language Scala, for compilation Maven is required.
1. Download and install Maven 2 or 3
2. Download sources from github repository
3. From the folder where sources is placed run: 
**Note: **you could download and build jar from maven repository directly:
ERIF currently not available from maven directly!
Also for developers using Maven kgem repository available, to be able to use it inside Maven project following configuration is necessary:
In the `pom.xml `add to tag repositories:
and to tag dependencies:
Georgia State University NGS Research Group