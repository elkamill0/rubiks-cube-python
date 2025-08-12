import convert
import cube_solver
from typing import List

class Cross:
    def __init__(self, cube):
        self.cube = cube
        self.start_state = convert.cube_to_binary_cross(self.cube)
        from cube import Cube
        self.end_state = convert.cube_to_binary_cross(Cube())

    def find_cross(self, length: int) -> List[str]:
        solutions = self.__find_solutions(length)
        return self.__convert_cross_numbers_to_notation(solutions)

    def __find_solutions(self, length: int) -> List[List[int]]:
        return cube_solver.combinations(length, self.start_state, self.end_state)

    def __convert_cross_numbers_to_notation(self, notation_int: List[List[int]]) -> List[str]:
        return [' '.join(convert.int_to_notation[x] for x in sol) for sol in notation_int]
            