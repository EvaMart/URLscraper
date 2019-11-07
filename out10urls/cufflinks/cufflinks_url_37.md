<-- http://cole-trapnell-lab.github.io/cufflinks/releases/v0.9.1/-->

* How it works
## Transcriptome assembly and differential expression analysis for RNA-Seq.
# Cufflinks 0.9.1 released
__ October 03, 2010 __ October 03, 2010 __ Permalink __ Like __ Tweet __ +1
This release includes two bug fixes and some enhancements for strand-specific RNA-Seq libraries:
* SAM files without headers, such as those produced by TopHat 1.0.14 and earlier, were being erroneously reported as unsorted during GTF-based quantification, causing Cufflinks and Cuffdiff to exit. This has been fixed, so that SAM files are now correctly handled, restoring compatibility with output from TopHat 1.0.14 and earlier.
* Cufflinks and Cuffdiff were sometimes producing different FPKM values for minor isoforms when run on the same sample. They are now consistent, and should agree on isoform abundance calls.
* Strand-specific, single end libraries are now supported. Some library type names have changed to reflect the expanded list of supported protocols.
Previous article Next article
© 2017 Cole Trapnell. Powered by Jekyll using the So Simple Theme.
window.jQuery || document.write('<script src="http://cole-trapnell- lab.github.io/cufflinks/assets/js/vendor/jquery-1.9.1.min.js"><\/script>') var _gaq = _gaq || []; var pluginUrl = '//www.google- analytics.com/plugins/ga/inpage_linkid.js'; _gaq.push(['_require', 'inpage_linkid', pluginUrl]); _gaq.push(['_setAccount', 'UA-6101038-2']); _gaq.push(['_trackPageview']); (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })();