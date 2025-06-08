import numpy as np 

from moves.moves import Moves


def cube_to_color(corners, edges, centers, show: bool = False) -> str:
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

def state_to_cube(state: str):
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
    corners_from_state = ((state[0], state[9], state[38]), (state[2], state[36], state[29]), 
                             (state[8], state[27], state[20]), (state[6], state[18], state[11]),
                             (state[51], state[44], state[15]), (state[53], state[35], state[42]),
                             (state[47], state[26], state[33]), (state[45], state[17], state[24]))

    edges_from_state = ((state[1], state[37]), (state[5], state[28]), (state[7], state[19]), (state[3], state[10]),
                           (state[52], state[43]), (state[50], state[34]), (state[46], state[25]), (state[48], state[16]),
                           (state[41], state[12]), (state[39], state[32]), (state[23], state[30]), (state[21], state[14]))

    centers_from_state = np.array((state[4], state[13], state[22], state[31], state[40], state[49]))

    def map_corners(element):
        return color_to_corners.get(element, np.array([None, None]))

    def map_edges(element):
        return color_to_edges.get(element, np.array([None, None]))

    mapped_corners = np.array(list(map(map_corners, corners_from_state)))
    mapped_edges = np.array(list(map(map_edges, edges_from_state)))
    color_to_centers = centers_from_state.astype(int)

    return mapped_corners, mapped_edges, color_to_centers


if __name__ == "__main__":
    corners = np.zeros((8, 2), dtype=np.int8)
    corners[:, 0] = np.arange(8, dtype=np.int8)
    corners[:, 1] = 0

    edges = np.zeros((12, 2), dtype=np.int16)
    edges[:, 0] = np.arange(12, dtype=np.int16)
    edges[:, 1] = 0

    centers = np.arange(6, dtype=np.uint8)

    moves = Moves(corners, edges)

    # notation = "302101501443513544230422322450333021115542542003501104"
    notation = "545305011121015533220120050443132344212543501432400423"
    corners, edges, centers = state_to_cube(state=notation)
    print(cube_to_color(corners, edges, centers))
