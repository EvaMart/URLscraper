<-- https://github.com/mzdb/pwiz-mzdb/blob/master/Jamroot.jam-->

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
1403 lines (1201 sloc)  53.7 KB
# $Id: Jamroot.jam 11391 2017-09-18 16:34:05Z chambm $
# Original author: Darren Kessner <darren@proteowizard.org>
# Copyright 2008 Spielberg Family Center for Applied Proteomics
# Cedars-Sinai Medical Center, Los Angeles, California 90048
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
if ( "--help" in [ modules.peek : ARGV ] )
{ # slip our own help text in here
## Targets and Related Options #
# build Build ProteoWizard applications
# --libraries-path=<DIR> Find libraries directory here.
# --boost-src=<DIR> Find Boost source distribution here.
# --zlib-src=<DIR> Find zlib source distribution here.
# --i-agree-to-the-vendor-licenses For windows builds, indicates
# your willingness to comply with
# license terms of the vendor DLLs
# that enable reading of proprietary
# binary data formats. Without this
# switch your build will not include
# support for reading vendor binary
# --incremental Skip the checks for extracting external library
# tarballs - useful after your initial build
# --without-mz5 Build without mz5 support
# --without-agilent Build without Agilent support
# --without-bruker Build without Bruker support
# --without-sciex Build without Sciex support
# --without-shimadzu Build without Shimadzu support
# --without-thermo Build without Thermo support
# --without-waters Build without Waters support
# --without-binary-msdata Build with support for mass spec text formats only
# (mzML, mzXML, MGF, etc - no binary formats
# like mz5 or vendor-specifics )
# There are some aliases to build commonly used subsets of pwiz:
# msconvert (just the command-line executable, copied to <BUILD_DIR>/<TOOLSET_DIR>)
# executables (all the pwiz core tools, copied to <BUILD_DIR>/<TOOLSET_DIR>)
# If you just want to build a specific subset of pwiz, add a target to
# your command line. For example to build just the msdata file
# read/write stuff, add:
# Or to build a particular item of that subset, such as a test,
# you could add (note the double slashes!) :
; # end of our own help text
.os = [ modules.peek : OS ] ; # NT, LINUX, MACOSX
.platform = [ modules.peek : OSPLAT ] ; # X86, X86_64, POWERPC
# set up explicit 32-bit or 64-bit builds
if "address-model=64" in [ modules.peek : ARGV ] || ( ! ( $(.os) = "NT" ) && $(.platform:L) = "x86_64" )
constant PROCESSOR_ARCHITECTURE : "AMD64" ;
constant PLATFORM : "x64" ;
else if "address-model=32" in [ modules.peek : ARGV ] || $(.platform:L) = "x86" || $(.os) = "NT"
constant PROCESSOR_ARCHITECTURE : "x86" ;
constant PLATFORM : "x86" ;
echo "Unable to determine address-model for platform $(.platform:L). The only supported platforms are x86 and x86_64." ;
local default_libraries_path = "./libraries" ;
local libraries_path = [ MATCH --libraries-path=(.*) : [ modules.peek : ARGV ] ] ;
libraries_path ?= $(default_libraries_path) ; # set default path in absence of command-line path
local default_boost_src = "$(libraries_path)/boost_1_56_0" ;
local boost_src = [ MATCH --boost-src=(.*) : [ modules.peek : ARGV ] ] ;
boost_src ?= $(default_boost_src) ; # set default path in absence of command- line path
local default_zlib_src = "$(libraries_path)/zlib-1.2.3" ;
local zlib_src = [ MATCH --zlib-src=(.*) : [ modules.peek : ARGV ] ] ;
zlib_src ?= $(default_zlib_src) ; # set default path in absence of command- line path
# TODO: get version from boost/version.hpp
local boost_version_suffix = [ MATCH "boost_(._..(_.)?)" : $(boost_src:L) ] ;
if ! $(boost_version_suffix) { errors.user-error "Unable to determine version from external Boost source; expected x_xx[_xx] format." ; }
constant BOOST_VERSION : [ regex.split $(boost_version_suffix[1]) _ ] ;
# declare a feature indicating vendor API support is desired (but not necessarily possible on the current platform)
if [ modules.peek : NT ] && --i-agree-to-the-vendor-licenses in [ modules.peek : ARGV ]
feature.feature vendor-api-support : on off : incidental propagated ; # on is the default
feature.feature vendor-api-support : off on : incidental propagated ; # off is the default
rule vendor-api-support ( properties * )
if [ modules.peek : NT ] && --i-agree-to-the-vendor-licenses in [ modules.peek : ARGV ]
if ( "--without-binary-msdata" in [ modules.peek : ARGV ] ) # support only text formats like mzML, mzXML, MGF etc
echo "NOTICE: building without support for binary msdata formats as requested" ;
else if ( "--without-mz5" in [ modules.peek : ARGV ] )
echo "NOTICE: building without mz5 support as requested" ;
# do we want to skip mz5 support?
rule without-mz5 ( properties * )
if --without-mz5 in [ modules.peek : ARGV ]
return <location-prefix>without-mz5 <define>WITHOUT_MZ5 ;
return [ without-binary-msdata $(properties) ] ;
# do we want to skip all binary file formats (vendors and mz5)?
rule without-binary-msdata ( properties * )
if --without-binary-msdata in [ modules.peek : ARGV ]
return <location-prefix>without-binary-msdata <define>WITHOUT_MZ5 <vendor-api- support>off ;
path-constant PWIZ_ROOT_PATH : . ;
path-constant PWIZ_BUILD_PATH : build-$(.os:L)-$(.platform:L) ;
path-constant PWIZ_LIBRARIES_PATH : $(libraries_path) ;
import testing ; # needed to enable unit-test rule
import package ; # needed for package install
import path ; # needed for glob, exists, etc.
import project ; # needed for project.current
modules.poke : BOOST_BUILD_PATH : [ modules.peek : BOOST_BUILD_PATH ] $(PWIZ_LIBRARIES_PATH)/predef/check ;
import $(PWIZ_LIBRARIES_PATH)/predef/check/predef : require check : predef- require predef-check ;
if --teamcity-test-decoration in [ modules.peek : ARGV ]
if [ modules.peek : NT ]
TEST_PRECOMMAND = "set pp=##\necho %pp%teamcity[testStarted name='%name%']" ;
"IF %status% NEQ 0"
"(echo %pp%teamcity[testFailed name='%name%' message='Exit status: %status%'] )\n" # TODO: does testFailed go to stderr? 1>&2
"echo %pp%teamcity[testFinished name='%name%']" ;
TEST_POSTCOMMAND = $(TEST_POSTCOMMAND:J=" ") ;
TEST_PRECOMMAND = "pp=##\necho $pp\"teamcity[testStarted name='$name']\"" ;
"if test $status -ne 0 ; then"
"echo $pp\"teamcity[testFailed name='$name' message='Exit status: $status']\" ;"
"echo $pp\"teamcity[testFinished name='$name']\"" ;
TEST_POSTCOMMAND = $(TEST_POSTCOMMAND:J=\n) ;
# put raw commands in global module
modules.poke : TEST_PRECOMMAND : $(TEST_PRECOMMAND) ;
modules.poke : TEST_POSTCOMMAND : $(TEST_POSTCOMMAND) ;
TEAMCITY_TEST_DECORATION = <testing.arg>--teamcity-test-decoration ;
# return the itemname if textonly build is off (the default)
rule binary-readers-build ( itemname )
if ( ! [ without-binary-msdata ] )
return $(itemname) ; # do build binary readers
# return the itemname if mz5 build is on (the default)
rule mz5-build ( itemname )
if ( ! [ without-mz5 ] )
return $(itemname) ; # do build mz5
if ! [ modules.peek : NT ]
# make msbuild targets a no-op
rule msbuild ( name : sources * : requirements * : default-build * : usage- requirements * )
# starting with gcc 4.8, gcc is extremely verbose about unused typedefs; heavily used in Boost concept checks
[ predef-check "BOOST_COMP_GNUC >= 4.8" : : <cxxflags>-Wno-unused-local- typedefs ]
# starting with gcc 4.9, gcc offers colored diagnostic messages, helpful when looking for an elusive "error" message in a sea of warning spam
[ predef-check "BOOST_COMP_GNUC >= 4.9" : : <cxxflags>-fdiagnostics- color=always ]
# any module which links with .NET (either dynamically or statically) must use the shared runtime
# SEH exceptions crossing native/managed boundaries are problematic with this set to off;
# also, catch(...) will catch SEH exceptions with this on
# special msvc hacks
<toolset>msvc:<define>_CRT_SECURE_NO_DEPRECATE # don't deprecate the standard library
<toolset>msvc:<define>_SCL_SECURE_NO_DEPRECATE # don't deprecate the standard library
<toolset>msvc:<define>_USE_MATH_DEFINES # for M_PI in <cmath>
<toolset>msvc:<define>BOOST_ALL_NO_LIB # disable auto-link
<toolset>msvc:<cxxflags>/wd4100 # warning: unreferenced formal parameter
<toolset>msvc:<cxxflags>/wd4512 # warning: assignment operator could not be generated
<toolset>msvc:<cxxflags>/wd4127 # warning: conditional expression is constant (boost::lexical_cast)
<toolset>msvc:<cxxflags>/wd4701 # warning: potentially uninitialized local variable 'result' used (boost::lexical_cast, debug)
<toolset>msvc:<cxxflags>/wd4245 # warning: conversion from 'type1' to 'type2', signed/unsigned mismatch (boost/filesystem/convenience.hpp)
<toolset>msvc:<cxxflags>/wd4251 # warning: class needs to have dll-interface to be used by clients of class
<toolset>msvc:<cxxflags>/wd4267 # warning: conversion from 'type1' to 'type2', possible loss of data (boost::lexical_cast)
<toolset>msvc:<cxxflags>/wd4244 # warning: conversion from 'int' to 'unsigned short', possible loss of data (boost/date_time/microsec_time_clock.hpp)
<toolset>msvc:<cxxflags>/wd4275 # warning: non dll-interface class 'base' used as base for dll-interface class 'derived'
<toolset>msvc:<cxxflags>/wd4702 # warning: unreachable code (boost::lexical_cast)
<toolset>msvc:<cxxflags>/wd4714 # warning: marked as __forceinline not inlined (boost::spirit::karma::sequence)
# special gcc hack - Cygwin gcc 3.4.4, Ubuntu gcc 4.1.2
# warning: '__cur' might be used uninitialized in this function
# set standard to C++11
# special Cygwin gcc-3.4.4 hack
# linker "multiple definition" error on inclusion of boost-1.34.1 filesystem headers
# allow "long long" even with -pedantic
# any GCC executable that uses shared libraries must have all its code built with -fPIC
# msdata text only?
# don't call 'strip' -- causes 'Bus error' in some cases
# e.g. find_if with inline predicate
# use of boost::thread requires multithreaded runtime
# change boost debug assertions to exceptions by force including Exception.hpp
# external library declarations
<toolset>gcc:<linkflags>-pthread # sometimes segfault without this -- dk
<toolset>gcc:<linkflags>-pthread # sometimes segfault without this -- dk
lib fftw3 : : <threading>multi <search>$(PWIZ_LIBRARIES_PATH)/fftw-3.1.2/.libs : : <include>$(PWIZ_LIBRARIES_PATH)/fftw-3.1.2/api ;
lib fftw3 : : <threading>multi <toolset>msvc <name>libfftw3-3 <search>$(PWIZ_LIBRARIES_PATH) : : <include>$(PWIZ_LIBRARIES_PATH)/fftw-3.1.2/api ;
alias svm : $(PWIZ_LIBRARIES_PATH)/libsvm-3.0//svm ;
modules.poke : BOOST_BUILD_PATH : [ modules.peek : BOOST_BUILD_PATH ] $(PWIZ_LIBRARIES_PATH) ;
# get version info (used for tarball filenames)
constant PWIZ_MAJOR : 3 ;
constant PWIZ_MINOR : 0 ;
generate-version.cpp $(PWIZ_ROOT_PATH)/pwiz/data/msdata/Version.cpp : pwiz msdata : $(PWIZ_MAJOR) : $(PWIZ_MINOR) :
: *.?pp *.h Jamfile.jam *.manifest* : Version.cpp
generate-version.cpp $(PWIZ_ROOT_PATH)/pwiz/analysis/Version.cpp : pwiz analysis : $(PWIZ_MAJOR) : $(PWIZ_MINOR) :
: *.?pp Jamfile.jam : Version.cpp
generate-version.cpp $(PWIZ_ROOT_PATH)/pwiz/data/identdata/Version.cpp : pwiz identdata : $(PWIZ_MAJOR) : $(PWIZ_MINOR) :
: *.?pp Jamfile.jam : Version.cpp
generate-version.cpp $(PWIZ_ROOT_PATH)/pwiz/data/tradata/Version.cpp : pwiz tradata : $(PWIZ_MAJOR) : $(PWIZ_MINOR) :
: *.?pp Jamfile.jam : Version.cpp
generate-version.cpp $(PWIZ_ROOT_PATH)/pwiz/data/proteome/Version.cpp : pwiz proteome : $(PWIZ_MAJOR) : $(PWIZ_MINOR) :
[ path.glob $(PWIZ_ROOT_PATH)/pwiz/data/proteome : *.?pp Jamfile.jam : Version.cpp ] ;
# TODO: collecting global revision info should use revision info that's already been collected;
# TODO: especially for things like SeeMS which have some MSVC-generated files that aren't versioned
[ generate-version.cpp $(PWIZ_ROOT_PATH)/pwiz/Version.cpp : pwiz : $(PWIZ_MAJOR) : $(PWIZ_MINOR) :
[ path.glob $(PWIZ_ROOT_PATH)/libraries : *.jam ]
: *.?pp *.h *.jam *.cs *.manifest* *.wxs.template
: tar.excluded Version.cpp Resources.Designer.cs Settings.Designer.cs *DataSet.Designer.cs AssemblyInfo.*
# revision-info is a sequence: <max revision> <max year> <max month> <max day> <number of modified files in working copy>
local year = $(revision-info[2]) ;
local month = $(revision-info[3]) ;
local day = $(revision-info[4]) ;
constant PWIZ_SVNREV : $(revision-info[1]) ;
constant PWIZ_SVNREVDATE : "(last committed change: $(year)-$(month)-$(day))" ;
if [ numbers.less 32000 $(PWIZ_SVNREV) ]
errors.error "out of range SVN revision $(PWIZ_SVNREV)." ;
version-tag = $(PWIZ_MAJOR) $(PWIZ_MINOR) $(PWIZ_SVNREV) ;
if $(revision-info[5]) > 0
version-tag += "modified" ;
echo NOTICE: WORKING COPY HAS $(revision-info[5]) MODIFIED FILES. ;
constant PWIZ_VERSION_TAG : $(version-tag:J=.) ;
echo ProteoWizard $(version-tag:J=.) $(PWIZ_SVNREVDATE:J=) $(PLATFORM) $(PROCESSOR_ARCHITECTURE) ;
# create a VERSION file which can be used by TC to parse the canonical pwiz version
make VERSION : : @make_VERSION : <location>$(PWIZ_BUILD_PATH) ;
actions make_VERSION { @($(STDOUT):E=$(version-tag:]=.)) > "$(<)" }
#actions make_VERSION { @($(STDOUT):E=$(version-tag:]=.)) > "$(<)" ; @($(STDOUT):E=<version>$(version-tag:J=.)</version>) > "$(PWIZ_BUILD_PATH)/VERSION.xml" }
if ! [ without-mz5 ]
tar.extract $(PWIZ_LIBRARIES_PATH)/hdf5-1.8.7.tar.bz2 : *.c* *.h* *.jam *.settings : <location>$(PWIZ_LIBRARIES_PATH) ;
path-constant BOOST_SOURCE : $(boost_src) ;
path-constant ZLIB_SOURCE : $(zlib_src) ;
path-constant GD_SOURCE : $(PWIZ_LIBRARIES_PATH)/libgd-2.1.0alpha ;
path-constant PNG_SOURCE : $(PWIZ_LIBRARIES_PATH)/libpng-1.5.6 ;
path-constant FREETYPE_SOURCE : $(PWIZ_LIBRARIES_PATH)/freetype-2.4.7 ;
path-constant EXPAT_SOURCE : $(PWIZ_LIBRARIES_PATH)/expat-2.0.1 ;
using ext-boost : $(BOOST_VERSION:J=.) : $(BOOST_SOURCE) : <zlib-src- location>$(ZLIB_SOURCE) ;
if [ modules.peek : NT ]
local args = [ modules.peek : ARGV ] ;
if ( ! --incremental in $(args) ) && ! [ without-binary-msdata ]
# extract the vendor APIs if the user agrees to the licenses
if --i-agree-to-the-vendor-licenses in $(args)
echo "Extracting vendor APIs..." ;
if ! --without-sciex in $(args) { SHELL "$(PWIZ_LIBRARIES_PATH)\\\7za.exe x -aoa -pi-agree-to-the-vendor-licenses -o$(PWIZ_ROOT_PATH)\\\pwiz_aux\\\msrc\\\utility $(PWIZ_ROOT_PATH)\\\pwiz_aux\\\msrc\\\utility\\\vendor_api_ABI.7z" ; }
if ! --without-agilent in $(args) { SHELL "$(PWIZ_LIBRARIES_PATH)\\\7za.exe x -aoa -pi-agree-to-the-vendor-licenses -o$(PWIZ_ROOT_PATH)\\\pwiz_aux\\\msrc\\\utility $(PWIZ_ROOT_PATH)\\\pwiz_aux\\\msrc\\\utility\\\vendor_api_Agilent.7z" ; }
if ! --without-bruker in $(args) { SHELL "$(PWIZ_LIBRARIES_PATH)\\\7za.exe x -aoa -pi-agree-to-the-vendor-licenses -o$(PWIZ_ROOT_PATH)\\\pwiz_aux\\\msrc\\\utility $(PWIZ_ROOT_PATH)\\\pwiz_aux\\\msrc\\\utility\\\vendor_api_Bruker.7z" ; }
if ! --without-shimadzu in $(args) { SHELL "$(PWIZ_LIBRARIES_PATH)\\\7za.exe x -aoa -pi-agree-to-the-vendor-licenses -o$(PWIZ_ROOT_PATH)\\\pwiz_aux\\\msrc\\\utility $(PWIZ_ROOT_PATH)\\\pwiz_aux\\\msrc\\\utility\\\vendor_api_Shimadzu.7z" ; }
if ! --without-thermo in $(args) { SHELL "$(PWIZ_LIBRARIES_PATH)\\\7za.exe x -aoa -pi-agree-to-the-vendor-licenses -o$(PWIZ_ROOT_PATH)\\\pwiz_aux\\\msrc\\\utility $(PWIZ_ROOT_PATH)\\\pwiz_aux\\\msrc\\\utility\\\vendor_api_Thermo.7z" ; }
#if ! --without-unifi in $(args) { SHELL "$(PWIZ_LIBRARIES_PATH)\\\7za.exe x -aoa -pi-agree-to-the-vendor-licenses -o$(PWIZ_ROOT_PATH)\\\pwiz_aux\\\msrc\\\utility $(PWIZ_ROOT_PATH)\\\pwiz_aux\\\msrc\\\utility\\\vendor_api_UNIFI.7z" ; }
if ! --without-waters in $(args) { SHELL "$(PWIZ_LIBRARIES_PATH)\\\7za.exe x -aoa -pi-agree-to-the-vendor-licenses -o$(PWIZ_ROOT_PATH)\\\pwiz_aux\\\msrc\\\utility $(PWIZ_ROOT_PATH)\\\pwiz_aux\\\msrc\\\utility\\\vendor_api_Waters.7z" ; }
echo "NOTICE: not extracting vendor APIs; use --i-agree-to-the-vendor-licenses to extract and use them." ;
# overwrite the original header files because of MSVC looking in the current header's path with #include "foo"
# HACK: bug in boost::interprocess (up to at least 1.55) requires a patch to support opening memory-mapped files with UTF-8 filenames
# Boost bug ticket: https://svn.boost.org/trac/boost/ticket/4335
#SHELL "@IF NOT EXIST $(BOOST_SOURCE)\\\boost\\\interprocess\\\detail\\\os_file_functions.hpp.bak rename $(BOOST_SOURCE)\\\boost\\\interprocess\\\detail\\\os_file_functions.hpp os_file_functions.hpp.bak" ;
SHELL "@IF NOT EXIST $(BOOST_SOURCE)\\\boost\\\interprocess\\\detail\\\win32_api.hpp.bak rename $(BOOST_SOURCE)\\\boost\\\interprocess\\\detail\\\win32_api.hpp win32_api.hpp.bak" ;
#SHELL "@copy /Y $(PWIZ_LIBRARIES_PATH)\\\boost_aux\\\boost\\\interprocess\\\d etail\\\os_file_functions.hpp $(BOOST_SOURCE)\\\boost\\\interprocess\\\detail" ;
SHELL "@copy /Y $(PWIZ_LIBRARIES_PATH)\\\boost_aux\\\boost\\\interprocess\\\de tail\\\win32_api.hpp $(BOOST_SOURCE)\\\boost\\\interprocess\\\detail" ;
rule project-exists ( project-path )
if [ path.exists $(project-path) ] &&
[ path.glob $(project-path) : [Jj]amroot.jam [Jj]amfile.jam [Jj]amroot [Jj]amfile ]
# to make subsetting the source tree much easier,
# use these rules to test that a sub-project path exists before building it
rule build-project-if-exists ( project-path )
local project = [ project.current ] ;
local p = [ path.native [ path.join [ $(project).location ] $(project-path) ] ] ;
if [ project-exists $(p) ]
local attributes = [ project.attributes [ $(project).name ] ] ;
local now = [ $(attributes).get projects-to-build ] ;
$(attributes).set projects-to-build : $(now) $(project-path) ;
rule run-if-exists ( sources + : args * : input-files * : requirements * : target-name ? : default-build * )
local project = [ project.current ] ;
local full-path = [ path.native [ path.join [ $(project).location ] $(project- path) $(sources[1]) ] ] ;
if [ path.exists $(full-path) ]
return [ run $(sources) : $(args) : $(input-files) : $(requirements) : $(target-name) : $(default-build) ] ;
rule run-fail-if-exists ( sources + : args * : input-files * : requirements * : target-name ? : default-build * )
local project = [ project.current ] ;
local full-path = [ path.native [ path.join [ $(project).location ] $(project- path) $(sources[1]) ] ] ;
if [ path.exists $(full-path) ]
return [ run-fail $(sources) : $(args) : $(input-files) : $(requirements) : $(target-name) : $(default-build) ] ;
rule unit-test-if-exists ( target : sources + : properties * )
local project = [ project.current ] ;
local full-path = [ path.native [ path.join [ $(project).location ] $(project- path) $(sources[1]) ] ] ;
if [ path.exists $(full-path) ]
return [ unit-test $(target) : $(sources) : $(properties) ] ;
rule doctest ( name : sources + : requirements * )
unit-test-if-exists $(name) : $(sources) : $(requirements) <define>PWIZ_DOCTEST <location-prefix>doctest ;
rule install-location ( properties * )
local toolsets = [ feature.get-values <toolset> : $(properties) ] ;
local variants = [ feature.get-values <variant> : $(properties) ] ;
local location = [ path.make $(PWIZ_BUILD_PATH)/$(toolsets[1])-$(variants[1]) ] ;
if <link>shared in $(properties) { location = $(location)-shared ; }
if <address-model>64 in $(properties) { location = $(location)-x86_64 ; }
rule install-type ( properties * )
local result = <install-type>EXE ;
if <link>shared in $(properties)
result += <install-dependencies>on <install-type>SHARED_LIB <install- type>MANIFEST ;
rule install-vendor-api-dependencies ( properties * )
properties = $(properties) [ vendor-api-support $(properties) ] ;
local location = [ feature.get-values <location> : $(properties) ] ;
if $(location) { location = [ string.join <location> [ path.make $(location[1]) ] ] ; }
location ?= [ install-location $(properties) ] ;
if <toolset>msvc in $(properties) && <link>static in $(properties) && ! [ without-binary-msdata ]
if [ path.exists pwiz_aux/msrc/utility/vendor_api/ABI ] { dependencies += <dep endency>$(PWIZ_ROOT_PATH)/pwiz_aux/msrc/utility/vendor_api/ABI//install_pwiz_v endor_api_abi_dlls/$(location) ; }
if [ path.exists pwiz_aux/msrc/utility/vendor_api/ABI ] { dependencies += <dep endency>$(PWIZ_ROOT_PATH)/pwiz_aux/msrc/utility/vendor_api/ABI//install_pwiz_v endor_api_abi_sqlite/$(location) ; }
if [ path.exists pwiz_aux/msrc/utility/vendor_api/ABI/T2D ] { dependencies +=
<dependency>$(PWIZ_ROOT_PATH)/pwiz_aux/msrc/utility/vendor_api/ABI/T2D//instal l_pwiz_vendor_api_abi_t2d/$(location) ; }
if [ path.exists pwiz_aux/msrc/utility/vendor_api/Agilent ] { dependencies +=
<dependency>$(PWIZ_ROOT_PATH)/pwiz_aux/msrc/utility/vendor_api/Agilent//instal l_pwiz_vendor_api_agilent/$(location) ; }
if [ path.exists pwiz_aux/msrc/utility/vendor_api/Bruker ] { dependencies += < dependency>$(PWIZ_ROOT_PATH)/pwiz_aux/msrc/utility/vendor_api/Bruker//install_ pwiz_vendor_api_bruker/$(location) ; }
if [ path.exists pwiz_aux/msrc/utility/vendor_api/Shimadzu ] { dependencies += <dependency>$(PWIZ_ROOT_PATH)/pwiz_aux/msrc/utility/vendor_api/Shimadzu//insta ll_pwiz_vendor_api_shimadzu/$(location) ; }
if [ path.exists pwiz_aux/msrc/utility/vendor_api/thermo ] { dependencies += < dependency>$(PWIZ_ROOT_PATH)/pwiz_aux/msrc/utility/vendor_api/thermo//install_ pwiz_vendor_api_thermo/$(location) ; }
if [ path.exists pwiz_aux/msrc/utility/vendor_api/UIMF ] { dependencies += <de pendency>$(PWIZ_ROOT_PATH)/pwiz_aux/msrc/utility/vendor_api/UIMF//install_pwiz _vendor_api_uimf/$(location) ; }
if [ path.exists pwiz_aux/msrc/utility/vendor_api/UNIFI ] { dependencies += <d ependency>$(PWIZ_ROOT_PATH)/pwiz_aux/msrc/utility/vendor_api/UNIFI//install_pw iz_vendor_api_unifi/$(location) ; }
if [ path.exists pwiz_aux/msrc/utility/vendor_api/Waters ] { dependencies += < dependency>$(PWIZ_ROOT_PATH)/pwiz_aux/msrc/utility/vendor_api/Waters//install_ pwiz_vendor_api_waters/$(location) ; }
if <vendor-api-support>on in $(properties) { dependencies += <dependency>$(PWI Z_ROOT_PATH)/pwiz_tools/prototype//ThermoRawMetaDumpInstall/$(location) ; }
rule install-identdata-dependencies ( properties * )
local location = [ feature.get-values <location> : $(properties) ] ;
if $(location) { location = [ string.join <location> [ path.make $(location[1]) ] ] ; }
location ?= [ install-location $(properties) ] ;
if [ path.exists pwiz/data/identdata ] { dependencies += <dependency>$(PWIZ_RO OT_PATH)/pwiz/data/identdata//install_pwiz_identdata/$(location) ; }
rule pwiz-bindings-dependency ( properties * )
if <toolset>msvc in $(properties)
local variants = [ feature.get-values <variant> : $(properties) ] ;
local location = <location>$(PWIZ_BUILD_PATH)/obj/$(PLATFORM)/$(variants[1]) ;
rule dotNET-dependencies ( properties * )
if <toolset-msvc:version>12.0 in $(properties)
local location = [ install-location $(properties) ] ;
rule gcc-install-dll-path ( properties * )
if <toolset>gcc in $(properties) && <link>shared in $(properties) && <target- os>linux in $(properties)
# convenient test targets
alias all-tests : pwiz pwiz_tools pwiz_aux ;
# for copying all libraries and headers to one dir each
alias libraries : install-pwiz-lib install-boost-headers ;
# default install location
local default-prefix = /usr/local ; # LINUX, MACOS
if [ modules.peek : NT ] { default-prefix = "C:\\\" ; }
# set the default option value to be used when building the lib tarball
option.set prefix : $(default-prefix) ;
local headers = [ path.glob-tree pwiz : *.h *.hpp : .svn ] ;
# move boost headers separately because install-source-root is different
local boost_headers = [ path.glob-tree $(BOOST_SOURCE)/boost : *.h *.hpp : .svn ] ;
# warning: _SECURE_SCL_THROWS is deprecated
# checked iterators throw instead of crash
rule secure-scl-throws ( properties * )
if <toolset>msvc in $(properties) &&
! ( <toolset-msvc:version>11.0 in $(properties) ) &&
! ( <toolset-msvc:version>12.0 in $(properties) )
# any GCC executable that uses shared libraries must have all its code built with -fPIC
rule static-with-fpic ( properties * )
if ( <toolset>gcc in $(properties) || <toolset>darwin in $(properties) ) &&
return <cflags>-fPIC <cxxflags>-fPIC <linkflags>-fPIC ;
# predicate for use as a <conditional> requirement of targets that must only build with MSVC
rule msvc-requirement ( properties * )
if ! <toolset>msvc in $(properties) { return <build>no ; }
# predicate for use as a <conditional> requirement of targets that must only build with MSVC and current .NET Framework
rule msvc-dotnet-requirement ( properties * )
# require VS 2013 because of .NET Framework version
if ! ( <toolset-msvc:version>12.0 in $(properties) )
{ return <build>no ; }
# predicate for use as a <conditional> requirement of targets that must only build with non-express version of MSVC
rule no-express-requirement ( properties * )
# only the latest, non-express version of MSVC
if ! <toolset-msvc:version>12.0 in $(properties) { return <build>no ; }
if 12.0express in $(properties:G=) { return <build>no ; }
# special support for MSFileReader on Windows
if [ modules.peek : NT ]
# can't build or run 64-bit version on Windows 32-bit OS
local ProgramFiles = [ os.environ ProgramFiles ] ;
local ProgramFilesX86 = [ os.environ "ProgramFiles(x86)" ] ;
ProgramFilesX86 = $(ProgramFilesX86:E=$(ProgramFiles)) ;
if ( [ MATCH (x64) : $(PLATFORM) ] )
# HACK: we can't just look at the PROCESSOR_ARCHITECTURE environment variable, because it is
# set to "x86" even on a 64-bit machine, probably because bjam is running in 32-bit mode
if ( ! $(ProgramFilesX86) && [ MATCH (x86) : $(ProgramFiles) ] ) # infer 64-bit machine from (x86) appended to ProgramFiles
EXIT "\n*** ERROR: It is not possible to build or run a 64-bit build on 32-bit Windows." ;
# MSFileReader install directory
constant ProgramFilesLibs : "C:\\\Program Files" ;
constant MSFILEREADER_SUFFIX : "_x64" ;
# MSFileReader install directory
constant ProgramFilesLibs : "$(ProgramFilesX86)" ;
constant MSFILEREADER_SUFFIX : "" ;
constant MSFILEREADER_INSTALL_DIR : "$(ProgramFilesLibs)\\\Thermo\\\MSFileReader" ;
} # if NT
# HACK: find location of WiffFileDataReader DLLs (it must be in Jamroot so both vendor_readers and vendor_api can use it)
rule wiff-dll-location ( api-path : properties * )
# .NET 4 DLLs should work for anything .NET 4 or greater (hopefully); there's no Boost.Build property for .NET version
local result = $(api-path) ;
if --i-agree-to-the-vendor-licenses in [ modules.peek : ARGV ] &&
[ path.exists $(result)\\\Clearcore2.Data.WiffReader.dll ]
rule unifi-dll-location ( api-path : properties * )
# .NET 4.5 DLLs should work for anything .NET 4 or greater (hopefully); there's no Boost.Build property for .NET version
local result = $(api-path) ;
if --i-agree-to-the-vendor-licenses in [ modules.peek : ARGV ] &&
[ path.exists $(result)\\\IdentityModel.dll ]
rule bruker-dll-location ( api-path : properties * )
if ( [ MATCH (x64) : $(PLATFORM) ] )
result = $(api-path)\\\x64 ;
result = $(api-path)\\\x86 ;
if --i-agree-to-the-vendor-licenses in [ modules.peek : ARGV ] &&
[ path.exists $(result)\\\CompassXtractMS.dll ]
rule shimadzu-dll-location ( api-path : properties * )
if ( [ MATCH (x64) : $(PLATFORM) ] )
result = $(api-path)\\\x64 ;
result = $(api-path)\\\x86 ;
if --i-agree-to-the-vendor-licenses in [ modules.peek : ARGV ] &&
[ path.exists $(result)\\\DataReader.dll ]
rule mhdac-dll-location ( api-path : properties * )
if ( [ MATCH (x64) : $(PLATFORM) ] )
result = $(api-path)\\\x64 ;
result = $(api-path)\\\x86 ;
if --i-agree-to-the-vendor-licenses in [ modules.peek : ARGV ] &&
[ path.exists $(result)\\\MassSpecDataReader.dll ]
rule uimf-dll-location ( api-path : properties * )
if <toolset-msvc:version>9.0 in $(properties) ||
else # VC10 DLLs should work for VC11 as well (it's dependent on .NET version)
if ( [ MATCH (x64) : $(PLATFORM) ] )
result = $(api-path)\\\x64 ;
result = $(api-path)\\\x86 ;
if --i-agree-to-the-vendor-licenses in [ modules.peek : ARGV ] &&
[ path.exists $(result)\\\UIMFLibrary.dll ]
rule masslynxraw-dll-location ( api-path : properties * )
if <toolset>msvc in $(properties) &&
if <toolset-msvc:version>12.0 in $(properties) ||
if ( [ MATCH (x64) : $(PLATFORM) ] )
result = $(api-path)\\\vc12_x64 ;
result = $(api-path)\\\vc12_x86 ;
# else we don't have DLLs for this MSVC version (it's dependent on CRT version)
if --i-agree-to-the-vendor-licenses in [ modules.peek : ARGV ] &&
[ path.exists $(result)\\\MassLynxRaw.dll ]
rule msparser-path ( properties * )
# Assign the most likely msparser library path
local msparser_path_arg = [ MATCH --msparser-path=(.*) : [ modules.peek : ARGV ] ] ;
lib-location = $(msparser_path_arg) ;
else if <toolset>msvc in $(properties)
if [ feature.get-values <toolset-msvc:version> : $(properties) ] in "9.0" "9.0express"
lib-location = "$(ProgramFilesLibs)\\\Matrix Science\\\Mascot Parser\\\vs2008" ;
else if [ feature.get-values <toolset-msvc:version> : $(properties) ] in "10.0" "10.0express"
lib-location = "$(ProgramFilesLibs)\\\Matrix Science\\\Mascot Parser\\\vs2010" ;
else if [ feature.get-values <toolset-msvc:version> : $(properties) ] in "11.0" "11.0express"
lib-location = "$(ProgramFilesLibs)\\\Matrix Science\\\Mascot Parser\\\vs2012" ;
else if [ feature.get-values <toolset-msvc:version> : $(properties) ] in "12.0" "12.0express"
lib-location = "$(ProgramFilesLibs)\\\Matrix Science\\\Mascot Parser\\\vs2013" ;
.warn-once = true ;
echo "Warning: Not using Mascot Parser due to unsupported version of MSVC." ;
lib-location = "" ;
else if <toolset>gcc in $(properties)
lib-location = "/usr/local/msparser/gnu" ;
.warn-once = true ;
echo "Note: Not using Mascot Parser due to unsupported compiler." ;
lib-location = "" ;
if [ without-binary-msdata ]
.warn-once = true ;
echo "Note: Not using Mascot Parser due to --without-binary-msdata ." ;
# Check for msparser existence.
else if <toolset>msvc in $(properties) && [ path.exists $(lib- location)/lib/msparser.lib ]
.warn-once = true ;
echo "Using Mascot Parser in $(lib-location)" ;
else if <toolset>gcc in $(properties) && [ path.exists $(lib- location)/lib/libmsparser.a ]
.warn-once = true ;
echo "Using Mascot Parser in $(lib-location)" ;
else if ! $(.warn-once)
.warn-once = true ;
echo "Warning: No Mascot Parser found at $(lib-location)." ;
echo "Warning: No Mascot Parser found." ;
echo " Mascot support will be disabled." ;
rule msparser-requirements ( properties * )
local msparser_path = [ msparser-path $(properties) ] ;
local result = <search>$(msparser_path)/lib ;
if <toolset>msvc in $(properties)
if <runtime-debugging>on in $(properties)
result += <name>msparserD ;
return $(result) [ msparser-usage-requirements $(properties) ] ;
rule msparser-usage-requirements ( properties * )
local msparser_path = [ msparser-path $(properties) ] ;
local result = <include>$(msparser_path)/include ;
if <toolset>msvc in $(properties)
result += <assembly-dependency>$(msparser_path)/../config/unimod_2.xsd <assembly-dependency>$(msparser_path)/../config/quantitation_1.xsd <assembly- dependency>$(msparser_path)/../config/quantitation_2.xsd ;
if <runtime-debugging>on in $(properties)
result += <assembly-dependency>$(msparser_path)/lib/msparserD.dll ;
result += <assembly-dependency>$(msparser_path)/lib/msparser.dll ;
searched-lib msparser : : <conditional>@msparser-requirements : : <conditional>@msparser-usage-requirements ;
# any source tree can build binary tarballs
.common-location = $(PWIZ_BUILD_PATH) ;
rule binary-tarball-requirements ( properties * )
local toolsets = [ feature.get-values <toolset> : $(properties) ] ;
local variants = [ feature.get-values <variant> : $(properties) ] ;
local location = [ install-location $(properties) ] ;
location = $(location:G=) ;
local non-redistributables = pwiz_bindings_cli.xml ; # .NET documentation
if $(variants[1]) = "release"
non-redistributables += *.pdb ; # MSVC debug symbols
non-redistributables = [ sequence.join $(non-redistributables) : "&&exclude:" ] ;
local result = <tar-source>path-anchor:$(location)&&exclude:$(non- redistributables)&&$(location) ;
if ! <architecture> in $(properties:G)
if $(.platform:L) = "x86_64" && <address-model>32 in $(properties) { properties += <architecture>x86 ; }
else if $(.platform:L) = "x86" && <address-model>64 in $(properties) { properties += <architecture>x86_64 ; }
else { properties += <architecture>$(.platform:L) ; }
if <link>shared in $(properties) { linkage = "-shared" ; }
local name = [ common.format-name <base> <property:target-os> <property:architecture> <toolset> <property:variant> $(linkage) -$(version- tag:J=_)
: pwiz-bin : TBZ2 : [ property-set.create $(properties) ] ] ;
result += <name>$(name) <dependency>executables <location>$(.common-location) <dependency>VERSION ;
: # sources are handled by the conditional
rule library-tarball-requirements ( properties * )
local toolsets = [ feature.get-values <toolset> : $(properties) ] ;
local variants = [ feature.get-values <variant> : $(properties) ] ;
# require that the location come from --prefix or default; do not allow --libdir or --includedir
if [ MATCH --libdir=(.*) : [ modules.peek : ARGV ] ] ||
[ MATCH --includedir=(.*) : [ modules.peek : ARGV ] ]
echo "--libdir and --includedir are not supported for pwiz-lib.tar.bz2; use --prefix instead" ;
local prefix = [ option.get prefix ] ;
local location = $(prefix:G=) ;
# no more redistributables!
#non-redistributables = [ sequence.join $(non-redistributables) : "&&exclude:" ] ;
#local result = <tar-source>path-anchor:$(location)&&exclude:$(non- redistributables)&&$(location) ;
local result = <tar-source>path-anchor:$(location)&&$(location) ;
if ! <architecture> in $(properties:G)
if $(.platform:L) = "x86_64" && <address-model>32 in $(properties) { properties += <architecture>x86 ; }
else if $(.platform:L) = "x86" && <address-model>64 in $(properties) { properties += <architecture>x86_64 ; }
else { properties += <architecture>$(.platform:L) ; }
if <link>shared in $(properties) { linkage = "-shared" ; }
local name = [ common.format-name <base> <property:target-os> <property:architecture> <toolset> <property:variant> $(linkage) -$(version- tag:J=_)
: pwiz-lib : TBZ2 : [ property-set.create $(properties) ] ] ;
result += <name>$(name) <dependency>libraries <location>$(.common-location) <dependency>VERSION ;
: # sources are handled by the conditional
# full source trees automatically build source tarballs
if ! [ path.exists $(PWIZ_ROOT_PATH)/SUBSET ]
using bcp : $(BOOST_SOURCE) : $(.common-location)/bcp ;
path-constant BOOST_SUBSET_PATH : $(.common-location)/boost-subset ;
# scan all source files for boost dependencies
[ path.glob-tree $(PWIZ_ROOT_PATH)/pwiz : *.cpp *.hpp ]
[ path.glob-tree $(PWIZ_ROOT_PATH)/pwiz_aux : *.cpp *.hpp ]
[ path.glob-tree $(PWIZ_ROOT_PATH)/pwiz_tools : *.cpp *.hpp *.h ]
[ path.glob-tree $(PWIZ_LIBRARIES_PATH)/boost_aux : *.cpp *.hpp ]
[ path.glob-tree $(PWIZ_LIBRARIES_PATH)/SQLite : *.cpp *.h ]
[ mz5-build $(PWIZ_LIBRARIES_PATH)/hdf5-1.8.7/src/init_once_workaround.cpp ]
# scan all targets and their dependencies
exclude:example_data/small* # large files in example_data
exclude:bootstrap exclude:bin.* # boost-build intermediate directories
exclude:bin exclude:obj exclude:TestResults # C#.NET intermediate directories
exclude:_ReSharper.* # ReSharper directory for C# projects
exclude:*.ncb exclude:*.suo exclude:*.user exclude:*.p12 # More visual studio files
exclude:*.xdc # .NET XML documentation sources
exclude:tar.excluded # a place to put any files in these directories that shouldn't be tarballed
# the SUBSET file acts as flag so that building a subset tarball doesn't build a source tarball
make SUBSET : : @make_SUBSET : <location>$(.common-location) ;
This source tree is a subset of the full pwiz source tree.
[ path.glob $(PWIZ_LIBRARIES_PATH) : *.bat *.sh *.h *.jam *.dll *.lib *.exe *.cpp libgd*.tar.bz2 libpng*.tar.bz2 freetype*.tar.bz2 zlib*.tar.bz2 hdf5*.tar.bz2 ]
# include the bcp'd boost tarball as if it was really located at "libraries/boost_*.tar.bz2"
exclude:*.pdf # pwiz posters in /doc
.common-requirements = <location>$(.common-location) <dependency>boost_$(BOOST_VERSION:J=_).tar.bz2 <dependency>SUBSET <dependency>VERSION ;
# l = without libraries, t = without tests, v = without vendor APIs
tar.create pwiz-src.tar.bz2 : $(.common-sources) $(.l) : $(.common- requirements) <name>pwiz-src-$(version-tag:J=_).tar.bz2 ;
tar.create pwiz-src-without-l.tar.bz2 : $(.common-sources) : $(.common- requirements) <name>pwiz-src-without-l-$(version-tag:J=_).tar.bz2 ;
tar.create pwiz-src-without-lt.tar.bz2 : $(.no-t) $(.common-sources) : $(.common-requirements) <name>pwiz-src-without-lt-$(version-tag:J=_).tar.bz2 ;
tar.create pwiz-src-without-ltv.tar.bz2 : $(.no-t) $(.no-v) $(.common-sources) : $(.common-requirements) <name>pwiz-src-without-ltv-$(version- tag:J=_).tar.bz2 ;
tar.create pwiz-src-without-lv.tar.bz2 : $(.no-v) $(.common-sources) : $(.common-requirements) <name>pwiz-src-without-lv-$(version-tag:J=_).tar.bz2 ;
tar.create pwiz-src-without-t.tar.bz2 : $(.no-t) $(.common-sources) $(.l) : $(.common-requirements) <name>pwiz-src-without-t-$(version-tag:J=_).tar.bz2 ;
tar.create pwiz-src-without-tv.tar.bz2 : $(.no-t) $(.no-v) $(.common-sources) $(.l) : $(.common-requirements) <name>pwiz-src-without-tv-$(version- tag:J=_).tar.bz2 ;
tar.create pwiz-src-without-v.tar.bz2 : $(.no-v) $(.common-sources) $(.l) : $(.common-requirements) <name>pwiz-src-without-v-$(version-tag:J=_).tar.bz2 ;
} # if SUBSET
* View git blame
* Reference in new issue
* © 2019 GitHub, Inc.
You can’t perform that action at this time.
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session.