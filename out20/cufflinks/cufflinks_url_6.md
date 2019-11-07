<-- http://cole-trapnell-lab.github.io/cufflinks/releases/v2.0.1/-->

* How it works
## Transcriptome assembly and differential expression analysis for RNA-Seq.
# Cufflinks 2.0.1 released
__ June 15, 2012 __ June 15, 2012 __ Permalink __ Like __ Tweet __ +1
This release addresses several bugs, most of which were introduced as part of the 2.0.0 release:
* Some users were experiencing a problem with the Linux pre-compiled binary packages where Cuffdiff was reporting many genes and transcripts as having expression levels of zero or “nan” or “inf”. This was determined to be caused by a recent change in the binary packaging process we use to distribute pre-compiled binaries.
* Multi-read correction in Cuffdiff 2.0 was not always being applied when the user specified `-u/–multi-read-correct`.
* Some rarely encountered GTF parsing issues have been corrected.
* Effective length correction can be disabled in Cufflinks and Cuffdiff with the new `–no-effective-length-correction` option.
Previous article Next article
© 2017 Cole Trapnell. Powered by Jekyll using the So Simple Theme.
window.jQuery || document.write('<script src="http://cole-trapnell- lab.github.io/cufflinks/assets/js/vendor/jquery-1.9.1.min.js"><\/script>') var _gaq = _gaq || []; var pluginUrl = '//www.google- analytics.com/plugins/ga/inpage_linkid.js'; _gaq.push(['_require', 'inpage_linkid', pluginUrl]); _gaq.push(['_setAccount', 'UA-6101038-2']); _gaq.push(['_trackPageview']); (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })();