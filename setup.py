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


# monkey-patch for parallel compilation
# See: https://stackoverflow.com/a/13176803
def parallelCCompile(self,
                     sources,
                     output_dir=None,
                     macros=None,
                     include_dirs=None,
                     debug=0,
                     extra_preargs=None,
                     extra_postargs=None,
                     depends=None):
    # those lines are copied from distutils.ccompiler.CCompiler directly
    macros, objects, extra_postargs, pp_opts, build = self._setup_compile(
        output_dir, macros, include_dirs, sources, depends, extra_postargs)
    cc_args = self._get_cc_args(pp_opts, debug, extra_preargs)

    # parallel code
    def _single_compile(obj):
        try:
            src, ext = build[obj]
        except KeyError:
            return
        self._compile(obj, src, ext, cc_args, extra_postargs, pp_opts)

    # convert to list, imap is evaluated on-demand
    thread_pool = multiprocessing.pool.ThreadPool(args[0].num_processes)
    list(thread_pool.imap(_single_compile, objects))
    return objects

# hack compile to support parallel compiling
distutils.ccompiler.CCompiler.compile = parallelCCompile

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
            'ThreadPool',
            'java/jdk1.8.0_171_x64/include/',
            'java/jdk1.8.0_171_x64/include/linux/'    
        ],
        #library_dirs=['java/jdk-10.0.1/lib/server'],
        library_dirs=['java/jdk1.8.0_171_x64/jre/lib/amd64/server'],
        libraries=LIBS,
        extra_compile_args=ARGS)
]

setup(
    name='gfg',
    version='1.1',
    description="""gfg""",
    ext_modules=decoders_module,
    py_modules=['gfg'], )