import convert
from random import randint


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
    INVERSE_MOVE_MAP = {
        "w": {  # z2
            "R":  "L",  "R'": "L'",  "R2": "L2",
            "L":  "R",  "L'": "R'",  "L2": "R2",
            "U":  "D",  "U'": "D'",  "U2": "D2",
            "D":  "U",  "D'": "U'",  "D2": "U2",
        },
        "o": {  # z'
            "R":  "U",  "R'": "U'",  "R2": "U2",
            "L":  "D",  "L'": "D'",  "L2": "D2",
            "U":  "L",  "U'": "L'",  "U2": "L2",
            "D":  "R",  "D'": "R'",  "D2": "R2",
        },
        "r": {  # z
            "R":  "D",  "R'": "D'",  "R2": "D2",
            "L":  "U",  "L'": "U'",  "L2": "U2",
            "U":  "R",  "U'": "R'",  "U2": "R2",
            "D":  "L",  "D'": "L'",  "D2": "L2",
        },
        "b": {  # x
            "U":  "B",  "U'": "B'",  "U2": "B2",
            "D":  "F",  "D'": "F'",  "D2": "F2",
            "F":  "U",  "F'": "U'",  "F2": "U2",
            "B":  "D",  "B'": "D'",  "B2": "D2",
        },
        "g": {  # x'
            "U":  "F",  "U'": "F'",  "U2": "F2",
            "D":  "B",  "D'": "B'",  "D2": "B2",
            "F":  "D",  "F'": "D'",  "F2": "D2",
            "B":  "U",  "B'": "U'",  "B2": "U2",
        },
        "y": {},  # identity – nic nie rób
    }

    mapping = INVERSE_MOVE_MAP.get(color, {})
    return " ".join(mapping.get(m, m) for m in notation.split())
 