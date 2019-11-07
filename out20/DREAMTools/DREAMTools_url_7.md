<-- https://github.com/dreamtools/dreamtools-->

* Why GitHub? 
* Customer stories →
* Explore GitHub →
#### Learn & contribute
* Open source guides
#### Connect with others
* In this repository  All GitHub  ↵
* No suggested jump to results
* In this repository  All GitHub  ↵
* In this repository  All GitHub  ↵
Sign in  Sign up
* Watch  10 
* Star  17 
* Fork  9 
Code Issues 8 Pull requests 1 Projects 0 Security  Insights
### Join GitHub today
GitHub is home to over 40 million developers working together to host and review code, manage projects, and build software together.
Code sharing related to DREAM challenges
* 702  commits 
* 1  branch 
* 3  releases 
* Fetching contributors 
* View license 
Python Jupyter Notebook MATLAB Component Pascal R Perl Shell
2. Jupyter Notebook 25.0%
4. Component Pascal 7.1%
_Branch:_ master New pull request
####  Clone with HTTPS
Use Git or checkout with SVN using the web URL.
Open in Desktop Download ZIP
Want to be notified of new releases in dreamtools/dreamtools?
Sign in Sign up
#### Launching GitHub Desktop...
If nothing happens, download GitHub Desktop and try again.
#### Launching GitHub Desktop...
If nothing happens, download GitHub Desktop and try again.
If nothing happens, download Xcode and try again.
#### Launching Visual Studio...
If nothing happens, download the GitHub extension for Visual Studio and try again.
Cannot retrieve the latest commit at this time.
Type Name Latest commit message Commit time
Failed to load latest commit information.
DREAMTools is supported for Python 2.7, 3.4 and 3.5. Pre-compiled versions are available for Linux and MAC platforms through Anaconda and the **bioconda** channel.
We do not run the entire test suite on Travis, which reports a 40% test coverage. Note however, that the actual test coverage is about 80%.
Issues and bug reports:
Cokelaer T, Bansal M, Bare C et al. DREAMTools: a Python package for scoring collaborative challenges [version 1; referees: awaiting peer review] F1000Research 2015, 4:1030 (doi: 10.12688/f1000research.7118.1) F1000 link
* Available challenges, templates and gold standards
**DREAMTools** aims at sharing code used in the scoring of DREAM challenges that pose fundamental questions about system biology and translational medicine.
The main goals of **DREAMTools** are to provide:
1. Scoring functions equivalent to those used during past DREAM challenges for **end-users** via a standalone application (called **dreamtools**).
2. A common place for **developers** involved in the DREAM challenges to share code
**DREAMTools** does not provide code related to aggregation, leaderboards, or more complex analysis even though such code may be provided (e.g., in D8C1 challenge).
Note that many scoring functions requires data hosted on Synapse . We therefore strongly encourage you to **register to Synapse**. Depending on the challenge, you may be requested to accept terms of agreements to use the data.
For those familiar with Python, you may use the pip executable provided with Python. It will install the latest release of **DREAMTools** and the dependencies:
If you are not familiar with compilation and/or Python, you may use conda since we have pre-compiled packages with a conda channel called **bioconda**:
conda config --add channels r
conda config --add channels bioconda
See Installation section on RTD for details.
**DREAMTools** can be used by developers as a Python package:
>>> from dreamtools import D6C3
>>> s = D6C3()
{'results': chi2            53.980741
R-square        34.733565
Spearman(Sp)     0.646917
Pearson(Cp)      0.647516
A standalone application can be used from a terminal. The executable is called **dreamtools**. Here is an example:
dreamtools --challenge D6C3 --submission path_to_a_file
See online documentation on for more details and examples. The source code also provides a set of IPython/Jupyter notebooks.
## Available challenges, templates and gold standards
**DREAMTools** includes about 80% of DREAM challenges from DREAM2 to DREAM9.5 Please visit F1000 link (Table 1).
All gold standards and templates are retrieved automatically. Once downloaded, you can obtain the location of a gold standard or template as follows:
dreamtools --challenge D6C3 --download-gold-standard
dreamtools --challenge D6C3 --download-template
See online documentation on RTD for details.
* © 2019 GitHub, Inc.
You can’t perform that action at this time.
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session.