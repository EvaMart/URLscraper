<-- http://alan.cs.gsu.edu/NGS/?q=content/isoem-->

* Funded Research Projects
* Request new password
You are hereSoftware / IsoEM 1.1.5: Inferring isoform and gene expression levels from RNA-Seq data
# IsoEM 1.1.5: Inferring isoform and gene expression levels from RNA-Seq data
Download **IsoEM 1.1.5** from github: https://github.com/mandricigor/isoem- bootstrap.
##  Installation: 
1. Create a isoem directory and download the compressed ISOEM-1.1.5 
from the github repository: https://github.com/mandricigor/isoem-bootstrap
2. Edit isoEMDir location in files under bin according to 
3. Uncompress IsoEM-1.1.5.zip into the directory.
4. Optional] On windows you might want to add the IsoEM 
installation directory to the path, such that you can invoke 
isoem from any location. On unix you can obtain a similar
5. If you want to rebuild isoem, run the unix script "build" 
provided in the compressed file.
##  Testing your installation:
To test the installation you can download the sample dataset from 
and unzip it in the installation directory of IsoEm. First see 
file for more details on what the archive provides.
IsoEM takes as input a set of known isoforms in GTF format, and a 
file with aligned reads in SAM format. The aligned reads MUST be 
sorted by read name. If not sure, run this command to sort the 
sort -k 1,1 aligned_reads.sam > aligned_reads_sorted.sam
The output consists of two files: one for isoform frequencies and one 
for gene frequencies. Each line in these files is a pair of isoform/gene 
name and isoform/gene FPKM (Fragments Per Kilobase per Million reads) 
representing the frequencies inferred from the data. The output file 
names are obtained from the sam file name by replacing the .sam extension 
with .iso_estimates and .gene_estimates respectively.They can also be set 
using the -o option.
You can run IsoEm from the command line as follows:
isoem [global options]* [library options]* <aligned_reads.sam>
Mandatory global options: 
-G, --GTF <GTF file> Known genes and isoforms in GTF format
Mandatory library options: either -a or both -m and -d must be present: 
-m, --fragment-mean <Double> Fragment length mean 
-d, --fragment-std-dev <Double> Fragment length standard deviation 
-a, --auto-fragment-distrib Automatically detect fragment length 
distribution from uniquely mapping 
paired reads (DOES NOT WORK FOR 
Optional global options: 
-c, --gene-clusters <Cluster file> Override isoform to gene mapping 
defined in the GTF file with a 
mapping taken from the given file. 
The format of each line in the file 
is "isoform gene" 
-g <genome fasta file> Genome reference sequence (needed by 
some library options) 
-b Perform hexamer bias correction  
-h, --help Show help 
-r <Repeats GTF> Drop alignments falling within 
Optional library options: 
-s, --directed Library obtained by directed RNA-Seq  
(the strand of each read is 
deterministically chosen: for single 
reads, the read always comes from 
the coding strand; for paired reads, 
the first read always comes from the 
coding strand, the second from the 
\--mate-pairs Paired reads come from the same strand 
(as opposed to the default behavior 
where the two reads in a pair are 
assumed to come from opposite 
\--max-mismatches <Integer> Maximum number of mismatched allowed 
for a read. This requires the genome 
sequence to be specified (see -g). 
Default: no limit 
-q, --quality-scores Weigh the reads based on their quality 
scores. This requires the genome 
sequence to be specified (see -g). 
\--repeat-threshold <nbases> Drop all reads that have more than 
this many bases inside annotated 
repeats. Default: 20 
\--polyA <nbases> Reads have been generated from mRNAs 
with polyA tails of approximately 
the given number of bases 
-o <file prefix> Output files prefix. It can include path. 
Default: same as sam file name
##  Read Alignment: 
To align the reads you can either use spliced alignment directly 
on the genome (for example using tophat), or you can align on the 
library of known isoforms. We recommend the second option. If you 
want to do this, we provide a full step by step guide at: 
Visualizing read coverage: 
If you want to visualize the isoforms and their coverage by reads, you can use the isoviz 
command. It produces a bedGraph file and a GTF with fpkm values file which can be uploaded 
to the UCSC browser. The name of the output files are automaticaly generated from the input 
file name and ends in _iso_read_coverage.bed and _isoforms_w_fpkm.gtf. They can also be set 
using the -o option.
The options are almost the same as for isoem except that isoviz also needs the isoform frequency 
file (e.g. obtained by running isoem). The frequency file is specified using the -f option. The 
full command line synopsis is given below:
isoviz [global options]* [library options]* <aligned_reads.sam>
Mandatory global options: 
-G, --GTF <GTF file> Known genes and isoforms in GTF format 
-f <frequency file> Isoform FPKMs computed by IsoEM
Mandatory library options: 
-m, --fragment-mean <Double> Fragment length mean 
-d, --fragment-std-dev <Double> Fragment length standard deviation
Optional global options: 
-c, --gene-clusters <Cluster file> Override isoform to gene mapping 
defined in the GTF file with a 
mapping taken from the given file. 
The format of each line in the file 
is "isoform gene" 
-g <genome fasta file> Genome reference sequence (needed by 
some library options) 
-b Perform hexamer bias correction 
-h, --help Show help
Optional library options: 
-s, --directed Dataset obtained by directed RNA-Seq 
(the strand of each read is 
deterministically chosen: for single 
reads, the read always comes from 
the coding strand; for paired reads, 
the first read always comes from the 
coding strand, the second from the 
\--mate-pairs Paired reads come from the same strand 
(as opposed to the default behavior 
where the two reads in a pair are 
assumed to come from opposite 
\--max-mismatches <Integer> Maximum number of mismatched allowed 
for a read. This requires the genome 
sequence to be specified (see -g). 
Default: no limit. 
-q, --quality-scores Weigh the reads based on their quality 
scores. This requires the genome 
sequence to be specified (see -g). 
-o <file prefix> Output files prefix. It can include path. 
Default: same as sam file name 
-O <dir prefix> Output directory prefix 
-B <nr bootstraps> Number of bootstraps to perform 
-C <confidence intervals> Confidence Intervals (CI). 
Default 95 % (200 bootstrap iterations).
\--endseq Reads have been generated using an end-sequencing protocol
##  Source Code: 
The source code can be found in the src directory under the 
###  Revision history 
*     Version 1.1.5 (1/20/16)  - added TPM and ECPM estimates for genes and isoforms
- added option to compute confidence intervals (bootstrapping)
- added option for reading alignments from standard input
*     Version 1.1.4 (12/31/15) - added `endseq` option
*     Version 1.1.3 (10/11/15) - bug fix in handling CIGAR with indels in convert-iso-to-genome-coords
- bug fix related to hisat/hisat2 alignments
*     Version 1.1.1 (11/5/12)  - bug fix related to clipped read alignments (CIGAR with S field)
*     Version 1.1.0 (4/24/12)  - added support for alignments with insertions and deletions
*     Version 1.0.6 (8/12/11)  - extract-isoform-sequences-from-genome (see 
generates transcripts in a randomized order
- isoviz generates a gtf with fpkm values
- added output file name option
*     Version 1.0.5 (5/08/11)  - bugfix related to paired read data
*     Version 1.0.4 (2/22/11)  - added polyATail option
- further memory and speed improvements
*     Version 1.0.3 (8/30/10)  - correct for annotated repeats
*     Version 1.0.2 (8/05/10)  - improved memory requirements for storing genome sequence
- added hexamer bias correction option
- added isoviz visualization tool
*     Version 1.0.1 (6/25/10)  - added support for mate pairs
- added support for max number of mismatches
*     Version 1.0.0 (6/16/10)  - first public release
##  **Contact** 
For questions or suggestions regarding IsoEM you can contact:
*     Igor Mandric (imandric1@student.gsu.edu)
*     Sahar Al Seesi (sahar@engr.uconn.edu)
*     Ion Mandoiu (ion@engr.uconn.edu)
*     Marius Nicolae (man09004@engr.uconn.edu)
*     Serghei Mangul (serghei@cs.gsu.edu)
*     Alex Zelikovsky (alexz@cs.gsu.edu)
Georgia State University NGS Research Group