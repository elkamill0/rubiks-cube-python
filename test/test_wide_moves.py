import random

import numpy as np

from src.cube import Cube


def random_moves(cube, n=20):
    moves = ["R", "Rp", "L", "Lp", "U", "Up", "D", "Dp", "F", "Fp", "B", "Bp"]
    for _ in range(n):
        getattr(cube, random.choice(moves))()


def test_wide_inverse():
    moves = ["r", "l", "u", "d", "f", "b"]
    for _ in range(30):
        c = Cube()
        random_moves(c, 20)
        start_corners = c.corners.copy()
        start_edges = c.edges.copy()
        start_centers = c.centers.copy()
        for m in moves:
            from copy import deepcopy

            copy = deepcopy(c)
            getattr(copy, m)()
            getattr(copy, m + "p")()
            assert np.array_equal(copy.corners, start_corners), (
                f"{m} corners inverse failed"
            )
            assert np.array_equal(copy.edges, start_edges), f"{m} edges inverse failed"
            assert np.array_equal(copy.centers, start_centers), (
                f"{m} centers inverse failed"
            )


def test_wide_4_identity():
    moves = [
        "r",
        "rp",
        "r2",
        "l",
        "lp",
        "l2",
        "u",
        "up",
        "u2",
        "d",
        "dp",
        "d2",
        "f",
        "fp",
        "f2",
        "b",
        "bp",
        "b2",
    ]
    for m in moves:
        c = Cube()
        start_corners = c.corners.copy()
        start_edges = c.edges.copy()
        start_centers = c.centers.copy()
        for _ in range(4):
            getattr(c, m)()
        assert np.array_equal(c.corners, start_corners), f"{m}^4 corners failed"
        assert np.array_equal(c.edges, start_edges), f"{m}^4 edges failed"
        assert np.array_equal(c.centers, start_centers), f"{m}^4 centers failed"


STATE = "230201445330510113331422433441534215205541100550250422"


def test_r_move():
    c = Cube(state=STATE)
    c.r()
    c.get_state()
    assert c.get_state() == "231222433330510113350450422254134541545101030501245402"


def test_rp_move():
    c = Cube(state=STATE)
    c.rp()
    c.get_state()
    assert c.get_state() == "201245402330510113330401445145431452225051050531222433"


def test_r2_move():
    c = Cube(state=STATE)
    c.r2()
    c.get_state()
    assert c.get_state() == "250250422330510113301445402512435144335221130530201445"


def test_l_move():
    c = Cube(state=STATE)
    c.get_state()
    c.l()
    assert c.get_state() == "000141505153113300231202443441534215224552155330420432"


def test_lp_move():
    c = Cube(state=STATE)
    c.lp()
    c.get_state()
    assert c.get_state() == "330421435003311351551252423441534215244502132000140502"


def test_l2_move():
    c = Cube(state=STATE)
    c.l2()
    c.get_state()
    assert c.get_state() == "550251425311015033001142503441534215234524133230200442"


def test_u_move():
    c = Cube(state=STATE)
    c.u()
    c.get_state()
    assert c.get_state() == "422403510331422113441534433205541215330510100550250422"


def test_up_move():
    c = Cube(state=STATE)
    c.up()
    c.get_state()
    assert c.get_state() == "015304224205541113330510433331422215441534100550250422"


def test_u2_move():
    c = Cube(state=STATE)
    c.u2()
    c.get_state()
    assert c.get_state() == "544102032441534113205541433330510215331422100550250422"


def test_d_move():
    c = Cube(state=STATE)
    c.d()
    c.get_state()
    assert c.get_state() == "230201445330541100331510113441422433205534215425255200"


def test_dp_move():
    c = Cube(state=STATE)
    c.dp()
    c.get_state()
    assert c.get_state() == "230201445330422433331534215441541100205510113002552524"


def test_d2_move():
    c = Cube(state=STATE)
    c.d2()
    c.get_state()
    assert c.get_state() == "230201445330534215331541100441510113205422433224052055"


def test_f_move():
    c = Cube(state=STATE)
    c.f()
    assert c.get_state() == "230113300325555100443323321421404515205541100254134422"


def test_fp_move():
    c = Cube(state=STATE)
    c.fp()
    c.get_state()
    assert c.get_state() == "230431452315504124123323344001554525205541100003311422"


def test_f2_move():
    c = Cube(state=STATE)
    c.f2()
    c.get_state()
    assert c.get_state() == "230052055312535144334224133311014035205541100544102422"


def test_b_move():
    c = Cube(state=STATE)
    c.b()
    c.get_state()
    assert c.get_state() == "145431445010300223331422433402552224152040015550311351"


def test_bp_move():
    c = Cube(state=STATE)
    c.bp()
    c.get_state()
    assert c.get_state() == "153113445420250203331422433422503210510040251550134541"


def test_b2_move():
    c = Cube(state=STATE)
    c.b2()
    c.get_state()
    assert c.get_state() == "224052445510430143331422433411515233001145502550102032"
