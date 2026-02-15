from typing import List
from cross import Cross
from f2l import F2L
from oll import OLL
from pll import PLL
from copy import deepcopy
# from cube import Cube


class Node:
    def __init__(self, cube, alg: str, stage: list[int] | None, name: str, parent:"Node"=None):
        self.cube = cube
        self.alg = alg
        self.stage = stage
        self.parent = parent
        self.child = []
        self.name = name
        self.total_moves = {
            "R": 5,
            "L": 3,
            "U": 2,
            "D": 1,
            "F": 5,
            "B": 2,
            "y": 2,
        }


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

    def build_tree(self, cross_length: int) -> list[Node]:
        root = Node(self.cube, "", None, "scramble", None)
        for c in Cross(self.cube).find_cross(cross_length):
            cube = deepcopy(self.cube)
            cube.move(c)
            f2l = F2L(cube)
            node = Node(cube=cube, alg=c, name="Cross: ", stage = f2l.free_slots, parent=root)
            self.total_cross += 1
            root.child.append(node)
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
                f2l = F2L(parent.cube)

                # for i, alg in zip(f2l.free_slots, f2l.solve()):
                for alg in f2l.solve():
                    cube = deepcopy(parent.cube)
                    cube.move(alg)

                    child = Node(cube=cube, alg=alg, name=f"F2L",
                                    stage=F2L(cube).free_slots, parent=parent)
                    
                    self.total_f2l+=1
                    parent.child.append(child)
                    self.tree.append(child)
        
        return root.child



    def _solve(self) -> List:
        """
        Tymczasowa funkcja rozwiązująca kostkę F2L + OLL + PLL.
        Obecnie nieużywana.
        """
        if not Cross(self.cube).is_solved():
            return ""


        def solve_f2l(combination: List[int]) -> List:
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

class Manual:
    def __init__(self, cube, cross_length):
        self.cube = cube
        self.cross_length = cross_length

    def loop(self):
        cross = Cross(self.cube)
        if not cross.is_solved():
            return cross.find_cross(self.cross_length)

        f2l = F2L(self.cube) 
        if not f2l.is_solved():
            print("f2l.free_slots:", f2l.free_slots)
            return f2l.solve()
        
        oll = OLL(self.cube)
        if not oll.is_solved():
            return [oll.solve()]
        
        pll = PLL(self.cube)
        if not pll.is_solved():
            return [pll.solve()]
        
        return []
