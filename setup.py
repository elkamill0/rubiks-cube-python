from setuptools import setup, Extension

module1 = Extension('helloworld', sources=['c-algorithms/python_extending.c'])
module2 = Extension('scramble', sources=['c-algorithms/scramble.c', "c-algorithms/moves.c"])
module3 = Extension('moves_py', sources=['c-algorithms/moves_py.c', 'c-algorithms/moves.c'])
module4 = Extension('f2l', sources=['c-algorithms/f2l.c', 'c-algorithms/moves.c'])
setup(
    name='HelloWorld',
    version='1.0',
    description='Python Package with Hello World C Extension',
    ext_modules=[module2, module3, module4]
)