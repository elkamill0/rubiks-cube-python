import convert
import cube_solver
from typing import List

class Cross:
    def __init__(self, cube):
        self.cube = cube
        self.cross_edges = [4,5,6,7]
        rot = self.cube.y_rotate % 4
        self.rotated_slots = self.cross_edges[rot:] + self.cross_edges[:rot]
        self.start_state = convert.edges_to_binary(self.cube, self.cross_edges)
        from cube import Cube
        self.end_state = convert.edges_to_binary(Cube(), self.cross_edges)


    def find_cross(self, length: int) -> List[str]:
        solutions = self.__find_solutions(length)
        return [(self.__convert_cross_numbers_to_notation([sol])[0], "cross") for sol in solutions]

    def __find_solutions(self, length: int) -> List[List[int]]:
        return cube_solver.combinations(length, self.start_state, self.end_state)

    def __convert_cross_numbers_to_notation(self, notation_int: List[List[int]]) -> List[str]:
        return [' '.join(convert.int_to_notation[x] for x in sol) for sol in notation_int]
    
    def is_solved(self) -> bool:
        for slot, edge in zip(self.rotated_slots, self.cross_edges):
            if not (self.cube.edges[slot] == [edge, 0]).all():
                return False

        return True
            