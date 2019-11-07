<-- https://github.com/mzdb/pwiz-mzdb-->

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
* Watch  5 
* Star  12 
* Fork  2 
Code Issues 20 Pull requests 0 Projects 0 Wiki  Security  Insights
### Join GitHub today
GitHub is home to over 40 million developers working together to host and review code, manage projects, and build software together.
An extension of the ProteoWizard framework enabling the support of the mzDB format
* 153  commits 
* 3  branches 
* 6  releases 
* Fetching contributors 
C++ C Shell HTML Python Makefile Other
_Branch:_ master New pull request
####  Clone with HTTPS
Use Git or checkout with SVN using the web URL.
Open in Desktop Download ZIP
Want to be notified of new releases in mzdb/pwiz-mzdb?
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
Raw2MzDB is an extension of the ProteoWizard framework enabling the support of the mzDB format. The current stable version is 0.9.10.
For details about mzDB concepts (scanSlice, runSlice...) and specifications, have a look to the related repository.
## Supported file formats
Raw2MzDB currently supports the following formats:
* Thermo Raw files
* AB Sciex Wiff files
* Bruker Baf files (warning: conversion of profile spectra into fitted mode does not work well, please avoid it for the moment)
* mzML files (warning: conversion of profile spectra into fitted mode does not work well, please avoid it for the moment)
* Add an option to filter spectra upon retention time (RT range) (#41)
* Restore the mzDB2mzML.exe (#42)
* Add acquisition method parameters for AB Sciex and Bruker data (#43)
* Add FK constraints (set "PRAGMA foreign_keys = ON" after sqlite3_open) + see "DEFERRABLE INITIALLY DEFERRED" change below (#44)
* Evaluate the performance benefits of "PRAGMA optimize;" (https://sqlite.org/pragma.html#pragma_optimize)
* Better support of mzML files (#63)
* Update ProteoWizard libraries (#45)
* Update SQLite library (#46)
* Add "DEFERRABLE INITIALLY DEFERRED" constraint to all FKs (#47)
* Upgrade mzDB specification to 1.0 (#48)
* Replace table bounding_box_msn_rtree with table msn_layer (#49)
* Replace blobs by vectors (#50)
* Support other instrument vendors (#51)
* Ion mobility support ? (#52)
* MS-Numpress compression algorithm support (#53)
* Quality control for fitting algorithm: compute difference between raw profile and reconstructed profile by calculating the RMSD based score (#54)
* Integration of the project with existing msconvert tool (#55)
* Linux build for "mzML -> mzDB" and "Thermo RAW file -> mzDB" (#56)
* <del>add missing CvTerms</del> (not present in Pwiz Msdata object, neither in converted mzML files) compare a mzML from mzDB and mzML from raw file (#58)
* Implement an mzDB validator using mzDB-access (#59)
* Issue #24 sample name is empty for AB Sciex analyses (also check for Bruker)
* Issue #26 is for AB Sciex DIA acquisition (and accession 1001954)
* Issue #38: Find and fix memory leak for AB Sciex data
* Issue #39: The field mzdb.param_tree can be corrupted for some Thermo raw files
* Issue #57: Check MS3 analyses
* Issue #60: Missing spectra in some mzDB files
* Issue #61: Problem with DIA analyses
* Issue #40: Improve cycle filtering by checking cycle number before centroiding data
* Issue #62: Improving DIA storing in bounding boxes
* FITTED mode is fully functional for Thermo, AB Sciex and Bruker analysis
* Safe mode added : fall back to centroid if requested mode is not possible (ie. centroid -> profile)
* \--cycles option in the command line to convert a subset of the input file
* Build number is added
* add an "--log" option to write logs to a file and/or to the console
* add an option to display version information (-v or --version)
* Using QTofPeakpicker algorithm for AB Sciex data
* Added a summary at the end of the conversion
* \--dia option has been replaced by -a or --acquisition option, user can tell if the analysis is DDA, DIA or let the converter determine it
* Better input and output file verification (convert AB Sciex data by calling .wiff or .wiff.scan files, convert Bruker data by calling .d directory)
* Added some dlls to avoid Visual C++ pre-requisites
* Wrong data peak count
* Algorithm to check DDA/DIA is now working on Thermo, AB Sciex and Bruker analysis
* mzML file support is improved
* fixed encoding issue with low resolution spectra
* fixed encoding issue with NO_LOSS option
* remove some temporary files after compiling
* see issues for more informations
* AbSciex (.WIFF) files support
* Bruker (.d) files support
* \--dia option in the command line to force DIA file creation
* <del>\--ignore-error option to force conversion even if error occured</del> (CRT translation to C++ exceptions makes the converter very slow)
* reduced time of spectrum table loading (table records stored at the end of the file)
* improvements in exception catching
* new columns 'mz_precision' ansd 'intensity_precision' in data-encoding table (instead of param-tree)
* insert only used data-encoding
* update proteowizard to the latest
* Wrong encoding for HCD spectra (32 instead of 64 bits)
* See fixed issues for more information
### Convert vendor raw files into mzDB files
#### Download and setup
* Download the zip archive
* Raw2mzDB should work on any modern 64 bits Windows environment. If you encounter missing dlls issues, you may try to install Microsoft's .NET Framework 3.5 SP1 and 4.0. Also consider Visual C++ Redistributable for Visual Studio 2008, 2012 and 2013.
#### Command line usage
Open a command line window in the directory containing raw2mzdb.exe then type:
**raw2mzdb.exe -i <rawfilename> -o <outputfilename>**
Example: **raw2mzdb.exe -i "D:\myfile.raw" -o "D:\myfile.mzDB"**
By defaut, the raw file will be converted in the "fitted" mode for the MS1 (MS2 is often in centroid mode and can not be converted in fitted mode). If the MS2 (or superior) are acquired in high resolution (i.e in profile mode), you could specify that you want to convert specific MS levels in the required mode:
**raw2mzdb.exe -i <rawfilename> -o <outputfilename> -f 1-2** will try to convert MS and MS/MS spectra in fitted mode.
There are two other available conversion modes:
* "profile", the command line is then: **raw2mzdb.exe -i <rawfilename> -o <outputfilename> -p 1** (means you want profile mode for MS1, other MS levels will be stored as they were stored in the raw file)
* "centroid" : **raw2mzdb.exe -i <rawfilename> -o <outputfilename> -c 1** (means you want centroid mode for MS1, other MS levels will be stored as they were stored in the raw file)
**Complete list of parameters:**
usage: raw2mzDB.exe --input filename <parameters>
-i, --input : specify the input rawfile path
-o, --output : specify the output filename
-c, --centroid : centroidization, eg: -c 1 (centroidization msLevel 1) or -c 1-5 (centroidization msLevel 1 to msLevel 5) 
-p, --profile : idem but for profile mode 
-f, --fitted : idem buf for fitted mode 
-T, --bbTimeWidth : bounding box width for ms1 in seconds, default: 15s for DDA, 60s for DIA
-t, --bbTimeWidthMSn : bounding box width for ms > 1 in seconds, default: 0s for DDA, 75s for DIA
-M, --bbMzWidth : bounding box height for ms1 in Da, default: 5Da for DDA and DIA
-m, --bbMzWidthMSn : bounding box height for msn in Da, default: 10000Da for DDA, 20Da for DIA
-a, --acquisition : dda, dia or auto (converter will try to determine if the analysis is DIA or DDA), default: auto
--noLoss : if present, leads to 64 bits conversion of mz and intenstites (larger ouput file)
--cycles : only convert the selected range of cycles, eg: 1-10 (first ten cycles) or 10- (from cycle 10 to the end) ; using this option will disable progress information
-s, --safeMode : use centroid mode if the requested mode is not available
--log : console, file or both (log file will be put in the same directory as the output file), default: console
-v, --version: display version information
-h --help : show help
#### Build from command line
The current project uses the MSVC compiler provided in the "Visual Studio Express 2013 for Windows desktop". Compilation on Linux may require some code corrections for the moment. We plan to be cross-platform some day.
After installing Visual Studio, check following points :
* Visual Studio path is added to system environment path : _C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin_
* If you are using 64-bit operating system : allow the cross compilation : 
* open commandline : Win+R, type _cmd_
* go to _Microsoft Visual Studio 12.0\VC_ : `cd C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC`
* execute `vcvarsall.bat x86_amd64` , you should have `Setting environment for using Microsoft Visual Studio 2013 x64 cross tools.` message.
In order to build with _bjam_:
* Unzip pwiz-mzdb-lib.zip file (containing project dependencies as static compiled libraries) located in `project_root/pwiz_mzdb/mzdb/lib` directory.
* Then run the script _raw2mzDB_quickbuild.bat_ from the project root
* Or else, run the following command from the project root:  
`quickbuild -j8 toolset=msvc-12.0 address-model=64 pwiz_mzdb --i-agree-to-the- vendor-licenses --incremental`
* _\--incremental_ is not mandatory but it speeds up the compilation process
**raw2mzdb.exe** file is generated in : `project_root/pwiz_mzdb/target`
To debug raw2mzDB, you first need to compile it with debug symbols. To do so, open the raw2mzDB_quickbuild.bat script and set _debug-symbols=on_ Or just run quickbuild.bat with this argument correctly set. This should create a raw2mzDB.pdb file in the target directory. Using this raw2mzDB.pdb file, you can use a debugging tool such as MTuner.
#### Project dependencies(headers already included in the root directory)
* PWIZ of course
* Visual Studio: not very well tested.
* QtCreator: importing project with existing sources (from the menu), will provide decent code completion.
### HOW TO ?
#### Iterate through spectra
To iterate over all spectra, simply do the following:
mzDBReader reader(mzdb); //build a mzdbreader object
MSData msdata; // build empty Pwiz msdata object
// the following will build a custom SpectrumList, ready for iteration
SpectrumListPtr sl = msdata.run.spectrumListPtr; // fetch spectrumList
for (size_t i=0; i < sl.size(); ++i) {
// fetch spectrum, second argument is for getting or not (i.e. fetch only metadata) 
// spectrum data points, it has no effect on the actual implementation, always 
// return a spectrum with mz/intensity arrays
SpectrumPtr s = sl.spectrum(i, true);
Warning: this is not suitable for accessing only one random spectrum. User may use the 'getSpectrum' function instead.
#### Iterate through run slices
Not yet implemented. You can only extract one runSlice at a time for the moment:
mzDBReader reader(mzdb); //build a mzdbreader object
MSData msdata; // build empty Pwiz msdata object
vector<mzScan*> results; // mzScan is a simple object containing vector members 'mz' and 'intensities'
reader.extractRunSlice(mzmin, mzmax, msLevel, results);
This feature is already implemented in the java reader mzDBAccess
#### Query LC-MS DDA/DIA data using R*Tree queries
To extract region using R*Tree:
mzDBReader reader(mzdb); //build a mzdbreader object
MSData msdata; // build empty Pwiz msdata object
vector<mzScan*> results; // mzScan is a simple object containing vector members 'mz' and 'intensities'
reader.extractRegion(mzmin, mzmax, rtmin, rtmax, msLevel, results);
Specifying a msLevel=1 will extract region using spectra acquired in mslevel=1, suitable for DDA analysis. Otherwise, it will request the msn R*Tree suitable to perform DIA analysis.
* © 2019 GitHub, Inc.
You can’t perform that action at this time.
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session.