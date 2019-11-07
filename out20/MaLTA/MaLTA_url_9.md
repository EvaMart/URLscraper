<-- http://alan.cs.gsu.edu/NGS/?q=content/xpathway-->

* Funded Research Projects
* Request new password
You are hereSoftware / XPathway
By admin \- Posted on 11 January 2016
XPathway, a set of tools that compares pathway activity analyzing mapping of contigs assembled from RNA-Seq reads to KEGG pathways. The XPathway analysis of pathway activity is based on expectation maximization and topological properties of pathway graphs.
The different tools that constitute XPathway are:
1\. **KGMLPathway2Graph**: Extraction tool of metabolic network
KGMLPathway2Graph aims at extracting metabolic pathways from KGML flatfile database. Readme, examples and software for KGMLPathway2Graph can be downloaded here .
2\. **Link Gopher 1.3.3**: Mozilla Firefox add-ons
* open kegg result page “pathway map”
* use this filter “http://www.kegg.jp/kegg-bin/show_pathway?@” with link gopher to copy all green nodes per pathway. These are part of the pathway urls. Save the output in a file.
3\. **java code**: To extract all green nodes
The code can be downloaded here along with Readme and examples.
4\. **Python code**: To compute pathway activity level and significance.
The code can be downloaded here  here along with Readme and examples.
5\. **shell script: **To download all KGML file from Kegg using wget. This is a one time operation since ko xml file do not change. Code is available  here
**Infer Pathway activity level pipeline and ****Pathway significance pipeline**
Use the steps provided in the Readme here Activity_level_and_Significance_Pipeline.
Georgia State University NGS Research Group