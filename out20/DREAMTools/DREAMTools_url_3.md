<-- https://github.com/dreamtools/dreamtools/blob/master/setup.py-->

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
executable file 120 lines (99 sloc)  4.09 KB
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from Cython.Build import cythonize
print("DREAMTools installation:: **cython** package not found")
print("You can try to install it using **pip** as follows::")
print(" pip install cython")
# On travis, Cython compilation hangs forever.
# We will skip the D8C1 tests where cython is required.
# On travis, we create a variable called __TRAVIS_DREAMTOOLS
# ext_modules = []
version = '%d.%d.%d' % (_MAJOR, _MINOR, _MICRO)
release = '%d.%d' % (_MAJOR, _MINOR)
'description':'Scoring functions for the DREAM / SAGE challenges' ,
'platforms' : ['Linux', 'Unix', 'MacOsX', 'Windows'],
'keywords' : ['DREAM challenges', 'DREAM', 'System Biology',
'Leaderboard', 'ROC', 'scoring', 'synapse','statistics' ],
'Development Status :: 5 - Production/Stable',
'Intended Audience :: Developers',
'Intended Audience :: Science/Research',
'License :: OSI Approved :: BSD License',
'Operating System :: OS Independent',
'Programming Language :: Python :: 2.7',
'Topic :: Software Development :: Libraries :: Python Modules',
'Topic :: Scientific/Engineering :: Bio-Informatics',
'Topic :: Scientific/Engineering :: Information Analysis',
'Topic :: Scientific/Engineering :: Mathematics',
'Topic :: Scientific/Engineering :: Physics']
with open('README.rst') as f:
# exclude test (somehow prevent conda recipes to work properly since test is
# considered as an independent package)
packages = [this for this in packages if this.startswith('test') is False]
# (you can provide an exclusion dictionary named exclude_package_data to
# remove parasites). alternatively to global inclusion, list the file
'' : ['*.pl', '*.txt', '*xls', '*.pyx', '*.so', '*.zip', '*.csv',
install_requires = ['cython', 'numpy', 'matplotlib', 'pandas',
'easydev>=0.9.11', 'fitter', 'synapseclient>=1.5', 'tabulate', 'scipy',
#using cythonize command gets the compiled cython code into the .egg
* View git blame
* Reference in new issue
* © 2019 GitHub, Inc.
You can’t perform that action at this time.
You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session.