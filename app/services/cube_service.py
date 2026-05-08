from pprint import pprint
from random import randint

from src.cube import Cube
from src.scramble import generate_scramble
from src.solving_stage import Solving


def _create_cube(scramble: str | None = None, color: str = "y") -> tuple:
    if scramble:
        return scramble, Cube(notation=scramble, color=color)
    generated = generate_scramble(randint(20, 21))
    return generated, Cube(notation=generated, color=color)


def get_scramble(scramble: str | None, color: str | None) -> tuple:
    scramble, cube = _create_cube(scramble=scramble, color=color)
    return scramble, cube.get_state()


def solve_cube(scramble: str | None, cross_color: str = "y", cross_length: int = 6):
    scramble, cube = _create_cube(scramble=scramble, color=cross_color)
    solving = Solving(cube)
    solving.build_tree(cross_length=cross_length)
    return [
        {"moves": log_names, "total_moves": moves}
        for log_names, moves in solving.shortest_path
    ]


if __name__ == "__main__":
    result = solve_cube("R2 D L2 F2 U' F2 D2 U L2 B2 U F L' U2 B' F L' U2 B2 U L'")
    pprint(result)
