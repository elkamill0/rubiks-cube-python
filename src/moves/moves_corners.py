import numpy as np
from .moves_base import MovesBase

R_CORNERS = [2, 1, 5, 6]
L_CORNERS = [0, 3, 7, 4]
U_CORNERS = [0, 1, 2, 3]
D_CORNERS = [7, 6, 5, 4]
F_CORNERS = [3, 2, 6, 7]
B_CORNERS = [1, 0, 4, 5]


class MovesCorners(MovesBase):
    def __init__(self, corners):
        self.corners = corners

    def _rotate_corner(self, element: list[int]):
        operation = np.array([-1, 1, -1, 1], dtype=np.int8)
        self.corners[element, 1] = (
            self.corners[element, 1].astype(np.int8) + operation
        ) % 3

    def R(self) -> None:
        self._cycle_right(self.corners, R_CORNERS)
        self._rotate_corner(R_CORNERS)

    def Rp(self) -> None:
        self._cycle_left(self.corners, R_CORNERS)
        self._rotate_corner(R_CORNERS)

    def R2(self) -> None:
        self._swap_pairs(self.corners, R_CORNERS)

    def L(self) -> None:
        self._cycle_right(self.corners, L_CORNERS)
        self._rotate_corner(L_CORNERS)

    def Lp(self) -> None:
        self._cycle_left(self.corners, L_CORNERS)
        self._rotate_corner(L_CORNERS)

    def L2(self) -> None:
        self._swap_pairs(self.corners, L_CORNERS)

    def U(self) -> None:
        self._cycle_right(self.corners, U_CORNERS)

    def Up(self) -> None:
        self._cycle_left(self.corners, U_CORNERS)

    def U2(self) -> None:
        self._swap_pairs(self.corners, U_CORNERS)

    def D(self) -> None:
        self._cycle_right(self.corners, D_CORNERS)

    def Dp(self) -> None:
        self._cycle_left(self.corners, D_CORNERS)

    def D2(self) -> None:
        self._swap_pairs(self.corners, D_CORNERS)

    def F(self) -> None:
        self._cycle_right(self.corners, F_CORNERS)
        self._rotate_corner(F_CORNERS)

    def Fp(self) -> None:
        self._cycle_left(self.corners, F_CORNERS)
        self._rotate_corner(F_CORNERS)

    def F2(self) -> None:
        self._swap_pairs(self.corners, F_CORNERS)

    def B(self) -> None:
        self._cycle_right(self.corners, B_CORNERS)
        self._rotate_corner(B_CORNERS)

    def Bp(self) -> None:
        self._cycle_left(self.corners, B_CORNERS)
        self._rotate_corner(B_CORNERS)

    def B2(self) -> None:
        self._swap_pairs(self.corners, B_CORNERS)

    def E(self) -> None:
        pass

    def Ep(self) -> None:
        pass

    def E2(self) -> None:
        pass

    def M(self) -> None:
        pass

    def Mp(self) -> None:
        pass

    def M2(self) -> None:
        pass

    def S(self) -> None:
        pass

    def Sp(self) -> None:
        pass

    def S2(self) -> None:
        pass

    def r(self) -> None:
        MovesCorners.R(self)
        MovesCorners.Mp(self)

    def rp(self) -> None:
        MovesCorners.Rp(self)
        MovesCorners.M(self)

    def r2(self) -> None:
        MovesCorners.R2(self)
        MovesCorners.M2(self)

    def l(self) -> None:
        MovesCorners.L(self)
        MovesCorners.M(self)

    def lp(self) -> None:
        MovesCorners.Lp(self)
        MovesCorners.Mp(self)

    def l2(self) -> None:
        MovesCorners.L2(self)
        MovesCorners.M2(self)

    def u(self) -> None:
        MovesCorners.U(self)
        MovesCorners.Ep(self)

    def up(self) -> None:
        MovesCorners.Up(self)
        MovesCorners.E(self)

    def u2(self) -> None:
        MovesCorners.U2(self)
        MovesCorners.E2(self)

    def d(self) -> None:
        MovesCorners.D(self)
        MovesCorners.E(self)

    def dp(self) -> None:
        MovesCorners.Dp(self)
        MovesCorners.Ep(self)

    def d2(self) -> None:
        MovesCorners.D2(self)
        MovesCorners.E2(self)

    def f(self) -> None:
        MovesCorners.F(self)
        MovesCorners.S(self)

    def fp(self) -> None:
        MovesCorners.Fp(self)
        MovesCorners.Sp(self)

    def f2(self) -> None:
        MovesCorners.F2(self)
        MovesCorners.S2(self)

    def b(self) -> None:
        MovesCorners.B(self)
        MovesCorners.Sp(self)

    def bp(self) -> None:
        MovesCorners.Bp(self)
        MovesCorners.S(self)

    def b2(self) -> None:
        MovesCorners.B2(self)
        MovesCorners.S2(self)

    def y(self) -> None:
        MovesCorners.U(self)
        MovesCorners.Dp(self)

    def yp(self) -> None:
        MovesCorners.Up(self)
        MovesCorners.D(self)

    def y2(self) -> None:
        MovesCorners.U2(self)
        MovesCorners.D2(self)

    def x(self) -> None:
        MovesCorners.R(self)
        MovesCorners.Lp(self)

    def xp(self) -> None:
        MovesCorners.Rp(self)
        MovesCorners.L(self)

    def x2(self) -> None:
        MovesCorners.R2(self)
        MovesCorners.L2(self)

    def z(self) -> None:
        MovesCorners.F(self)
        MovesCorners.Bp(self)

    def zp(self) -> None:
        MovesCorners.Fp(self)
        MovesCorners.B(self)

    def z2(self) -> None:
        MovesCorners.F2(self)
        MovesCorners.B2(self)
