import pytest
from cube import Cube
import numpy as np


def test_moves():
    cube = Cube()
    cube.Lp()
    assert np.array_equal(cube.get_cube(), np.array([[3,2],[1,0],[2,0],[7,1],[0,1],[5,0],[6,0],[4,2]]))
    cube.Fp()
    assert np.array_equal(cube.get_cube(), np.array([[3,2],[1,0],[6,1],[2,2],[0,1],[5,0],[4,1],[7,2]]))
    cube.D2()
    assert np.array_equal(cube.get_cube(), np.array([[3,2],[1,0],[6,1],[2,2],[4,1],[7,2],[0,1],[5,0]]))
    cube.F2()
    assert np.array_equal(cube.get_cube(), np.array([[3,2],[1,0],[5,0],[0,1],[4,1],[7,2],[2,2],[6,1]]))
    cube.D2()
    assert np.array_equal(cube.get_cube(), np.array([[3,2],[1,0],[5,0],[0,1],[2,2],[6,1],[4,1],[7,2]]))
    cube.Lp()
    assert np.array_equal(cube.get_cube(), np.array([[0,0],[1,0],[5,0],[7,0],[3,0],[6,1],[4,1],[2,1]]))
    cube.Up()
    assert np.array_equal(cube.get_cube(), np.array([[1,0],[5,0],[7,0],[0,0],[3,0],[6,1],[4,1],[2,1]]))
    cube.Fp()
    assert np.array_equal(cube.get_cube(), np.array([[1,0],[5,0],[4,2],[7,2],[3,0],[6,1],[2,0],[0,1]]))
    cube.L2()
    assert np.array_equal(cube.get_cube(), np.array([[0,1],[5,0],[4,2],[3,0],[7,2],[6,1],[2,0],[1,0]]))
    cube.F()
    assert np.array_equal(cube.get_cube(), np.array([[0,1],[5,0],[3,1],[1,2],[7,2],[6,1],[4,1],[2,1]]))
    cube.U2()
    assert np.array_equal(cube.get_cube(), np.array([[3,1],[1,2],[0,1],[5,0],[7,2],[6,1],[4,1],[2,1]]))
