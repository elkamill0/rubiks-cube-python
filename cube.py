from cross import Cross
import scramble
import f2l
import cube_upgrade


class Cube(Cross):
    def __init__(self, moves: str = None):
        if moves:
            self.cube = scramble.init(list(map(lambda move: self.convert_moves_to_numbers().get(move), moves.split())))
        else:
            self.cube = scramble.init()

    def print_cube(self):
        scramble.print_cube_py(self.cube)

    def reset(self):
        self.cube = scramble.init()

    def sequence(self, moves):
        scramble.sequence(list(map(lambda move: self.convert_moves_to_numbers().get(move), moves.split())), self.cube)

    def f2l(self, length):
        return f2l.check_f2l_pair(length, self.cube)