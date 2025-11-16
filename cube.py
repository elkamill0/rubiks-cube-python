import numpy as np
from moves.moves import Moves
from pll import PLL
import scramble
import convert
import visualization
from cross import Cross
from f2l import F2L
from oll import OLL
from solving_stage import Solving
from pprint import pprint



class Cube(Moves):
    def __init__(self, notation: str = None, state: str = None):
        self.reset()
        if notation: 
            convert.notation_to_moves(moves=notation, cube=self)
        elif state:
            self.corners, self.edges, self.centers = convert.state_to_cube(state=state)

    def __str__(self):
        return convert.replace_numbers_with_colors(convert.cube_to_color(self.corners, self.edges, self.centers, show=True))

    def print_cube_with_numbers(self):
        return convert.cube_to_color(self.corners, self.edges, self.centers, show=True)
    
    def move(self, notation: str) -> None:
        convert.notation_to_moves(notation, self)

    def get_state(self):
        return convert.cube_to_color(self.corners, self.edges, self.centers, show=False)
    
    def streamlit_print(self):
        return "    "+convert.replace_numbers_with_colors(convert.cube_to_color(self.corners, self.edges, self.centers, show=True))

    # def get_cube(self):
        # return kk

    def reset(self) -> None:
        self.corners = np.zeros((8, 2), dtype=np.int8)
        self.corners[:, 0] = np.arange(8)
        self.edges = np.zeros((12, 2), dtype=np.int8)
        self.edges[:, 0] = np.arange(12)
        self.centers = np.arange(6, dtype=np.uint8)


    # def f2l(self, length):
    #     return f2l.check_f2l_pair(length, self.cube)

if __name__ == "__main__":
    # print(scramble.generate_scramble(10))
    # notation="B' U L' B2 R F2 L' R2 B2 U2 R2 D2 F2 D' B' U L2 B' D F"
    # state = "305203242215110113300222024102334534110344044453555551"
    # notation="F' R2 F' U2 F R2 F' U2 R2 F U2 R U F L2 B D' B' R"
    # notation="F' B2 L F2 L D2 L2 U2 R D2 B2 L D' B2 F L' B L2 D U'"
    # notation = "R U R' L D2 F' B U' R2 L' F2 D' B2 U2 L2 D B' F"
    # notation = "U2 R' F D B2 L U' R2 F' D' L2 B U L' D2 R F2 B' U'"
    # notation = "L "#D2 B' R U2 F' L' B2 U R' D F2 L2 U' B R2 F D' U B'"

    # notation = "U2 D L2 B F2 R2 F B' D F' B' R' B F' U' R2 U2 B L D' R'"
    notation = "B L B2 U' L' B L' R2 D' L B F2 L' B2 L U2 L F' U' R2 D2"
    # notation = "U' L F2 D' R2 D B L B R B D2 U' L B' D L' R' B' F' L2"


    cube = Cube(notation=notation)
    # solving = Solving(cube).build_tree(6)
    # node = solving[0]
    # while node.child:
    #     print(node.alg)
    #     node = node.child[0]
    # print(node.alg)

    print(cube.get_state())

    

    # while node.parent:
    #     print(node.alg)
    #     node = node.parent
    # print(node.alg)

    # print(solving[0].parent.alg)



    # crosses_list = Cross(cube).find_cross(6)
    # print(crosses_list[0])
    # cube.move(crosses_list[0])


    # pprint(Solving(cube).solve())




    
    # print(F2L(cube, Cube()).find_pairs())
    # print(F2L(cube).solve_slot(3))


    # print(F2L(Cube(), Cube()).prepare_algs("algs/f2l4.json", 3))


    # cross = Cross(cube).find_cross(7)
    # print(len(cross))
    # print(cross)
    # print(cube)

    # OLL(Cube()).prepare_algs()
    # cross = Cross(cube).find_cross(6)
    # # print(cross)
    # print(notation)
    # print(cross[0])
    # cube.move(cross[0])
    # f2l = F2L(cube, Cube()).solve()
    # [cube.move(i) for i in f2l]
    # print(cube)
    # oll = OLL(cube).solve()
    # print(oll)

    # cube.move(oll)
    # print(cube)
    # pll = PLL(cube).solve()
    # print(pll)
    # cube.move(pll)

    # pll = PLL(Cube()).prepare_algs("algs/pll.json")

    # print(cube)
    # print(cube.get_state())

    # L B R B' L U R2 D2 B2 F D2 L B2 R2 B D2 F B U' L' F2
