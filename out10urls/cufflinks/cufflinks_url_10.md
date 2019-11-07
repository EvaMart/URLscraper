<-- http://cole-trapnell-lab.github.io/cufflinks/releases/v1.0.3/-->

* How it works
## Transcriptome assembly and differential expression analysis for RNA-Seq.
# Cufflinks 1.3.0 released
__ June 01, 2011 __ May 04, 2012 __ Permalink __ Like __ Tweet __ +1
This is a fix release to address several issues reported by our users:
* Several Cuffmerge bugs have been fixed. One of these caused Cuffmerge to fail with a message about chromosome sort ordering.
* A comment parsing issue in Cuffmerge has been fixed.
* GTF files emitted by Cuffcompare are now lexicographically sorted by chromosome.
* Gffread now has some transcript clustering and redundancy reduction features, similar to those found in Cuffcompare
* The header size limit in Cufflinks’ BAM parser used to have a 4 megabyte limit. This has been removed to allow Cufflinks to be used on assemblies with many contigs.
Previous article Next article
© 2017 Cole Trapnell. Powered by Jekyll using the So Simple Theme.
window.jQuery || document.write('<script src="http://cole-trapnell- lab.github.io/cufflinks/assets/js/vendor/jquery-1.9.1.min.js"><\/script>') var _gaq = _gaq || []; var pluginUrl = '//www.google- analytics.com/plugins/ga/inpage_linkid.js'; _gaq.push(['_require', 'inpage_linkid', pluginUrl]); _gaq.push(['_setAccount', 'UA-6101038-2']); _gaq.push(['_trackPageview']); (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })();