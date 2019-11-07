<-- http://cole-trapnell-lab.github.io/cufflinks/releases/v1.0.2/-->

* How it works
## Transcriptome assembly and differential expression analysis for RNA-Seq.
# Cufflinks 1.0.2 released
__ May 22, 2011 __ May 22, 2011 __ Permalink __ Like __ Tweet __ +1
This release fixes several bugs and adds a few enhancements:
* The differential splicing and promoter and cds use testing in 1.0.0 and later was broken, resulting in very few (often zero) differentially regulated genes. This has been fixed.
* Many users were confused about the magnitude of quartile-normalized FPKM values in Cuffdiff. Now, quartile normalized FPKM values are scaled by a constant such that they are numerically in roughly the same range as non-quartile normalized FPKMs. Thanks to Ariel Schwartz for suggesting this change.
* A performance issue when processing BAMs with many unmapped reads has been fixed.
* Cuffcompare now creates `.tmap` and `.refmap` in the directory of the input file(s) with the same prefix as given by -o
* An issue that caused cuffmerge to fail with a message about improperly sorted SAM files has been corrected.
* Improved cuffcompare GFF support.
* Cuffdiff and Cufflinks now accept new options controlling whether all hits are counted towards the FPKM denominator, or only those compatible with some transcript in the reference annotation. Counting only compatible hits avoids certain types of bias that arise when one sample contains far more hits that aren’t compatible with any transcript than the other sample does. For example, if one sample contains vastly more mapped ribosomal RNA hits, FPKM values will appear lower in that sample, potentially leading to false positive differential expression calls. Cuffdiff by default now uses only compatible hits. Cufflinks still uses total hits by default, as using compatible hit accounting requires a reference GTF.
Previous article Next article
© 2017 Cole Trapnell. Powered by Jekyll using the So Simple Theme.
window.jQuery || document.write('<script src="http://cole-trapnell- lab.github.io/cufflinks/assets/js/vendor/jquery-1.9.1.min.js"><\/script>') var _gaq = _gaq || []; var pluginUrl = '//www.google- analytics.com/plugins/ga/inpage_linkid.js'; _gaq.push(['_require', 'inpage_linkid', pluginUrl]); _gaq.push(['_setAccount', 'UA-6101038-2']); _gaq.push(['_trackPageview']); (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })();