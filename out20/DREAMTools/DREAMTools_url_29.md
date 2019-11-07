<-- https://github.com/dreamtools/dreamtools/tree/master/docker-->

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
Create new file  Find file  History
Cannot retrieve the latest commit at this time.
Type Name Latest commit message Commit time
Failed to load latest commit information.
Docker will not be supported. We now provide a bioconda pre-compiled verison.
In principle, you should be able to install **DREAMTools** without problems using **pip** tool. However, we provide here a docker image http://www.docker.io that may be use to try **DREAMTools**. This provides a FEDORA/Linux docker.
To build an image with docker, go into the docker directory and build the image:
sudo docker  build  -t="dreamtools_test" .
This will take about 10-15 minutes to finish depending on your connection.
In brief, the command above download a fedora distribution and installs all dependencies (e.g., numpy) and dreamtools 0.10.5.
Then, start the docker:
sudo docker run -i -t -entrypoint='/bin/bash' dreamtools_test -i
This will start a docker and provides a Linux shell. There, type:
Inside the IPython shell, you can try **DREAMTools** directly:
from dreamtools import *
s.Ntf = 2 # to speed up the test
We also provide a Docker for ubuntu (See Dockerfile_ubuntu and dreamtools_install_ubuntu.sh).
* © 2019 GitHub, Inc.
You can’t perform that action at this time.
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session.