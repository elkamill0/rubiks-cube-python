from typing import List
from cross import Cross
from f2l import F2L
from oll import OLL
from pll import PLL
from copy import deepcopy
# from cube import Cube


class Node:
    def __init__(self, cube, alg, stage, name, parent=None):
        self.cube = cube
        self.alg = alg
        self.stage = stage
        self.parent = parent
        self.child = []
        self.name = name


class Solving:
    def __init__(self, cube):
        self.cube = cube
        self.tree = []
        self.solutions = []
        self.root = []
        self.total_cross = 0
        self.total_f2l = 0
        self.total_oll = 0
        self.total_pll = 0

    def build_tree(self, cross_length):
        cross = Cross(self.cube).find_cross(cross_length)
        for c in cross:
            cube = deepcopy(self.cube)
            cube.move(c)
            self.total_cross += 1
            node = Node(cube=cube, alg=c, stage=None, name="Cross: ", parent=None)
            self.root.append(node)
            node.stage = F2L(cube).check_free_slots()
            self.tree.append(node)

        while self.tree:
            parent: Node = self.tree.pop()
            if not parent.stage:
                alg = OLL(parent.cube).solve()
                cube = deepcopy(parent.cube)
                if alg:
                    self.total_oll += 1
                    cube.move(alg)
                node = Node(cube=cube, alg=alg, stage=None, name="OLL: ", parent=parent)
                parent.child.append(node)
                parent = node
                alg = PLL(parent.cube).solve()
                cube = deepcopy(parent.cube)
                if alg:
                    self.total_pll += 1
                    cube.move(alg)
                node = Node(cube=cube, alg=alg, stage=None, name="PLL: ", parent=parent)
                parent.child.append(node)
                self.solutions.append(node)
            else:
                original_stage = deepcopy(parent.stage)
                while parent.stage:
                    index = parent.stage.pop()
                    alg = F2L(parent.cube).solve_slot(index)
                    if not alg:
                        continue
                    self.total_f2l += 1
                    cube = deepcopy(parent.cube)
                    cube.move(alg)
                    stage = deepcopy(original_stage)
                    stage.remove(index)
                    node = Node(cube=cube, alg=alg, stage=stage, name=f"F2L {index+1}: ", parent=parent)
                    parent.child.append(node)
                    self.tree.append(node)
        
        return self.root



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
