from typing import List
from cross import Cross
from f2l import F2L
from oll import OLL
from pll import PLL
from copy import deepcopy
# from cube import Cube

class Solving:
    def __init__(self, cube):
        self.cube = cube
        self.f2l_combinations = [
            [0, 1, 2, 3],
            [0, 1, 3, 2],
            [0, 2, 1, 3],
            [0, 2, 3, 1],
            [0, 3, 1, 2],
            [0, 3, 2, 1],
            [1, 0, 2, 3],
            [1, 0, 3, 2],
            [1, 2, 0, 3],
            [1, 2, 3, 0],
            [1, 3, 0, 2],
            [1, 3, 2, 0],
            [2, 0, 1, 3],
            [2, 0, 3, 1],
            [2, 1, 0, 3],
            [2, 1, 3, 0],
            [2, 3, 0, 1],
            [2, 3, 1, 0],
            [3, 0, 1, 2],
            [3, 0, 2, 1],
            [3, 1, 0, 2],
            [3, 1, 2, 0],
            [3, 2, 0, 1],
            [3, 2, 1, 0]
        ]
    
    def solve(self):
        if not Cross(self.cube).is_cross_solved():
            print("cross is not solved")
            return None


        def solve_f2l(combination: List):
            f2l_list = []
            for slot in combination:
                alg = F2L(cube).solve_slot(slot)
                if not alg:
                    return None
                cube.move(alg)
                f2l_list.append(alg)
            return f2l_list


        solutions = []
        for combination in self.f2l_combinations:
            combination_list = []
            cube = deepcopy(self.cube)
            f2l_list = solve_f2l(combination)
            if not f2l_list:
                continue
            combination_list.append(f2l_list)
            oll = OLL(cube).solve()
            if oll:
                cube.move(oll)
            combination_list.append(oll)
            combination_list.append(PLL(cube).solve())
            solutions.append(combination_list)
        return solutions
