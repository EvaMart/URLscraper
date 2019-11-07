<-- http://cole-trapnell-lab.github.io/cufflinks/tools/-->

* How it works
## Transcriptome assembly and differential expression analysis for RNA-Seq.
# Bowtie: ultrafast short read alignment
# Bowtie: ultrafast short read alignment
Bowtie is an ultrafast and memory-efficient tool for aligning sequencing reads to long reference sequences. It is particularly good at aligning reads of about 50 up to 100s or 1,000s of characters, and particularly good at aligning to relatively long (e.g. mammalian) genomes. Bowtie 2 indexes the genome with an FM Index to keep its memory footprint small: for the human genome, its memory footprint is typically around 3.2 GB. Bowtie 2 supports gapped, local, and paired-end alignment modes.
Bowtie is provided under the OSI-approved Artistic License 2.0.
# TopHat: alignment of short RNA-Seq reads
TopHat is a fast splice junction mapper for RNA-Seq reads. It aligns RNA-Seq reads to mammalian-sized genomes using the ultra high-throughput short read aligner Bowtie, and then analyzes the mapping results to identify splice junctions between exons.
TopHat is provided under the OSI-approved Artistic License 2.0.
# CummeRbund: visualization of RNA-Seq differential analysis
CummeRbund is an R package that is designed to aid and simplify the task of analyzing Cufflinks RNA-Seq output.
CummeRbund is provided under the OSI-approved Artistic License 2.0.
# Monocle: Differential expression for single-cell RNA-Seq and qPCR.
Monocle is a toolkit for analyzing single-cell gene expression experiments. Monocle was designed for RNA-Seq, but can also work with single cell qPCR. It performs differential expression analysis, and can find genes that differ between cell types or between cell states. When used to study an ongoing biological process such as cell differentiation, Monocle learns that process and places cells in order according to their progress through it. Monocle finds genes that are dynamically regulated during that process.
Monocle is provided under the OSI-approved Artistic License (version 2.0)
© 2017 Cole Trapnell. Powered by Jekyll using the So Simple Theme.
window.jQuery || document.write('<script src="http://cole-trapnell- lab.github.io/cufflinks/assets/js/vendor/jquery-1.9.1.min.js"><\/script>') var _gaq = _gaq || []; var pluginUrl = '//www.google- analytics.com/plugins/ga/inpage_linkid.js'; _gaq.push(['_require', 'inpage_linkid', pluginUrl]); _gaq.push(['_setAccount', 'UA-6101038-2']); _gaq.push(['_trackPageview']); (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })();