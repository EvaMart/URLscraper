<-- http://cole-trapnell-lab.github.io/cufflinks/releases/v0.9.0/-->

* How it works
## Transcriptome assembly and differential expression analysis for RNA-Seq.
# Cufflinks 0.9.0 released
__ September 27, 2010 __ September 27, 2010 __ Permalink __ Like __ Tweet __ +1
This release includes significant bug fixes as well as some major new features. Enhancements include:
* Thanks to the work of Adam Roberts, Cufflinks now automatically learns certain properties of each RNA-Seq library you analyze with it, including sequence specific biases. Transcript and gene abundance estimates are significantly more accurate when run with our (optional) new bias correction technology. A manuscript describing these changes is in preparation.
* Due to Adam’s changes, we do not recommend that you supply the mean and standard deviations of the fragment length distribution for your library. Cufflinks now learns these automatically.
* Cuffdiff now allows you to supply reads from multiple technical or biological replicates, and adjusts transcript and gene abundance estimates and their confidence intervals accordingly.
* Cuffdiff will by default report testing results between all pairs of samples, rather than treating samples as a time series. Time series analysis is still supported via the –time-series option.
* Cufflinks and Cuffdiff now offer improved compatibility with reads aligned with Life Technology’s BioScope aligner. Strand specific SOLiD RNA-Seq runs are fully supported.
* Cufflinks and Cuffdiff support quantile normalization of FPKM.
* Cufflinks and Cuffdiff now support both BAM and SAM files. Both file types require that the chromosome names in header @SQ records, if present, must be sorted in the same order as the reads.
* Cufflinks and Cuffdiff are much less verbose in their output by default, but each supports a “verbose” mode with a text progress bar for users that want to keep an eye on their runs
* In response to user requests, FPKM values are now provided by Cufflinks and Cuffdiff, even if their expression levels are zero, in an effort to make downstream analysis of Cuffdiff easier.
* The new “mask” GTF option allows you to supply Cufflinks with regions of the genome that it should ignore during assembly and quantification. Cuffdiff also supports mask GTF files for convenience.
* Significant assembler fixes and improvements.
* Some of the output files produced by Cuffdiff have updated and simplified formats.
* There are a number of new command line options that users may wish to set under certain circumstances.
* Note that building Cufflinks from source now requires the SAM tools. See the installation instructions for more details.
Previous article Next article
© 2017 Cole Trapnell. Powered by Jekyll using the So Simple Theme.
window.jQuery || document.write('<script src="http://cole-trapnell- lab.github.io/cufflinks/assets/js/vendor/jquery-1.9.1.min.js"><\/script>') var _gaq = _gaq || []; var pluginUrl = '//www.google- analytics.com/plugins/ga/inpage_linkid.js'; _gaq.push(['_require', 'inpage_linkid', pluginUrl]); _gaq.push(['_setAccount', 'UA-6101038-2']); _gaq.push(['_trackPageview']); (function() { var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true; ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js'; var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s); })();