<-- https://github.com/rmtheis/mummergpu/tree/master/mummergpu-2.0/data-->

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
This directory has sample data to use with MUMmerGPU.
- Obtaining data used in the paper
Run MUMmerGPU as follows:
$ mummergpu -l 2 shortref.fa shortqry.fa > alignments.mummergpu
This will produce exactly the same results as MUMmer
$ mummer -l 2 -maxmatch shortref.fa shortqry.fa > alignment.mummer
1         1         2
5         1         2
This means that sequences 0 and 2 in shortqry.fa had no 2bp or longer exact
alignments to shortref.fa. Read 1 has 2 alignments: one starting at base 1
in shortref.fa and 1 starting at base 5 in shortref.fa. Both alignments began
at base 1 of read 1 and lasted for 2bp. 
For example, the exact same 2,537,145 alignments are computed using mummer
and mummergpu for 10,000 25bp reads:
$ python genreads.py B.anthracis.10k.fa 25 10000 > 10kreads.seq
$ mummer -maxmatch -l 5 B.anthracis.10k.fa 10kreads.seq > cpu
$ ../bin/release/mummergpu -l 5 B.anthracis.10k.fa 10kreads.seq > gpu
$ diff -w -I'>' cpu gpu
For more information, see the website: http://mummergpu.sourceforge.net
Obtaining data used in the paper
Genome: GenBank ID: NC_003997.3
Reads: Simulated by extracting various length reads from the genome using
genreads.py NC_003997.fna 800  312500 > NC_003997_q800bp.fna
genreads.py NC_003997.fna 400  675000 > NC_003997_q400bp.fna
genreads.py NC_003997.fna 200 1250000 > NC_003997_q200bp.fna
genreads.py NC_003997.fna 100 2500000 > NC_003997_q100bp.fna
genreads.py NC_003997.fna 50  5000000 > NC_003997_q50bp.fna
genreads.py NC_003997.fna 25 10000000 > NC_003997_q25bp.fna
10 copies of the reads were concatented to simulate a full run of a Solexa
Genome: GenBank ID: NC_003210.1
Reads: TI numbers: 1405533909-1405634798, 1406562010-1406781638, 
Download from the trace archive:
$ for i in `seq 0 165`; \
do echo $i; 
query_tracedb "query page_size 40000 page_number $i binary \
SPECIES_CODE = 'LISTERIA MONOCYTOGENES'" \
(echo -n "retrieve_gz fasta 0b"; cat page$i.bin) | \
query_tracedb > data$i.fa.gz; \
$ zcat *.fa.gz > allreads.fa
Reads: TI Numbers: 36038503-36832860, 38251430-38350285, 38350351-38452820,
40417388-40467055, 43189877-43242567, 58160800-58654425, 59144485-59161076,
59161078-59166329, 59166331-59190841, 59190843-59199663, 59199665-59201364,
59201366-59206805, 59206807-59208205, 59208207-59218643, 59218645-59222212,
59222214-59244348, 59244350-59268819, 59268821-59276022, 59276024-59284748,
59284750-59298383, 59298385-59303938, 59303940-59309481, 59309483-59333492,
59333494-59344446, 62886552-62887633, 62887635-62888977, 62888979-62918435,
62918437-62953501, 62953503-62994109, 62994111-63006546, 65922015-66002808,
66002810-66021716, 66581062-66700697, 67687433-67746120, 77950765-77962883,
77962885-78029725, 81821261-81821261, 88113135-88133134, 88377800-88397799,
88917800-88937799, 89214110-89230859, 94491265-94491329, 111970178-111979689,
$ for i in `seq 0 58`; \
do echo $i; 
query_tracedb "query page_size 40000 page_number $i binary \
SPECIES_CODE = 'Caenorhabditis briggsae'" \
(echo -n "retrieve_gz fasta 0b"; cat page$i.bin) | \
query_tracedb > data$i.fa.gz; \
$ zcat *.fa.gz > allreads.fa
* © 2019 GitHub, Inc.
You can’t perform that action at this time.
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session.