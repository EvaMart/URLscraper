<-- https://github.com/mzdb/pwiz-mzdb/blob/master/raw2mzDB_quickbuild.bat-->

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
56 lines (48 sloc)  2.3 KB
rem erase former directory
IF EXIST "pwiz_mzdb\target" (
rmdir /S /Q "pwiz_mzdb\target"
rem start building raw2mzDB
echo Build started at %start%
rem -j<n> indicates using the number of processors used for compiling (some say that you should use n+1 cores, in my case I have a quad-core so I set -j5)
rem set debug-symbols=on to compile in debug mode
rem call quickbuild -j5 toolset=msvc-12.0 address-model=64 pwiz_mzdb --i-agree-to-the-vendor-licenses --without-mz5 --without-agilent --without- bruker --without-sciex --without-shimadzu --without-waters --incremental debug-symbols=off > raw2mzDB.log 2>&1
call quickbuild -j5 toolset=msvc-12.0 address-model=64 pwiz_mzdb --i-agree-to- the-vendor-licenses --incremental debug-symbols=off > raw2mzDB.log 2>&1
rem return code is not very informative because success can have a code of 0 or 1... (the real test is to check if raw2mzDB.exe file exists or not)
echo Compilation return code is %ERRORLEVEL%
rem check if raw2mzDB.exe has been generated
IF EXIST "pwiz_mzdb\target\raw2mzDB.exe" (
rem remove files that should be removed with bjam
echo File raw2mzDB has been generated !
rem this is a problem !
echo File raw2mzDB is missing !
echo Build finished at %end%
rem calculate elapsed time
for /f %options% %%a in ("%start%") do set start_h=%%a&set /a start_m=100%%b %% 100&set /a start_s=100%%c %% 100&set /a start_ms=100%%d %% 100
for /f %options% %%a in ("%end%") do set end_h=%%a&set /a end_m=100%%b %% 100&set /a end_s=100%%c %% 100&set /a end_ms=100%%d %% 100
if %hours% lss 0 set /a hours = 24%hours%
if %mins% lss 0 set /a hours = %hours% - 1 & set /a mins = 60%mins%
if %secs% lss 0 set /a mins = %mins% - 1 & set /a secs = 60%secs%
if %ms% lss 0 set /a secs = %secs% - 1 & set /a ms = 100%ms%
if 1%ms% lss 100 set ms=0%ms%
set /a totalsecs = %hours%*3600 + %mins%*60 + %secs%
echo Elapsed time: %hours%:%mins%:%secs%
* View git blame
* Reference in new issue
* © 2019 GitHub, Inc.
You can’t perform that action at this time.
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session.