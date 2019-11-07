<-- https://github.com/mzdb/pwiz-mzdb/blob/master/clean.sh-->

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
Code Issues 20 Pull requests 0 Projects 0 Wiki Security Pulse
### Join GitHub today
GitHub is home to over 40 million developers working together to host and review code, manage projects, and build software together.
Find file  Copy path
Find file  Copy path
Cannot retrieve contributors at this time
40 lines (33 sloc)  2.68 KB
pushd $pwiz_root > /dev/null
if (ls build-*-* > /dev/null 2>&1); then rm -fr build-*-*; fi;
if (ls libraries/boost_*_*_? > /dev/null 2>&1); then rm -fr libraries/boost_*_*_?; fi;
if [ -d libraries/boost-build/src/engine/bin ]; then rm -fr libraries/boost- build/src/engine/bin; fi;
if [ -d libraries/boost-build/src/engine/bootstrap ]; then rm -fr libraries/boost-build/src/engine/bootstrap; fi;
if [ -d libraries/gd-2.0.33 ]; then rm -fr libraries/gd-2.0.33; fi;
if [ -d libraries/zlib-1.2.3 ]; then rm -fr libraries/zlib-1.2.3; fi;
if [ -d libraries/libgd-2.1.0alpha ]; then rm -fr libraries/libgd-2.1.0alpha; fi;
if [ -d libraries/libpng-1.5.6 ]; then rm -fr libraries/libpng-1.5.6; fi;
if [ -d libraries/freetype-2.4.7 ]; then rm -fr libraries/freetype-2.4.7; fi;
if [ -d libraries/hdf5-1.8.7 ]; then rm -fr libraries/hdf5-1.8.7; fi;
if [ -d libraries/fftw-3.1.2 ]; then rm -fr libraries/fftw-3.1.2; fi;
if [ -d libraries/expat-2.0.1 ]; then rm -fr libraries/expat-2.0.1; fi;
if [ -f libraries/libfftw3-3.def ]; then rm -f libraries/libfftw3-3.def; fi;
if [ -f libraries/libfftw3-3.dll ]; then rm -f libraries/libfftw3-3.dll; fi;
if [ -f pwiz/Version.cpp ]; then rm -f pwiz/Version.cpp; fi;
if [ -f pwiz/data/msdata/Version.cpp ]; then rm -f pwiz/data/msdata/Version.cpp; fi;
if [ -f pwiz/data/tradata/Version.cpp ]; then rm -f pwiz/data/tradata/Version.cpp; fi;
if [ -f pwiz/data/identdata/Version.cpp ]; then rm -f pwiz/data/identdata/Version.cpp; fi;
if [ -f pwiz/data/proteome/Version.cpp ]; then rm -f pwiz/data/proteome/Version.cpp; fi;
if [ -f pwiz/analysis/Version.cpp ]; then rm -f pwiz/analysis/Version.cpp; fi;
if [ -d pwiz/data/vendor_readers/Thermo/Reader_Thermo_Test.data ]; then rm -fr pwiz/data/vendor_readers/Thermo/Reader_Thermo_Test.data; fi;
if [ -d pwiz/data/vendor_readers/Agilent/Reader_Agilent_Test.data ]; then rm -fr pwiz/data/vendor_readers/Agilent/Reader_Agilent_Test.data; fi;
if [ -d pwiz/data/vendor_readers/ABI/Reader_ABI_Test.data ]; then rm -fr pwiz/data/vendor_readers/ABI/Reader_ABI_Test.data; fi;
if [ -d pwiz/data/vendor_readers/ABI/T2D/Reader_ABI_T2D_Test.data ]; then rm -fr pwiz/data/vendor_readers/ABI/T2D/Reader_ABI_T2D_Test.data; fi;
if [ -d pwiz/data/vendor_readers/Waters/Reader_Waters_Test.data ]; then rm -fr pwiz/data/vendor_readers/Waters/Reader_Waters_Test.data; fi;
if [ -d pwiz/data/vendor_readers/Bruker/Reader_Bruker_Test.data ]; then rm -fr pwiz/data/vendor_readers/Bruker/Reader_Bruker_Test.data; fi;
if [ -d pwiz_tools/BiblioSpec/tests/inputs ]; then rm -fr pwiz_tools/BiblioSpec/tests/inputs; fi;
if [ -d pwiz_tools/BiblioSpec/tests/output ]; then rm -fr pwiz_tools/BiblioSpec/tests/output; fi;
* View git blame
* Reference in new issue
* © 2019 GitHub, Inc.
You can’t perform that action at this time.
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session.