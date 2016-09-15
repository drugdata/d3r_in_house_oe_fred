jeffs_fred_implementation
=========================

.. image:: https://img.shields.io/pypi/v/jeffs_fred_implementation.svg
    :target: https://pypi.python.org/pypi/jeffs_fred_implementation
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/cookiecutter/cookiecutter-pycustomdock.png
   :target: https://travis-ci.org/cookiecutter/cookiecutter-pycustomdock
   :alt: Latest Travis CI build status

Jeff's test of CELPPade by implementing a minimal version of Openeye FRED docking

Usage
-----

Installation
------------

** Here I implement oedock and omegaprep using cookiecutter **

#Get a miniconda

wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh

bash Miniconda2-latest-Linux-x86_64.sh -b -p miniconda2

# turn on the root environment

source miniconda2/bin/activate

conda update --yes conda

#Manually install rdkit

conda install -y -c rdkit rdkit=2016.03.3



#Install most current d3r jeffdev

git clone git@github.com:drugdata/D3R.git

cd D3R

git branch jeffdev

git pull origin jeffdev

make dist

cd dist

pip install d3r-1.5.0-py2.py3-none-any.whl

cd ../

cd ../


#Get cookiecutter

pip install cookiecutter

cookiecutter https://github.com/drugdata/cookiecutter-pycustomdock.git

## (Follow prompts) ##

### (Implement prep and docking functions here) ###

#Test functions

Go into test_data 

. test.sh

Note: Evaluation fails because miniconda doesn’t see openeye.oechem 



### Yay! Tests work ###



## Upload onto new github repo

#(Go on github, make new repo called "drugdata/jeffs_fred_implementation"

#(cd into top level dir)

git init

#(REMOVE BULKY TEST DATA) 

rm -r test_data/?-*

git add ./*

git add .gitignore 

git commit -a -m “first commit”

git remote add origin git@github.com:drugdata/jeffs_fred_implementation.git


git push -u origin master




Requirements
^^^^^^^^^^^^

Compatibility
-------------

Licence
-------

Authors
-------

`jeffs_fred_implementation` was written by `Jeff Wagner <j5wagner@ucsd.edu>`_.
