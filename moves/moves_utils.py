import numpy as np

class MovesUtils:
    def __init__(self, y_rotation):
        self.y_rotation = y_rotation

    def R(self) -> None: pass
    def Rp(self) -> None: pass
    def R2(self) -> None: pass

    def L(self) -> None: pass
    def Lp(self) -> None: pass
    def L2(self) -> None: pass

    def U(self) -> None: pass
    def Up(self) -> None: pass
    def U2(self) -> None: pass

    def D(self) -> None: pass
    def Dp(self) -> None: pass
    def D2(self) -> None: pass

    def F(self) -> None: pass
    def Fp(self) -> None: pass
    def F2(self) -> None: pass

    def B(self) -> None: pass
    def Bp(self) -> None: pass
    def B2(self) -> None: pass

    def E(self) -> None: 
        self.y_rotation = (self.y_rotation - 1) % 4

    def Ep(self) -> None:
        self.y_rotation = (self.y_rotation + 1) % 4

    def E2(self) -> None: 
        self.y_rotation = (self.y_rotation + 2) % 4

    def Mp(self) -> None: pass
    def M(self) -> None: pass
    def M2(self) -> None: pass
    def Sp(self) -> None: pass
    def S(self) -> None: pass
    def S2(self) -> None: pass

    def r(self) -> None: pass
    def rp(self) -> None: pass
    def r2(self) -> None: pass
    def l(self) -> None: pass
    def lp(self) -> None: pass
    def l2(self) -> None: pass
    def u(self) -> None: pass
    def up(self) -> None: pass
    def u2(self) -> None: pass
    def d(self) -> None: pass
    def dp(self) -> None: pass
    def d2(self) -> None: pass
    def f(self) -> None: pass
    def fp(self) -> None: pass
    def f2(self) -> None: pass
    def b(self) -> None: pass
    def bp(self) -> None: pass
    def b2(self) -> None: pass

    def y(self) -> None: pass
    def yp(self) -> None: pass
    def y2(self) -> None: pass
    def x(self) -> None: pass
    def xp(self) -> None: pass
    def x2(self) -> None: pass
    def z(self) -> None: pass
    def zp(self) -> None: pass
    def z2(self) -> None: pass