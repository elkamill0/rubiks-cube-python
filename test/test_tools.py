from src.tools import (
    binary_to_faces,
    decimal_to_faces,
    format_pairs_with_faces,
    inverse,
    reduce,
    remap_notation_by_rotation,
)


def test_empty_returns_empty():
    assert reduce("") == ""


def test_whitespace_returns_empty():
    assert reduce("   ") == ""


def test_single_move_unchanged():
    assert reduce("R") == "R"


def test_R_R_reduces_to_R2():
    assert reduce("R R") == "R2"


def test_R_R_R_reduces_to_Rp():
    assert reduce("R R R") == "R'"


def test_R_R_R_R_cancels():
    assert reduce("R R R R") == ""


def test_Rp_Rp_reduces_to_R2():
    assert reduce("R' R'") == "R2"


def test_R2_R2_cancels():
    assert reduce("R2 R2") == ""


def test_R_Rp_cancels():
    assert reduce("R R'") == ""


def test_different_faces_not_combined():
    assert reduce("R U") == "R U"


def test_R_R_U_U_reduces():
    assert reduce("R R U U") == "R2 U2"


def test_R_U_R_U_unchanged():
    assert reduce("R U R U") == "R U R U"


def test_R4_U_reduces_to_U():
    assert reduce("R R R R U") == "U"


def test_long_same_face():
    assert reduce("R R R R R") == "R"


def test_multistep_R_R2_reduces_to_Rp():
    assert reduce("R R2") == "R'"


def test_inverse_empty_returns_empty():
    assert inverse("") == ""


def test_inverse_R_returns_Rp():
    assert inverse("R") == "R'"


def test_inverse_Rp_returns_R():
    assert inverse("R'") == "R"


def test_inverse_R2_returns_R2():
    assert inverse("R2") == "R2"


def test_inverse_order_reversed():
    assert inverse("R U") == "U' R'"


def test_inverse_of_inverse():
    seq = "R U R' U' F2 D"
    assert inverse(inverse(seq)) == seq


def test_inverse_complex_sequence():
    assert inverse("R U R' U'") == "U R U' R'"


def test_inverse_wide_moves():
    assert inverse("r u") == "u' r'"


def test_inverse_middle_moves():
    assert inverse("M E S") == "S' E' M'"


def test_inverse_rotations():
    assert inverse("x y z") == "z' y' x'"


def test_inverse_whitespace_trimmed():
    assert inverse("  R U  ") == "U' R'"


# Tests for remap_notation_by_rotation
def test_remap_z_rotation():
    assert remap_notation_by_rotation("R L U D F B", "z") == "D U R L F B"
    assert remap_notation_by_rotation("R' L' U' D' F' B'", "z") == "D' U' R' L' F' B'"
    assert remap_notation_by_rotation("R2 L2 U2 D2 F2 B2", "z") == "D2 U2 R2 L2 F2 B2"


def test_remap_z_prime_rotation():
    assert remap_notation_by_rotation("R L U D F B", "z'") == "U D L R F B"
    assert remap_notation_by_rotation("R' L' U' D' F' B'", "z'") == "U' D' L' R' F' B'"
    assert remap_notation_by_rotation("R2 L2 U2 D2 F2 B2", "z'") == "U2 D2 L2 R2 F2 B2"


def test_remap_z2_rotation():
    assert remap_notation_by_rotation("R L U D F B", "z2") == "L R D U F B"
    assert remap_notation_by_rotation("R' L' U' D' F' B'", "z2") == "L' R' D' U' F' B'"
    assert remap_notation_by_rotation("R2 L2 U2 D2 F2 B2", "z2") == "L2 R2 D2 U2 F2 B2"


def test_remap_x_rotation():
    assert remap_notation_by_rotation("R L U D F B", "x") == "R L B F U D"
    assert remap_notation_by_rotation("R' L' U' D' F' B'", "x") == "R' L' B' F' U' D'"
    assert remap_notation_by_rotation("R2 L2 U2 D2 F2 B2", "x") == "R2 L2 B2 F2 U2 D2"


def test_remap_x_prime_rotation():
    assert remap_notation_by_rotation("R L U D F B", "x'") == "R L F B D U"
    assert remap_notation_by_rotation("R' L' U' D' F' B'", "x'") == "R' L' F' B' D' U'"
    assert remap_notation_by_rotation("R2 L2 U2 D2 F2 B2", "x'") == "R2 L2 F2 B2 D2 U2"


def test_remap_x2_rotation():
    assert remap_notation_by_rotation("R L U D F B", "x2") == "R L D U B F"
    assert remap_notation_by_rotation("R' L' U' D' F' B'", "x2") == "R' L' D' U' B' F'"
    assert remap_notation_by_rotation("R2 L2 U2 D2 F2 B2", "x2") == "R2 L2 D2 U2 B2 F2"


def test_remap_y_rotation():
    assert remap_notation_by_rotation("R L U D F B", "y") == "F B U D L R"
    assert remap_notation_by_rotation("R' L' U' D' F' B'", "y") == "F' B' U' D' L' R'"
    assert remap_notation_by_rotation("R2 L2 U2 D2 F2 B2", "y") == "F2 B2 U2 D2 L2 R2"


def test_remap_y_prime_rotation():
    assert remap_notation_by_rotation("R L U D F B", "y'") == "B F U D R L"
    assert remap_notation_by_rotation("R' L' U' D' F' B'", "y'") == "B' F' U' D' R' L'"
    assert remap_notation_by_rotation("R2 L2 U2 D2 F2 B2", "y'") == "B2 F2 U2 D2 R2 L2"


def test_remap_y2_rotation():
    assert remap_notation_by_rotation("R L U D F B", "y2") == "L R U D B F"
    assert remap_notation_by_rotation("R' L' U' D' F' B'", "y2") == "L' R' U' D' B' F'"
    assert remap_notation_by_rotation("R2 L2 U2 D2 F2 B2", "y2") == "L2 R2 U2 D2 B2 F2"


def test_remap_preserves_modifiers():
    assert remap_notation_by_rotation("R' U2", "z") == "D' R2"


def test_remap_unknown_rotation_unchanged():
    assert remap_notation_by_rotation("R U", "w") == "R U"


def test_remap_unaffected_moves_unchanged():
    center_moves = "M M' M2 E E' E2 S S' S2"
    assert remap_notation_by_rotation(center_moves, "z") == "E' E E2 M M' M2 S S' S2"
    assert remap_notation_by_rotation(center_moves, "z'") == "E E' E2 M' M M2 S S' S2"
    assert remap_notation_by_rotation(center_moves, "z2") == "M' M M2 E' E E2 S S' S2"
    assert remap_notation_by_rotation(center_moves, "x") == "M M' M2 S S' S2 E' E E2"
    assert remap_notation_by_rotation(center_moves, "x'") == "M M' M2 S' S S2 E E' E2"
    assert remap_notation_by_rotation(center_moves, "x2") == "M M' M2 E' E E2 S' S S2"
    assert remap_notation_by_rotation(center_moves, "y") == "S' S S2 E E' E2 M M' M2"
    assert remap_notation_by_rotation(center_moves, "y'") == "S S' S2 E E' E2 M' M M2"
    assert remap_notation_by_rotation(center_moves, "y2") == "M' M M2 E E' E2 S' S S2"


# Tests for decimal_to_faces
def test_decimal_to_faces_zero():
    assert decimal_to_faces(0) == ""


def test_decimal_to_faces_one():
    assert decimal_to_faces(1) == "R"


def test_decimal_to_faces_two():
    assert decimal_to_faces(2) == "L"


def test_decimal_to_faces_R_and_L():
    assert decimal_to_faces(3) == "RL"


def test_decimal_to_faces_102():
    assert decimal_to_faces(102) == "LUB1"


def test_decimal_to_faces_all_faces():
    assert decimal_to_faces(255) == "RLUDFB12"


# Tests for binary_to_faces
def test_binary_to_faces_zero():
    assert binary_to_faces("0") == ""


def test_binary_to_faces_one():
    assert binary_to_faces("1") == "R"


def test_binary_to_faces_two():
    assert binary_to_faces("10") == "L"


def test_binary_to_faces_three():
    assert binary_to_faces("11") == "RL"


def test_binary_to_faces_complex():
    assert binary_to_faces("01100110") == "LUB1"
    assert binary_to_faces("01010101") == "RUF1"
    assert binary_to_faces("10101010") == "LDB2"
    assert binary_to_faces("00001100") == "UD"
    assert binary_to_faces("00110000") == "FB"
    assert binary_to_faces("01001100") == "UD1"
    assert binary_to_faces("00110011") == "RLFB"


def test_binary_to_faces_all_ones():
    assert binary_to_faces("11111111") == "RLUDFB12"


def test_format_pairs_empty():
    assert format_pairs_with_faces([]) == []


def test_format_pairs_single():
    result = format_pairs_with_faces([(1, 2)])
    assert result == [("R", "L")]


def test_format_pairs_multiple():
    result = format_pairs_with_faces([(1, 2), (3, 4)])
    assert result == [("R", "L"), ("RL", "U")]


def test_format_pairs_with_complex_numbers():
    result = format_pairs_with_faces([(102, 51)])
    assert result == [("LUB1", "RLFB")]
