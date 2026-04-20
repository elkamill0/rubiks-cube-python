import pytest
import numpy as np
from src.cube import Cube
import random


STATE = "231201341334510413034422433542534215005541101550250022"


def random_moves(cube, n=20):
    moves = ["R", "Rp", "L", "Lp", "U", "Up", "D", "Dp", "F", "Fp", "B", "Bp"]
    for _ in range(n):
        getattr(cube, random.choice(moves))()


def test_centers_inverse():
    moves = ["E", "M", "S"]
    for _ in range(30):
        c = Cube()
        random_moves(c, 20)
        start = c.centers.copy()
        for m in moves:
            from copy import deepcopy
            copy = deepcopy(c)
            getattr(copy, m)()
            getattr(copy, m + "p")()
            assert np.array_equal(copy.centers, start), f"{m} centers inverse failed"


def test_centers_4_identity():
    moves = ["E", "M", "S"]
    for m in moves:
        c = Cube()
        start = c.centers.copy()
        for _ in range(4):
            getattr(c, m)()
        assert np.array_equal(c.centers, start), f"{m}^4 centers failed"


def test_centers_no_duplication():
    for _ in range(30):
        c = Cube()
        random_moves(c, 30)
        assert len(set(c.centers)) == 6, "Center duplication"


def test_E_centers():
    c = Cube(state=STATE)
    c.E()
    assert np.array_equal(c.centers, [0, 4, 1, 2, 3, 5])


def test_Ep_centers():
    c = Cube(state=STATE)
    c.Ep()
    assert np.array_equal(c.centers, [0, 2, 3, 4, 1, 5])


def test_E2_centers():
    c = Cube(state=STATE)
    c.E2()
    assert np.array_equal(c.centers, [0, 3, 4, 1, 2, 5])


def test_M_centers():
    c = Cube(state=STATE)
    c.M()
    assert np.array_equal(c.centers, [4, 1, 0, 3, 5, 2])


def test_Mp_centers():
    c = Cube(state=STATE)
    c.Mp()
    assert np.array_equal(c.centers, [2, 1, 5, 3, 0, 4])


def test_M2_centers():
    c = Cube(state=STATE)
    c.M2()
    assert np.array_equal(c.centers, [5, 1, 4, 3, 2, 0])


def test_S_centers():
    c = Cube(state=STATE)
    c.S()
    assert np.array_equal(c.centers, [1, 5, 2, 0, 4, 3])


def test_Sp_centers():
    c = Cube(state=STATE)
    c.Sp()
    assert np.array_equal(c.centers, [3, 0, 2, 5, 4, 1])


def test_S2_centers():
    c = Cube(state=STATE)
    c.S2()
    assert np.array_equal(c.centers, [5, 3, 2, 1, 4, 0])