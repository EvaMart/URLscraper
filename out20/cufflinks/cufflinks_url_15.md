<-- http://cole-trapnell-lab.github.io/cufflinks/releases/v1.3.0/-->

* How it works
## Transcriptome assembly and differential expression analysis for RNA-Seq.
# Cufflinks 1.3.0 released
__ January 02, 2012 __ January 02, 2012 __ Permalink __ Like __ Tweet __ +1
This release improves the accuracy of Cuffdiff’s isoform switching tests and fixes several bugs:
* Cuffdiff find genes that are differentially spliced or switch promoters between conditions using the Jensen-Shannon distance metric. Previous versions of Cuffdiff tested for the signficance of observed shifts in relative isoform abundance using an analytic approximation of the variance of this metric for each gene. However, when few replicates are available or sequencing is shallow, this approximation can be poor. This release improves Cuffdiff’s accuracy with a computational-derived estimate of the variance of the Jensen-Shannon metric by sampling in each gene. This improvement substantially reduces the false positive rate of Cuffdiff’s tests in `splicing.diff`, `promoters.diff`, and `cds.diff`. Tests for changes in global expression are not affected.
* A bug in Cuffmerge that caused a crash with a warning about improper sorting of SAM files has been corrected.
* A bug that caused Cuffmerge to drop some reference transcripts from the output has been fixed.
* A few minor issues with Cufflinks’ pre-assembly alignment filters have been fixed.
Previous article Next article
© 2017 Cole Trapnell. Powered by Jekyll using the So Simple Theme.
window.jQuery || document.write('<script src="http://cole-trapnell- lab.github.io/cufflinks/assets/js/vendor/jquery-1.9.1.min.js"><\/script>') var _gaq = _gaq || []; var pluginUrl = '//www.google- analytics.com/plugins/ga/inpage_linkid.js'; _gaq.push(['_require', 'inpage_linkid', pluginUrl]); _gaq.push(['_setAccount', 'UA-6101038-2']); _gaq.push(['_trackPageview']); (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })();