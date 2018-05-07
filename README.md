# swig_wrapper
A sample code to use JAVA, PYTHON, and C++ together using swig

- Install SWIG: sudo apt-get install swig

- Download [JAVA](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

- Update JAVA JDK location in setup.py at line numbers 75,76,79

- set export LD_LIBRARY_PATH='(JAVA JDK location)/jre/lib/amd64/server'

- Run: sh setup.sh

- Run: python test.py
