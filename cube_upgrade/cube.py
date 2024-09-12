import cube_upgrade
import time
import moves_upgrade_py
from cross import Cross

class Cube(Cross):
    def __init__(self, moves: str = None):
        if moves:
            self.cube = cube_upgrade.init(list(map(lambda move: self.convert_moves_to_numbers().get(move), moves.split())))
        else:
            self.cube = cube_upgrade.init()

    def print_cube(self):
        cube_upgrade.print_cube(self.cube)

    def reset(self):
        self.cube = cube_upgrade.init()

    def sequence(self, moves):
        cube_upgrade.sequence(list(map(lambda move: self.convert_moves_to_numbers().get(move), moves.split())), self.cube)

    # def f2l(self, length):
    #     return f2l.check_f2l_pair(length, self.cube)
