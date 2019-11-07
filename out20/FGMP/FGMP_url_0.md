<-- http://github.com/stajichlab/FGMP-->

* Why GitHub? 
* Customer stories →
* Explore GitHub →
#### Learn & contribute
* Open source guides
#### Connect with others
* In this repository  All GitHub  ↵
* No suggested jump to results
* In this repository  All GitHub  ↵
* In this repository  All GitHub  ↵
Sign in  Sign up
* Watch  5 
* Star  7 
* Fork  4 
Code Issues 3 Pull requests 0 Projects 0 Wiki  Security  Insights
### Join GitHub today
GitHub is home to over 40 million developers working together to host and review code, manage projects, and build software together.
Fungal Genome Mapping Pipeline
* 139  commits 
* 3  branches 
* 6  releases 
* Fetching contributors 
_Branch:_ master New pull request
####  Clone with HTTPS
Use Git or checkout with SVN using the web URL.
Open in Desktop Download ZIP
Want to be notified of new releases in stajichlab/FGMP?
Sign in Sign up
#### Launching GitHub Desktop...
If nothing happens, download GitHub Desktop and try again.
#### Launching GitHub Desktop...
If nothing happens, download GitHub Desktop and try again.
If nothing happens, download Xcode and try again.
#### Launching Visual Studio...
If nothing happens, download the GitHub extension for Visual Studio and try again.
Latest commit 20e8dcb  Jun 9, 2019
Type Name Latest commit message Commit time
Failed to load latest commit information.
use FindBin to find the library file
remove .DS_Store and add to ignore file
update to MIT license
rename Fgmp to FGMP for simplicity
Fungal Genome Mapping Pipeline
*     1. Description
*     2. Installation
*     3. File Listing
*     4. Running FGMP
*     5. Testing FGMP
*     6. Authors and help
*     7. Citing FGMP
FGMP (Fungal Genome Mapping Project) is a bioinformatic pipeline designed to provide in an unbiased manner an estimation of genome completeness of a fungal genome assembly. The strategy is based on the screening of the genome using a set of highly diversified fungal proteins. This approach is likely to capture homologs from any fungal genome. FGMP is based on 593 protein markers and 31 highly conserved fungal genomic segments .
A local version of FGMP can be installed on UNIX platforms. The tool requires the pre-installation of Perl, NCBI BLAST, HMMER, EXONERATE and AUGUSTUS.
The pipeline uses information from the selected genes of 25 fungi by first using TBLASTn to identify candidate regions in a new genome. Gene structures are delineated using EXONERATE and AUGUSTUS and validated using HMMER. At the end of the process FGMP produces a set of best predictions and an estimation of the genome completeness.
FGMP uses NHMMER to screen the genome with a set of highly conserved DNA segments. When raw reads are provided in fasta format, FGMP searches protein markers directly in the unassembled reads. Reads are randomly sampled using reservoir sampling algorithm and screened using BLASTx.
FGMP source code and documentation are available under the GNU GENERAL PUBLIC LICENSE.
* System requirements 
* Perl 5 (tested with the version 20)
* HMMER v3.0 http://hmmer.org/
* NCBI BLASTALL (tested using version 2.2.31+) ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.31/
* Exonerate (tested using version 2.2.0) https://www.ebi.ac.uk/about/vertebrate-genomics/software/exonerate
* Augustus (tested using version 3.0.3) http://augustus.gobics.de/
These software can be installed via bioconda
conda install -c bioconda perl-bioperl
Note: Augustus version 3.3 might cause compiling issues on Mac OS (but not on linux). We recommend using the version 3.2.3 for Mac.
echo "Installation via github"
* Description The FGMP distribution includes the following files and directories:
* data/ Proteins, profiles and cutoff
* lib/ Perl modules
* sample/ Sample dna
* sample_output/ Sample output
* src/ Source code of FGMP.
* utils/ FGMP scripts
To use FGMP with default settings run:
fgmp.pl -g < genomic_fasta_file > fgmp_report.out
You can specify the number of cpus to use using the -T option, which will be passed to all subsequent softwares.
-p, --protein		fasta file of the protein sequence
--fuces_hmm		Directory that contains hmm files
--hmm_profiles		Directory that contains hmm files
launch the following command and compare the output with the sample files in 'sample_output'
./fgmp.pl -g sample_test.dna -T 3 --tag OMA
* Output FGMP will create some intermediate files during the annotation.
final files: \- sample.dna.bestPreds.fas: predicted best predictions (fasta format)
- sample.dna.unfiltered.renamed.hmmsearch.full_report: detailed analysis of best predictions
intermediate files: \- sample.dna.tblastn: tblastn output
- sample.dna.candidates.fa: Genomic regions extracted based on Tblastn matches coordinates (fasta format)
- sample.dna.candidates.fa.p2g: Alignment of 593 proteins to candidates.fa
- sample.dna.candidates.fa.p2g.aa: exonerate alignment matches
- sample.dna.candidates.fa.p2g.aa.proteins: translated CDS (amino acids)
- sample.dna.trainingSet: augustus training set
- sample.dna.trainingSet.gb: augustus training set (genbank format)
- sample.dna.unfiltered: unfiltered predicted peptides
- sample.dna.unfiltered.renamed : renamed predicted peptides to avoid name conflits
- sample.dna.unfiltered.renamed.hmmsearch : Hmmsearch output
* Search in reads (experimental)
./fgmp.pl -g sample_test.dna -T $CPU -r sd_merge.fq.fasta
Cisse, O. H. and Stajich, J.E. (2019). FGMP: assessing fungal genome completeness. BMC Bioinformatics 20(1): 184. https://rdcu.be/bFV81
* © 2019 GitHub, Inc.
You can’t perform that action at this time.
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session.