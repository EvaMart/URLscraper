<-- http://www.popgen.dk/angsd/index.php/Association-->

ANGSD: Analysis of next generation Sequencing Data
Latest tar.gz version is (0.930/0.931 on github), see Change_log for changes, and download it  here.
Jump to: navigation, search
Association can be performed using two approaches.
1. Based on testing differences in allele frequencies between cases and controls, using genotype likelihoods
2. Based on a generalized linear framework which also allows for quantitative traits and binary and for including additional covariates, using genotype posteriors. 
* 1 Brief Overview
* 2 Case control association using allele frequencies
* 2.2 Dependency Chain
* 3 Score statistic
* 3.2 Example with imputation (using BEAGLE)
* 3.3 Dependency Chain
* 4 Latent genotype model (EM algorithm)
* 4.1 Example with genotype probabilities
* 5 Hybrid model (Score Test + EM algorithm)
* 5.1 Example with genotype probabilities
* 6 Dosage model
* 7.1 Output format
* 7.2 Example with genotype probabilities
* 8 Problems with inflation of p-values
We recommend that users don't perform association analysis on all sites, but limit the analysis to informative sites, and in the case of alignement data (BAM), we advise that users filter away the low mapping quality reads and the low qscore bases.
The filtering of the alignment data is described in Input, and filtering based on frequencies/polymorphic sites are described  here.
This can be done easily at the command line by adding the below commands
-minQ 20 -minMapQ 30 -SNP_pval 1e-6 #Use polymorphic sites with a p-value of 10^-6
-minQ 20 -minMapQ 30 -minMaf 0.05 #Use sites with a MAF >0.05
1: Frequency Test (Known Major and Minor)
4: Latent genotype model
5: Score Test with latent genotype model - hybrid test
-yBin		(null)	(File containing disease status)	
Score, Latent, Hybrid and Dosage Test Options:
-yBin		(null)	(File containing disease status)
-cov		(null)	(File containing additional covariates)
-minHigh	10	(Require atleast minHigh number of high credible genotypes)
-minCount	10	(Require this number of minor alleles, estimated from MAF)
-assoThres	0.000001	Threshold for logistic regression
-assoIter	100	Number of iterations for logistic regression
-emThres	0.000100	Threshold for convergence of EM algorithm in doAsso 4 and 5
-emIter	40	Number of max iterations for EM algorithm in doAsso 4 and 5
-hybridThres		0.050000	(p-value value threshold for when to perform latent genotype model)
# Case control association using allele frequencies
To test for differences in the allele frequencies, genotype likelihood needs to be provided or  estimated. The test is an implimentation of the likelihoods ratio test for differences between cases and controls described in details in Kim2011.
**1**: The test is performed assuming the minor allele is known.   
A file containing the case control status. 0 being the controls, 1 being the cases and -999 being missing phenotypes. The file should contain a single phenotype entry per line.
Example of cases control phenotype file
create a large number of individuals by recycling the example files (500 individuals) and simulate some phentypes (case/control) using R
for i in `seq 1 50`;do cat bam.filelist>>large.filelist;done
./angsd -yBin pheno.ybin -doAsso 1 -GL 1 -out out -doMajorMinor 1 -doMaf 1 -SNP_pval 1e-6 -bam large.filelist -r 1: -P 5
Note that because you are reading 500 bam files it takes a little while
gunzip -c out.lrt0.gz | head
The LRT is the likelihood ration statistics which is chi square distributed with one degree of freedom.
The method is based on estimating frequencies from genotype likelihoods. If alignment data has been supplied you need to specify the following.
1. Genotype likelihood model (-GL).
2. Determine Major/Minor (-doMajorMinor).
3. Maf estimator (-doMaf).
If you have supplied genotype likelihood files as input for angsd you can skip 1.
To perform the test in a generalized linear framework posterior genotype probabilities must be provided or estimated. The approach is published here skotte2012.
A file containing the case control status. 0 being the controls, 1 being the cases and -999 being missing phenotypes.
Example of cases control phenotype file
File containing the phenotype values.-999 being missing phenotypes. The file should contain a single phenotype entry per line.
Example of quantitative phenotype file
Files containing additional covariates in the analysis. Each lines should contain the additional covariates for a single individuals. Thus the number of lines should match the number of individuals and the number of coloums should match the number of additional covariates.
Example of covariate file
1 0 0 1 
1 0.1 0 0 
2 0 1 0 
2 0 1 0 
2 0.1 0 1 
1 0 0 1 
1 0.3 0 0 
2 0 0 0 
1 0 0 0 
2 0.2 0 1 
1 0 1 0 
1 0 0 0 
1 0.1 0 0 
1 0 0 0 
2 0 0 1 
2 0 0 0 
2 0 0 0 
1 0 0 1 
1 0.5 0 0 
2 0 0 0
default = 10 
This approach needs a certain amount of variability in the genotype probabilities. minHigh filters out sites that does not have at least [int] number of of homozygous major, heterozygous and homozygous minor genotypes. At least two of the three genotypes categories needs at least [int] individuals with a genotype probability above 0.9. This filter avoids the scenario where all individuals have genotypes with the same probability e.g. all are heterozygous with a high probability or all have 0.33333333 probability for all three genotypes.
default = 10 
The minimum expected minor alleles in the sample. This is the frequency multiplied by two times the number of individuals. Performing association on extremely low minor allele frequencies does not make sence.
1. Additive/Log-additive for Linear/Logistic Regression (Default).
create a large number of individuals by recycling the example files (500 individuals) and simulate some phentypes (case/control) using R
for i in `seq 1 50`;do cat bam.filelist>>large.filelist;done
For cases control data for polymorphic sites (p-value < 1e-6)
./angsd -yBin pheno.ybin -doAsso 2 -GL 1 -doPost 1 -out out -doMajorMinor 1 -SNP_pval 1e-6 -doMaf 1 -bam large.filelist -P 5 -r 1:
For quantitative traits (normal distributed errors) for polymorphic sites (p-value < 1e-6) and additional covariates
./angsd -yQuant pheno.yquant -doAsso 2 -cov cov.file -GL 1 -doPost 1 -out out -doMajorMinor 1 -SNP_pval 1e-6 -doMaf 1  -bam large.filelist -P 5  -r 1:
## Example with imputation (using BEAGLE)
First the polymorphic sites to be analysed needs to be selected (-doMaf 1 -SNP_pval -doMajorMinor) and the genotype likelihoods estimated (-GL 1) for use in the Beagle software (-doGlf 2).
./angsd -GL 1 -out input -doMajorMinor 1 -SNP_pval 1e-6 -doMaf 1  -bam large.filelist -P 5  -r 1: -doGlf 2
java -Xmx15000m -jar beagle.jar like=input.beagle.gz out=beagleOut
the reference fai can be obtained by indexing the reference genome or by using a bam files header
samtools view -H  bams/smallNA11830.mapped.ILLUMINA.bwa.CEU.low_coverage.20111114.bam | grep SN |cut -f2,3 | sed 's/SN\://g' |  sed 's/LN\://g' > ref.fai
The association can then be performed on the genotype probabilities using the score statistics
./angsd -doMaf 4 -beagle beagleOut.impute.beagle.gz.gprobs.gz -fai ref.fai  -yBin pheno.ybin -doAsso 2 
The method is based on genotype probabilities. If alignment data has been supplied you need to specify the following.
1. Genotype likelihood model (-GL).
2. Determine Major/Minor (-doMajorMinor).
3. Maf estimator (-doMaf).
4. Calculate posterior genotype probability (-doPost). If you use the score statistics -doAsso 2 then calculate the posterior using the allele frequency as prior (-doPost 1). 
If you have supplied genotype likelihoods for angsd, then you should skip 1.  
If you have supplied genotype probabilities (as beagle output format), there are no dependencies.
# Latent genotype model (EM algorithm)
To perform the test in a generalized linear framework posterior genotype probabilities must be provided or estimated. The approach is employing an EM algorithm where the genotype is the introduced as a latent variable and then the likelihood is maximised using weighted least squares regression, similar to the approach in asaMap.
Otherwise works exactly like the Score Test, the only thing that has to be changed is the -doAsso flag. This method has an advantage in that effect sizes are estimated and reported.
## Example with genotype probabilities
It can be run thus, with a binary phenotype (can also be used for a quantitative phenotype with the -yQuant flag):
./angsd -doMaf 4 -beagle beagleOut.impute.beagle.gz.gprobs.gz -fai ref.fai  -yBin pheno.ybin -doAsso 4 
# Hybrid model (Score Test + EM algorithm)
To perform the test in a generalized linear framework posterior genotype probabilities must be provided or estimated. The approach is employing the score test first, and then if the chi-square test statistic is below a certain threshold, also apply the latent genotype model, thereby getting the effect size. The idea behind this, is that the score test is faster, as we do need to apply the EM algorithm, however using the EM algorithm gives us an effect size.
-doAsso 5 -hybridThres 0.05 (p-value threshold for when to perform latent genotype)
Otherwise works exactly like the score test + latent genotype model, the only thing that has to be changed is the -doAsso flag. This method has an advantage in that effect sizes are estimated and reported.
## Example with genotype probabilities
It can be run thus, with a binary phenotype (can also be used for a quantitative phenotype with the -yQuant flag):
./angsd -doMaf 4 -beagle beagleOut.impute.beagle.gz.gprobs.gz -fai ref.fai  -yBin pheno.ybin -doAsso 5
To perform the test in a generalized linear framework posterior genotype probabilities must be provided or estimated. The approach is calculating the dosage or the expected genotype from the genotype probabilities, using the following formula:
E[G|X] = p(G=1|X) + 2*p(G=2|X)
And then doing a normal linear/logistic model with the dosages as the tested variable. This approach is almost as fast as the score test and effect sizes are also estimated.
Otherwise works exactly like the score test + latent genotype model, the only thing that has to be changed is the -doAsso flag. This method has an advantage in that effect sizes are estimated and reported.
The output from the association analysis is a list of files called **prefix.lrt**. These are tab separated plain text files, with nine columns.
Chromosome  Position  Major  Minor  Frequency  N*  LRT  beta^  SE^  highHe* highHo*  emIter~
***** Indicates that these columns are only used for the score test, latent genotype model, hybrid model and dosage model. **^** Indicates that these columns are only used for the latent genotype model, hybrid model and dosage model. **~** Indicates that these columns are only used for the latent genotype model and hybrid model. 
The Major allele as determined by -doMajorMinor. If posterior genotype files has been supplied as input, this column is not defined.
The Minor allele as determined by -doMajorMinor. If posterior genotype files has been supplied as input, this column is not defined.
The Minor allele frequency as determined by -doMaf.
Number of individuals. That is the number of samples that have both sequencing data and phenotypic data.
The likelihood ratio statistic. This statistic is chi square distributed with one degree of freedom. Sites that fails one of the filters are given the value -999.000000.
The estimated effect size. Sites that fails one of the filters are given the value nan.
The estimated standard error. Sites that fails one of the filters are given the value nan.
Number of sites with a WE/HE/HO genotype posterior probability above 0.9. WT=major/major,HE=major/minor,HO=minor/minor.
Number of iterations of EM algorithm for maximising likelihood.
Example without effect sizes (beta):
## Example with genotype probabilities
It can be run thus, with a binary phenotype (can also be used for a quantitative phenotype with the -yQuant flag):
./angsd -doMaf 4 -beagle beagleOut.impute.beagle.gz.gprobs.gz -fai ref.fai  -yBin pheno.ybin -doAsso 6 
# Problems with inflation of p-values
You can evaluate the behavior of the tests by making a QQ plot of the LRT. There are several reasons why it might show signs of inflation
-doPost (when using doAsso 2, 4, 5 or 6 without the use of posterior input -beagle
if you estimate the posterior genotype probability using a uniform prior (-doPost 2) then small differences in depth between sample will inflate the test statistics (see Skotte2012). Use the allele frequency as a prior (-doPost 1)
If you set this too low then it will results in inflation of the test statistics.
-yQuant (when using -doAsso 2, 4, 5 or 6 with a quantitative trait)
If your trait is not continues or the distribution of the trait is skewed or has outliers then you will get inflation of p-values. Same rules apply as for a standard regression. Consider transforming you trait into a normal distribution
If you have population structure then you will have to adjust for it in the regression model (-doAssso 2, 4, 5 or 6). Consider using NGSadmix or PCAngsd and use the results as covariates. Note that the model will still have some issues because it uses the allele frequency as a prior. For the adventurous you can use PCAngsd or NGSadmix to estimate the individual allele frequencies and calculate your own genotype probabilities that take structure into account. These can then be used in angsd using the -beagle input format.
Usually a GWAS is performed on thousands of samples and we have only tested the use of the score statistics on hundreds of samples. If you have a low number of samples then try to figure out what minor allele frequency you would need in order to have some power. Also be careful with reducing -minCount/-minHigh.
* (Multi) SFS Estimation
* Population branch statistics (pbs)
* PCA (sampling approach)
* HWE and inbreeding with ngsF
* Create Fasta file
### SNPs and genotypes
* Major and Minor
* Genotype likelihood files
* overview of class
* accessing core data
* custom data containers
* What links here
* This page was last modified on 25 March 2019, at 17:49.