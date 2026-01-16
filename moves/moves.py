from moves.moves_corners import MovesCorners
from moves.moves_edges import MovesEdges
from moves.moves_centers import MovesCenters
import numpy as np


class Moves(MovesCorners, MovesEdges, MovesCenters):
    def __init__(self, corners, edges):
        self.corners = corners
        self.edges = edges
        self.centers = centers

move_names = [
    "R", "Rp", "R2",
    "L", "Lp", "L2",
    "U", "Up", "U2",
    "D", "Dp", "D2",
    "F", "Fp", "F2",
    "B", "Bp", "B2",
    "E", "Ep", "E2",
    "M", "Mp", "M2",
    "S", "Sp", "S2",
    "y", "yp", "y2",
    "x", "xp", "x2",
    "z", "zp", "z2",
]

def make_move_function(name):
    def move(self):
        getattr(MovesCorners, name)(self)
        getattr(MovesEdges, name)(self)
        getattr(MovesCenters, name)(self)
    return move

# Dynamicznie tworzymy metody
for move_name in move_names:
    setattr(Moves, move_name, make_move_function(move_name))



if __name__ == "__main__":
    corners = np.zeros((8, 2), dtype=np.int8)
    corners[:, 0] = np.arange(8, dtype=np.int8)
    corners[:, 1] = 0

    edges = np.zeros((12, 2), dtype=np.int16)
    edges[:, 0] = np.arange(12, dtype=np.int16)
    edges[:, 1] = 0

    centers = np.arange(6, dtype=np.uint8)

    moves = Moves(corners, edges)

    moves.R()
    moves.U()


    print(corners)

