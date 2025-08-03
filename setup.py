from setuptools import setup, Extension
import sysconfig


# module1 = Extension('helloworld', sources=['c-algorithms/python_extending.c'])
# module2 = Extension('scramble', sources=['c-algorithms/scramble.c', "c-algorithms/moves.c"])
# module3 = Extension('moves_py', sources=['c-algorithms/moves_py.c', 'c-algorithms/moves.c'])
# module4 = Extension('f2l', sources=['c-algorithms/f2l.c', 'c-algorithms/moves.c'])
# module5 = Extension('cube_upgrade', sources=['c-algorithms/cube_upgrade/cube-upgrade.c', 'c-algorithms/cube_upgrade/moves.c'])
# module6 = Extension('moves_upgrade_py', sources=['c-algorithms/cube_upgrade/moves_upgrade_py.c', 'c-algorithms/cube_upgrade/moves.c'])
# module7 = Extension('python_extension_test', sources=['c-algorithms/cube_upgrade/python_extension_test.c'])
module8 = Extension("cube_solver", sources=["cube_solver_wrapper.c", "dfs_concept.c"], extra_compile_args=["-O3"])
# module = Extension('test', sources=['test.c'])

setup(
    name='cross_find_c',
    version='1.0',
    description='Example C extension',
    ext_modules=[module8],
)
