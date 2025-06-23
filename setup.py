from setuptools import setup, Extension
import numpy
import sysconfig

module = Extension(
    'mymodule',
    sources=['mymodule.c'],
    include_dirs=[
        numpy.get_include(),
        sysconfig.get_path('include')
    ],
)

module1 = Extension(
    'cross_c',
    sources=['cross.c'],
    include_dirs=[
        numpy.get_include(),
        sysconfig.get_path('include')
    ],

)

setup(
    name='mymodule',
    version='1.0',
    ext_modules=[module, module1],
)
