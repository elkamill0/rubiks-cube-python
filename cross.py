from cube import Cube
import numpy as np
from convert import notation_to_moves, int_to_move
from moves.moves import Moves



def find_cross(length):
    # return scramble.combinations(length, self.cube)
    combination_list = np.array()


def check_cross(self, cube: Cube):
    if cube.edges[4] == [4,0] and cube.edges[5] == [5,0] and cube.edges[6] == [6,0] and cube.edges[7] == [7,0]:
        return True
    return False


def _loop(self, depth: int, current_combination: list[int], cube: Cube):
    if len(current_combination) >= 2:
        ignored_move = current_combination[-1] // 3
        opposite_move = current_combination[-2] // 3
    else:
        ignored_move = opposite_move = -1

    if check_cross(self.cube):
        move_sequence = ''.join(notation_to_moves(move, cube) for move in current_combination)
        return move_sequence

    if depth == 0:
        return

    for i in range(6):
        if ignored_move == i or (opposite_move == i and ignored_move == (i ^ 1)):
            continue
        for j in range(3):
            move_index = i * 3 + j

            # Zapisz stan przed ruchem
            cube_copy = cube.copy()

            # Wykonaj ruch
            notation_to_moves(int_to_move(move_index))                        

            # Rekurencja
            _loop(depth - 1, current_combination + [move_index], cube)

            # Cofnij stan
            cube[:] = cube_copy

def combinations(cube: np.ndarray, length: int) -> list[str]:
    combination_list.clear()

    for i in range(6):
        for j in range(3):
            move_index_1 = i * 3 + j
            cube_copy_1 = cube.copy()
            moving[i](cube, j)

            for k in range(6):
                if i == k:
                    continue
                for l in range(3):
                    move_index_2 = k * 3 + l
                    cube_copy_2 = cube.copy()
                    moving[k](cube, l)

                    _loop(length - 2, [move_index_1, move_index_2], cube)

                    cube[:] = cube_copy_2
            cube[:] = cube_copy_1

    print(f"exact moves: {len(combination_list)}")
    return combination_list



