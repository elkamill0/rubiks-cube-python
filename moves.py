import copy


class Moves:
    def __init__(self, cube):
        self.cube = cube
        self.cube_backup = copy.deepcopy(cube)

    def R(self):
        for i in [2, 5, 8]:
            self.cube[0][i], self.cube[2][i], self.cube[5][i], self.cube[4][8 - i] = \
                self.cube[2][i], self.cube[5][i], self.cube[4][8 - i], self.cube[0][i]
        self._flip(self.cube[3])

    def Rp(self):
        for i in [2, 5, 8]:
            self.cube[0][i], self.cube[2][i], self.cube[4][8 - i], self.cube[5][i] = \
                self.cube[4][8 - i], self.cube[0][i], self.cube[5][i], self.cube[2][i]
        self._flipp(self.cube[3])

    def R2(self):
        self.R()
        self.R()
        # self._flip2(self.cube[3])

    def L(self):
        for i in [0, 3, 6]:
            self.cube[0][i], self.cube[2][i], self.cube[5][i], self.cube[4][8 - i] = \
                self.cube[4][8 - i], self.cube[0][i], self.cube[2][i], self.cube[5][i]
        self._flip(self.cube[1])

    def Lp(self):
        for i in [0, 3, 6]:
            self.cube[0][i], self.cube[2][i], self.cube[5][i], self.cube[4][8 - i] = \
                self.cube[2][i], self.cube[5][i], self.cube[4][8 - i], self.cube[0][i]
        self._flipp(self.cube[1])

    def L2(self):
        self.L()
        self.L()
        # self._flip2(self.cube[1])

    def U(self):
        for i in range(3):
            self.cube[1][i], self.cube[2][i], self.cube[3][i], self.cube[4][i] = \
                self.cube[2][i], self.cube[3][i], self.cube[4][i], self.cube[1][i]
        self._flip(self.cube[0])

    def Up(self):
        for i in range(3):
            self.cube[1][i], self.cube[2][i], self.cube[3][i], self.cube[4][i] = \
                self.cube[4][i], self.cube[1][i], self.cube[2][i], self.cube[3][i]
        self._flipp(self.cube[0])

    def U2(self):
        self.U()
        self.U()
        # self._flip2(self.cube[0])

    def D(self):
        for i in range(6, 9):
            self.cube[1][i], self.cube[2][i], self.cube[3][i], self.cube[4][i] = \
                self.cube[4][i], self.cube[1][i], self.cube[2][i], self.cube[3][i]
        self._flip(self.cube[5])

    def Dp(self):
        for i in range(6, 9):
            self.cube[1][i], self.cube[2][i], self.cube[3][i], self.cube[4][i] = \
                self.cube[2][i], self.cube[3][i], self.cube[4][i], self.cube[1][i]
        self._flipp(self.cube[5])

    def D2(self):
        self.D()
        self.D()
        # self._flip2(self.cube[5])

    def F(self):
        for i in range(3):
            self.cube[0][6 + i], self.cube[3][i * 3], self.cube[5][2 - i], self.cube[1][8 - i * 3] = \
                self.cube[1][8 - i * 3], self.cube[0][6 + i], self.cube[3][i * 3], self.cube[5][2 - i]
        self._flip(self.cube[2])

    def Fp(self):
        for i in range(3):
            self.cube[0][6 + i], self.cube[3][i * 3], self.cube[5][2 - i], self.cube[1][8 - i * 3] = \
                self.cube[3][i * 3], self.cube[5][2 - i], self.cube[1][8 - i * 3], self.cube[0][6 + i]
        self._flipp(self.cube[2])

    def F2(self):
        self.F()
        self.F()
        # self._flip2(self.cube[2])

    def B(self):
        for i in range(3):
            self.cube[0][i], self.cube[3][i * 3 + 2], self.cube[5][8 - i], self.cube[1][6 - i * 3] = \
                self.cube[3][i * 3 + 2], self.cube[5][8 - i], self.cube[1][6 - i * 3], self.cube[0][i]
        self._flip(self.cube[4])

    def Bp(self):
        for i in range(3):
            self.cube[0][i], self.cube[3][i * 3 + 2], self.cube[5][8 - i], self.cube[1][6 - i * 3] = \
                self.cube[1][6 - i * 3], self.cube[0][i], self.cube[3][i * 3 + 2], self.cube[5][8 - i]
        self._flipp(self.cube[4])

    def B2(self):
        self.B()
        self.B()
        # self._flip2(self.cube[4])

    @staticmethod
    def _flip(layer_name):
        layer_name[0], layer_name[2], layer_name[6], layer_name[8] = \
            layer_name[6], layer_name[0], layer_name[8], layer_name[2]
        layer_name[1], layer_name[3], layer_name[5], layer_name[7] = \
            layer_name[3], layer_name[7], layer_name[1], layer_name[5]

    @staticmethod
    def _flipp(layer_name):
        layer_name[0], layer_name[2], layer_name[6], layer_name[8] = layer_name[2], layer_name[8], layer_name[0], \
            layer_name[6]
        layer_name[1], layer_name[3], layer_name[5], layer_name[7] = layer_name[5], layer_name[1], layer_name[7], \
            layer_name[3]

    @staticmethod
    def _flip2(layer_name):
        layer_name[0], layer_name[8] = layer_name[8], layer_name[0]
        layer_name[2], layer_name[6] = layer_name[6], layer_name[2]
        layer_name[1], layer_name[7] = layer_name[7], layer_name[1]
        layer_name[3], layer_name[5] = layer_name[5], layer_name[3]

    def move_mapping(self):
        return {
            "R": lambda: self.R(),
            "R'": lambda: self.Rp(),
            "R2": lambda: self.R2(),
            "L": lambda: self.L(),
            "L'": lambda: self.Lp(),
            "L2": lambda: self.L2(),
            "U": lambda: self.U(),
            "U'": lambda: self.Up(),
            "U2": lambda: self.U2(),
            "D": lambda: self.D(),
            "D'": lambda: self.Dp(),
            "D2": lambda: self.D2(),
            "F": lambda: self.F(),
            "F'": lambda: self.Fp(),
            "F2": lambda: self.F2(),
            "B": lambda: self.B(),
            "B'": lambda: self.Bp(),
            "B2": lambda: self.B2()
        }

    def reset(self, cube_backup=None):
        if cube_backup:
            self.cube = cube_backup
            return cube_backup
        self.cube = [[0] * 9, [1] * 9, [2] * 9, [3] * 9, [4] * 9, [5] * 9]
        return self.cube
