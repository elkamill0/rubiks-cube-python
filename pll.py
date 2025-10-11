from copy import deepcopy
import json
# from cube import Cube
from tools import inverse, reduce

class PLL:
    def __init__(self, cube):
        self.cube = cube
        self.solved_cube = deepcopy(cube)
        self.solved_cube.reset()

        self.cases = {
            ((0, 1, 2, 3), (1, 2, 0, 3)): "R' F R' B2 R F' R' B2 R2 ", #PLL 1
            ((0, 1, 2, 3), (2, 0, 1, 3)): "R' B' R U' R D R' U R D' R2 B R ", #PLL 2
            ((0, 1, 2, 3), (1, 0, 3, 2)): "R2 U F' R' U R U' R' U R U' R' U R U' F U' R2 ", #PLL 3
            ((1, 0, 3, 2), (2, 1, 3, 0)): "R' U R U' R2 F' U' F U R F R' F' R2 ", #PLL 4
            ((2, 3, 1, 0), (0, 2, 1, 3)): "R2 U R' U R' U' R U' R2 D U' R' U R D' ", #PLL 5
            ((3, 2, 0, 1), (0, 2, 1, 3)): "D R' U' R U D' R2 U R' U R U' R U' R2 ", #PLL 6
            ((1, 3, 0, 2), (0, 2, 1, 3)): "D R2 U' R U' R U R' U R2 D' U R U' R' ", #PLL 7
            ((2, 0, 3, 1), (0, 2, 1, 3)): "R U R' U' D R2 U' R U' R' U R' U R2 D' ", #PLL 8
            ((2, 3, 0, 1), (0, 1, 2, 3)): "R2 U2 R U2 R2 U2 R2 U2 R U2 R2 ", #PLL 9
            ((3, 0, 2, 1), (2, 0, 1, 3)): "L' U' L F L' U' L U L F' L2 U L ", #PLL 10
            ((1, 3, 2, 0), (1, 3, 2, 0)): "R U R' F' R U R' U' R' F R2 U' R' ", #PLL 11
            ((0, 3, 2, 1), (0, 3, 2, 1)): "R U R' U R U R' F' R U R' U' R' F R2 U' R' U2 R U' R' ", #PLL 12
            ((0, 3, 2, 1), (2, 1, 0, 3)): "R' U R U' R' F' U' F R U R' F R' F' R U' R ", #PLL 13
            ((3, 0, 2, 1), (0, 3, 1, 2)): "L U2 L' U2 L F' L' U' L U L F L2", #PLL 14
            ((1, 3, 2, 0), (2, 1, 3, 0)): "R' U2 R U2 R' F R U R' U' R' F' R2 ", #PLL 15
            ((0, 3, 2, 1), (0, 2, 1, 3)): "R U R' U' R' F R2 U' R' U' R U R' F' ", #PLL 16
            ((1, 2, 0, 3), (2, 3, 0, 1)): "R U R' U R' U' R2 U' R' U R' U R ", #PLL 17
            ((1, 3, 2, 0), (0, 1, 2, 3)): "R' U R' U' R' U' R' U R U R2 ", #PLL 18
            ((1, 0, 2, 3), (2, 1, 0, 3)): "R' U R' U' R D' R' D R' U D' R2 U' R2 D R2 ", #PLL 19
            ((3, 1, 2, 0), (2, 1, 0, 3)): "F R U' R' U' R U R' F' R U R' U' R' F R F' ", #PLL 20
            ((1, 0, 3, 2), (2, 3, 0, 1)): "R U R' U R' U' R' U R U' R' U' R2 U R ", #PLL 21
        }

    def prepare_algs(self, path="pll.json"):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for i, case in enumerate(data):
            cube = deepcopy(self.solved_cube)
            cube.move(inverse(case))
            # cube = self.solved_cube.move(inverse(case))
            print(f"({tuple(int(e[0]) for e in cube.edges[0:4])}, {tuple(int(e[0]) for e in cube.corners[0:4])}): \"{case}\", #PLL {i+1}")

    
    def solve(self) -> str:
        new_notation = ""
        cube = deepcopy(self.cube)
        for _ in range(4):
            edges = tuple(int(e[0]) for e in cube.edges[0:4])
            corners = tuple(int(c[0]) for c in cube.corners[0:4])
            
            if (edges, corners) in self.cases:
                new_notation += self.cases.get((edges, corners))
                return reduce(new_notation)
            new_notation += "U "
            cube.U()
        return None

# if __name__ == "__main__":
#     state = "000000000224111111133222222412333333341444444555555555"
#     cube = Cube(state=state)
#     pll = PLL(cube).prepare_algs()

