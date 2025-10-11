import numpy as np

class MovesEdges:
    def __init__(self, edges):
        self.edges = edges

    def __rotate(self, element: list[int]):
        self.edges[element,1] = 1 - self.edges[element, 1]

    def R(self) -> None:
        self.edges[[1,9,5,10]] = self.edges[[10,1,9,5]]
        
    def Rp(self) -> None:
        self.edges[[1,9,5,10]] = self.edges[[9,5,10,1]]

    def R2(self) -> None:
        self.edges[[1,9,5,10]] = self.edges[[5,10,1,9]]

    def L(self) -> None:
        self.edges[[3,11,7,8]] = self.edges[[8,3,11,7]]
        
    def Lp(self) -> None:
        self.edges[[3,11,7,8]] = self.edges[[11,7,8,3]]

    def L2(self) -> None:
        self.edges[[3,11,7,8]] = self.edges[[7,8,3,11]]

    def U(self) -> None:
        self.edges[[0,1,2,3]] = self.edges[[3,0,1,2]]
        
    def Up(self) -> None:
        self.edges[[0,1,2,3]] = self.edges[[1,2,3,0]]

    def U2(self) -> None:
        self.edges[[0,1,2,3]] = self.edges[[2,3,0,1]]

    def D(self) -> None:
        self.edges[[4,5,6,7]] = self.edges[[5,6,7,4]]
        
    def Dp(self) -> None:
        self.edges[[4,5,6,7]] = self.edges[[7,4,5,6]]

    def D2(self) -> None:
        self.edges[[4,5,6,7]] = self.edges[[6,7,4,5]]

    def F(self) -> None:
        self.edges[[2,10,6,11]] = self.edges[[11,2,10,6]]
        MovesEdges.__rotate(self, [2,10,6,11])
        
    def Fp(self) -> None:
        self.edges[[2,10,6,11]] = self.edges[[10,6,11,2]]
        MovesEdges.__rotate(self, [2,10,6,11])

    def F2(self) -> None:
        self.edges[[2,10,6,11]] = self.edges[[6,11,2,10]]

    def B(self) -> None:
        self.edges[[0,8,4,9]] = self.edges[[9,0,8,4]]
        MovesEdges.__rotate(self, [0,8,4,9])
        
    def Bp(self) -> None:
        self.edges[[0,8,4,9]] = self.edges[[8,4,9,0]]
        MovesEdges.__rotate(self, [0,8,4,9])

    def B2(self) -> None:
        self.edges[[0,8,4,9]] = self.edges[[4,9,0,8]]

    def y(self) -> None:
        MovesEdges.U(self)
        MovesEdges.Dp(self)
        MovesEdges.__rotate(self, [i for i in self.edges[:8] if i[0] >= 8])
        MovesEdges.Ep(self)

    def yp(self) -> None:
        MovesEdges.Up(self)
        MovesEdges.D(self)
        MovesEdges.__rotate(self, [i for i in self.edges[:8] if i[0] >= 8])
        MovesEdges.E(self)

    def y2(self) -> None:
        MovesEdges.U2(self)
        MovesEdges.D2(self)
        MovesEdges.E2(self)

    def E(self) -> None:
        MovesEdges.__rotate(self, [i for i in self.edges[8:] if i[0] < 8])
        self.edges[[8,9,10,11]] = self.edges[[9,10,11,8]]

    def Ep(self) -> None:
        MovesEdges.__rotate(self, [i for i in self.edges[8:] if i[0] >= 8])
        self.edges[[8,9,10,11]] = self.edges[[11,8,9,10]]

    def E2(self) -> None:
        self.edges[[8,9,10,11]] = self.edges[[10,11,8,9]] 

    def Mp(self) -> None:
        for i,e in enumerate(self.edges[:8]):
            if (e[0]%2) == (i%2):
                e[1]^=1
        for i,e in enumerate(self.edges[8:12], start=8):
            if (e[0]%2) != (i%2) and e[0] != i:
                e[1]^=1
        self.edges[[0,2,6,4]] = self.edges[[2,6,4,0]]

    def M(self) -> None:
        for i,e in enumerate(self.edges[:8]):
            if (e[0]%2) == (i%2):
                e[1]^=1
        for i,e in enumerate(self.edges[8:12], start=8):
            if (e[0]%2) == (i%2):
                e[1]^=1
        self.edges[[0,2,6,4]] = self.edges[[4,0,2,6]]
    
    def M2(self) -> None:
        self.edges[[0,2,6,4]] = self.edges[[6,4,2,0]]


    def x(self) -> None:
        MovesEdges.Mp(self)
        # MovesEdges.R(self)
        # MovesEdges.Lp(self)
        
    


if __name__ == "__main__":
    edges = np.zeros((12, 2), dtype=np.int8)
    edges[:, 0] = np.arange(12, dtype=np.int8)
    edges[:, 1] = 0

    centers = np.arange(6, dtype=np.uint8)

    moves = MovesEdges(edges)

    moves.Rp()

    print(edges)


    