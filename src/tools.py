def reduce(notation: str) -> str:
    if not notation or not notation.strip():
        return ""

    SUFFIX_TO_QUARTERS = {"'": 3, "2": 2}
    QUARTERS_TO_SUFFIX = {1: "", 2: "2", 3: "'"}

    def get_quarters(move: str) -> int:
        return SUFFIX_TO_QUARTERS.get(move[-1], 1)

    notes = notation.strip().split()
    reduced = []
    i = 0

    while i < len(notes):
        face = notes[i][0]
        quarters = 0

        while i < len(notes) and notes[i][0] == face:
            quarters += get_quarters(notes[i])
            i += 1

        quarters %= 4

        if quarters in QUARTERS_TO_SUFFIX:
            reduced.append(face + QUARTERS_TO_SUFFIX[quarters])

    result = " ".join(reduced)
    return result if result == notation.strip() else reduce(result)


def inverse(notation: str) -> str:
    if not notation or not notation.strip():
        return ""

    def invert_move(move: str) -> str:
        if move.endswith("2"):
            return move
        elif move.endswith("'"):
            return move[:-1]
        else:
            return move + "'"

    moves = notation.strip().split()
    inverted_moves = [invert_move(move) for move in reversed(moves)]
    return " ".join(inverted_moves)


def remap_notation_by_rotation(notation: str, rotation_move: str):
    ROTATION_MAPS = {
        "z":  {"R": "D", "L": "U", "U": "R", "D": "L",
               "r": "d", "l": "u", "u": "r", "d": "l"},
        "z'": {"R": "U", "L": "D", "U": "L", "D": "R",
               "r": "u", "l": "d", "u": "l", "d": "r"},
        "z2": {"R": "L", "L": "R", "U": "D", "D": "U",
               "r": "l", "l": "r", "u": "d", "d": "u"},
        "x":  {"U": "B", "D": "F", "F": "U", "B": "D",
               "u": "b", "d": "f", "f": "u", "b": "d"},
        "x'": {"U": "F", "D": "B", "F": "D", "B": "U",
               "u": "f", "d": "b", "f": "d", "b": "u"},
        "x2": {"U": "D", "D": "U", "F": "B", "B": "F",
               "u": "d", "d": "u", "f": "b", "b": "f"},
        "y":  {"R": "F", "F": "L", "L": "B", "B": "R",
               "r": "f", "f": "l", "l": "b", "b": "r"},
        "y'": {"R": "B", "F": "R", "L": "F", "B": "L",
               "r": "b", "f": "r", "l": "f", "b": "l"},
        "y2": {"R": "L", "L": "R", "F": "B", "B": "F",
               "r": "l", "l": "r", "f": "b", "b": "f"},
    }
    SLICE_MAPS = {
        "z":  {"M":"E'", "M'":"E", "M2":"E2", "E":"M", "E'": "M'", "E2":"M2"},
        "z'": {"M": "E", "M'":"E'","M2":"E2", "E":"M'", "E'":"M", "E2":"M2"},
        "z2": {"M": "M'", "M'":"M", "E":"E'", "E'":"E"},
        "x":  {"E": "S", "E'": "S'", "E2":"S2", "S": "E'", "S'":"E", "S2":"E2"},
        "x'": {"E": "S'", "E'":"S", "E2":"S2", "S": "E", "S'":"E'", "S2":"E2"},
        "x2": {"E": "E'", "E'": "E", "S": "S'", "S'": "S"},
        "y":  {"M": "S'", "M'": "S", "M2": "S2", "S": "M", "S'": "M'", "S2": "M2"},
        "y'": {"M": "S", "M'": "S'", "M2": "S2", "S": "M'", "S'": "M", "S2": "M2"},
        "y2": {"M": "M'", "M'": "M", "S": "S'", "S'": "S"}
    }

    mapping = ROTATION_MAPS.get(rotation_move, {})
    slicing = SLICE_MAPS.get(rotation_move, {})
    def remap_move(move: str) -> str:
        base = move[0]
        modifier = move[1:]
        new_base = mapping.get(base, base)
        new_move = new_base + modifier
        return slicing.get(new_move, new_move)  # ✅ slice mapping po każdym ruchu

    return " ".join(remap_move(m) for m in notation.split())


FACES = ["R", "L", "U", "D", "F", "B", "1", "2"]

def decimal_to_faces(number: int):
    return "".join(face for i, face in enumerate(FACES) if number & (1 << i))

def binary_to_faces(binary: str):
    return decimal_to_faces(int(binary, 2))

def format_pairs_with_faces(pairs):
    return [(decimal_to_faces(edge), decimal_to_faces(corner)) for edge, corner in pairs]

if __name__ == "__main__":
    print(decimal_to_faces(102))
