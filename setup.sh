#!/bin/bash
# A simple script

#swig -python gfg.i

#g++ -std=c++11 -c -fpic -I/home/user/genv/local/include/python2.7 -I java/jdk-10.0.1/include/ -I java/jdk-10.0.1/include/linux/ -L java/jdk-10.0.1/lib/server  gfg_wrap.c gfg.cpp -ljvm


#g++ -shared gfg.o gfg_wrap.o -o _gfg.so


#swig -python -c++ gfg.i
#c++ -c -fpic gfg.cpp -I/home/user/genv/local/include/python2.7 -I java/jdk-10.0.1/include/ -I java/jdk-10.0.1/include/linux/ -L java/jdk-10.0.1/lib/server -ljvm
#c++ -shared gfg.o -o _gfg.so 


if [ ! -d ThreadPool ]; then
    git clone https://github.com/progschj/ThreadPool.git
    echo -e "\n"
fi


echo "Install decoders ..."
python setup.py install --num_processes 4

