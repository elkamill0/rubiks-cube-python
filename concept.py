from cube import Cube
import numpy as np
from typing import List
from functools import reduce
import operator

class BinaryRepresentation:
    def __init__(self, cube: Cube):
        self.cross = self.find_cross_blocks(cube=cube)
        self.color_to_binary = {
            0: 36,
            1: 5,
            2: 20,
            3: 6,
            4: 40,
            5: 9,
            6: 24,
            7: 10,
            8: 34,
            9: 33,
            10: 17,
            11: 18,
        }

    def find_cross_blocks(self, cube: Cube):
        target_values = [4,5,6,7]
        return [(np.where(cube.edges == val)[0][0], cube.edges[np.where(cube.edges == val)[0][0]][1]) for val in target_values]

    def conversion(self, numbers):
        print(numbers)
        return [self.color_to_binary[n[0]]*(-1 if n[1] else 1) for n in numbers]

    def binary_or_number(self, list_of_biaries):
        result = list_of_biaries[0]
        for val in list_of_biaries[1:]:
            result |= val
        return result
    
    def final_solution(self):
        conversion = self.conversion(self.cross)
        return self.binary_or_number(conversion)

        
    
    
class CubeMoves:
    def __init__(self, cross: List, final_state: List):
        self.cross = cross
        self.final_state = final_state

        def m(pairs):
            return {x: y for x, y in pairs}

        self.R  = m([(5, 33), (33, 9), (9, 17), (17, 5), (-5, -33), (-33, -9), (-9, -17), (-17, -5)])
        self.Rp = m([(33, 5), (9, 33), (17, 9), (5, 17), (-33, -5), (-9, -33), (-17, -9), (-5, -17)])
        self.R2 = m([(33, 17), (17, 33), (5, 9), (9, 5), (-33, -17), (-17, -33), (-5, -9), (-9, -5)])

        self.L  = m([(6, 18), (18, 10), (10, 34), (34, 6), (-6, -18), (-18, -10), (-10, -34), (-34, -6)])
        self.Lp = m([(6, 34), (18, 6), (10, 18), (34, 10), (-6, -34), (-18, -6), (-10, -18), (-34, -10)])
        self.L2 = m([(6, 10), (10, 6), (18, 34), (34, 18), (-6, -10), (-10, -6), (-18, -34), (-34, -18)])

        self.U  = m([(36, 5), (5, 20), (20, 6), (6, 36), (-36, -5), (-5, -20), (-20, -6), (-6, -36)])
        self.Up = m([(36, 6), (6, 20), (20, 5), (5, 36), (-36, -6), (-6, -20), (-20, -5), (-5, -36)])
        self.U2 = m([(36, 20), (20, 36), (5, 6), (6, 5), (-36, -20), (-20, -36), (-5, -6), (-6, -5)])

        self.D  = m([(40, 10), (10, 24), (24, 9), (9, 40), (-40, -10), (-10, -24), (-24, -9), (-9, -40)])
        self.Dp = m([(40, 9), (9, 24), (24, 10), (10, 40), (-40, -9), (-9, -24), (-24, -10), (-10, -40)])
        self.D2 = m([(40, 24), (24, 40), (10, 9), (9, 10), (-40, -24), (-24, -40), (-10, -9), (-9, -10)])

        self.F  = m([(20, -17), (-20, 17), (17, -24), (-17, 24), (24, -18), (-24, 18), (18, -20), (-18, 20)])
        self.Fp = m([(-20, 18), (20, -18), (-18, 24), (18, -24), (-24, 17), (24, -17), (-17, 20), (17, -20)])
        self.F2 = m([(20, 24), (24, 20), (17, 18), (18, 17), (-20, -24), (-24, -20), (-17, -18), (-18, -17)])

        self.B  = m([(36, -34), (-36, 34), (34, -40), (-34, 40), (40, -33), (-40, 33), (33, -36), (-33, 36)])
        self.Bp = m([(36, -33), (-36, 33), (33, -40), (-33, 40), (40, -34), (-40, 34), (34, -36), (-34, 36)])
        self.B2 = m([(36, 40), (40, 36), (34, 33), (33, 34), (-36, -40), (-40, -36), (-34, -33), (-33, -34)])

        self.process_moves = {
            0: lambda: self.apply_list(self.R),
            1: lambda: self.apply_list(self.L),
            2: lambda: self.apply_list(self.U),
            3: lambda: self.apply_list(self.D),
            4: lambda: self.apply_list(self.F),
            5: lambda: self.apply_list(self.B)
        }

    def apply(self, move_map, x):
        self.cross = move_map.get(x,x)
        return move_map.get(x, x)
    

    def apply_list(self, move_map):
        cube.cross = [move_map.get(x, x) for x in self.cross]
        # return [move_map.get(x, x) for x in xs]

    def check_cross(self):
        return self.cross == self.final_state

    def is_invalid(self, one, two, three):
        return True if (three == one) and ((two^1) == one) else False

    def is_repeat(self, one, two):
        return True if two == one else False    

    def is_solved(self, layer):
        self.process_moves[layer]()
        print(layer)


    def combinations(self, depth):
        def recurse(path):
            if len(path) == depth:
                return

            for i in range(0, path[-1]):
                if len(path) >= 2 and self.is_invalid(i, path[-1], path[-2]):
                    continue

                if not bool(reduce(operator.or_, self.cross) & pow(2,i)):
                    continue

                for _ in range(3):
                    self.is_solved(i)
                    recurse(path + [i])
                    self.is_solved(i)

            for i in range(path[-1]+1, 6):

                if len(path) >= 2 and self.is_invalid(i, path[-1], path[-2]):
                    continue

                if not bool(reduce(operator.or_, self.cross) & pow(2,i)):
                    continue

                for _ in range(3):
                    self.is_solved(i)
                    recurse(path + [i])
                    self.is_solved(i)

        for i in range(6):
            for _ in range(3):
                self.is_solved(i)
                recurse([i])
                self.is_solved(i)
        # recurse([])


if __name__ == "__main__":
    cube = Cube("R")
    b = BinaryRepresentation(cube)
    conversion = b.conversion(b.cross)
    print(conversion)


    from time import time

    cube = CubeMoves(conversion, [40, 9, 24, 10])
    cube1 = Cube()
    cube1 = Cube("L2 B2 L2 U' B2 L2 U' R2 D' L2 U B2 R B' D F L F2 D F2")
    sum = 0
    times = 3
    for i in range(times):
        start = time()
        cube.combinations(1)
        end = time()
        sum += end-start
    print(sum/times)
