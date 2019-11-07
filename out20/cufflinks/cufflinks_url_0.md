<-- http://cole-trapnell-lab.github.io/cufflinks/releases/v1.0.1/-->

* How it works
## Transcriptome assembly and differential expression analysis for RNA-Seq.
# Cufflinks 1.0.1 released
__ May 06, 2011 __ May 06, 2011 __ Permalink __ Like __ Tweet __ +1
This fix release corrects several issues introduced with 1.0.0:
* The binary packages for 1.0.0 failed to include gtf_to_sam and gffread, causing cuffmerge to fail.
* Cuffdiff’s `splicing.diff` was missing the `q_value` column header
* Several portability issues have been fixed (thanks to Nathan Weeks for the patches)
* Cuffmerge’s help message incorrectly listed several options.
Previous article Next article
© 2017 Cole Trapnell. Powered by Jekyll using the So Simple Theme.
window.jQuery || document.write('<script src="http://cole-trapnell- lab.github.io/cufflinks/assets/js/vendor/jquery-1.9.1.min.js"><\/script>') var _gaq = _gaq || []; var pluginUrl = '//www.google- analytics.com/plugins/ga/inpage_linkid.js'; _gaq.push(['_require', 'inpage_linkid', pluginUrl]); _gaq.push(['_setAccount', 'UA-6101038-2']); _gaq.push(['_trackPageview']); (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })();