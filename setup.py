"""Script to build and install decoder package."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import setup, Extension, distutils
import glob
import platform
import os, sys
import multiprocessing.pool
import argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    "--num_processes",
    default=1,
    type=int,
    help="Number of cpu processes to build package. (default: %(default)d)")
args = parser.parse_known_args()

# reconstruct sys.argv to pass to setup below
sys.argv = [sys.argv[0]] + args[1]




LIBS = ['stdc++', 'jvm']
if platform.system() != 'Darwin':
    LIBS.append('rt')

ARGS = ['-std=c++11']

os.system('swig -python -c++ ./gfg.i')

decoders_module = [
    Extension(
        name='_gfg',
        sources=glob.glob('*.cxx') + glob.glob('*.cpp'),
        language='c++',
        include_dirs=[
            '.',
            'java/jdk-10.0.1/include/',
            'java/jdk-10.0.1/include/linux/'    
        ],
        library_dirs=['java/jdk-10.0.1/lib/server'],
        libraries=LIBS,
        extra_compile_args=ARGS)
]

setup(
    name='gfg',
    version='1.1',
    description="""gfg""",
    ext_modules=decoders_module,
    py_modules=['gfg'], )