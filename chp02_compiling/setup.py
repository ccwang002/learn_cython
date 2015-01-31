# from distutils.core import setup
from setuptools import setup, Extension
from Cython.Build import cythonize

exts = [
    # C code self-contained
    Extension(
        name="fib",
        sources=['fib.pyx'],
    ),
    # statically link to lib/cfib.c
    Extension(
        name="wrap_fib",
        sources=["lib/cfib.c", "wrap_fib.pyx"],
        include_dirs=['.'],
    ),
    # dynamically link to lib/libcfib.so
    # setup steps:
    #   1. build the libcfib
    #       clang -Wall -c cfib.c
    #       clang -shared -undefined dynamic_lookup
    #           -I../ -o ../libcfib.so cfib.o
    #   2. build cython extension and link to libcfib
    #       setup.py build --inplace
    # note:
    #   1. if putting libcfib in ./lib, LD_LIBRARY_PATH have to be set
    #      before running Python.
    #      Ref http://stackoverflow.com/questions/856116
    Extension(
        name="wrap_fib_ext",
        sources=["wrap_fib_ext.pyx"],   # cfib.c is excluded
        library_dirs=["."],
        libraries=["cfib"]
    ),
]

setup(ext_modules=cythonize(exts))
