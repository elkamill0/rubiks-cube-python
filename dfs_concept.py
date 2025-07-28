from cube import Cube
import numpy as np
from typing import List
from collections import deque
import psutil, os
import struct

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
        # return [self.color_to_binary[n[0]]*(-1 if n[1] else 1) for n in numbers]
        return [self.color_to_binary[n[0]]+(64 if n[1] else 0) for n in numbers]


    def binary_or_number(self, list_of_biaries):
        result = list_of_biaries[0]
        for val in list_of_biaries[1:]:
            result |= val
        return result
    
    def final_solution(self):
        conversion = self.conversion(self.cross)
        return self.binary_or_number(conversion)

        
    



class CubeMoves:
    def __init__(self, state: List, final_state: List):
        self.state = bytes(state)
        self.final_state = bytes(final_state)
        self.stack = []
        self.min = 0

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
             0: lambda state: self.apply_list(state, self.R),
             1: lambda state: self.apply_list(state, self.R2),
             2: lambda state: self.apply_list(state, self.Rp),
             3: lambda state: self.apply_list(state, self.L),
             4: lambda state: self.apply_list(state, self.L2),
             5: lambda state: self.apply_list(state, self.Lp),
             6: lambda state: self.apply_list(state, self.U),
             7: lambda state: self.apply_list(state, self.U2),
             8: lambda state: self.apply_list(state, self.Up),
             9: lambda state: self.apply_list(state, self.D),
            10: lambda state: self.apply_list(state, self.D2),
            11: lambda state: self.apply_list(state, self.Dp),
            12: lambda state: self.apply_list(state, self.F),
            13: lambda state: self.apply_list(state, self.F2),
            14: lambda state: self.apply_list(state, self.Fp),
            15: lambda state: self.apply_list(state, self.B),
            16: lambda state: self.apply_list(state, self.B2),
            17: lambda state: self.apply_list(state, self.Bp),
        }

    def check_cross(self):
        return self.state == self.final_state
    
    def apply_list(self, state: List, move_map: List):
        return bytes([move_map.get(x, x) for x in state])

    def is_invalid(self, one, two, three):
        return True if (three == one) and ((two^1) == one) else False

    def combinations(self, depth):
        for i in range(0, 18, 3):
            state = bytes(self.process_moves[i](self.state))
            if not (state == self.state):
                self.stack.append(SearchCube(state=state, path=i, parent=None, depth=1))
                for j in range(1,3):
                    self.stack.append(SearchCube(state=bytes(self.process_moves[i+j](self.state)), path=i+j, parent=None, depth=1))
        
        while self.stack:

            node = self.stack.pop()
            if node.state == self.final_state:
                while node.parent != None:
                    print(node.path)
                    node = node.parent
                print(node.path)
                print("-------")
                continue
            # print(node.path)
            # mem = round(psutil.Process(os.getpid()).memory_info().rss / 1024**2, 2)
            # if mem > self.min:
            #     self.min = mem
            #     print(mem)
            # print(mem)
            if node.depth == depth:
                continue
            for i in range(0, 18, 3):
                if (i//3 == node.path//3):
                    continue
                if node.parent and self.is_invalid(i//3, node.path//3, node.parent.path//3):
                    continue
                state = bytes(self.process_moves[i](node.state))
                if not (state == node.state):
                    self.stack.append(SearchCube(state=bytes(state), path=i, parent=node, depth=node.depth+1))
                    for j in range(1,3):
                        self.stack.append(SearchCube(state=bytes(self.process_moves[i+j](node.state)), path=i+j, parent=node, depth=node.depth+1))


class SearchCube:
    __slots__ = ('state', 'path', 'parent', 'depth')

    def __init__(self, state: bytes, path: int, parent, depth: int):
        self.state = bytes(state)
        self.path = path
        self.parent = parent
        self.depth = depth


if __name__ == "__main__":
    # cube = Cube("R U F B")
    # cube = Cube("R U")
    cube = Cube("L D' L D R F R L2 B R2 D2 R2 F2 U2 B R2 B L2 F D'")
    # cube = Cube("R")
    b = BinaryRepresentation(cube)
    conversion = b.conversion(b.cross)
    print(conversion)
    print("---------------")


    from time import time

    cube = CubeMoves(bytes(conversion), bytes((40, 9, 24, 10)))
    cube1 = Cube()
    cube1 = Cube("L2 B2 L2 U' B2 L2 U' R2 D' L2 U B2 R B' D F L F2 D F2")
    # sum = 0
    # times = 2
    # for i in range(times):
    #     start = time()
    #     cube.combinations(7)
    #     end = time()
    #     sum += end-start
    # print(round(sum/times,4))
    start = time()
    cube.combinations(6)
    stop = time()
    print(stop-start)
    print(round(psutil.Process(os.getpid()).memory_info().rss / 1024**2,2))
