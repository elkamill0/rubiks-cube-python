import numpy as np

import src.convert as convert
from src.moves.moves import Moves
from src.scramble import remap_scramble_by_color
from src.tools import inverse
from src.logger import get_logger

logging = get_logger(__name__)


class Cube(Moves):
    def __init__(self, color="y", notation: str = None, state: str = None):
        self.color = color
        self.reset()
        if notation:
            convert.notation_to_moves(
                moves=remap_scramble_by_color(notation, color=self.color), cube=self
            )
        elif state:
            self.corners, self.edges, self.centers = convert.state_to_cube(state=state)

    def move(self, notation: str, name: str | None = None) -> None:
        convert.notation_to_moves(notation, self)
        self.total_moves += len(notation.strip().split())
        self.log.append(notation)
        self.log_names.append(f"{notation}\t// {name} " or "")

    def apply_step(self, step: tuple) -> None:
        self.move(notation=step[0], name=step[1])

    def undo(self) -> None:
        convert.notation_to_moves(inverse(self.log[-1]), self)
        self.total_moves -= len(self.log[-1].strip().split())
        self.log_names.pop()
        return self.log.pop()

    def __str__(self):
        return convert.replace_numbers_with_colors(
            convert.cube_to_color(self, cross_color=self.color, show=True)
        )

    def get_state(self) -> str:
        return convert.cube_to_color(self, show=False)

    def is_solved(self) -> bool:
        return (
            np.all(self.corners[:, 0] == np.arange(8))
            and np.all(self.corners[:, 1] == 0)
            and np.all(self.edges[:, 0] == np.arange(12))
            and np.all(self.edges[:, 1] == 0)
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
            "b": [2, 1, 5, 3, 0, 4],
        }
        self.centers[:] = colors[self.color]
        self.y_rotate = 0
        self.total_moves = 0
        self.log = []
        self.log_names = []


if __name__ == "__main__":
    notation = "R2 D L2 F2 U' F2 D2 U L2 B2 U F L' U2 B' F L' U2 B2 U L'"
    state = "230201445330510113331422433441534215205541100550250422"
    # notation = ""
    # c = Cube(notation=notation)
    # c.r()
    # print(c.get_state())
    # print(c)
    # print("-----------------------------------------------------------------")
    c = Cube(state=state)
    c.r()
    # logging.debug(c.centers)
    st = c.get_state()
    logging.debug(st)
    logging.debug(c)
    # print(st[4], st[13], st[22], st[31], st[40], st[49])

    # print("-----------------------------------------------------------------")
    print(st)
    # st = "231222433330510113350420422254134541545141030501255402"
    print(st[4], st[13], st[22], st[31], st[40], st[49])
    c = Cube(state=st)
    logging.debug(c.centers)
    st = c.get_state()
    logging.debug(c.get_state())
    logging.debug(c)
    print(st[4], st[13], st[22], st[31], st[40], st[49])

    # L B R B' L U R2 D2 B2 F D2 L B2 R2 B D2 F B U' L' F2
