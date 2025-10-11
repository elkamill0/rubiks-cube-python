import json
# from cube import Cube
import numpy as np
from convert import edges_to_binary, corners_to_binary
from typing import List
from tools import inverse, reduce
from copy import deepcopy

class F2L:
    def __init__(self, cube, solved_cube):
        self.solved_cube = solved_cube
        self.cube = deepcopy(cube)
        self.edges = edges_to_binary(self.cube, [10,11,8,9]) 
        self.corners = corners_to_binary(self.cube, [6,7,4,5])
        self.free_slots = self.__check_free_slots()
        self.pairs = [{
            (149, 5): "U R U' R'", #F2L 1
            (85, 84): "F R' F' R", #F2L 2
            (149, 70): "F' U' F", #F2L 3
            (85, 36): "R U R'", #F2L 4
            (149, 36): "U' R U R' U2 R U' R'", #F2L 5
            (85, 70): "U F' U' F U2 F' U F", #F2L 6
            (149, 6): "U' R U2 R' U' R U2 R'", #F2L 7
            (85, 100): "F' U' L' U2 L U' F", #F2L 8
            (149, 100): "U' R U' R' U F' U' F", #F2L 9
            (85, 6): "U' R U R' U R U R'", #F2L 10
            (149, 69): "U' R U2 R' U F' U' F", #F2L 11
            (85, 20): "R U' R' U R U' R' U2 R U' R'", #F2L 12
            (37, 36): "R U R' F R' F' R U' R U R'", #F2L 13
            (85, 5): "U' R U' R' U R U R'", #F2L 14
            (149, 20): "R' D' R U' R' D R U R U' R'", #F2L 15
            (85, 69): "R U' R' U2 F' U' F", #F2L 16
            (21, 5): "R U2 R' U' R U R'", #F2L 17
            (21, 84): "F' U2 F U F' U' F", #F2L 18
            (21, 36): "U R U2 R' U R U' R'", #F2L 19
            (21, 70): "U' R U' R2 F R F' R U' R'", #F2L 20
            (21, 6): "U2 R U R' U R U' R'", #F2L 21
            (21, 100): "F' L' U2 L F", #F2L 22
            (21, 20): "U R U' R' U' R U' R' U R U' R'", #F2L 23
            (21, 69): "F U R U' R' F' R U' R'", #F2L 24
            (25, 5): "U' R' F R F' R U R'", #F2L 25
            (25, 84): "U R U' R' F R' F' R", #F2L 26
            (89, 5): "R U' R' U R U' R'", #F2L 27
            (153, 84): "R U R' U' F R' F' R", #F2L 28
            (89, 84): "R' F R F' U R U' R'", #F2L 29
            (153, 5): "R U R' U' R U R'", #F2L 30
            (21, 81): "U' R' F R F' R U' R'", #F2L 31
            (21, 17): "U R U' R' U R U' R' U R U' R'", #F2L 32
            (149, 17): "U' R U' R' U2 R U' R'", #F2L 33
            (85, 17): "U R U R' U2 R U R'", #F2L 34
            (149, 81): "U' R U R' U F' U' F", #F2L 35
            (85, 81): "U F' U' F U' R U R'", #F2L 36
            (25, 81): "R2 U2 F R2 F' U2 R' U R'", #F2L 37
            (89, 17): "R U' R' U' R U R' U2 R U' R'", #F2L 38
            (153, 17): "R U' R' U R U2 R' U R U' R'", #F2L 39
            (89, 81): "F' L' U2 L F R U R'", #F2L 40
            (153, 81): "R U' R' F' L' U2 L F", #F2L 41
        },
        {
            (150, 84): "F' L F L'", #F2L 1
            (86, 6): "U' L' U L", #F2L 2
            (150, 36): "L' U' L", #F2L 3
            (86, 69): "F U F'", #F2L 4
            (150, 69): "U2 F R U R' U2 F'", #F2L 5
            (86, 36): "U L' U' L U2 L' U L", #F2L 6
            (150, 100): "F U R U2 R' U F'", #F2L 7
            (86, 5): "U L' U2 L U L' U2 L ", #F2L 8
            (150, 5): "U L' U' L U' L' U' L ", #F2L 9
            (86, 100): "U L' U L U' F U F' ", #F2L 10
            (150, 20): "L' U L U' L' U L U2 L' U L ", #F2L 11
            (86, 70): "U L' U2 L U' F U F' ", #F2L 12
            (150, 6): "U L' U L U' L' U' L ", #F2L 13
            (86, 84): "U2 F R U' R' U R U2 R' F' ", #F2L 14
            (150, 70): "L' U L U2 F U F' ", #F2L 15
            (86, 20): "F U' R U' R' U2 F' ", #F2L 16
            (22, 84): "L F' L' F L' U L U' L' U L ", #F2L 17
            (22, 6): "L' U2 L U L' U' L ", #F2L 18
            (22, 69): "U L' U L2 F' L' F L' U L ", #F2L 19
            (22, 36): "U' L' U2 L U' L' U L ", #F2L 20
            (22, 100): "F R U2 R' F'", #F2L 21
            (22, 5): "L' U L U2 L' U' L ", #F2L 22
            (22, 70): "F' U' L' U L F L' U L ", #F2L 23
            (22, 20): "U' L' U L U L' U L U' L' U L ", #F2L 24
            (26, 84): "U' L' U L F' L F L' ", #F2L 25
            (26, 6): "U L F' L' F L' U' L ", #F2L 26
            (90, 84): "L' U' L U F' L F L' ", #F2L 27
            (154, 6): "L' U L U' L' U L ", #F2L 28
            (90, 6): "L' U' L U L' U' L ", #F2L 29
            (154, 84): "L F' L' F U' L' U L ", #F2L 30
            (22, 82): "U L F' L' F L' U L ", #F2L 31
            (22, 18): "U' L' U L U' L' U L U' L' U L ", #F2L 32
            (150, 18): "R' D R U' R' D' R ", #F2L 33
            (86, 18): "U L' U L U2 L' U L ", #F2L 34
            (150, 82): "U2 F U F' U' L' U L ", #F2L 35
            (86, 82): "U2 L' U' L F' L F L' ", #F2L 36
            (26, 82): "L2 U2 F' L2 F U2 L U' L ", #F2L 37
            (90, 18): "L' U L U' L' U2 L U' L' U L ", #F2L 38
            (154, 18): "L' U' L U L' U2 L U L' U' L ", #F2L 39
            (90, 82): "L' U L F R U2 R' F' ", #F2L 40
            (154, 82): "F R U2 R' F' L' U' L ", #F2L 41
        },
        {
            (166, 6): "U L U' L' ", #F2L 1
            (102, 100): "B L' B' L ", #F2L 2
            (166, 69): "B' U' B ", #F2L 3
            (102, 20): "L U L' ", #F2L 4
            (166, 20): "U' L U L' U2 L U' L' ", #F2L 5
            (102, 69): "U L F' L' U' L U F L' ", #F2L 6
            (166, 5): "U' L U2 L' U2 L U' L' ", #F2L 7
            (102, 84): "F' L' U' L2 U L' F ", #F2L 8
            (166, 84): "L2 U F U' F' L2 ", #F2L 9
            (102, 5): "U' L U L' U L U L' ", #F2L 10
            (166, 70): "U' L U2 L' U B' U' B", #F2L 11
            (102, 36): "L' U2 L2 U L2 U L ", #F2L 12
            (166, 100): "U L U' L F' L2 U' L U F U L' ", #F2L 13
            (102, 6): "U' L U' L' U L U L' ", #F2L 14
            (166, 36): "L U L' U2 L U' L' U L U' L' ", #F2L 15
            (102, 70): "L2 F' L' F L' U2 L U' L' ", #F2L 16
            (38, 6): "L U2 L' U' L U L' ", #F2L 17
            (38, 100): "U F U R U' R' F' L U L' ", #F2L 18
            (38, 20): "U L U2 L' U L U' L' ", #F2L 19
            (38, 69): "U' L F U2 F' L' U' L U L' ", #F2L 20
            (38, 5): "L U' L' U2 L U L' ", #F2L 21
            (38, 84): "U2 B' U' B U' B' U B", #F2L 22
            (38, 36): "U L U' L' U' L U' L' U L U' L' ", #F2L 23
            (38, 70): "U2 F U R U' R' F' U2 L U' L' ", #F2L 24
            (42, 6): "L U' L' U' L U' L' U L U L' ", #F2L 25
            (42, 100): "U2 F' L2 U' L2 U L2 F ", #F2L 26
            (106, 6): "L U' L' U L U' L' ", #F2L 27
            (170, 100): "L U2 L F' L' F L' ", #F2L 28
            (106, 100): "L' B L B' U L U' L'", #F2L 29
            (170, 6): "L U L' U' L U L' ", #F2L 30
            (38, 98): "L U' L F' L' F L' ", #F2L 31
            (38, 34): "L U L' U' L U L' U' L U L'", #F2L 32
            (166, 34): "U' L U' L' U2 L U' L' ", #F2L 33
            (102, 34): "U L U L' U2 L U L' ", #F2L 34
            (166, 98): "U2 L U L' U' L F U F' L' ", #F2L 35
            (102, 98): "L F' L F L' U' L' U L U L' ", #F2L 36
            (42, 98): "L U' L' F' L' U' L2 U L' F ", #F2L 37
            (106, 34): "L U L' U' L U2 L' U' L U L' ", #F2L 38
            (170, 34): "L U L' U2 L U' L' U L U L' ", #F2L 39
            (106, 98): "L U' L U F U' F' L2 ", #F2L 40
            (170, 98): "L2 F U F' U' L' U L' ", #F2L 41
        },
        {
            (165, 100): "U2 R2 F R F' R ", #F2L 1
            (101, 5): "U' R' U R ", #F2L 2
            (165, 20): "R' U' R ", #F2L 3
            (149, 69): "B U' B'", #F2L 4
            (165, 70): "U' R' F R U R' U' F' R ", #F2L 5
            (101, 20): "U R' U' R U2 R' U R ", #F2L 6
            (165, 84): "F R U R2 U' R F' ", #F2L 7
            (101, 6): "U R' U2 R U R' U2 R ", #F2L 8
            (165, 6): "U R' U' R U' R' U' R ", #F2L 9
            (101, 84): "R2 U' F' U F R2 ", #F2L 10
            (165, 36): "R' U R U' R' U R U2 R' U R ", #F2L 11
            (101, 69): "U R' U2 R U' B U B' ", #F2L 12
            (165, 5): "U R' U R U' R' U' R ", #F2L 13
            (101, 100): "U' R' U R' F R2 U R' U' F' U' R ", #F2L 14
            (165, 69): "R2 F R F' R U R' U2 R ", #F2L 15
            (101, 36): "R' U' R U2 R' U R U' R' U R ", #F2L 16
            (37, 100): "R' U2 F R U R' U' F' R ", #F2L 17
            (37, 5): "R' U2 R U R' U' R ", #F2L 18
            (37, 70): "U R' F' U2 F R U R' U' R ", #F2L 19
            (37, 20): "U' R' U2 R U' R' U R ", #F2L 20
            (37, 84): "U2 B U B' U B U' B'", #F2L 21
            (37, 6): "R' U R U2 R' U' R ", #F2L 22
            (37, 69): "U R' F R' F' R2 U' R' U R ", #F2L 23
            (37, 36): "R' U' R U2 R' U' R U R' U' R ", #F2L 24
            (41, 100): "U2 F R2 U R2 U' R2 F' ", #F2L 25
            (41, 5): "R' U R U R' U R U' R' U' R ", #F2L 26
            (105, 100): "R' U2 R' F R F' R ", #F2L 27
            (169, 5): "R' U R U' R' U R ", #F2L 28
            (105, 5): "R' U' R U R' U' R ", #F2L 29
            (169, 100): "U' R' F' U' F U2 R U' R' U R ", #F2L 30
            (37, 97): "R' U R' F R F' R ", #F2L 31
            (37, 33): "U' R' U R U' R' U R U' R' U R ", #F2L 32
            (165, 33): "U' R D R' U R D' R' ", #F2L 33
            (101, 33): "U R' U R U R' U2 R ", #F2L 34
            (165, 97): "R' F R' F' R U R U' R' U' R ", #F2L 35
            (101, 97): "U2 R' U' R U R' F' U' F R ", #F2L 36
            (41, 97): "R' U R F R U R2 U' R F' ", #F2L 37
            (105, 33): "R' U' R U2 R' U R U' R' U' R ", #F2L 38
            (169, 33): "R' U' R U R' U2 R U R' U' R ", #F2L 39
            (105, 97): "R2 F' U' F U R U' R ", #F2L 40
            (169, 97): "R' U R' U' F' U F R2 ", #F2L 41
        }
        ]

    def prepare_algs(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for i, case in enumerate(data):
            cube = self.solved_cube
            cube.move(inverse(case))
            edges = edges_to_binary(cube, [10,11,8,9]) 
            corners = corners_to_binary(cube, [6,7,4,5])
            print(f"({corners[3]}, {edges[3]}): \"{case}\", #F2L {i+1}")

    def __check_free_slots(self) -> List[int]:
        edges = edges_to_binary(self.solved_cube, [10,11,8,9]) 
        corners = corners_to_binary(self.solved_cube, [6,7,4,5])

        solved_pairs = list(zip(edges, corners))
        pairs = list(zip(self.edges, self.corners))

        differences = []

        for i, (solved, current) in enumerate(zip(solved_pairs, pairs)):
            if solved != current:
                differences.append(i)

        return differences
    
    def solve(self, verbose:bool = False):
        i = 0
        new_notation = ""
    
        final = []

        while i <= 4 and self.free_slots:
            for slot in self.free_slots:
                key = (self.corners[slot], self.edges[slot])
                if key in self.pairs[slot]:
                    alg = self.pairs[slot][key]
                    new_notation += alg
                    reduced = reduce(new_notation)
                    final.append(reduced)
                    new_notation = ""
                    if verbose:
                        print(reduced, f" # Slot {slot}")
                    self.cube.move(alg)
                    self.free_slots.remove(slot)
                    i = 0
                    break
            else:
                self.cube.U()
                new_notation+="U "
                self.edges = edges_to_binary(self.cube, [10, 11, 8, 9])
                self.corners = corners_to_binary(self.cube, [6, 7, 4, 5])
                i += 1

        return final


if __name__ == "__main__":
    # state = "144304304520113211220024422303331332514240540055555151"
    state = "305203242215110113300222024102334534110344044453555551"
    # state = "404304022524314510100123323105032033113144542254555152"
    # state = "542400105114211014544023023330232534132140342152555350"
    # cube = Cube(state=state)
    # f2l = F2L(cube)
    # print(f2l.solve(verbose=True))