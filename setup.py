from setuptools import setup, Extension, find_packages
import sysconfig


module8 = Extension(
    "cube_solver",
    sources=["dfs_concept_wrapper.c", "dfs_concept.c"],
    extra_compile_args=["-O3"],
)

setup(
    name="cross_find_c",
    version="1.0",
    description="Example C extension",
    ext_modules=[module8],
    packages=[],
)
