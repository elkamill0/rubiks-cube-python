import numpy as np
from moves.moves import Moves
from scramble import remap_scramble_by_color
import convert
from cross import Cross
from f2l import F2L
from oll import OLL
from pll import PLL
from solving_stage import Solving
from tools import inverse, remap_notation_by_rotation
from time import time



class Cube(Moves):
    def __init__(self, color="y", notation: str = None, state: str = None):
        self.color = color
        self.reset()
        if notation: 
            convert.notation_to_moves(moves=remap_scramble_by_color(notation, color=self.color), cube=self)
        elif state:
            self.corners, self.edges, self.centers = convert.state_to_cube(state=state)

    def move(self, notation: str, name: str | None = None) -> None:
        convert.notation_to_moves(notation, self)
        self.total_moves += len(notation.strip().split())
        self.log.append(notation)
        self.log_names.append(f"{notation}\t// {name} "or "")

    def apply_step(self, step: tuple) -> None:
        self.move(notation=step[0], name=step[1])

    def undo(self) -> None:
        convert.notation_to_moves(inverse(self.log[-1]), self)
        self.total_moves -= len(self.log[-1].strip().split())
        self.log_names.pop()
        return self.log.pop()

    def __str__(self):
        return convert.replace_numbers_with_colors(convert.cube_to_color(self, cross_color=self.color, show=True))

    def get_state(self)->str:
        return convert.cube_to_color(self, show=False)
    
    def is_solved(self) -> bool:
        return (
            np.all(self.corners[:, 0] == np.arange(8)) and
            np.all(self.corners[:, 1] == 0) and
            np.all(self.edges[:, 0] == np.arange(12)) and
            np.all(self.edges[:, 1] == 0)
        )


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
        self.y_rotate = 0
        self.total_moves = 0
        self.log = []
        self.log_names = []


if __name__ == "__main__":
    state = "305203242215110113300222024102334534110344044453555551"

    # L B R B' L U R2 D2 B2 F D2 L B2 R2 B D2 F B U' L' F2
