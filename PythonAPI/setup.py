import os
from setuptools import setup, Extension
import numpy as np

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"
common_dir = None

if os.path.exists("common"):
    if not os.path.islink("common"):
        common_dir = "common"

if not common_dir:
    common_dir = "../common"

maskApi_path = os.path.realpath(os.path.join(common_dir, "maskApi.c"))

ext_modules = [
    Extension(
        'pycocotools._mask',
        sources=[maskApi_path, 'pycocotools/_mask.pyx'],
        include_dirs = [np.get_include(), common_dir],
        extra_compile_args=['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    )
]

setup(
    name='pycocotools',
    packages=['pycocotools'],
    package_dir = {'pycocotools': 'pycocotools'},
    install_requires=[
        'setuptools>=18.0',
        'cython>=0.27.3',
        'matplotlib>=2.1.0'
    ],
    version='2.0',
    ext_modules= ext_modules
)
