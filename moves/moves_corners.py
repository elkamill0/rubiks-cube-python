import numpy as np

class MovesCorners:
    def __init__(self, corners):
        self.corners = corners

    def __rotate_corner(self, element: list[int], clockwise=True):
        operation = np.array([1, -1, 1, -1], dtype=np.int8)
        if not clockwise:
            operation = -operation
        self.corners[element, 1] = self.corners[element, 1].astype(np.int8) + operation
        self.corners[element, 1] = np.where(self.corners[element, 1] < 0, 2, self.corners[element, 1])
        self.corners[element, 1] = np.where(self.corners[element, 1] > 2, 0, self.corners[element, 1])
        

    def R(self) -> None:
        self.corners[[1,2,6,5]] = self.corners[[2,6,5,1]]
        self.__rotate_corner([1,2,6,5], clockwise=True)
        
    def Rp(self) -> None:
        self.corners[[1,2,6,5]] = self.corners[[5,1,2,6]]
        self.__rotate_corner([1,2,6,5], clockwise=True)

    def R2(self) -> None:
        self.corners[[1,2,6,5]] = self.corners[[6,5,1,2]]

    def L(self) -> None:
        self.corners[[0,3,7,4]] = self.corners[[4,0,3,7]]
        self.__rotate_corner([0,3,7,4], clockwise=False)
        
    def Lp(self) -> None:
        self.corners[[0,3,7,4]] = self.corners[[3,7,4,0]]
        self.__rotate_corner([0,3,7,4], clockwise=False)

    def L2(self) -> None:
        self.corners[[0,3,7,4]] = self.corners[[7,4,0,3]]

    def U(self) -> None:
        self.corners[[0,1,2,3]] = self.corners[[3,0,1,2]]
        
    def Up(self) -> None:
        self.corners[[0,1,2,3]] = self.corners[[1,2,3,0]]

    def U2(self) -> None:
        self.corners[[0,1,2,3]] = self.corners[[2,3,0,1]]

    def D(self) -> None:
        self.corners[[4,5,6,7]] = self.corners[[5,6,7,4]]
        
    def Dp(self) -> None:
        self.corners[[4,5,6,7]] = self.corners[[7,4,5,6]]

    def D2(self) -> None:
        self.corners[[4,5,6,7]] = self.corners[[6,7,4,5]]

    def F(self) -> None:
        self.corners[[3,2,6,7]] = self.corners[[7,3,2,6]]
        self.__rotate_corner([3,2,6,7], clockwise=False)
        
    def Fp(self) -> None:
        self.corners[[3,2,6,7]] = self.corners[[2,6,7,3]]
        self.__rotate_corner([3,2,6,7], clockwise=False)

    def F2(self) -> None:
        self.corners[[3,2,6,7]] = self.corners[[6,7,3,2]]

    def B(self) -> None:
        self.corners[[0,4,5,1]] = self.corners[[1,0,4,5]]
        self.__rotate_corner([0,4,5,1], clockwise=True)
        
    def Bp(self) -> None:
        self.corners[[0,4,5,1]] = self.corners[[4,5,1,0]]
        self.__rotate_corner([0,4,5,1], clockwise=True)

    def B2(self) -> None:
        self.corners[[0,4,5,1]] = self.corners[[5,1,0,4]]
    

if __name__ == "__main__":
    corners = np.zeros((8, 2), dtype=np.int8)
    corners[:, 0] = np.arange(8, dtype=np.int8)
    corners[:, 1] = 0

    edges = np.zeros((12, 2), dtype=np.int16)
    edges[:, 0] = np.arange(12, dtype=np.int16)
    edges[:, 1] = 0

    centers = np.arange(6, dtype=np.uint8)

    moves = Moves(corners, edges, centers)

    moves.B2()

    print(corners)


    