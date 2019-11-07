<-- https://github.com/rmtheis/mummergpu/tree/master/mummergpu-2.0-->

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
* Watch  2 
* Star  7 
* Fork  1 
Code Issues 1 Pull requests 0 Projects 0 Security  Insights
Create new file  Find file  History
Cannot retrieve the latest commit at this time.
Type Name Latest commit message Commit time
Failed to load latest commit information.
Michael Schatz, Cole Trapnel, Art Delcher, & Amitabh Varshney
MUMmerGPU is a high-throughput DNA exact sequence alignment program that
runs on nVidia G80-class GPUs. It aligns sequences in parallel on the video
card to achieve a more than 3-fold speedup over the widely used serial CPU
program MUMmer. It is supports many of the same options as MUMmer, and in
many cases, can be used as a drop in replacement.
MUMmerGPU uses the "Compute Unified Device Architecture" (CUDA) Software
development kit to program the graphics cards. If you do not have a nVidia
G80, you can still use MUMmerGPU using the G80 emulator available in CUDA.
The emulated version with run much slower than the native version, and
potentially slower than the CPU version of MUMmer.
MUMmerGPU 2.0 was described in:
Optimizing data intensive GPGPU computations for DNA sequence alignment.
Trapnell, C, Schatz, MC (2009) Parallel Computing 35(8-9):429-440.
MUMmerGPU 1.0 was described in:
High-throughput sequence alignment using Graphics Processing Units.
Schatz, MC, Trapnell, C, Delcher, AL, Varshney, A. (2007) BMC Bioinformatics 8:474.
. Build & Usage Instructions
Build & Usage Instructions
1) Download and install the CUDA Toolkit 2.3 and display driver from: 
2) Edit the CUDA_INSTALL_PATH in the src/Makefile to point to the top level
directory where you installed the CUDA Toolkit.
3) Run 'make' in the src directory, which will compile the program to run on
4) Usage: mummergpu [options] reference.fa query.fa
reference.fa must be a single sequence in fasta format
query.fa is a multi-fasta file containing your sequences the more
sequences you provide, the faster MUMmerGPU will execute.
See mummergpu -h for an explanation of the options, many of the options are
the same as those available in MUMmer.
See: http://mummer.sourceforge.net/manual/#mummer for more information
Q: I have a G70 or other older nVidia graphics card. Can I run MUMmerGPU on it?
A: No, MUMmerGPU requires a G80 or later video card. You can run MUMmerGPU
with the G80 emulator, but the alignments will be computed much slower than
if you had a G80.
Q: How does MUMmerGPU handle the MUMmer uniqueness options: -mum, -mumcand,
-mumreference, and -maxmatch?  
A: MUMmerGPU does not filter matches by uniques and always computes all
maximal matches regardless of their uniqueness (-maxmatch). The filtering
options provided by MUMmer (-mum, -mumcand, & -mumreference) are heuristics to
speed up the alignment process. This is not necessary with the very efficient
MUMmerGPU. If you want to filter your alignments to report only the most
biologically significant, you should use 'delta-filter' instead, which uses a
more sophisticated algorithm for finding the best set of alignments.
See the MUMmer manual for more information: 
Q: How does MUMmerGPU handle ambiguous bases?
A: MUMmerGPU only supports DNA characters (ACGT). Non DNA characters in the
reference are converted arbitrarily to a DNA character (A). Non-DNA characters
in the query set are converted to 'x' to guarantee a mis-match.
Q: How can I get help with MUMmerGPU?
A: Subscribe and post to the mailing list at: 
Q. How does the output compare to (regular cpu-version) mummer?
A: The alignments should be identical when run mummer is run in a compatible
mode. There should only be slight differences in the formatting, such as the
amount of white space, or the order of alignments.
For example, the exact same 2,537,145 alignments are computed using mummer
and mummergpu for 10,000 25bp reads:
$ python genreads.py B.anthracis.10k.fa 25 10000 > 10kreads.seq
$ mummer -maxmatch -l 5 B.anthracis.10k.fa 10kreads.seq > cpu
$ ../bin/release/mummergpu -l 5 B.anthracis.10k.fa 10kreads.seq > gpu
$ diff -w -I'>' cpu gpu
This work was supported in part by National Institutes of Health grants
R01-LM006845 and R01-LM007938, and National Science Foundation CISE RI grant
* © 2019 GitHub, Inc.
You can’t perform that action at this time.
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session.