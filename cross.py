import copy

from moves import Moves
import itertools
import time


class Cross(Moves):
    def __init__(self, cube):
        super().__init__(cube)
        self.cube_backup = copy.deepcopy(self.cube)

    def cross_validation(self):
        return (all(x == self.cube[5][4] for x in (self.cube[5][1], self.cube[5][3], self.cube[5][5], self.cube[5][7]))
                and all(self.cube[i][4] == self.cube[i][7] for i in range(1, 5)))

    def cross_solve(self):
        groups_of_moves = [["R", "R'", "R2"], ["L", "L'", "L2"], ["U", "U'", "U2"],
                           ["D", "D'", "D2"], ["F", "F'", "F2"], ["B", "B'", "B2"], ]
        moves_instructions = self.move_mapping()

        print(self.cube)
        print(self.cube_backup)
        for moves in itertools.product(moves_instructions, repeat=2):
            for move in moves:
                moves_instructions[move]()

            if self.cross_validation():
                print(f'cross solved with {moves}')
            self.reset(cube_backup)
