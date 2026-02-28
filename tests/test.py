import pytest
from cube import Cube
import numpy as np
from convert import cube_to_color

def test_moves():
    cube = Cube()

    cube.R()
    assert np.array_equal(cube.corners, np.array([[0, 0], [2, 1], [6, 2], [3, 0], [4, 0], [1, 2], [5, 1], [7, 0]]))
    assert np.array_equal(cube.edges, np.array([[ 0, 0],[10, 0],[ 2, 0],[ 3, 0],[ 4, 0],[ 9, 0],[ 6, 0],[ 7, 0],[ 8, 0],[ 1, 0],[ 5, 0],[11, 0]]))
    assert cube_to_color(cube, show=True).strip() == """        002
        002
        002
        ---
    111|225|333|044
    111|225|333|044
    111|225|333|044
        ---
        554
        554
        554""".strip()

    cube.U()
    assert np.array_equal(cube.corners, np.array([[3, 0], [0, 0], [2, 1], [6, 2], [4, 0], [1, 2], [5, 1], [7, 0]]))
    assert np.array_equal(cube.edges, np.array([[ 3, 0],[ 0, 0],[10, 0],[ 2, 0],[ 4, 0],[ 9, 0],[ 6, 0],[ 7, 0],[ 8, 0],[ 1, 0],[ 5, 0],[11, 0]]
        # TODO: po U
    ))
    assert cube_to_color(cube.corners, cube.edges, cube.centers, show=True).strip() == """        000
        000
        222
        ---
    225|333|044|111
    111|225|333|044
    111|225|333|044
        ---
        554
        554
        554""".strip()

    cube.Rp()
    assert np.array_equal(cube.corners, np.array([[3, 0],[1, 0],[0, 2],[6, 2],[4, 0],[5, 0],[2, 2],[7, 0]]))
    assert np.array_equal(cube.edges, np.array([[ 3, 0],[ 1, 0],[10, 0],[ 2, 0],[ 4, 0],[ 5, 0],[ 6, 0],[ 7, 0],[ 8, 0],[ 9, 0],[ 0, 0],[11, 0]]))
    assert cube_to_color(cube.corners, cube.edges, cube.centers, show=True).strip() == """        000
        000
        221
        ---
    225|330|433|411
    111|220|433|444
    111|222|033|444
        ---
        553
        555
        555""".strip()

    cube.L()
    assert np.array_equal(cube.corners, np.array([[4, 2],[1, 0],[0, 2],[3, 1],[7, 1],[5, 0],[2, 2],[6, 1]]))
    assert np.array_equal(cube.edges, np.array([[ 3, 0],[ 1, 0],[10, 0],[ 8, 0],[ 4, 0],[ 5, 0],[ 6, 0],[11, 0],[ 7, 0],[ 9, 0],[ 0, 0],[ 2, 0]]))
    assert cube_to_color(cube.corners, cube.edges, cube.centers, show=True).strip() == """        400
        400
        121
        ---
    112|030|433|415
    112|020|433|445
    115|222|033|445
        ---
        353
        255
        255""".strip()

    cube.D2()
    assert np.array_equal(cube.corners, np.array([[4, 2],[1, 0],[0, 2],[3, 1],[2, 2],[6, 1],[7, 1],[5, 0]]))
    assert np.array_equal(cube.edges, np.array([[ 3, 0],[ 1, 0],[10, 0],[ 8, 0],[ 6, 0],[11, 0],[ 4, 0],[ 5, 0],[ 7, 0],[ 9, 0],[ 0, 0],[ 2, 0]]))
    assert cube_to_color(cube.corners, cube.edges, cube.centers, show=True).strip() == """        400
        400
        121
        ---
    112|030|433|415
    112|020|433|445
    033|445|115|222
        ---
        552
        552
        353""".strip()

    cube.Fp()
    assert np.array_equal(cube.corners, np.array([[4, 2],[1, 0],[7, 2],[0, 1],[2, 2],[6, 1],[5, 2],[3, 2]]))
    assert np.array_equal(cube.edges, np.array([[ 3, 0],[ 1, 0],[ 0, 1],[ 8, 0],[ 6, 0],[11, 0],[ 2, 1],[ 5, 0],[ 7, 0],[ 9, 0],[ 4, 1],[10, 1]]))
    assert cube_to_color(cube.corners, cube.edges, cube.centers, show=True).strip() == """        400
        400
        441
        ---
    111|005|233|415
    112|324|533|445
    031|004|515|222
        ---
        223
        552
        353""".strip()

    cube.B()
    assert np.array_equal(cube.corners, np.array([[1, 1],[6, 0],[7, 2],[0, 1],[4, 1],[2, 0],[5, 2],[3, 2]]))
    assert np.array_equal(cube.edges, np.array([[ 9, 1],[ 1, 0],[ 0, 1],[ 8, 0],[ 7, 1],[11, 0],[ 2, 1],[ 5, 0],[ 3, 1],[ 6, 1],[ 4, 1],[10, 1]]))
    assert cube_to_color(cube.corners, cube.edges, cube.centers, show=True).strip() == """        335
        400
        441
        ---
    011|005|233|244
    012|324|535|241
    431|004|513|255
        ---
        223
        552
        110""".strip()

    cube.Up()
    assert np.array_equal(cube.corners, np.array([[6, 0],[7, 2],[0, 1],[1, 1],[4, 1],[2, 0],[5, 2],[3, 2]]))
    assert np.array_equal(cube.edges, np.array([[ 1, 0],[ 0, 1],[ 8, 0],[ 9, 1],[ 7, 1],[11, 0],[ 2, 1],[ 5, 0],[ 3, 1],[ 6, 1],[ 4, 1],[10, 1]]))
    assert cube_to_color(cube.corners, cube.edges, cube.centers, show=True).strip() == """        501
        304
        344
        ---
    244|011|005|233
    012|324|535|241
    431|004|513|255
        ---
        223
        552
        110""".strip()

    cube.R2()
    assert np.array_equal(cube.corners, np.array([[6, 0],[5, 2],[2, 0],[1, 1],[4, 1],[0, 1],[7, 2],[3, 2]]))
    assert np.array_equal(cube.edges, np.array([[ 1, 0],[11, 0],[ 8, 0],[ 9, 1],[ 7, 1],[ 0, 1],[ 2, 1],[ 5, 0],[ 3, 1],[ 4, 1],[ 6, 1],[10, 1]]))
    assert cube_to_color(cube.corners, cube.edges, cube.centers, show=True).strip() == """        503
        302
        340
        ---
    244|012|315|433
    012|322|535|441
    431|002|500|155
        ---
        221
        554
        114""".strip()

    cube.Lp()
    assert np.array_equal(cube.corners, np.array([[1, 0],[5, 2],[2, 0],[3, 0],[6, 1],[0, 1],[7, 2],[4, 0]]))
    assert np.array_equal(cube.edges, np.array([[ 1, 0],[11, 0],[ 8, 0],[10, 1],[ 7, 1],[ 0, 1],[ 2, 1],[ 3, 1],[ 9, 1],[ 4, 1],[ 6, 1],[ 5, 0]]))
    assert cube_to_color(cube.corners, cube.edges, cube.centers, show=True).strip() == """        003
        302
        040
        ---
    421|212|315|433
    413|522|535|443
    204|102|500|155
        ---
        521
        154
        314""".strip()
    

    cube.F2()
    assert np.array_equal(cube.corners, np.array([[1, 0],[5, 2],[4, 0],[7, 2],[6, 1],[0, 1],[3, 0],[2, 0]]))
    assert np.array_equal(cube.edges, np.array([[ 1, 0],[11, 0],[ 2, 1],[10, 1],[ 7, 1],[ 0, 1],[ 8, 0],[ 3, 1],[ 9, 1],[ 4, 1],[ 5, 0],[ 6, 1]]))
    assert cube_to_color(cube.corners, cube.edges, cube.centers, show=True).strip() == """        003
        302
        125
        ---
    425|201|415|433
    415|225|335|443
    203|212|100|155
        ---
        040
        154
        314""".strip()

    cube.Dp()
    assert np.array_equal(cube.corners, np.array([[1, 0],[5,2],[4,0],[7,2],[2,0],[6,1],[0,1],[3,0]]))
    assert np.array_equal(cube.edges, np.array([[ 1, 0],[11, 0],[ 2, 1],[10, 1],[ 3, 1],[ 7, 1],[ 0, 1],[ 8, 0],[ 9, 1],[ 4, 1],[ 5, 0],[ 6, 1]]))
    assert cube_to_color(cube.corners, cube.edges, cube.centers, show=True).strip() == """        003
        302
        125
        ---
    425|201|415|433
    415|225|335|443
    212|100|155|203
        ---
        044
        451
        013""".strip()

    cube.B2()
    assert np.array_equal(cube.corners, np.array([[6, 1],[2, 0],[4, 0],[7, 2],[5, 2],[1, 0],[0, 1],[3, 0]]))
    assert np.array_equal(cube.edges, np.array([[ 3, 1],[11, 0],[ 2, 1],[10, 1],[ 1, 0],[ 7, 1],[ 0, 1],[ 8, 0],[ 4, 1],[ 9, 1],[ 5, 0],[ 6, 1]]))
    assert cube_to_color(cube.corners, cube.edges, cube.centers, show=True).strip() == """        310
        302
        125
        ---
    525|201|412|302
    515|225|334|344
    512|100|154|334
        ---
        044
        451
        300""".strip()


    cube.U2()
    assert np.array_equal(cube.corners, np.array([[4, 0],[7, 2],[6, 1],[2, 0],[5, 2],[1, 0],[0, 1],[3, 0]]))
    assert np.array_equal(cube.edges, np.array([[ 2, 1],[10, 1],[ 3, 1],[11, 0],[ 1, 0],[ 7, 1],[ 0, 1],[ 8, 0],[ 4, 1],[ 9, 1],[ 5, 0],[ 6, 1]]))
    assert cube_to_color(cube.corners, cube.edges, cube.centers, show=True).strip() == """        521
        203
        013
        ---
    412|302|525|201
    515|225|334|344
    512|100|154|334
        ---
        044
        451
        300""".strip()

    cube.L2()
    assert np.array_equal(cube.corners, np.array([[3, 0],[7, 2],[6, 1],[5, 2],[2, 0],[1, 0],[0, 1],[4, 0]]))
    assert np.array_equal(cube.edges, np.array([[ 2, 1],[10, 1],[ 3, 1],[ 8, 0],[ 1, 0],[ 7, 1],[ 0, 1],[11, 0],[ 6, 1],[ 9, 1],[ 5, 0],[ 4, 1]]))
    assert cube_to_color(cube.corners, cube.edges, cube.centers, show=True).strip() == """        021
        403
        313
        ---
    215|402|525|201
    515|425|334|342
    214|100|154|333
        ---
        544
        251
        000""".strip()

    cube.D()
    assert np.array_equal(cube.corners, np.array([[3, 0],[7, 2],[6, 1],[5, 2],[1, 0],[0, 1],[4, 0],[2, 0]]))
    assert np.array_equal(cube.edges, np.array([[ 2, 1],[10, 1],[ 3, 1],[ 8, 0],[ 7, 1],[ 0, 1],[11, 0],[ 1, 0],[ 6, 1],[ 9, 1],[ 5, 0],[ 4, 1]]))
    assert cube_to_color(cube.corners, cube.edges, cube.centers, show=True).strip() == """        021
        403
        313
        ---
    215|402|525|201
    515|425|334|342
    333|214|100|154
        ---
        025
        054
        014""".strip()

    cube.Bp()
    assert np.array_equal(cube.corners, np.array([[1, 1],[3, 2],[6, 1],[5, 2],[0, 0],[7, 0],[4, 0],[2, 0]]))
    assert np.array_equal(cube.edges, np.array([[ 6, 0],[10, 1],[ 3, 1],[ 8, 0],[ 9, 0],[ 0, 1],[11, 0],[ 1, 0],[ 7, 0],[ 2, 0],[ 5, 0],[ 4, 1]]))
    assert cube_to_color(cube.corners, cube.edges, cube.centers, show=True).strip() == """        352
        403
        313
        ---
    015|402|520|124
    115|425|332|045
    433|214|101|231
        ---
        025
        054
        045""".strip()

    cube.F()
    assert np.array_equal(cube.corners, np.array([[1, 1],[3, 2],[5, 0],[2, 2],[0, 0],[7, 0],[6, 0],[4, 1]]))
    assert np.array_equal(cube.edges, np.array([[ 6, 0],[10, 1],[ 4, 0],[ 8, 0],[ 9, 0],[ 0, 1],[ 5, 1],[ 1, 0],[ 7, 0],[ 2, 0],[ 3, 0],[11, 1]]))
    assert cube_to_color(cube.corners, cube.edges, cube.centers, show=True).strip() == """        352
        403
        355
        ---
    010|244|320|124
    112|120|132|045
    435|452|301|231
        ---
        135
        054
        045""".strip()



# def test_moves():
#     cube = Cube("")
#     cube.Lp()
#     assert np.array_equal(cube.corners, np.array([[3,2],[1,0],[2,0],[7,1],[0,1],[5,0],[6,0],[4,2]]))
#     cube.Fp()
#     assert np.array_equal(cube.corners, np.array([[3,2],[1,0],[6,1],[2,2],[0,1],[5,0],[4,1],[7,2]]))
#     cube.D2()
#     assert np.array_equal(cube.corners, np.array([[3,2],[1,0],[6,1],[2,2],[4,1],[7,2],[0,1],[5,0]]))
#     cube.F2()
#     assert np.array_equal(cube.corners, np.array([[3,2],[1,0],[5,0],[0,1],[4,1],[7,2],[2,2],[6,1]]))
#     cube.D2()
#     assert np.array_equal(cube.corners, np.array([[3,2],[1,0],[5,0],[0,1],[2,2],[6,1],[4,1],[7,2]]))
#     cube.Lp()
#     assert np.array_equal(cube.corners, np.array([[0,0],[1,0],[5,0],[7,0],[3,0],[6,1],[4,1],[2,1]]))
#     cube.Up()
#     assert np.array_equal(cube.corners, np.array([[1,0],[5,0],[7,0],[0,0],[3,0],[6,1],[4,1],[2,1]]))
#     cube.Fp()
#     assert np.array_equal(cube.corners, np.array([[1,0],[5,0],[4,2],[7,2],[3,0],[6,1],[2,0],[0,1]]))
#     cube.L2()
#     assert np.array_equal(cube.corners, np.array([[0,1],[5,0],[4,2],[3,0],[7,2],[6,1],[2,0],[1,0]]))
#     cube.F()
#     assert np.array_equal(cube.corners, np.array([[0,1],[5,0],[3,1],[1,2],[7,2],[6,1],[4,1],[2,1]]))
#     cube.U2()
#     assert np.array_equal(cube.corners, np.array([[3,1],[1,2],[0,1],[5,0],[7,2],[6,1],[4,1],[2,1]]))


# def test_scramble():
#     notation="B' U L' B2 R F2 L' R2 B2 U2 R2 D2 F2 D' B' U L2 B' D F"
#     cube = Cube(notation=notation)
#     assert np.array_equal(cube.get_cube(), np.array([[7,1],[0,1],[3,0],[5,1],[4,0],[1,0],[6,0],[2,2]]))

# def test_state_to_cube():



# def test_reset():
#     cube = Cube()
#     cube.Lp()
#     cube.Fp()
#     cube.D2()
#     cube.reset()
#     assert np.array_equal(cube.get_cube(), np.array([[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]]))

# def test_state():
#     state = "WWWWWWWWWRRRRRRRRRBBBBBBBBBOOOOOOOOOGGGGGGGGGYYYYYYYYY"
#     cube = Cube(state=state)
#     assert np.array_equal(cube.get_cube(), np.array([[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0]]))
#     assert cube.get_state() == state
#     notation="B' U L' B2 R F2 L' R2 B2 U2 R2 D2 F2 D' B' U L2 B' D F"
#     cube = Cube(notation=notation)  

# def test_str():
#     notation="B' U L' B2 R F2 L' R2 B2 U2 R2 D2 F2 D' B' U L2 B' D F"
#     cube = Cube(notation=notation)
#     expected_str = "Y Y Y Y Y Y Y Y \nY Y Y Y Y Y Y Y \nY Y Y Y Y Y Y Y \nR R R R R R R R \nR R R R R R R R \nR R R R R R R R \nG G G G G G G G \nG G G G G G G G \nG G G G G G G G \nB B B B B B B B \nB B B B B B B B \nB B B B B B B B \nO O O O O O O O \nO O O O O O O O \nO O O O O O O O \n"
#     assert str(cube) == expected_str

# def test_invalid_state():
#     invalid_state = "WWWWWWWWWRRRRRRRRRBBBBBBBBBOOOOOOOOOGGGGGGGGGYYYYYYYY"  # 41 characters instead of 54
#     with pytest.raises(ValueError):
#         cube = Cube(state=invalid_state)

# def test_invalid_move():
#     cube = Cube()
#     with pytest.raises(KeyError):
#         cube.move("X")  # Invalid move notation
