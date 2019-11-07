<-- https://github.com/dreamtools/dreamtools/blob/master/build_manifest.py-->

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
Code Issues 8 Pull requests 1 Projects 0 Security Pulse
### Join GitHub today
GitHub is home to over 40 million developers working together to host and review code, manage projects, and build software together.
Find file  Copy path
Find file  Copy path
Cannot retrieve contributors at this time
40 lines (26 sloc)  1.01 KB
directories = glob.glob('dreamtools' + os.sep + 'dream*')
for directory in directories:
sub_directories = glob.glob(directory + os.sep + 'D*')
if len(sub_directories) == 0:
for that in sub_directories:
contents = glob.glob(that + '/' + '*')
for this in contents:
if this.endswith('data') or this.endswith('goldstandard') or this.endswith('templates'):
if len(glob.glob(this + os.sep + '*'))>0:
print("recursive-include %s *" % this)
recursive-include dreamtools/dream8/D8C1/data *.csv *.json *dat
# exclude D7C2, D6C1
* View git blame
* Reference in new issue
* © 2019 GitHub, Inc.
You can’t perform that action at this time.
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session.