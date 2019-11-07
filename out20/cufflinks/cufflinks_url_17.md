<-- http://cole-trapnell-lab.github.io/cufflinks/releases/v0.8.0/-->

* How it works
## Transcriptome assembly and differential expression analysis for RNA-Seq.
# Cufflinks 0.8.1 released
__ February 05, 2010 __ February 05, 2010 __ Permalink __ Like __ Tweet __ +1
We are happy to announce a major update to Cufflinks that introduces some powerful new features and includes a number of performance improvement and bug fixes. Highlights include:
* Cufflinks now includes a new tool, “Cuffdiff”, which performs testing for differential expression, splicing, promoter use, and coding sequence output on two or more RNA-Seq samples. See the greatly expanded manual for details.
* Cuffcompare now reports a file containing the “union” of all transfrags in the files you give it as input, greatly simplifying downstream validatation of novel transcripts.
* Cufflinks’ assembler has been overhauled and optimized, resulting in a speedup of 4-5 times over version 0.7.0, and a greatly reduced memory footprint. Phasing of splicing events has also been improved.
Previous article Next article
© 2017 Cole Trapnell. Powered by Jekyll using the So Simple Theme.
window.jQuery || document.write('<script src="http://cole-trapnell- lab.github.io/cufflinks/assets/js/vendor/jquery-1.9.1.min.js"><\/script>') var _gaq = _gaq || []; var pluginUrl = '//www.google- analytics.com/plugins/ga/inpage_linkid.js'; _gaq.push(['_require', 'inpage_linkid', pluginUrl]); _gaq.push(['_setAccount', 'UA-6101038-2']); _gaq.push(['_trackPageview']); (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })();