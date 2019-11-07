<-- http://cole-trapnell-lab.github.io/cufflinks/releases/v1.1.0/-->

* How it works
## Transcriptome assembly and differential expression analysis for RNA-Seq.
# Cufflinks 1.1.0 released
__ September 08, 2011 __ September 08, 2011 __ Permalink __ Like __ Tweet __ +1
This is a fix release to address several issues reported by our users:
* Cuffdiff now includes a more sophisticated check for sufficient sequencing depth prior to testing for differences, which substantially improves the accuracy of differential expression analysis in loci with low to medium depth.
* A bug in the calculation of the parameters for the beta negative binomial distribution used during variance estimation has been fixed.
* Some users have reported that Cufflinks or Cuffdiff crashes due to running out of memory when processing highly expressed loci. Both programs now have a maximum number of fragments that can fall within a locus. If a locus has more than this maximum, it is skipped. The threshold is configurable via the `–max-bundle-frags` option.
* Gffread now keeps the longest CDS when collapsing transcripts.
* By popular request, fold changes are now reported log2, rather than natural log
* The status column in fpkm tracking files has been replaced by a per-condition quantification status column
* The header size limit in Cufflinks’ BAM parser used to have a 4 megabyte limit. This has been removed to allow Cufflinks to be used on assemblies with many contigs.
Previous article Next article
© 2017 Cole Trapnell. Powered by Jekyll using the So Simple Theme.
window.jQuery || document.write('<script src="http://cole-trapnell- lab.github.io/cufflinks/assets/js/vendor/jquery-1.9.1.min.js"><\/script>') var _gaq = _gaq || []; var pluginUrl = '//www.google- analytics.com/plugins/ga/inpage_linkid.js'; _gaq.push(['_require', 'inpage_linkid', pluginUrl]); _gaq.push(['_setAccount', 'UA-6101038-2']); _gaq.push(['_trackPageview']); (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })();