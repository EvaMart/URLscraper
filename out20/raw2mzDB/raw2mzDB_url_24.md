<-- https://github.com/mzdb/pwiz-mzdb/blob/master/quickbuild.bat-->

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
68 lines (56 sloc)  2.3 KB
echo Build started at %start%
REM # Get the location of quickbuild.bat and drop trailing slash
REM # msvc.jam assumes it will find "ShowVer.exe" in %PATH%
REM # determine address-model (default 32)
REM # remove pesky '=' character for subsequent string substitution
for /f "usebackq tokens=*" %%a in ('%ALL_ARGS%') do set ALL_ARGS=%%~a
REM # need to check if no arguments were passed, or else batch will complain
REM # about a comparison with an empty string
if "%ALL_ARGS%"=="" GOTO SKIP_ADDRESS_CHECK
if "%ALL_ARGS:address-model 64=%" neq "%ALL_ARGS%" set ADDRESS_MODEL=64
REM # Build local copy of bjam
IF EXIST %PWIZ_BJAM% GOTO SKIP_BJAM
echo Building bjam for %ADDRESS_MODEL%-bit build...
call build.bat --UPDATE -sLOCATE_TARGET=bin.nt
IF NOT EXIST %PWIZ_BJAM% echo Error building bjam. & exit /b 1
REM # Do full build of ProteoWizard, passing quickbuild's arguments to bjam
echo Building pwiz (%ADDRESS_MODEL%-bit)...
echo Build finished at %end%
REM # Calculate elapsed time
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