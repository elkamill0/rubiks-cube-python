import convert
from random import randint
from tools import remap_notation_by_rotation


def generate_scramble(length: int) -> list[int]:
    output = [randint(0,5)]
    num = randint(0,5)
    while num == output[-1]:
        num = randint(0,5) 
    output.append(num)
    
    for _ in range(2, length):
        num = randint(0,5)
        if output[-1]^1 == output[-2]:
            while num == output[-1] or num == output[-1]^1:
                num = randint(0,5)
        while output[-1] == num:
            num = randint(0,5)
        output.append(num)
    
    # return convert.int_to_moves_scramble([x * 3 + randint(0,2) for x in output], convert.int_to_notation)
    return convert.int_to_moves_scramble([x * 3 + randint(0,2) for x in output])

def remap_scramble_by_color(notation: str, color: str = "y"):
    COLOR_TO_ROTATION = {
        "w": "z2",
        "o": "z'",
        "r": "z",
        "b": "x",
        "g": "x'",
        "y": None,
    }

    rotation = COLOR_TO_ROTATION.get(color)
    if rotation is None:
        return notation

    return remap_notation_by_rotation(notation, rotation)


