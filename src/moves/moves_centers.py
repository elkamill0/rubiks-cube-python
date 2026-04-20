from .moves_base import MovesBase

E_CENTERS = [1,2,3,4]
M_CENTERS = [5,2,0,4]
S_CENTERS = [5,3,0,1]

class MovesCenters(MovesBase):
    def __init__(self, centers):
        self.centers = centers

    def R(self) -> None:
        pass

    def Rp(self) -> None:
        pass

    def R2(self) -> None:
        pass

    def L(self) -> None:
        pass

    def Lp(self) -> None:
        pass

    def L2(self) -> None:
        pass

    def U(self) -> None:
        pass

    def Up(self) -> None:
        pass

    def U2(self) -> None:
        pass

    def D(self) -> None:
        pass

    def Dp(self) -> None:
        pass

    def D2(self) -> None:
        pass

    def F(self) -> None:
        pass

    def Fp(self) -> None:
        pass

    def F2(self) -> None:
        pass

    def B(self) -> None:
        pass

    def Bp(self) -> None:
        pass

    def B2(self) -> None:
        pass

    def E(self) -> None:
        self._cycle_right(self.centers, E_CENTERS)

    def Ep(self) -> None:
        self._cycle_left(self.centers, E_CENTERS)

    def E2(self) -> None:
        self._swap_pairs(self.centers, E_CENTERS)

    def M(self) -> None:
        self._cycle_left(self.centers, M_CENTERS)

    def Mp(self) -> None:
        self._cycle_right(self.centers, M_CENTERS)

    def M2(self) -> None:
        self._swap_pairs(self.centers, M_CENTERS)

    def S(self) -> None:
        self._cycle_left(self.centers, S_CENTERS)
        
    def Sp(self) -> None:
        self._cycle_right(self.centers, S_CENTERS)

    def S2(self) -> None:
        self._swap_pairs(self.centers, S_CENTERS)

    def r(self) -> None:
        MovesCenters.Mp(self)

    def rp(self) -> None:
        MovesCenters.M(self)

    def r2(self) -> None:
        MovesCenters.M2(self)

    def l(self) -> None:
        MovesCenters.M(self)

    def lp(self) -> None:
        MovesCenters.Mp(self)

    def l2(self) -> None:
        MovesCenters.M2(self)

    def u(self) -> None:
        MovesCenters.Ep(self)

    def up(self) -> None:
        MovesCenters.E(self)

    def u2(self) -> None:
        MovesCenters.E2(self)

    def d(self) -> None:
        MovesCenters.E(self)

    def dp(self) -> None:
        MovesCenters.Ep(self)

    def d2(self) -> None:
        MovesCenters.E2(self)

    def f(self) -> None:
        MovesCenters.S(self)

    def fp(self) -> None:
        MovesCenters.Sp(self)

    def f2(self) -> None:
        MovesCenters.S2(self)

    def b(self) -> None:
        MovesCenters.Sp(self)

    def bp(self) -> None:
        MovesCenters.S(self)

    def b2(self) -> None:
        MovesCenters.S2(self)

    def y(self) -> None:
        MovesCenters.Ep(self)

    def yp(self) -> None:
        MovesCenters.E(self)

    def y2(self) -> None:
        MovesCenters.E2(self)

    def x(self) -> None:
        MovesCenters.Mp(self)

    def xp(self) -> None:
        MovesCenters.M(self)

    def x2(self) -> None:
        MovesCenters.M2(self)

    def z(self) -> None:
        MovesCenters.S(self)

    def zp(self) -> None:
        MovesCenters.Sp(self)

    def z2(self) -> None:
        MovesCenters.S2(self)
