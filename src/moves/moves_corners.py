import numpy as np


class MovesCorners:
    def __init__(self, corners):
        self.corners = corners

    def __rotate_corner(self, element: list[int], clockwise=True):
        operation = np.array([1, -1, 1, -1], dtype=np.int8)
        if not clockwise:
            operation = -operation
        self.corners[element, 1] = self.corners[element, 1].astype(np.int8) + operation
        self.corners[element, 1] = np.where(
            self.corners[element, 1] < 0, 2, self.corners[element, 1]
        )
        self.corners[element, 1] = np.where(
            self.corners[element, 1] > 2, 0, self.corners[element, 1]
        )

    def R(self) -> None:
        self.corners[[1, 2, 6, 5]] = self.corners[[2, 6, 5, 1]]
        MovesCorners.__rotate_corner(self, [1, 2, 6, 5], clockwise=True)

    def Rp(self) -> None:
        self.corners[[1, 2, 6, 5]] = self.corners[[5, 1, 2, 6]]
        MovesCorners.__rotate_corner(self, [1, 2, 6, 5], clockwise=True)

    def R2(self) -> None:
        self.corners[[1, 2, 6, 5]] = self.corners[[6, 5, 1, 2]]

    def L(self) -> None:
        self.corners[[0, 3, 7, 4]] = self.corners[[4, 0, 3, 7]]
        MovesCorners.__rotate_corner(self, [0, 3, 7, 4], clockwise=False)

    def Lp(self) -> None:
        self.corners[[0, 3, 7, 4]] = self.corners[[3, 7, 4, 0]]
        MovesCorners.__rotate_corner(self, [0, 3, 7, 4], clockwise=False)

    def L2(self) -> None:
        self.corners[[0, 3, 7, 4]] = self.corners[[7, 4, 0, 3]]

    def U(self) -> None:
        self.corners[[0, 1, 2, 3]] = self.corners[[3, 0, 1, 2]]

    def Up(self) -> None:
        self.corners[[0, 1, 2, 3]] = self.corners[[1, 2, 3, 0]]

    def U2(self) -> None:
        self.corners[[0, 1, 2, 3]] = self.corners[[2, 3, 0, 1]]

    def D(self) -> None:
        self.corners[[4, 5, 6, 7]] = self.corners[[5, 6, 7, 4]]

    def Dp(self) -> None:
        self.corners[[4, 5, 6, 7]] = self.corners[[7, 4, 5, 6]]

    def D2(self) -> None:
        self.corners[[4, 5, 6, 7]] = self.corners[[6, 7, 4, 5]]

    def F(self) -> None:
        self.corners[[3, 2, 6, 7]] = self.corners[[7, 3, 2, 6]]
        MovesCorners.__rotate_corner(self, [3, 2, 6, 7], clockwise=False)

    def Fp(self) -> None:
        self.corners[[3, 2, 6, 7]] = self.corners[[2, 6, 7, 3]]
        MovesCorners.__rotate_corner(self, [3, 2, 6, 7], clockwise=False)

    def F2(self) -> None:
        self.corners[[3, 2, 6, 7]] = self.corners[[6, 7, 3, 2]]

    def B(self) -> None:
        self.corners[[0, 4, 5, 1]] = self.corners[[1, 0, 4, 5]]
        MovesCorners.__rotate_corner(self, [0, 4, 5, 1], clockwise=True)

    def Bp(self) -> None:
        self.corners[[0, 4, 5, 1]] = self.corners[[4, 5, 1, 0]]
        MovesCorners.__rotate_corner(self, [0, 4, 5, 1], clockwise=True)

    def B2(self) -> None:
        self.corners[[0, 4, 5, 1]] = self.corners[[5, 1, 0, 4]]

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
