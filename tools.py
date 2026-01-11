def reduce(notation: str) -> str:
    note = notation.strip().split()
    if not(len(note)):
        return 

    def note_to_quarters(note):
        return 3 if note.endswith("'") else 2 if note.endswith("2") else 1

    i = 1
    combo = 0
    new_notation = ""
    changed = False
    while i < len(note):
        if note[i-1][0] == note[i][0]:
            combo+=note_to_quarters(note[i-1]) 
            changed = True
        else:
            if combo > 0:
                combo+=note_to_quarters(note[i-1])
                combo%=4
                if combo == 1:
                    new_notation += note[i-1][0]+" "
                elif combo == 2:
                    new_notation += note[i-1][0]+"2"+" "
                elif combo == 3:
                    new_notation += note[i-1][0]+"'"+" "
                combo = 0
            else:
                new_notation+=note[i-1]+" "
        i+=1
    new_notation+=note[i-1]

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
        "z2": "z2"
    }

    moves = notation.split()
    inverted_moves = [inverse_mapping[move] for move in reversed(moves)]
    return ' '.join(inverted_moves)


if __name__ == "__main__":
    notation = "L' U2 L2 U L2 U L U U U U R U' R' F R' F' R U U U U R' U' R U' R' U' R U U U L' U' L U2 L' U L"
    reduce(notation)