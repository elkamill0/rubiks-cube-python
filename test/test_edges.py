import pytest
import numpy as np
from src.cube import Cube
import random


STATE = "231201341334510413034422433542534215005541101550250022"


def random_moves(cube, n=20):
    moves = ["R", "Rp", "L", "Lp", "U", "Up", "D", "Dp", "F", "Fp", "B", "Bp"]
    for _ in range(n):
        getattr(cube, random.choice(moves))()


def test_edges_inverse():
    moves = ["R", "L", "U", "D", "F", "B"]
    for _ in range(30):
        c = Cube()
        random_moves(c, 20)
        start = c.edges.copy()
        for m in moves:
            from copy import deepcopy

            copy = deepcopy(c)
            getattr(copy, m)()
            getattr(copy, m + "p")()
            assert np.array_equal(copy.edges, start), f"{m} edges inverse failed"


def test_edges_4_identity():
    moves = ["R", "L", "U", "D", "F", "B"]
    for m in moves:
        c = Cube()
        start = c.edges.copy()
        for _ in range(4):
            getattr(c, m)()
        assert np.array_equal(c.edges, start), f"{m}^4 edges failed"


def test_edges_no_duplication():
    for _ in range(30):
        c = Cube()
        random_moves(c, 30)
        indices = c.edges[:, 0]
        assert len(set(indices)) == 12, "Edge duplication"


def test_R_edges():
    c = Cube(state=STATE)
    c.R()
    expected = np.array(
        [
            [1, 1],
            [6, 1],
            [9, 0],
            [10, 0],
            [2, 1],
            [4, 0],
            [5, 0],
            [11, 0],
            [7, 1],
            [8, 1],
            [3, 0],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_Rp_edges():
    c = Cube(state=STATE)
    c.Rp()
    expected = np.array(
        [
            [1, 1],
            [4, 0],
            [9, 0],
            [10, 0],
            [2, 1],
            [6, 1],
            [5, 0],
            [11, 0],
            [7, 1],
            [3, 0],
            [8, 1],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_R2_edges():
    c = Cube(state=STATE)
    c.R2()
    expected = np.array(
        [
            [1, 1],
            [3, 0],
            [9, 0],
            [10, 0],
            [2, 1],
            [8, 1],
            [5, 0],
            [11, 0],
            [7, 1],
            [6, 1],
            [4, 0],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_L_edges():
    c = Cube(state=STATE)
    c.L()
    expected = np.array(
        [
            [1, 1],
            [8, 1],
            [9, 0],
            [7, 1],
            [2, 1],
            [3, 0],
            [5, 0],
            [0, 1],
            [11, 0],
            [4, 0],
            [6, 1],
            [10, 0],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_Lp_edges():
    c = Cube(state=STATE)
    c.Lp()
    expected = np.array(
        [
            [1, 1],
            [8, 1],
            [9, 0],
            [0, 1],
            [2, 1],
            [3, 0],
            [5, 0],
            [7, 1],
            [10, 0],
            [4, 0],
            [6, 1],
            [11, 0],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_L2_edges():
    c = Cube(state=STATE)
    c.L2()
    expected = np.array(
        [
            [1, 1],
            [8, 1],
            [9, 0],
            [11, 0],
            [2, 1],
            [3, 0],
            [5, 0],
            [10, 0],
            [0, 1],
            [4, 0],
            [6, 1],
            [7, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_U_edges():
    c = Cube(state=STATE)
    c.U()
    expected = np.array(
        [
            [10, 0],
            [1, 1],
            [8, 1],
            [9, 0],
            [2, 1],
            [3, 0],
            [5, 0],
            [11, 0],
            [7, 1],
            [4, 0],
            [6, 1],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_Up_edges():
    c = Cube(state=STATE)
    c.Up()
    expected = np.array(
        [
            [8, 1],
            [9, 0],
            [10, 0],
            [1, 1],
            [2, 1],
            [3, 0],
            [5, 0],
            [11, 0],
            [7, 1],
            [4, 0],
            [6, 1],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_U2_edges():
    c = Cube(state=STATE)
    c.U2()
    expected = np.array(
        [
            [9, 0],
            [10, 0],
            [1, 1],
            [8, 1],
            [2, 1],
            [3, 0],
            [5, 0],
            [11, 0],
            [7, 1],
            [4, 0],
            [6, 1],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_D_edges():
    c = Cube(state=STATE)
    c.D()
    expected = np.array(
        [
            [1, 1],
            [8, 1],
            [9, 0],
            [10, 0],
            [3, 0],
            [5, 0],
            [11, 0],
            [2, 1],
            [7, 1],
            [4, 0],
            [6, 1],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_Dp_edges():
    c = Cube(state=STATE)
    c.Dp()
    expected = np.array(
        [
            [1, 1],
            [8, 1],
            [9, 0],
            [10, 0],
            [11, 0],
            [2, 1],
            [3, 0],
            [5, 0],
            [7, 1],
            [4, 0],
            [6, 1],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_D2_edges():
    c = Cube(state=STATE)
    c.D2()
    expected = np.array(
        [
            [1, 1],
            [8, 1],
            [9, 0],
            [10, 0],
            [5, 0],
            [11, 0],
            [2, 1],
            [3, 0],
            [7, 1],
            [4, 0],
            [6, 1],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_F_edges():
    c = Cube(state=STATE)
    c.F()
    expected = np.array(
        [
            [1, 1],
            [8, 1],
            [0, 0],
            [10, 0],
            [2, 1],
            [3, 0],
            [6, 0],
            [11, 0],
            [7, 1],
            [4, 0],
            [9, 1],
            [5, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_Fp_edges():
    c = Cube(state=STATE)
    c.Fp()
    expected = np.array(
        [
            [1, 1],
            [8, 1],
            [6, 0],
            [10, 0],
            [2, 1],
            [3, 0],
            [0, 0],
            [11, 0],
            [7, 1],
            [4, 0],
            [5, 1],
            [9, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_F2_edges():
    c = Cube(state=STATE)
    c.F2()
    expected = np.array(
        [
            [1, 1],
            [8, 1],
            [5, 0],
            [10, 0],
            [2, 1],
            [3, 0],
            [9, 0],
            [11, 0],
            [7, 1],
            [4, 0],
            [0, 1],
            [6, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_B_edges():
    c = Cube(state=STATE)
    c.B()
    expected = np.array(
        [
            [4, 1],
            [8, 1],
            [9, 0],
            [10, 0],
            [7, 0],
            [3, 0],
            [5, 0],
            [11, 0],
            [1, 0],
            [2, 0],
            [6, 1],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_Bp_edges():
    c = Cube(state=STATE)
    c.Bp()
    expected = np.array(
        [
            [7, 0],
            [8, 1],
            [9, 0],
            [10, 0],
            [4, 1],
            [3, 0],
            [5, 0],
            [11, 0],
            [2, 0],
            [1, 0],
            [6, 1],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_B2_edges():
    c = Cube(state=STATE)
    c.B2()
    expected = np.array(
        [
            [2, 1],
            [8, 1],
            [9, 0],
            [10, 0],
            [1, 1],
            [3, 0],
            [5, 0],
            [11, 0],
            [4, 0],
            [7, 1],
            [6, 1],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_E_edges():
    c = Cube(state=STATE)
    c.E()
    expected = np.array(
        [
            [1, 1],
            [8, 1],
            [9, 0],
            [10, 0],
            [2, 1],
            [3, 0],
            [5, 0],
            [11, 0],
            [4, 1],
            [6, 0],
            [0, 0],
            [7, 0],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_Ep_edges():
    c = Cube(state=STATE)
    c.Ep()
    expected = np.array(
        [
            [1, 1],
            [8, 1],
            [9, 0],
            [10, 0],
            [2, 1],
            [3, 0],
            [5, 0],
            [11, 0],
            [0, 0],
            [7, 0],
            [4, 1],
            [6, 0],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_E2_edges():
    c = Cube(state=STATE)
    c.E2()
    expected = np.array(
        [
            [1, 1],
            [8, 1],
            [9, 0],
            [10, 0],
            [2, 1],
            [3, 0],
            [5, 0],
            [11, 0],
            [6, 1],
            [0, 1],
            [7, 1],
            [4, 0],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_M_edges():
    c = Cube(state=STATE)
    c.M()
    expected = np.array(
        [
            [2, 0],
            [8, 1],
            [1, 0],
            [10, 0],
            [5, 1],
            [3, 0],
            [9, 1],
            [11, 0],
            [7, 1],
            [4, 0],
            [6, 1],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_Mp_edges():
    c = Cube(state=STATE)
    c.Mp()
    expected = np.array(
        [
            [9, 1],
            [8, 1],
            [5, 1],
            [10, 0],
            [1, 0],
            [3, 0],
            [2, 0],
            [11, 0],
            [7, 1],
            [4, 0],
            [6, 1],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_M2_edges():
    c = Cube(state=STATE)
    c.M2()
    expected = np.array(
        [
            [5, 0],
            [8, 1],
            [2, 1],
            [10, 0],
            [9, 0],
            [3, 0],
            [1, 1],
            [11, 0],
            [7, 1],
            [4, 0],
            [6, 1],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_S_edges():
    c = Cube(state=STATE)
    c.S()
    expected = np.array(
        [
            [1, 1],
            [10, 1],
            [9, 0],
            [11, 1],
            [2, 1],
            [8, 0],
            [5, 0],
            [3, 1],
            [7, 1],
            [4, 0],
            [6, 1],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_Sp_edges():
    c = Cube(state=STATE)
    c.Sp()
    expected = np.array(
        [
            [1, 1],
            [3, 1],
            [9, 0],
            [8, 0],
            [2, 1],
            [11, 1],
            [5, 0],
            [10, 1],
            [7, 1],
            [4, 0],
            [6, 1],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)


def test_S2_edges():
    c = Cube(state=STATE)
    c.S2()
    expected = np.array(
        [
            [1, 1],
            [11, 0],
            [9, 0],
            [3, 0],
            [2, 1],
            [10, 0],
            [5, 0],
            [8, 1],
            [7, 1],
            [4, 0],
            [6, 1],
            [0, 1],
        ]
    )
    assert np.array_equal(c.edges, expected)
