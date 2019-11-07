<-- http://alan.cs.gsu.edu/NGS/?q=content/2snv-->

* Funded Research Projects
* Request new password
You are hereSoftware / 2SNV Quasispecies reconstruction from long reads
# 2SNV Quasispecies reconstruction from long reads
Supplementary materials are available here
To run the tool Java Runtime Environment is necessary (http://java.com/en/download/index.jsp)
Software requires aligned reads in MSA format (fasta reads padded to the same length of all entries)
It is possible to convert pairwise aligned SAM(BAM) file to MSA with the help of program b2w (part of ShoRAH assembler)
Recommended aligner for long SMRT reads is BWA
`bwa mem -k17 -W40 -r10 -A1 -B1 -O1 -E1 -L0 input.fasta > output.sam `
To compress sort and index SAM to BAM(BAI) install samtools
`samtools view -b reads.sam > reads.bam 
samtools sort reads.bam -o reads.sorted -O bam 
To run b2w it is not necessary to install whole ShoRAH software, as an alternative one can download C code from github b2w it is not necessary to install whole ShoRAH software, as an alternative one can download C code from github b2w.c and compile it with gcc or any other compartible C-compiler
`b2w -w 2300 -i 0 -x 100000 -o aligned.reads.fas reads.sorted.bam ref.fasta ref_name:0:2300`
To run 2snv use jar file
`java -jar 2snv-1.0.jar aligned.reads.fas 1000 -t 30 -o haplotypes.fa`
2SNV is available at
For developers source code and instructions
Clones in fasta format available clones.fa
Raw sequencing data have been submitted to the NIH Short Read Archive (SRA) under accession number: BioProject PRJNA284802
Georgia State University NGS Research Group