from cube import Cube
import numpy as np
from convert import notation_to_moves, int_to_notation
from moves.moves import Moves
from time import time
from itertools import product


def map_move_from_numbers(cube: Cube, move_as_int):
    moves_map = {
        0: cube.R(),
        1: cube.L(),
        2: cube.U(),
        3: cube.D(),
        4: cube.F(),
        5: cube.B()
    }
    return moves_map[move_as_int]


def find_cross(length):
    # return scramble.combinations(length, self.cube)
    combination_list = np.array()


def check_cross(cube: Cube):
    if cube.edges[4] == [4,0] and cube.edges[5] == [5,0] and cube.edges[6] == [6,0] and cube.edges[7] == [7,0]:
        return True
    return False

def generate_numpy_combinations(n, limit):
    grid = np.indices((limit,) * n)
    combinations = grid.reshape(n, -1).T
    return combinations

def generate_combinations(n, limit):
    ranges = [range(limit) for _ in range(n)]
    return product(*ranges)  # to jest generator


def is_invalid(one, two, three):
    return True if (three == one) and ((two^1) == one) else False

def is_repeat(one, two):
    return True if two == one else False

def combinations():
    cube = Cube()
    iterator = 0
    for i in range(6):
        for _ in range(3):
            map_move_from_numbers(cube,i)
            for j in range(6):
                if i == j:
                    continue
                for _ in range(3):
                    map_move_from_numbers(cube,j)
                    for k in range(6):
                        if is_invalid(k, j, i) or j == k:
                            continue
                        for _ in range(3):
                            map_move_from_numbers(cube,k)
                            for l in range(6):
                                if is_invalid(l, k, j) or k == l:
                                    continue
                                for _ in range(3):
                                    map_move_from_numbers(cube,l)
                                    # for m in range(6):
                                    #     if is_invalid(m, l, k) or l == m:
                                    #         continue
                                    #     for _ in range(3):
                                    #         map_move_from_numbers(cube,m)
                                    #         # print(i,j,k,l,m)
                                    iterator += 1
                                map_move_from_numbers(cube,l)
                        map_move_from_numbers(cube, k)
                map_move_from_numbers(cube,j)
        map_move_from_numbers(cube,i)

    print(iterator)

    
if __name__ == "__main__":
    a=6
    b=15

    # start = time()
    # generate_combinations(a,15)
    # end = time()
    # print(end-start)


    start = time()
    combinations()
    # generated = generate_numpy_combinations(a,15)
    end = time()
    print(end-start)