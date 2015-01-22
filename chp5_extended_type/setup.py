from setuptools import setup, Extension
from Cython.Build import cythonize

exts = [
    Extension(name="inheritance", sources=['inheritance.pyx']),
    Extension(name="iteration", sources=['iteration.pyx'])
]

setup(ext_modules=cythonize(exts))
