def reduce(notation: str) -> str:
    note = notation.strip().split()
    if not (len(note)):
        return

    def note_to_quarters(note):
        return 3 if note.endswith("'") else 2 if note.endswith("2") else 1

    i = 1
    combo = 0
    new_notation = ""
    changed = False
    while i < len(note):
        if note[i - 1][0] == note[i][0]:
            combo += note_to_quarters(note[i - 1])
            changed = True
        else:
            if combo > 0:
                combo += note_to_quarters(note[i - 1])
                combo %= 4
                if combo == 1:
                    new_notation += note[i - 1][0] + " "
                elif combo == 2:
                    new_notation += note[i - 1][0] + "2" + " "
                elif combo == 3:
                    new_notation += note[i - 1][0] + "'" + " "
                combo = 0
            else:
                new_notation += note[i - 1] + " "
        i += 1
    new_notation += note[i - 1]

    if changed:
        reduce(notation=new_notation)
    return new_notation


def inverse(notation: str) -> str:
    inverse_mapping = {
        "R": "R'",
        "R'": "R",
        "R2": "R2",
        "L": "L'",
        "L'": "L",
        "L2": "L2",
        "U": "U'",
        "U'": "U",
        "U2": "U2",
        "D": "D'",
        "D'": "D",
        "D2": "D2",
        "F": "F'",
        "F'": "F",
        "F2": "F2",
        "B": "B'",
        "B'": "B",
        "B2": "B2",
        "r": "r'",
        "r'": "r",
        "r2": "r2",
        "l": "l'",
        "l'": "l",
        "l2": "l2",
        "u": "u'",
        "u'": "u",
        "u2": "u2",
        "d": "d'",
        "d'": "d",
        "d2": "d2",
        "f": "f'",
        "f'": "f",
        "f2": "f2",
        "b": "b'",
        "b'": "b",
        "b2": "b2",
        "M": "M'",
        "M'": "M",
        "M2": "M2",
        "E": "E'",
        "E'": "E",
        "E2": "E2",
        "S": "S'",
        "S'": "S",
        "S2": "S2",
        "x": "x'",
        "x'": "x",
        "x2": "x2",
        "y": "y'",
        "y'": "y",
        "y2": "y2",
        "z": "z'",
        "z'": "z",
        "z2": "z2",
    }

    moves = notation.split()
    inverted_moves = [inverse_mapping[move] for move in reversed(moves)]
    return " ".join(inverted_moves)


def remap_notation_by_rotation(notation: str, rotation_move: str):
    INVERSE_MOVE_MAP = {
        "z": {  # z
            "R": "D",
            "R'": "D'",
            "R2": "D2",
            "L": "U",
            "L'": "U'",
            "L2": "U2",
            "U": "R",
            "U'": "R'",
            "U2": "R2",
            "D": "L",
            "D'": "L'",
            "D2": "L2",
        },
        "z'": {  # z'
            "R": "U",
            "R'": "U'",
            "R2": "U2",
            "L": "D",
            "L'": "D'",
            "L2": "D2",
            "U": "L",
            "U'": "L'",
            "U2": "L2",
            "D": "R",
            "D'": "R'",
            "D2": "R2",
        },
        "z2": {  # z2
            "R": "L",
            "R'": "L'",
            "R2": "L2",
            "L": "R",
            "L'": "R'",
            "L2": "R2",
            "U": "D",
            "U'": "D'",
            "U2": "D2",
            "D": "U",
            "D'": "U'",
            "D2": "U2",
        },
        "x": {  # x
            "U": "B",
            "U'": "B'",
            "U2": "B2",
            "D": "F",
            "D'": "F'",
            "D2": "F2",
            "F": "U",
            "F'": "U'",
            "F2": "U2",
            "B": "D",
            "B'": "D'",
            "B2": "D2",
        },
        "x'": {  # x'
            "U": "F",
            "U'": "F'",
            "U2": "F2",
            "D": "B",
            "D'": "B'",
            "D2": "B2",
            "F": "D",
            "F'": "D'",
            "F2": "D2",
            "B": "U",
            "B'": "U'",
            "B2": "U2",
        },
        "x2": {  # x2
            "U": "D",
            "U'": "D'",
            "U2": "D2",
            "D": "U",
            "D'": "U'",
            "D2": "U2",
            "F": "B",
            "F'": "B'",
            "F2": "B2",
            "B": "F",
            "B'": "F'",
            "B2": "F2",
        },
        "y": {  # y
            "R": "F",
            "R'": "F'",
            "R2": "F2",
            "F": "L",
            "F'": "L'",
            "F2": "L2",
            "L": "B",
            "L'": "B'",
            "L2": "B2",
            "B": "R",
            "B'": "R'",
            "B2": "R2",
        },
        "y'": {  # y'
            "R": "B",
            "R'": "B'",
            "R2": "B2",
            "F": "R",
            "F'": "R'",
            "F2": "R2",
            "L": "F",
            "L'": "F'",
            "L2": "F2",
            "B": "L",
            "B'": "L'",
            "B2": "L2",
        },
        "y2": {  # y2
            "R": "L",
            "R'": "L'",
            "R2": "L2",
            "L": "R",
            "L'": "R'",
            "L2": "R2",
            "F": "B",
            "F'": "B'",
            "F2": "B2",
            "B": "F",
            "B'": "F'",
            "B2": "F2",
        },
    }

    mapping = INVERSE_MOVE_MAP.get(rotation_move, {})
    return " ".join(mapping.get(m, m) for m in notation.split())


def decimal_to_faces(number: int):
    faces = ["R", "L", "U", "D", "F", "B", "1", "2"]
    result = ""

    for i, face in enumerate(faces):
        if number & (1 << i):
            result += face

    return result


def binary_to_faces(binary: str):
    faces = ["R", "L", "U", "D", "F", "B", "1", "2"]
    result = ""

    for i, bit in enumerate(binary[::-1]):
        if bit == "1" and i < len(faces):
            result += faces[i]

    return result


def format_pairs_with_faces(pairs):
    return [
        (decimal_to_faces(edge), decimal_to_faces(corner)) for edge, corner in pairs
    ]


if __name__ == "__main__":
    print(decimal_to_faces(102))
    # notation = "L' U2 L2 U L2 U L U U U U R U' R' F R' F' R U U U U R' U' R U' R' U' R U U U L' U' L U2 L' U L"
    # reduce(notation)
