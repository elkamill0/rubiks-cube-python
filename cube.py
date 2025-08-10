import numpy as np
from moves.moves import Moves
import scramble
import convert
import visualization



class Cube(Moves):
    def __init__(self, notation: str = None, state: str = None):
        self.reset()
        if notation: 
            convert.sequence_to_moves(moves=notation, cube=self)
        elif state:
            self.corners, self.edges, self.centers = visualization.state_to_cube(state=state)

    def __str__(self):
        return visualization.cube_to_color(self.corners, self.edges, self.centers, show=True)
    
    def move(self, notation: str) -> None:
        convert.sequence_to_moves(notation, self)

    def get_state(self):
        return convert.cube_to_color(self.corners, self.edges, self.centers, show=False)
    
    # def get_cube(self):
        # return kk

    def reset(self) -> None:
        self.corners = np.zeros((8, 2), dtype=np.int8)
        self.corners[:, 0] = np.arange(8)
        self.edges = np.zeros((12, 2), dtype=np.int8)
        self.edges[:, 0] = np.arange(12)
        self.centers = np.arange(6, dtype=np.uint8)

    # def f2l(self, length):
    #     return f2l.check_f2l_pair(length, self.cube)

if __name__ == "__main__":
    # print(scramble.generate_scramble(10))
    notation="B' U L' B2 R F2 L' R2 B2 U2 R2 D2 F2 D' B' U L2 B' D F"
    cube = Cube(notation=notation)
    print(cube.get_state())
    # cube.R()
    print(cube)