# from cube import Cube
from tools import inverse, reduce
import json
from copy import deepcopy


class OLL():
    def __init__(self, cube):
        self.cube = deepcopy(cube)
        self.solved_cube = deepcopy(cube)
        self.solved_cube.reset()
        self.cases = { 
            ((1, 1, 1, 1), (1, 2, 1, 2)): "R U2 R2 F R F' U2 R' F R F' ", #OLL 1
            ((1, 1, 1, 1), (1, 1, 2, 2)): "F R U R' U' F' U2 F U R U' R' F' ", #OLL 2
            ((1, 1, 1, 1), (2, 2, 2, 0)): "F U2 F R' F' R U R U R' U F' ", #OLL 3
            ((1, 1, 1, 1), (1, 1, 0, 1)): "F' U2 F' L F L' U' L' U' L U' F ", #OLL 4
            ((1, 0, 0, 1), (2, 2, 0, 2)): "F R U R' U' F' U' F R U R' U' F' ", #OLL 5
            ((0, 0, 1, 1), (1, 0, 1, 1)): "F U' R2 D R' U' R D' R2 U F' ", #OLL 6
            ((0, 1, 1, 0), (2, 2, 2, 0)): "L' U2 L U2 L F' L' F ", #OLL 7
            ((0, 0, 1, 1), (1, 1, 0, 1)): "R U2 R' U2 R' F R F' ", #OLL 8
            ((1, 1, 0, 0), (1, 0, 1, 1)): "U R' U' R F R' F' U F R F' ", #OLL 9
            ((1, 1, 0, 0), (2, 0, 2, 2)): "R U R' U R' F R F' R U2 R' ", #OLL 10
            ((1, 0, 0, 1), (2, 2, 2, 0)): "U2 R U R' U' R' F R F' L' U' L U L F' L' F ", #OLL 11
            ((1, 0, 0, 1), (1, 0, 1, 1)): "F R U R' U' F' U F R U R' U' F' ", #OLL 12
            ((1, 0, 1, 0), (2, 2, 2, 0)): "F U R U2 R' U' R U R' F' ", #OLL 13
            ((1, 0, 1, 0), (1, 1, 0, 1)): "R' F R U R' F' R F U' F' ", #OLL 14
            ((1, 0, 1, 0), (2, 2, 0, 2)): "L F' L' U' L U F L' U L U2 L' ", #OLL 15
            ((1, 1, 1, 1), (0, 1, 0, 2)): "R U R' U R' F R F' U2 R' F R F' ", #OLL 16
            ((1, 1, 1, 1), (0, 0, 2, 1)): "F R' F' R U R U' R' U F R U R' U' F' ", #OLL 17
            ((1, 1, 1, 1), (0, 0, 1, 2)): "R' U2 F R U R' U' F2 U2 F R ", #OLL 18
            ((1, 1, 1, 1), (0, 0, 0, 0)): "R U R' U' R' F R F' R U2 R2 F R F' R U2 R' ", #OLL 19
            ((0, 0, 0, 0), (1, 2, 1, 2)): "R U R' U R U' R' U R U2 R' ", #OLL 20
            ((0, 0, 0, 0), (1, 1, 2, 2)): "R U2 R2 U' R2 U' R2 U2 R ", #OLL 21
            ((0, 0, 0, 0), (0, 0, 2, 1)): "R2 D R' U2 R D' R' U2 R' ", #OLL 22
            ((0, 0, 0, 0), (2, 0, 0, 1)): "L F R' F' L' F R F' ", #OLL 23
            ((0, 0, 0, 0), (0, 2, 0, 1)): "R U2 R D R' U2 R D' R2 ", #OLL 24
            ((0, 0, 0, 0), (0, 1, 1, 1)): "R' U' R U' R' U2 R ", #OLL 25
            ((0, 0, 0, 0), (2, 2, 2, 0)): "R U R' U R U2 R' ", #OLL 26
            ((0, 1, 1, 0), (0, 0, 0, 0)): "F R U R' U' F2 L' U' L U F ", #OLL 27
            ((1, 1, 0, 0), (0, 0, 1, 2)): "L2 U' L B L' U L2 U' L' B' L ", #OLL 28
            ((1, 0, 0, 1), (0, 0, 1, 2)): "R2 U R' B' R U' R2 U R B R' ", #OLL 29
            ((0, 0, 1, 1), (2, 0, 0, 1)): "R' U' F U R U' R' F' R ", #OLL 30
            ((1, 0, 0, 1), (2, 0, 0, 1)): "R U B' U' R' U R B R' ", #OLL 31
            ((1, 0, 1, 0), (2, 0, 0, 1)): "R U R' U' R' F R F' ", #OLL 32
            ((1, 0, 1, 0), (0, 0, 1, 2)): "R U2 R' F R U R' U' F' U R U R' ", #OLL 33
            ((1, 0, 0, 1), (0, 2, 0, 1)): "R U2 R2 F R F' R U2 R' ", #OLL 34
            ((1, 1, 0, 0), (0, 2, 0, 1)): "R U R' U' F' U2 F U R U R' ", #OLL 35
            ((0, 1, 1, 0), (0, 2, 0, 1)): "F R' F' R U R U' R' ", #OLL 36
            ((0, 1, 1, 0), (2, 0, 1, 0)): "R U R' U R U' R' U' R' F R F' ", #OLL 37
            ((0, 1, 0, 1), (0, 1, 0, 2)): "F R' F' U' F U R U' F' ", #OLL 38
            ((0, 1, 0, 1), (1, 0, 2, 0)): "U F R U R' F' R' F U' F' U R ", #OLL 39
            ((1, 0, 0, 1), (0, 0, 2, 1)): "R U' R' U2 R U B U' B' U' R' ", #OLL 40
            ((1, 1, 0, 0), (0, 0, 2, 1)): "R' U' R U' R' U2 R F R U R' U' F'", #OLL 41
            ((1, 1, 0, 0), (0, 2, 1, 0)): "B' U' R' U R B ", #OLL 42
            ((1, 0, 0, 1), (1, 0, 0, 2)): "B L' B' L U B' U F U R' U' R F' B ", #OLL 43
            ((1, 0, 1, 0), (1, 0, 0, 2)): "F R U R' U' F' ", #OLL 44
            ((0, 1, 0, 1), (0, 2, 1, 0)): "R' U' R' F R F' U R ", #OLL 45
            ((0, 0, 1, 1), (2, 2, 1, 1)): "F' L' U' L U L' U' L U F ", #OLL 46
            ((0, 1, 1, 0), (1, 1, 2, 2)): "F R U R' U' R U R' U' F' ", #OLL 47
            ((1, 1, 0, 0), (2, 2, 1, 1)): "R B' R2 F R2 B R2 F' R ", #OLL 48
            ((1, 0, 0, 1), (1, 1, 2, 2)): "R U R2 F R F' U F R' F' R ", #OLL 49
            ((0, 1, 0, 1), (2, 2, 1, 1)): "R U R' U R U' B U' B' R' ", #OLL 50
            ((1, 0, 0, 1), (1, 2, 1, 2)): "U2 F R U R' U' F' R U R' U' R' F R F' ", #OLL 51
            ((0, 0, 1, 1), (1, 2, 1, 2)): "F' L' U' L U F U2 R U R' U' R' F R F' ", #OLL 52
            ((0, 1, 0, 1), (1, 2, 1, 2)): "R U2 R2 U' R U' R' U2 F R F' ", #OLL 53
            ((1, 0, 1, 0), (1, 2, 1, 2)): "R' F' R U' L' U L U' L' U L R' F R ", #OLL 54
            ((1, 0, 1, 0), (0, 0, 0, 0)): "R L' U R' U' L R' F R F' ", #OLL 55
        }


    def prepare_algs(self, path="pll.json"):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for i, case in enumerate(data):
            cube = self.solved_cube.move(inverse(case))
            print(f"({tuple(int(e[1]) for e in cube.edges[0:4])}, {tuple(int(e[1]) for e in cube.corners[0:4])}): \"{case}\", #PLL {i+1}")


    def solve(self) -> str:
        new_notation = ""
        cube = deepcopy(self.cube)
        for _ in range(4):
            edges = tuple(int(e[1]) for e in cube.edges[0:4])
            corners = tuple(int(c[1]) for c in cube.corners[0:4])
            
            if (edges, corners) in self.cases:
                new_notation += self.cases.get((edges, corners))
                return reduce(new_notation)
            new_notation += "U "
            cube.U()
        return None




# if __name__ == "__main__":
    # state = "004104200300111111133222222401333333022444444555555555"
    # cube = solved_cube.move(state=state)
    # oll = OLL(cube)
    # print(oll.find_oll())