from typing import List
from src.cross import Cross
from src.f2l import F2L
from src.oll import OLL
from src.pll import PLL
from copy import deepcopy, copy

from time import time


class Node:
    def __init__(self, cube, alg: str, stage, parent: "Node" = None):
        self.cube = cube
        self.alg = alg
        self.stage = stage
        self.parent = parent
        self.child = []


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
        self.shortest_path = []

    def build_tree(self, cross_length: int) -> list[Node]:
        root = Node(self.cube, "", stage="cross")
        self.tree = [root]

        while self.tree:
            parent = self.tree.pop()
            if parent.stage == "cross":
                cross = Cross(parent.cube).find_cross(cross_length)
                for alg in cross:
                    self.total_cross += 1
                    cube = deepcopy(parent.cube)
                    cube.apply_step(alg)

                    child = Node(cube, alg, stage="f2l", parent=parent)
                    parent.child.append(child)
                    self.tree.append(child)

            elif parent.stage == "f2l":
                f2l = F2L(parent.cube)

                if not f2l.free_slots:
                    self.tree.append(Node(parent.cube, "", stage="oll", parent=parent))
                    continue

                for alg in f2l.solve():
                    self.total_f2l += 1
                    cube = deepcopy(parent.cube)
                    cube.apply_step(alg)

                    child = Node(cube, alg, stage="f2l", parent=parent)
                    parent.child.append(child)
                    self.tree.append(child)

            elif parent.stage == "oll":
                alg = OLL(parent.cube).solve()
                cube = deepcopy(parent.cube)
                if alg:
                    self.total_oll += 1
                    cube.apply_step(alg)

                child = Node(cube, alg, stage="pll", parent=parent)
                parent.child.append(child)
                self.tree.append(child)

            elif parent.stage == "pll":
                alg = PLL(parent.cube).solve()
                cube = deepcopy(parent.cube)
                if alg:
                    self.total_pll += 1
                    cube.apply_step(alg)

                child = Node(cube, alg, stage="done", parent=parent)
                parent.child.append(child)
                self.solutions.append(child)
                self.shortest_path.append((cube.log_names.copy(), cube.total_moves))

        self.shortest_path = sorted(self.shortest_path, key=lambda x: x[1])

        return root.child


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
            return f2l.solve()

        oll = OLL(self.cube)
        if not oll.is_solved():
            return [oll.solve()]

        pll = PLL(self.cube)
        if not pll.is_solved():
            return [pll.solve()]

        return [("", "Done")]
