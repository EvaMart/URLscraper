<-- https://github.com/dreamtools/dreamtools/blob/master/.travis.yml-->

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
58 lines (49 sloc)  1.85 KB
\- wget http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh -O miniconda.sh
\- chmod +x miniconda.sh
\- conda update --yes conda
# are not specific to using mini
# \- sudo rm -rf /dev/shm
# \- sudo ln -s /run/shm /dev/shm
# This help testing code with pylab
\- "sh -e /etc/init.d/xvfb start"
\- 'if [ "${TRAVIS_PULL_REQUEST}" = "false" ]; then openssl aes-256-cbc -K $encrypted_key -iv $encrypted_iv -in test.synapseConfig.enc -out test.synapseConfig -d; mv test.synapseConfig ~/.synapseConfig; fi'
# sometimes cython compilation of the cython files takes forever
# here we install cython with specific options
#\- pip install --install-option="--no-cython-compile" cython --upgrade
\- conda install --yes python=$TRAVIS_PYTHON_VERSION numpy scipy matplotlib nose pandas coverage scikit-learn numexpr xlrd cython
# coverage packages are elsewhere
#\- conda install --yes -c python-coveralls nose-cov
\- pip install nose easydev --upgrade
\- pip install coveralls -v
\- pip install biokit fitter -v
\- pip install tabulate -v
\- pip install git+https://git@github.com/cokelaer/synapsePythonClient.git@v1. 4.0_py3_dreamtools#egg=synapsePythonClient -v
# # command to run tests, e.g. python setup.py test
\- python setup.py nosetests --with-coverage --cover-package dreamtools
* View git blame
* Reference in new issue
* © 2019 GitHub, Inc.
You can’t perform that action at this time.
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session.