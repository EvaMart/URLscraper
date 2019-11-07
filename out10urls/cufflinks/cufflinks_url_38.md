<-- http://cole-trapnell-lab.github.io/cufflinks/releases/v2.2.1/-->

* How it works
## Transcriptome assembly and differential expression analysis for RNA-Seq.
# Cufflinks 2.2.1 released
__ May 05, 2014 __ May 05, 2014 __ Permalink __ Like __ Tweet __ +1
This issue fixes several bugs:
* Cuffnorm was not sometimes permuting replicate numbering, leading to inconsistent expression calls between Cuffnorm and Cuffdiff.
* The contrast file parser had a problem that could crash Cuffdiff
* Several Cuffnorm output files had minor output formatting issues
Previous article Next article
© 2017 Cole Trapnell. Powered by Jekyll using the So Simple Theme.
window.jQuery || document.write('<script src="http://cole-trapnell- lab.github.io/cufflinks/assets/js/vendor/jquery-1.9.1.min.js"><\/script>') var _gaq = _gaq || []; var pluginUrl = '//www.google- analytics.com/plugins/ga/inpage_linkid.js'; _gaq.push(['_require', 'inpage_linkid', pluginUrl]); _gaq.push(['_setAccount', 'UA-6101038-2']); _gaq.push(['_trackPageview']); (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })();