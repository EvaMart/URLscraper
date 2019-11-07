<-- http://cole-trapnell-lab.github.io/cufflinks/releases/v2.0.2/-->

* How it works
## Transcriptome assembly and differential expression analysis for RNA-Seq.
# Cufflinks 2.0.2 released
__ July 08, 2012 __ July 08, 2012 __ Permalink __ Like __ Tweet __ +1
This release fixes several bugs:
* Some users were experiencing a crash on exit in Cufflinks when run with bias correction. The source of the crash has been fixed.
* A few minor fixes in the estimation routines for cross-replicate variability.
* Providing the same BAM file multiple times was producing inconsistent expression values. This has been corrected.
Previous article Next article
© 2017 Cole Trapnell. Powered by Jekyll using the So Simple Theme.
window.jQuery || document.write('<script src="http://cole-trapnell- lab.github.io/cufflinks/assets/js/vendor/jquery-1.9.1.min.js"><\/script>') var _gaq = _gaq || []; var pluginUrl = '//www.google- analytics.com/plugins/ga/inpage_linkid.js'; _gaq.push(['_require', 'inpage_linkid', pluginUrl]); _gaq.push(['_setAccount', 'UA-6101038-2']); _gaq.push(['_trackPageview']); (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })();