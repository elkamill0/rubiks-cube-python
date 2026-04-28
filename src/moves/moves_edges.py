import numpy as np
from .moves_base import MovesBase

R_EDGES = [1, 9, 5, 10]
L_EDGES = [3, 11, 7, 8]
U_EDGES = [0, 1, 2, 3]
D_EDGES = [7, 6, 5, 4]
F_EDGES = [2, 10, 6, 11]
B_EDGES = [0, 8, 4, 9]
M_EDGES = [6, 2, 0, 4]
E_EDGES = [11, 10, 9, 8]
S_EDGES = [5, 1, 3, 7]


class MovesEdges(MovesBase):
    def __init__(self, edges):
        self.edges = edges

    def _rotate(self, element: list[int]):
        self.edges[element, 1] = 1 - self.edges[element, 1]

    def R(self) -> None:
        self._cycle_right(self.edges, R_EDGES)

    def Rp(self) -> None:
        self._cycle_left(self.edges, R_EDGES)

    def R2(self) -> None:
        self._swap_pairs(self.edges, R_EDGES)

    def L(self) -> None:
        self._cycle_right(self.edges, L_EDGES)

    def Lp(self) -> None:
        self._cycle_left(self.edges, L_EDGES)

    def L2(self) -> None:
        self._swap_pairs(self.edges, L_EDGES)

    def U(self) -> None:
        self._cycle_right(self.edges, U_EDGES)

    def Up(self) -> None:
        self._cycle_left(self.edges, U_EDGES)

    def U2(self) -> None:
        self._swap_pairs(self.edges, U_EDGES)

    def D(self) -> None:
        self._cycle_right(self.edges, D_EDGES)

    def Dp(self) -> None:
        self._cycle_left(self.edges, D_EDGES)

    def D2(self) -> None:
        self._swap_pairs(self.edges, D_EDGES)

    def F(self) -> None:
        self._cycle_right(self.edges, F_EDGES)
        self._rotate(F_EDGES)

    def Fp(self) -> None:
        self._cycle_left(self.edges, F_EDGES)
        self._rotate(F_EDGES)

    def F2(self) -> None:
        self._swap_pairs(self.edges, F_EDGES)

    def B(self) -> None:
        self._cycle_right(self.edges, B_EDGES)
        self._rotate(B_EDGES)

    def Bp(self) -> None:
        self._cycle_left(self.edges, B_EDGES)
        self._rotate(B_EDGES)

    def B2(self) -> None:
        self._swap_pairs(self.edges, B_EDGES)

    def E(self) -> None:
        self._rotate(E_EDGES)
        self._cycle_right(self.edges, E_EDGES)

    def Ep(self) -> None:
        self._rotate(E_EDGES)
        self._cycle_left(self.edges, E_EDGES)

    def E2(self) -> None:
        self._swap_pairs(self.edges, E_EDGES)

    def M(self) -> None:
        self._rotate(M_EDGES)
        self._cycle_left(self.edges, M_EDGES)

    def Mp(self) -> None:
        self._rotate(M_EDGES)
        self._cycle_right(self.edges, M_EDGES)

    def M2(self) -> None:
        self._swap_pairs(self.edges, M_EDGES)

    def S(self) -> None:
        self._cycle_left(self.edges, S_EDGES)
        self._rotate(S_EDGES)

    def Sp(self) -> None:
        self._cycle_right(self.edges, S_EDGES)
        self._rotate(S_EDGES)

    def S2(self) -> None:
        self._swap_pairs(self.edges, S_EDGES)

    def r(self) -> None:
        MovesEdges.R(self)
        MovesEdges.Mp(self)

    def rp(self) -> None:
        MovesEdges.Rp(self)
        MovesEdges.M(self)

    def r2(self) -> None:
        MovesEdges.R2(self)
        MovesEdges.M2(self)

    def l(self) -> None:
        MovesEdges.L(self)
        MovesEdges.M(self)

    def lp(self) -> None:
        MovesEdges.Lp(self)
        MovesEdges.Mp(self)

    def l2(self) -> None:
        MovesEdges.L2(self)
        MovesEdges.M2(self)

    def u(self) -> None:
        MovesEdges.U(self)
        MovesEdges.Ep(self)

    def up(self) -> None:
        MovesEdges.Up(self)
        MovesEdges.E(self)

    def u2(self) -> None:
        MovesEdges.U2(self)
        MovesEdges.E2(self)

    def d(self) -> None:
        MovesEdges.D(self)
        MovesEdges.E(self)

    def dp(self) -> None:
        MovesEdges.Dp(self)
        MovesEdges.Ep(self)

    def d2(self) -> None:
        MovesEdges.D2(self)
        MovesEdges.E2(self)

    def f(self) -> None:
        MovesEdges.F(self)
        MovesEdges.S(self)

    def fp(self) -> None:
        MovesEdges.Fp(self)
        MovesEdges.Sp(self)

    def f2(self) -> None:
        MovesEdges.F2(self)
        MovesEdges.S2(self)

    def b(self) -> None:
        MovesEdges.B(self)
        MovesEdges.Sp(self)

    def bp(self) -> None:
        MovesEdges.Bp(self)
        MovesEdges.S(self)

    def b2(self) -> None:
        MovesEdges.B2(self)
        MovesEdges.S2(self)

    def x(self) -> None:
        MovesEdges.Mp(self)
        MovesEdges.R(self)
        MovesEdges.Lp(self)

    def xp(self) -> None:
        MovesEdges.M(self)
        MovesEdges.Rp(self)
        MovesEdges.L(self)

    def x2(self) -> None:
        MovesEdges.M2(self)
        MovesEdges.R2(self)
        MovesEdges.L2(self)

    def z(self) -> None:
        MovesEdges.F(self)
        MovesEdges.S(self)
        MovesEdges.Bp(self)

    def zp(self) -> None:
        MovesEdges.Fp(self)
        MovesEdges.Sp(self)
        MovesEdges.B(self)

    def z2(self) -> None:
        MovesEdges.F2(self)
        MovesEdges.S2(self)
        MovesEdges.B2(self)

    def y(self) -> None:
        MovesEdges.U(self)
        MovesEdges.Dp(self)
        MovesEdges.Ep(self)

    def yp(self) -> None:
        MovesEdges.Up(self)
        MovesEdges.D(self)
        MovesEdges.E(self)

    def y2(self) -> None:
        MovesEdges.U2(self)
        MovesEdges.D2(self)
        MovesEdges.E2(self)


if __name__ == "__main__":
    edges = np.zeros((12, 2), dtype=np.int8)
    edges[:, 0] = np.arange(12, dtype=np.int8)
    edges[:, 1] = 0

    centers = np.arange(6, dtype=np.uint8)

    moves = MovesEdges(edges)

    moves.Rp()

    print(edges)
