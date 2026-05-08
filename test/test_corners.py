import random

import numpy as np

from src.cube import Cube


def random_moves(cube, n=20):
    moves = ["R", "Rp", "L", "Lp", "U", "Up", "D", "Dp", "F", "Fp", "B", "Bp"]
    for _ in range(n):
        getattr(cube, random.choice(moves))()


STATE = "231201341334510413034422433542534215005541101550250022"


def test_R_changes_state():
    c = Cube(state=STATE)
    before = c.corners.copy()
    c.R()
    assert not np.array_equal(c.corners, before)


def test_R_inverse():
    c = Cube(state=STATE)
    start = c.corners.copy()
    c.R()
    c.Rp()
    assert np.array_equal(c.corners, start)


def test_inverse_all_moves():
    moves = ["R", "L", "U", "D", "F", "B"]
    for _ in range(50):
        c = Cube()
        random_moves(c, 20)
        start = c.corners.copy()
        for m in moves:
            from copy import deepcopy

            copy = deepcopy(c)
            getattr(copy, m)()
            getattr(copy, m + "p")()
            assert np.array_equal(copy.corners, start), f"{m} inverse failed"


def test_R4_identity():
    c = Cube(state=STATE)
    start = c.corners.copy()
    c.R()
    c.R()
    c.R()
    c.R()
    assert np.array_equal(c.corners, start)


def test_moves_4_identity():
    moves = ["R", "L", "U", "D", "F", "B"]
    for m in moves:
        c = Cube()
        start = c.corners.copy()
        for _ in range(4):
            getattr(c, m)()
        assert np.array_equal(c.corners, start), f"{m}^4 failed"


def test_no_corner_duplication():
    for _ in range(50):
        c = Cube()
        random_moves(c, 30)
        indices = c.corners[:, 0]
        assert len(set(indices)) == 8


def test_R_move():
    c = Cube(state=STATE)
    c.R()
    expected = np.array(
        [[6, 2], [4, 2], [2, 2], [1, 1], [0, 0], [3, 0], [7, 2], [5, 0]]
    )
    assert np.array_equal(c.corners, expected)


def test_Rp_move():
    c = Cube(state=STATE)
    c.Rp()
    expected = np.array(
        [[6, 2], [7, 2], [3, 0], [1, 1], [0, 0], [2, 2], [4, 2], [5, 0]]
    )
    assert np.array_equal(c.corners, expected)


def test_R2_move():
    c = Cube(state=STATE)
    c.R2()
    expected = np.array(
        [[6, 2], [2, 0], [7, 1], [1, 1], [0, 0], [4, 1], [3, 1], [5, 0]]
    )
    assert np.array_equal(c.corners, expected)


def test_L_move():
    c = Cube(state=STATE)
    c.L()
    expected = np.array(
        [[0, 2], [3, 1], [4, 1], [6, 0], [5, 1], [7, 1], [2, 0], [1, 0]]
    )
    assert np.array_equal(c.corners, expected)


def test_Lp_move():
    c = Cube(state=STATE)
    c.Lp()
    expected = np.array(
        [[1, 0], [3, 1], [4, 1], [5, 1], [6, 0], [7, 1], [2, 0], [0, 2]]
    )
    assert np.array_equal(c.corners, expected)


def test_L2_move():
    c = Cube(state=STATE)
    c.L2()
    expected = np.array(
        [[5, 0], [3, 1], [4, 1], [0, 0], [1, 1], [7, 1], [2, 0], [6, 2]]
    )
    assert np.array_equal(c.corners, expected)


def test_U_move():
    c = Cube(state=STATE)
    c.U()
    expected = np.array(
        [[1, 1], [6, 2], [3, 1], [4, 1], [0, 0], [7, 1], [2, 0], [5, 0]]
    )
    assert np.array_equal(c.corners, expected)


def test_Up_move():
    c = Cube(state=STATE)
    c.Up()
    expected = np.array(
        [[3, 1], [4, 1], [1, 1], [6, 2], [0, 0], [7, 1], [2, 0], [5, 0]]
    )
    assert np.array_equal(c.corners, expected)


def test_U2_move():
    c = Cube(state=STATE)
    c.U2()
    expected = np.array(
        [[4, 1], [1, 1], [6, 2], [3, 1], [0, 0], [7, 1], [2, 0], [5, 0]]
    )
    assert np.array_equal(c.corners, expected)


def test_D_move():
    c = Cube(state=STATE)
    c.D()
    expected = np.array(
        [[6, 2], [3, 1], [4, 1], [1, 1], [7, 1], [2, 0], [5, 0], [0, 0]]
    )
    assert np.array_equal(c.corners, expected)


def test_Dp_move():
    c = Cube(state=STATE)
    c.Dp()
    expected = np.array(
        [[6, 2], [3, 1], [4, 1], [1, 1], [5, 0], [0, 0], [7, 1], [2, 0]]
    )
    assert np.array_equal(c.corners, expected)


def test_D2_move():
    c = Cube(state=STATE)
    c.D2()
    expected = np.array(
        [[6, 2], [3, 1], [4, 1], [1, 1], [2, 0], [5, 0], [0, 0], [7, 1]]
    )
    assert np.array_equal(c.corners, expected)


def test_F_move():
    c = Cube(state=STATE)
    c.F()
    expected = np.array(
        [[6, 2], [3, 1], [1, 2], [5, 2], [0, 0], [7, 1], [4, 0], [2, 1]]
    )
    assert np.array_equal(c.corners, expected)


def test_Fp_move():
    c = Cube(state=STATE)
    c.Fp()
    expected = np.array(
        [[6, 2], [3, 1], [2, 1], [4, 0], [0, 0], [7, 1], [5, 2], [1, 2]]
    )
    assert np.array_equal(c.corners, expected)


def test_F2_move():
    c = Cube(state=STATE)
    c.F2()
    expected = np.array(
        [[6, 2], [3, 1], [5, 0], [2, 0], [0, 0], [7, 1], [1, 1], [4, 1]]
    )
    assert np.array_equal(c.corners, expected)


def test_B_move():
    c = Cube(state=STATE)
    c.B()
    expected = np.array(
        [[3, 2], [7, 0], [4, 1], [1, 1], [6, 1], [0, 1], [2, 0], [5, 0]]
    )
    assert np.array_equal(c.corners, expected)


def test_Bp_move():
    c = Cube(state=STATE)
    c.Bp()
    expected = np.array(
        [[0, 1], [6, 1], [4, 1], [1, 1], [7, 0], [3, 2], [2, 0], [5, 0]]
    )
    assert np.array_equal(c.corners, expected)


def test_B2_move():
    c = Cube(state=STATE)
    c.B2()
    expected = np.array(
        [[7, 1], [0, 0], [4, 1], [1, 1], [3, 1], [6, 2], [2, 0], [5, 0]]
    )
    assert np.array_equal(c.corners, expected)
