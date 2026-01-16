import numpy as np

class MovesCenters:
    def __init__(self, centers):
        self.centers = centers

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
        self.centers[[1,2,3,4]] = self.centers[[4,1,2,3]]
    
    def Ep(self) -> None:
        self.centers[[1,2,3,4]] = self.centers[[2,3,4,1]]

    def E2(self) -> None:
        self.centers[[1,2,3,4]] = self.centers[[3,4,1,2]]

    def Mp(self) -> None:
        self.centers[[0,2,5,4]] = self.centers[[2,5,4,0]]

    def M(self) -> None:
        self.centers[[0,2,5,4]] = self.centers[[4,0,2,5]]

    def M2(self) -> None:
        self.centers[[0,2,5,4]] = self.centers[[5,4,0,2]]

    def Sp(self) -> None:
        self.centers[[0,3,5,1]] = self.centers[[3,5,1,0]]

    def S(self) -> None:
        self.centers[[0,3,5,1]] = self.centers[[1,0,3,5]]

    def S2(self) -> None:
        self.centers[[0,3,5,1]] = self.centers[[5,1,0,3]]

    def y(self) -> None:
        MovesCenters.Ep(self)
        self.rotation += "y "

    def yp(self) -> None:
        MovesCenters.E(self)
        self.rotation += "y' "

    def y2(self) -> None:
        MovesCenters.E2(self)
        self.rotation += "y2 "

    def x(self) -> None:
        MovesCenters.Mp(self)
        self.rotation += "x "

    def xp(self) -> None:
        MovesCenters.M(self)
        self.rotation += "x' "

    def x2(self) -> None:
        MovesCenters.M2(self)
        self.rotation += "x2 "

    def z(self) -> None:
        MovesCenters.S(self)
        self.rotation += "z "

    def zp(self) -> None:
        MovesCenters.Sp(self)
        self.rotation += "z' "

    def z2(self) -> None:
        MovesCenters.S2(self)
        self.rotation += "z2 "