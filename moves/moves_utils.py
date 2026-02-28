import numpy as np

class MovesUtils:
    def __init__(self, y_rotate):
        self.y_rotate = y_rotate

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
        self.y_rotate = (self.y_rotate - 1) % 4

    def Ep(self) -> None:
        self.y_rotate = (self.y_rotate + 1) % 4

    def E2(self) -> None: 
        self.y_rotate = (self.y_rotate + 2) % 4

    def Mp(self) -> None: pass
    def M(self) -> None: pass
    def M2(self) -> None: pass
    def Sp(self) -> None: pass
    def S(self) -> None: pass
    def S2(self) -> None: pass

    def r(self) -> None:
        MovesUtils.R(self)
        MovesUtils.Mp(self)

    def rp(self) -> None:
        MovesUtils.Rp(self)
        MovesUtils.M(self)

    def r2(self) -> None:
        MovesUtils.R2(self)
        MovesUtils.M2(self)

    def l(self) -> None:
        MovesUtils.L(self)
        MovesUtils.M(self)

    def lp(self) -> None:
        MovesUtils.Lp(self)
        MovesUtils.Mp(self)

    def l2(self) -> None:
        MovesUtils.L2(self)
        MovesUtils.M2(self)

    def u(self) -> None:
        MovesUtils.U(self)
        MovesUtils.Ep(self)

    def up(self) -> None:
        MovesUtils.Up(self)
        MovesUtils.E(self)

    def u2(self) -> None:
        MovesUtils.U2(self)
        MovesUtils.E2(self)

    def d(self) -> None:
        MovesUtils.D(self)
        MovesUtils.E(self)

    def dp(self) -> None:
        MovesUtils.Dp(self)
        MovesUtils.Ep(self)

    def d2(self) -> None:
        MovesUtils.D2(self)
        MovesUtils.E2(self)

    def f(self) -> None:
        MovesUtils.F(self)
        MovesUtils.S(self)

    def fp(self) -> None:
        MovesUtils.Fp(self)
        MovesUtils.Sp(self)

    def f2(self) -> None:
        MovesUtils.F2(self)
        MovesUtils.S2(self)

    def b(self) -> None:
        MovesUtils.B(self)
        MovesUtils.Sp(self)

    def bp(self) -> None:
        MovesUtils.Bp(self)
        MovesUtils.S(self)

    def b2(self) -> None:
        MovesUtils.B2(self)
        MovesUtils.S2(self)

    def x(self) -> None:
        MovesUtils.Mp(self)
        MovesUtils.R(self)
        MovesUtils.Lp(self)
        
    def xp(self) -> None:
        MovesUtils.M(self)
        MovesUtils.Rp(self)
        MovesUtils.L(self)
    
    def x2(self) -> None:
        MovesUtils.M2(self)
        MovesUtils.R2(self)
        MovesUtils.L2(self)

    def z(self) -> None:
        MovesUtils.F(self)
        MovesUtils.S(self)
        MovesUtils.Bp(self)
        
    def zp(self) -> None:
        MovesUtils.Fp(self)
        MovesUtils.Sp(self)
        MovesUtils.B(self)
    
    def z2(self) -> None:
        MovesUtils.F2(self)
        MovesUtils.S2(self)
        MovesUtils.B2(self)

    def y(self) -> None:
        MovesUtils.U(self)
        MovesUtils.Dp(self)
        MovesUtils.Ep(self)

    def yp(self) -> None:
        MovesUtils.Up(self)
        MovesUtils.D(self)
        MovesUtils.E(self)

    def y2(self) -> None:
        MovesUtils.U2(self)
        MovesUtils.D2(self)
        MovesUtils.E2(self)