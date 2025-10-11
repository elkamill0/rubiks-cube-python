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
        self.centers[[1,2,3,4]] = self.centers[[2,3,4,1]]
    
    def Ep(self) -> None:
        self.centers[[1,2,3,4]] = self.centers[[4,1,2,3]]

    def E2(self) -> None:
        self.centers[[1,2,3,4]] = self.centers[[3,4,1,2]]

    def Mp(self) -> None:
        self.centers[[0,2,5,4]] = self.centers[[4,0,2,5]]

    def M(self) -> None:
        self.centers[[0,2,5,4]] = self.centers[[2,5,4,0]]

    def M2(self) -> None:
        self.centers[[0,2,5,4]] = self.centers[[5,4,0,2]]


    def y(self) -> None:
        MovesCenters.E(self)

    def yp(self) -> None:
        MovesCenters.Ep(self)

    def y2(self) -> None:
        MovesCenters.E2(self)

    def x(self) -> None:
        MovesCenters.M(self)
