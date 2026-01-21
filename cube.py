import numpy as np
from moves.moves import Moves
from pll import PLL
from scramble import remap_scramble_by_color
import convert
import visualization
from cross import Cross
from f2l import F2L
from oll import OLL
from solving_stage import Solving
from pprint import pprint
from tools import inverse



class Cube(Moves):
    def __init__(self, color="y", notation: str = None, state: str = None):
        self.color = color
        self.reset()
        if notation: 
            convert.notation_to_moves(moves=remap_scramble_by_color(notation, color=self.color), cube=self)
        elif state:
            self.corners, self.edges, self.centers = convert.state_to_cube(state=state)

    def move(self, notation: str) -> None:
        convert.notation_to_moves(notation, self)

    def __str__(self):
        return convert.replace_numbers_with_colors(convert.cube_to_color(self, cross_color=self.color, show=True))

    def get_state(self)->str:
        return convert.cube_to_color(self, show=False)

    def reset(self) -> None:
        self.corners = np.zeros((8, 2), dtype=np.int8)
        self.corners[:, 0] = np.arange(8)
        self.edges = np.zeros((12, 2), dtype=np.int8)
        self.edges[:, 0] = np.arange(12)
        self.centers = np.zeros(6, dtype=np.uint8)
        colors = {
            "y": [0, 1, 2, 3, 4, 5],
            "w": [5, 3, 2, 1, 4, 0],
            "r": [1, 5, 2, 0, 4, 3],
            "o": [3, 0, 2, 5, 4, 1],
            "g": [4, 1, 0, 3, 5, 2],
            "b": [2, 1, 5, 3, 0, 4]
        }
        self.centers[:] = colors[self.color]
        self.y_rotation = 0   # 0 or 64 for f2l only


if __name__ == "__main__":
    state = "305203242215110113300222024102334534110344044453555551"

    notation = "B L B2 U' L' B L' R2 D' L B F2 L' B2 L U2 L F' U' R2 D2"

    color = "y"
    print(notation)
    cube = Cube(notation=notation, color=color)
    

    # print(cube)
    cross = Cross(cube).find_cross(6)
    print(cross[0])
    # cube.move(cross[0])
    # cube.y()
    # cube.U2()
    print(cube)
    print(cube.edges)
    # f2l = F2L(cube, [10,11,8,9], [6,7,4,5]).solve(verbose=True)
    # f2l = F2L(cube, [9,10,11,8], [5,6,7,4]).solve(verbose=True) # y
    # f2l = F2L(cube, [8,9,10,11], [4,5,6,7]).solve(verbose=True) # y2
    # f2l = F2L(cube, [11,8,9,10], [7,4,5,6]).solve(verbose=True) # y'
    # cube.move(f2l[0])
    # cube.move(f2l[1])
    # cube.move(f2l[2])
    # cube.move(f2l[3])
    # print(cube)
    # cube.move(f2l[2])
    # cube.move(f2l[3])
    # oll = OLL(cube).solve()
    # print(oll)
    # cube.move(oll)
    # pll = PLL(cube).solve()
    # print(pll)
    # cube.move(pll)


    # L B R B' L U R2 D2 B2 F D2 L B2 R2 B D2 F B U' L' F2
