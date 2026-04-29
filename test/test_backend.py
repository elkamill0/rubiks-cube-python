from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_scramble_returns_200():
    response = client.post("/cube/scramble", json={})
    assert response.status_code == 200


def test_scramble_with_known_input():
    response = client.post(
        "/cube/scramble",
        json={
            "scramble": "R2 D L2 F2 U' F2 D2 U L2 B2 U F L' U2 B' F L' U2 B2 U L'",
            "color": "y",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert (
        data["scramble"] == "R2 D L2 F2 U' F2 D2 U L2 B2 U F L' U2 B' F L' U2 B2 U L'"
    )
    assert (
        data["cube_state"] == "230201445330510113331422433441534215205541100550250422"
    )


def test_scramble_without_input():
    response = client.post("/cube/scramble", json={})
    data = response.json()
    assert data["scramble"] != ""
    assert data["cube_state"] != ""


def test_solve_returns_solutions():
    response = client.post("/cube/solve", json={})
    data = response.json()
    assert len(data["solutions"]) > 0
    assert "moves" in data["solutions"][0]
    assert "total_moves" in data["solutions"][0]


def test_solve_returns_solutions():
    response = client.post(
        "/cube/solve",
        json={
            "scramble": "R2 D L2 F2 U' F2 D2 U L2 B2 U F L' U2 B' F L' U2 B2 U L'",
            "cross_color": "y",
            "cross_length": 5,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert len(data["solutions"]) > 0
    assert "moves" in data["solutions"][0]
    assert "total_moves" in data["solutions"][0]
