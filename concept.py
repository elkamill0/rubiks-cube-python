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
        # print(numbers)
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
        self.sum = reduce(operator.or_, self.cross)

        def m(pairs):
            return {x: y for x, y in pairs}

        self.R  = m([(5, 33), (33, 9), (9, 17), (17, 5), (69, 97), (97, 73), (73, 81), (81, 69)])
        self.Rp = m([(33, 5), (9, 33), (17, 9), (5, 17), (97, 69), (73, 97), (81, 73), (69, 81)])
        self.R2 = m([(33, 17), (17, 33), (5, 9), (9, 5), (97, 81), (81, 97), (69, 73), (73, 69)])

        self.L  = m([(6, 18), (18, 10), (10, 34), (34, 6), (70, 82), (82, 74), (74, 98), (98, 70)])
        self.Lp = m([(6, 34), (18, 6), (10, 18), (34, 10), (70, 98), (82, 70), (74, 82), (98, 74)])
        self.L2 = m([(6, 10), (10, 6), (18, 34), (34, 18), (70, 74), (74, 70), (82, 98), (98, 82)])

        self.U  = m([(36, 5), (5, 20), (20, 6), (6, 36), (100, 69), (69, 84), (84, 70), (70, 100)])
        self.Up = m([(36, 6), (6, 20), (20, 5), (5, 36), (100, 70), (70, 84), (84, 69), (69, 100)])
        self.U2 = m([(36, 20), (20, 36), (5, 6), (6, 5), (100, 84), (84, 100), (69, 70), (70, 69)])

        self.D  = m([(40, 10), (10, 24), (24, 9), (9, 40), (104, 74), (74, 88), (88, 73), (73, 104)])
        self.Dp = m([(40, 9), (9, 24), (24, 10), (10, 40), (104, 73), (73, 88), (88, 74), (74, 104)])
        self.D2 = m([(40, 24), (24, 40), (10, 9), (9, 10), (104, 88), (88, 104), (74, 73), (73, 74)])

        self.F  = m([(20, 81), (84, 17), (17, 88), (81, 24), (24, 82), (88, 18), (18, 84), (82, 20)])
        self.Fp = m([(84, 18), (20, 82), (82, 24), (18, 88), (88, 17), (24, 81), (81, 20), (17, 84)])
        self.F2 = m([(20, 24), (24, 20), (17, 18), (18, 17), (84, 88), (88, 84), (81, 82), (82, 81)])

        self.B  = m([(36, 98), (100, 34), (34, 104), (98, 40), (40, 97), (104, 33), (33, 100), (97, 36)])
        self.Bp = m([(36, 97), (100, 33), (33, 104), (97, 40), (40, 98), (104, 34), (34, 100), (98, 36)])
        self.B2 = m([(36, 40), (40, 36), (34, 33), (33, 34), (100, 104), (104, 100), (98, 97), (97, 98)])

        self.process_moves = {
            0: lambda: self.apply_list(self.R),
            1: lambda: self.apply_list(self.L),
            2: lambda: self.apply_list(self.U),
            3: lambda: self.apply_list(self.D),
            4: lambda: self.apply_list(self.F),
            5: lambda: self.apply_list(self.B)
        }
    
    def apply_list(self, move_map: List):
        for i in range(len(self.cross)):
            diff = move_map.get(self.cross[i],self.cross[i])
            # print(self.cross[i], diff)
            if self.cross[i] != diff:
                self.cross[i] = diff
                # print(self.cross)
                self.sum = reduce(operator.or_, self.cross)
                # self.sum = (-self.cross[i]+diff)
                # print("sum:", self.sum)
        # cube.cross = [move_map.get(x, x) for x in self.cross]

    def check_cross(self):
        return self.cross == self.final_state

    def is_invalid(self, one, two, three):
        return True if (three == one) and ((two^1) == one) else False

    def is_solved(self, layer):
        self.process_moves[layer]()
        # print(layer)


    def combinations(self, depth):
        def recurse(path):
            if len(path) == depth:
                return

            for i in range(0, path[-1]):
                # print("actual move:", i)
                if len(path) >= 2 and self.is_invalid(i, path[-1], path[-2]):
                    continue

                if not bool(self.sum & pow(2,i)):
                    continue

                for _ in range(3):
                    self.is_solved(i)
                    recurse(path + [i])
                    self.is_solved(i)

            for i in range(path[-1]+1, 6):
                # print("actual move:", i)

                if len(path) >= 2 and self.is_invalid(i, path[-1], path[-2]):
                    continue

                if not bool(self.sum & pow(2,i)):
                    continue

                for _ in range(3):
                    self.is_solved(i)
                    recurse(path + [i])
                    self.is_solved(i)

        for i in range(6):
            for _ in range(3):
                # print("actual move:", i)
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
    times = 10
    for i in range(times):
        start = time()
        cube.combinations(5)
        end = time()
        sum += end-start
    print(sum/times)
    # cube.combinations(1)
