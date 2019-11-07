<-- https://github.com/mzdb/pwiz-mzdb/blob/master/quickbuild.sh-->

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
40 lines (35 sloc)  1.15 KB
# script for getting bjam and ProteoWizard up and running
# Get the location of quickbuild.sh and drop trailing slash
if [ ! -e $PWIZ_ROOT/quickbuild.sh ]; then
echo "quickbuild.sh must be run from the directory it resides in - quitting"
# per platform in case of multi OS shared volume (VMware etc)
# Build local copy of bjam
if [ ! -e $PWIZ_BJAM ]; then
cp -f $BOOST_BUILD_PATH/src/engine/bin/bjam $PWIZ_BJAM
#if $(hash setarch > /dev/null 2>&1); then
# ADDRESS_MODEL=$(expr "$*" : '.*address-model=\\([36][24]\\).*');
# if [ $ADDRESS_MODEL ]; then
# Do full build of ProteoWizard, passing quickbuild's arguments to bjam
if ! BOOST_BUILD_PATH=$BOOST_BUILD_PATH $PWIZ_BJAM "$@"; then
echo "At least one pwiz target failed to build."
* View git blame
* Reference in new issue
* © 2019 GitHub, Inc.
You can’t perform that action at this time.
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session.