<-- http://cole-trapnell-lab.github.io/cufflinks/releases/v0.8.2/-->

* How it works
## Transcriptome assembly and differential expression analysis for RNA-Seq.
# Cufflinks 0.8.2 released
__ March 26, 2010 __ March 26, 2010 __ Permalink __ Like __ Tweet __ +1
Numerous bug fixes and significant performance improvements in Cufflinks and Cuffdiff. Note that some the formats of some files have changed. Other changes:
* Expression values were not being reported for a small number of genes when using certain annotation files.
* Fixed a divide-by-zero error in Cuffdiff
* Various GTF parser fixes.
* .expr files produced by Cufflinks now contain FPKM confidence interval columns
* Isoform filtering was being innappropriately applied when working with annotation in Cufflinks (via –GTF)
* The .tmap files reported by Cuffdiff contained zero in FPKM field.
* New command line options –num-importance-samples and –max-mle-iterations allow advanced users to influence of the transcript abundance estimation.
Previous article Next article
© 2017 Cole Trapnell. Powered by Jekyll using the So Simple Theme.
window.jQuery || document.write('<script src="http://cole-trapnell- lab.github.io/cufflinks/assets/js/vendor/jquery-1.9.1.min.js"><\/script>') var _gaq = _gaq || []; var pluginUrl = '//www.google- analytics.com/plugins/ga/inpage_linkid.js'; _gaq.push(['_require', 'inpage_linkid', pluginUrl]); _gaq.push(['_setAccount', 'UA-6101038-2']); _gaq.push(['_trackPageview']); (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })();