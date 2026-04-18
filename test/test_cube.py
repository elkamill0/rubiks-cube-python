from cube import Cube

def test_solved_cube_is_solved():
    cube = Cube()
    assert cube.is_solved()

def test_move_and_inverse():
    cube = Cube()
    cube.move("R U R' U'")
    cube.move("U R U' R'")
    assert cube.is_solved()