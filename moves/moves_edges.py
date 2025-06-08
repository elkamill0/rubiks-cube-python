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
        self.__rotate([2,10,6,11])
        
    def Fp(self) -> None:
        self.edges[[2,10,6,11]] = self.edges[[10,6,11,2]]
        self.__rotate([2,10,6,11])

    def F2(self) -> None:
        self.edges[[2,10,6,11]] = self.edges[[6,11,2,10]]

    def B(self) -> None:
        self.edges[[0,8,4,9]] = self.edges[[9,0,8,4]]
        self.__rotate([0,8,4,9])
        
    def Bp(self) -> None:
        self.edges[[0,8,4,9]] = self.edges[[8,4,9,0]]
        self.__rotate([0,8,4,9])

    def B2(self) -> None:
        self.edges[[0,8,4,9]] = self.edges[[4,9,0,8]]
    

if __name__ == "__main__":
    edges = np.zeros((12, 2), dtype=np.int8)
    edges[:, 0] = np.arange(12, dtype=np.int8)
    edges[:, 1] = 0

    centers = np.arange(6, dtype=np.uint8)

    moves = MovesEdges(edges)

    moves.Rp()

    print(edges)


    