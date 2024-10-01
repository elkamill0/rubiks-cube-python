from setuptools import setup, Extension

module1 = Extension('helloworld', sources=['c-algorithms/python_extending.c'])
module2 = Extension('scramble', sources=['c-algorithms/scramble.c', "c-algorithms/moves.c"])
module3 = Extension('moves_py', sources=['c-algorithms/moves_py.c', 'c-algorithms/moves.c'])
module4 = Extension('f2l', sources=['c-algorithms/f2l.c', 'c-algorithms/moves.c'])
module5 = Extension('cube_upgrade', sources=['c-algorithms/cube_upgrade/cube-upgrade.c', 'c-algorithms/cube_upgrade/moves.c'])
module6 = Extension('moves_upgrade_py', sources=['c-algorithms/cube_upgrade/moves_upgrade_py.c', 'c-algorithms/cube_upgrade/moves.c'])
# module7 = Extension('python_extension_test', sources=['c-algorithms/cube_upgrade/python_extension_test.c'])
setup(
    name='HelloWorld',
    version='1.0',
    description='Python Package with Hello World C Extension',
    ext_modules=[module2, module3, module4, module5, module6]
)