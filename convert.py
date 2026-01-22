from moves.moves import Moves
import numpy as np


notation_to_int = {
    "R": 0,
    "R2": 1,
    "R'": 2,
    "L": 3,
    "L2": 4,
    "L'": 5,
    "U": 6,
    "U2": 7,
    "U'": 8,
    "D": 9,
    "D2": 10,
    "D'": 11,
    "F": 12,
    "F2": 13,
    "F'": 14,
    "B": 15,
    "B2": 16,
    "B'": 17
}

int_to_notation = {
    0: "R",
    1: "R2",
    2: "R'",
    3: "L",
    4: "L2",
    5: "L'",
    6: "U",
    7: "U2",
    8: "U'",
    9: "D",
    10: "D2",
    11: "D'",
    12: "F",
    13: "F2",
    14: "F'",
    15: "B",
    16: "B2",
    17: "B'"
}



def state_to_cube(state: str):
    if not isinstance(state, str):
        raise TypeError("Argument 'state' musi być napisem (str).")

    if len(state) != 54:
        raise ValueError(f"Stan kostki musi mieć długość 54")

    if not all(ch.isdigit() for ch in state):
        raise ValueError("Stan kostki może zawierać tylko cyfry (0–9).")
    
    color_to_corners = {
        ('0','1','4'): np.array((0,0)), ('4','0','1'): np.array((0,1)), ('1','4','0'): np.array((0,2)),
        ('0','4','3'): np.array((1,0)), ('3','0','4'): np.array((1,1)), ('4','3','0'): np.array((1,2)),
        ('0','3','2'): np.array((2,0)), ('2','0','3'): np.array((2,1)), ('3','2','0'): np.array((2,2)),
        ('0','2','1'): np.array((3,0)), ('1','0','2'): np.array((3,1)), ('2','1','0'): np.array((3,2)),
        ('5','4','1'): np.array((4,0)), ('1','5','4'): np.array((4,1)), ('4','1','5'): np.array((4,2)),
        ('5','3','4'): np.array((5,0)), ('4','5','3'): np.array((5,1)), ('3','4','5'): np.array((5,2)),
        ('5','2','3'): np.array((6,0)), ('3','5','2'): np.array((6,1)), ('2','3','5'): np.array((6,2)),
        ('5','1','2'): np.array((7,0)), ('2','5','1'): np.array((7,1)), ('1','2','5'): np.array((7,2))
    }

    color_to_edges = {
        ('0','4'):  np.array((0,0)), ('4','0'):  np.array((0,1)),
        ('0','3'):  np.array((1,0)), ('3','0'):  np.array((1,1)),
        ('0','2'):  np.array((2,0)), ('2','0'):  np.array((2,1)),
        ('0','1'):  np.array((3,0)), ('1','0'):  np.array((3,1)),
        ('5','4'):  np.array((4,0)), ('4','5'):  np.array((4,1)),
        ('5','3'):  np.array((5,0)), ('3','5'):  np.array((5,1)),
        ('5','2'):  np.array((6,0)), ('2','5'):  np.array((6,1)),
        ('5','1'):  np.array((7,0)), ('1','5'):  np.array((7,1)),
        ('4','1'):  np.array((8,0)), ('1','4'):  np.array((8,1)),
        ('4','3'):  np.array((9,0)), ('3','4'):  np.array((9,1)),
        ('2','3'): np.array((10,0)), ('3','2'): np.array((10,1)),
        ('2','1'): np.array((11,0)), ('1','2'): np.array((11,1))
    }

    corners_from_state = (
        (state[0], state[9],  state[38]), (state[2], state[36], state[29]),
        (state[8], state[27], state[20]), (state[6], state[18], state[11]),
        (state[51], state[44], state[15]), (state[53], state[35], state[42]),
        (state[47], state[26], state[33]), (state[45], state[17], state[24])
    )

    edges_from_state = (
        (state[1],  state[37]), (state[5],  state[28]),
        (state[7],  state[19]), (state[3],  state[10]),
        (state[52], state[43]), (state[50], state[34]),
        (state[46], state[25]), (state[48], state[16]),
        (state[41], state[12]), (state[39], state[32]),
        (state[23], state[30]), (state[21], state[14])
    )

    centers_from_state = np.array((state[4], state[13], state[22], state[31], state[40], state[49])).astype(int)

    def map_corners(element):
        val = color_to_corners.get(element)
        if val is None:
            raise ValueError(f"Niepoprawny układ kolorów narożnika")
        return val

    def map_edges(element):
        val = color_to_edges.get(element)
        if val is None:
            raise ValueError(f"Niepoprawny układ kolorów krawędzi")
        return val

    mapped_corners = np.array([map_corners(e) for e in corners_from_state])
    mapped_edges   = np.array([map_edges(e)   for e in edges_from_state])

    return mapped_corners, mapped_edges, centers_from_state


def notation_to_moves(moves: str, cube):

    move_map = {
        'R': cube.R,
        "R'": cube.Rp,
        'R2': cube.R2,
        'L': cube.L,
        "L'": cube.Lp,
        'L2': cube.L2,
        'U': cube.U,
        "U'": cube.Up,
        'U2': cube.U2,
        'D': cube.D,
        "D'": cube.Dp,
        'D2': cube.D2,
        'F': cube.F,
        "F'": cube.Fp,
        'F2': cube.F2,
        'B': cube.B,
        "B'": cube.Bp,
        'B2': cube.B2
    }

    moves_list = moves.split()
    for move in moves_list:
        if move in move_map:
            move_map[move]()

    return cube


def cube_to_color(cube, show: bool = False) -> str:

    corners = cube.corners
    edges = cube.edges
    centers = cube.centers
    
    corners_to_color = {
        0: ['0','1','4'],
        1: ['0','4','3'],
        2: ['0','3','2'],
        3: ['0','2','1'],
        4: ['5','4','1'],
        5: ['5','3','4'],
        6: ['5','2','3'],
        7: ['5','1','2']
    }
    edges_to_color = {
        0: ['0','4'],
        1: ['0','3'],
        2: ['0','2'],
        3: ['0','1'],
        4: ['5','4'],
        5: ['5','3'],
        6: ['5','2'],
        7: ['5','1'],
        8: ['4','1'],
        9: ['4','3'],
        10:['2','3'],
        11:['2','1'] 
    }

    mapped_edges = np.array([edges_to_color[i] for i in edges[:, 0]])
    mapped_corners = np.array([corners_to_color[i] for i in corners[:, 0]])

    rotated_edges = np.array([np.roll(mapped_edge, edge[1]) for mapped_edge, edge in zip(mapped_edges, edges)])
    rotated_corners = np.array([np.roll(mapped_corner, edge[1]) for mapped_corner, edge in zip(mapped_corners, corners)])

    mapped_centers = np.array(centers, dtype=str)

    numbers = [
        rotated_corners[0,0], rotated_edges[0,0], rotated_corners[1,0],
        rotated_edges[3,0], mapped_centers[0], rotated_edges[1,0],
        rotated_corners[3,0], rotated_edges[2,0], rotated_corners[2,0],
        rotated_corners[0,1], rotated_edges[3,1], rotated_corners[3,2],
        rotated_edges[8,1], mapped_centers[1], rotated_edges[11,1],
        rotated_corners[4,2], rotated_edges[7,1], rotated_corners[7,1],
        rotated_corners[3,1], rotated_edges[2,1], rotated_corners[2,2],
        rotated_edges[11,0], mapped_centers[2], rotated_edges[10,0],
        rotated_corners[7,2], rotated_edges[6,1], rotated_corners[6,1],
        rotated_corners[2,1], rotated_edges[1,1], rotated_corners[1,2],
        rotated_edges[10,1], mapped_centers[3], rotated_edges[9,1],
        rotated_corners[6,2], rotated_edges[5,1], rotated_corners[5,1],
        rotated_corners[1,1], rotated_edges[0,1], rotated_corners[0,2],
        rotated_edges[9,0], mapped_centers[4], rotated_edges[8,0],
        rotated_corners[5,2], rotated_edges[4,1], rotated_corners[4,1],
        rotated_corners[7,0], rotated_edges[6,0], rotated_corners[6,0],
        rotated_edges[7,0], mapped_centers[5], rotated_edges[5,0],
        rotated_corners[4,0], rotated_edges[4,0], rotated_corners[5,0]
    ]

    if show:
        return(f"""
            {rotated_corners[0, 0]}{rotated_edges[0, 0]}{rotated_corners[1, 0]}
            {rotated_edges[3, 0]}{centers[0]}{rotated_edges[1, 0]}
            {rotated_corners[3, 0]}{rotated_edges[2, 0]}{rotated_corners[2, 0]}
        ---
    {rotated_corners[0, 1]}{rotated_edges[3, 1]}{rotated_corners[3, 2]}|{rotated_corners[3, 1]}{rotated_edges[2, 1]}{rotated_corners[2, 2]}|{rotated_corners[2, 1]}{rotated_edges[1, 1]}{rotated_corners[1, 2]}|{rotated_corners[1, 1]}{rotated_edges[0, 1]}{rotated_corners[0, 2]}
    {rotated_edges[8, 1]}{centers[1]}{rotated_edges[11, 1]}|{rotated_edges[11, 0]}{centers[2]}{rotated_edges[10, 0]}|{rotated_edges[10, 1]}{centers[3]}{rotated_edges[9, 1]}|{rotated_edges[9, 0]}{centers[4]}{rotated_edges[8, 0]}
    {rotated_corners[4, 2]}{rotated_edges[7, 1]}{rotated_corners[7, 1]}|{rotated_corners[7, 2]}{rotated_edges[6, 1]}{rotated_corners[6, 1]}|{rotated_corners[6, 2]}{rotated_edges[5, 1]}{rotated_corners[5, 1]}|{rotated_corners[5, 2]}{rotated_edges[4, 1]}{rotated_corners[4, 1]}
        ---
            {rotated_corners[7, 0]}{rotated_edges[6, 0]}{rotated_corners[6, 0]}
            {rotated_edges[7, 0]}{centers[5]}{rotated_edges[5, 0]}
            {rotated_corners[4, 0]}{rotated_edges[4, 0]}{rotated_corners[5, 0]}""")


    return ''.join(numbers)


def int_to_moves_scramble(nums: list[int]) -> str:
    return " ".join(int_to_notation[number] for number in nums if number in int_to_notation)



def edges_to_binary(cube, target: list[int]) -> list[int]:
    color_to_binary = {
        0: 36,  1: 5,   2: 20,  3: 6,
        4: 40,  5: 9,   6: 24,  7: 10,
        8: 34,  9: 33, 10: 17, 11: 18,
    }

    # target_values = [4, 5, 6, 7]
    cross = [
        (np.where(cube.edges == val)[0][0],
         cube.edges[np.where(cube.edges == val)[0][0]][1])
        for val in target
    ]
    return [color_to_binary[n[0]]+(64 if n[1] else 0) for n in cross]

def corners_to_binary(cube, target: list[int]) -> list[int]:
    color_to_binary = {
        0: 38,  1: 37,  2: 21,  3: 22,
        4: 42,  5: 41,  6: 25,  7: 26
    }

    # target_values = [4, 5, 6, 7]
    cross = [
        (int(np.where(cube.corners == val)[0][0]),
         int(cube.corners[np.where(cube.corners == val)[0][0]][1]))
        for val in target
    ]
    return [color_to_binary[n[0]]+(n[1] * 64) for n in cross]

def replace_numbers_with_colors(ascii_cube: str) -> str:
    number_to_emoji = {
        "0": "⬜",  # white
        "1": "🟧",  # orange
        "2": "🟩",  # green
        "3": "🟥",  # red
        "4": "🟦",  # blue
        "5": "🟨",  # yellow
    }

    result = ascii_cube
    for number, emoji in number_to_emoji.items():
        result = result.replace(number, emoji)
    
    return result


if __name__ == "__main__":
    corners = np.zeros((8, 2), dtype=np.int8)
    corners[:, 0] = np.arange(8, dtype=np.int8)
    corners[:, 1] = 0

    edges = np.zeros((12, 2), dtype=np.int16)
    edges[:, 0] = np.arange(12, dtype=np.int16)
    edges[:, 1] = 0

    centers = np.arange(6, dtype=np.uint8)

    moves = Moves(corners, edges)

    notation = "545305011121015533220120050443132344212543501432400423"
    corners, edges, centers = state_to_cube(state=notation)
    print(cube_to_color(corners, edges, centers))