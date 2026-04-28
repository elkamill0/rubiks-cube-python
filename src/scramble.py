from random import randint, choice

import src.convert as convert
from src.tools import remap_notation_by_rotation


def generate_scramble(length: int, numbers: bool = False) -> list[int]:
    def next_move(last, second_last=None):
        excluded = {last}
        if second_last is not None and last ^ 1 == second_last:
            excluded.add(last ^ 1)
        choices = [x for x in range(6) if x not in excluded]
        return choice(choices)

    output = [randint(0, 5)]
    for _ in range(1, length):
        second_last = output[-2] if len(output) >= 2 else None
        output.append(next_move(output[-1], second_last))
    if numbers:
        return [x * 3 + randint(0, 2) for x in output]
    return convert.int_to_moves_scramble([x * 3 + randint(0, 2) for x in output])


def remap_scramble_by_color(notation: str, color: str = "y"):
    COLOR_TO_ROTATION = {
        "w": "z2",
        "o": "z'",
        "r": "z",
        "b": "x",
        "g": "x'",
        "y": None,
    }
    if color not in COLOR_TO_ROTATION:
        raise ValueError(f"Nieznany kolor: {color}")
    rotation = COLOR_TO_ROTATION.get(color)
    if rotation is None:
        return notation
    return remap_notation_by_rotation(notation, rotation)
