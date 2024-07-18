from moves import Moves
from scramble import Scramble
from cross import Cross
import copy
from test import Combination
import time


class Cube(Moves):
    def __init__(self, cube, moves: str = None):
        # self.cube = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8],
        #              [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8]]
        super().__init__(cube)
        self.cube = [[0] * 9, [1] * 9, [2] * 9, [3] * 9, [4] * 9, [5] * 9]
        self.cube_backup = copy.deepcopy(self.cube)
        if moves:
            Scramble(self.cube, moves)

    def __str__(self):
        return f"""
              {self.cube[0][0:3]}
              {self.cube[0][3:6]}
              {self.cube[0][6:9]}
    {self.cube[1][0:3]} {self.cube[2][0:3]} {self.cube[3][0:3]} {self.cube[4][0:3]}
    {self.cube[1][3:6]} {self.cube[2][3:6]} {self.cube[3][3:6]} {self.cube[4][3:6]}
    {self.cube[1][6:9]} {self.cube[2][6:9]} {self.cube[3][6:9]} {self.cube[4][6:9]}
              {self.cube[5][0:3]}
              {self.cube[5][3:6]}
              {self.cube[5][6:9]}
            """

    def cross(self):
        Cross(self.cube).cross_solve()

    def combination(self, length):
        Combination(self.cube).combination_test(length)

    def reset(self):
        self.cube = self.cube_backup


a = Cube("F U2 B2 R2 D' R2 F2 U' B2 F2 L2 F2 U B' U B L' R' D' R F'")
a.R()
print(a)
