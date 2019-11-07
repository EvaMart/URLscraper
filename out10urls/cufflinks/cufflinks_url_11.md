<-- http://cole-trapnell-lab.github.io/cufflinks/releases/v1.2.0/-->

* How it works
## Transcriptome assembly and differential expression analysis for RNA-Seq.
# Cufflinks 1.2.0 released
__ November 23, 2011 __ November 23, 2011 __ Permalink __ Like __ Tweet __ +1
This release fixes a number of bugs and includes some signficant accuracy and performance improvements:
* Some users were experiencing a large number of genes or transcripts marked FAIL during Cuffdiff runs or Cufflinks quantification runs. These were caused by one of several issues. Most of these genes were due to numerical exceptions generated during importance sampling, a procedure originally intended to improve accuracy of abundance estimates in genes with one or more very low abundance isoforms. After detailed simulation experiments, we have concluded that the gains in accuracy are minor and do not justify the number of genes that FAIL when this procudure can’t be executed. We have dropped both this routine and the bootstrap check, which can similarly generate FAIL genes under similar conditions.
* Improvements to FPKM variance estimates for genes and transcripts, resulting in better differential expression accuracy in Cuffdiff.
* A bug that reduced accuracy in certain abundant genes has been corrected.
* The `–max-bundle-frags` option, which skips extremely deeply sequenced loci that might otherwise crash the program, has been improved so that those loci are never allowed to fully load into memory. This improves overall memory footprint and should prevent memory-related crashes.
* A bug in bias correction that results in “Inf” and “NaN” values has been fixed. An improved pre-quantification fragment collapse optimization has substantially lowered memory footprint and improved running time for Cuffdiff and Cufflinks abundance estimation.
* A bug that halts runs on hash-collisions for read names has been fixed.
* A buffer overflow in the SAM parser has been fixed.
* Other minor bugfixes and accuracy improvements for quantification.
Previous article Next article
© 2017 Cole Trapnell. Powered by Jekyll using the So Simple Theme.
window.jQuery || document.write('<script src="http://cole-trapnell- lab.github.io/cufflinks/assets/js/vendor/jquery-1.9.1.min.js"><\/script>') var _gaq = _gaq || []; var pluginUrl = '//www.google- analytics.com/plugins/ga/inpage_linkid.js'; _gaq.push(['_require', 'inpage_linkid', pluginUrl]); _gaq.push(['_setAccount', 'UA-6101038-2']); _gaq.push(['_trackPageview']); (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })();