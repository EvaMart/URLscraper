<-- https://github.com/dreamtools/dreamtools/blob/master/notes.txt-->

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
33 lines (20 sloc)  1.08 KB
To test dreamtools/synapseclient on travis, we must provide a login/password.
Of course, it cannot be added in the repository. Instead, we will provide an
encoded version (test.synapseConfig.enc). On travis side, a hidden environment
variable will contain the key to decode that file.
We need to create the file test.synapseConfig.enc ; Starting from the input file
Let assume the input file is called test.synapseConfig, then type::
openssl aes-256-cbc -in test.synapseConfig -out test.synapseConfig.enc -p -nosalt
You will need to enter a password, which is the encrypted file. Keep the
The -nosalt option seems recommended. http://security.stackexchange.com/questions/29106/openssl-recover-key-and-iv- by-passphrase
The -p option will print information (key + iv) These should be keep for
82E85ADBAA6C87CF8058C7A7B31C99FD -in test.synapseConfig.enc -d -out test.dec
* View git blame
* Reference in new issue
* © 2019 GitHub, Inc.
You can’t perform that action at this time.
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session.