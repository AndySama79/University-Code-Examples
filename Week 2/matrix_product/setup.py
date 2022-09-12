from distutils.core import Extension, setup
from Cython.Build import cythonize

ext = Extension(name="my_algo_c", sources=["my_algo.pyx"])
setup(ext_modules=cythonize(ext))