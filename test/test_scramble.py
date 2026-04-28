import pytest
from random import seed
from src.scramble import generate_scramble, remap_scramble_by_color


@pytest.fixture(autouse=True)
def set_seed():
    seed(42)


@pytest.mark.parametrize("length", [1, 2, 5, 10, 20])
def test_scramble_has_correct_length(length):
    assert len(generate_scramble(length).split()) == length


@pytest.mark.parametrize("_", range(100))
def test_no_consecutive_same_axis(_):
    axes = [m // 3 for m in generate_scramble(20, True)]
    for a, b in zip(axes, axes[1:]):
        assert a != b


@pytest.mark.parametrize("_", range(100))
def test_no_three_same_axis_in_a_row(_):
    axes = [m // 3 for m in generate_scramble(20, True)]
    for a, b, c in zip(axes, axes[1:], axes[2:]):
        assert not (a ^ 1 == b and b == c ^ 1)


@pytest.mark.parametrize("_", range(100))
def test_all_moves_in_valid_range(_):
    for move in generate_scramble(20, True):
        assert 0 <= move <= 17


@pytest.mark.parametrize("length", [1, 2])
def test_scramble_edge_cases(length):
    result = generate_scramble(length, True)
    assert len(result) == length
    assert all(0 <= m <= 17 for m in result)


@pytest.mark.parametrize("_", range(10))
def test_no_consecutive_same_axis_numbers(_):
    scramble = generate_scramble(20, numbers=True)
    axes = [m // 3 for m in scramble]
    for a, b in zip(axes, axes[1:]):
        assert a != b, f"Niedozwolone: {a} {b}"


@pytest.mark.parametrize("_", range(10))
def test_no_three_same_axis_in_a_row_numbers(_):
    scramble = generate_scramble(20, numbers=True)
    axes = [m // 3 for m in scramble]
    for a, b, c in zip(axes, axes[1:], axes[2:]):
        if a ^ 1 == b:
            assert c != a and c != b, f"Niedozwolone: {a} {b} {c}"


@pytest.mark.parametrize("color", ["w", "o", "r", "b", "g", "y"])
def test_valid_colors_dont_raise(color):
    remap_scramble_by_color("R U R'", color)


def test_unknown_color_raises():
    with pytest.raises(ValueError):
        remap_scramble_by_color("R U R'", "p")


def test_yellow_returns_unchanged():
    assert remap_scramble_by_color("R U R'", "y") == "R U R'"


@pytest.mark.parametrize("color", ["w", "o", "r", "b", "g"])
def test_non_yellow_returns_different(color):
    assert remap_scramble_by_color("R U R'", color) != "R U R'"
