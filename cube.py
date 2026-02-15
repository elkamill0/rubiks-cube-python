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
from tools import inverse, remap_notation_by_rotation



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
        self.total_moves += len(notation.strip().split())
        


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
        self.y_rotate = 0   # 0 or 64 for f2l only
        self.total_moves = 0


if __name__ == "__main__":
    state = "305203242215110113300222024102334534110344044453555551"

    # notation = "B L B2 U' L' B L' R2 D' L B F2 L' B2 L U2 L F' U' R2 D2"

    # color = "y"
    # print(notation)
    # cube = Cube(notation=notation, color=color)
    

    # # print(cube)
    # cross = Cross(cube).find_cross(6)
    # print(cross[0])
    # cube.move(cross[0])
    # cube.y()
    # # cube.U2()
    # print(cube)
    # f2l = F2L(cube)
    
    # pairs = f2l.find_pairs()
    # print(pairs)
    # cube.move(pairs[1])
    # f2l = F2L(cube)
    # pairs = f2l.find_pairs()
    # print(pairs)
    # cube.move(pairs[0])


    notation = "R2 D L2 F2 U' F2 D2 U L2 B2 U F L' U2 B' F L' U2 B2 U L'"
    cube = Cube(notation=notation, color="y")
    cross = Cross(cube).find_cross(6)[0]
    print(cross)
    cube.move(cross)
    f2l = F2L(cube).possible_moves()
    cube.move(f2l[0].alg)
    print(f2l)

    
    # solving = Solving(cube)
    # tree = solving.build_tree(6)
    # print(tree[0].cube.edges)
    # print(tree[0].cube.corners)
    # print(tree[0])
    
    # cube.move(Cross(cube).find_cross(6)[0])






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

    # R2 D L2 F2 U' F2 D2 U L2 B2 U F L' U2 B' F L' U2 B2 U L'
    # B U' L' D B F
    # f2l2, f2l4, 

    # L B R B' L U R2 D2 B2 F D2 L B2 R2 B D2 F B U' L' F2
