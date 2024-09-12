import moves_upgrade_py

class Moves:
    def __init__(self, cube):
        self.cube = cube

    def R(self):
        moves_upgrade_py.R(self.cube)

    def Rp(self):
        moves_upgrade_py.Rp(self.cube)

    def R2(self):
        moves_upgrade_py.R2(self.cube)

    def L(self):
        moves_upgrade_py.L(self.cube)

    def Lp(self):
        moves_upgrade_py.Lp(self.cube)

    def L2(self):
        moves_upgrade_py.L2(self.cube)

    def U(self):
        moves_upgrade_py.U(self.cube)

    def Up(self):
        moves_upgrade_py.Up(self.cube)

    def U2(self):
        moves_upgrade_py.U2(self.cube)

    def D(self):
        moves_upgrade_py.D(self.cube)

    def Dp(self):
        moves_upgrade_py.Dp(self.cube)

    def D2(self):
        moves_upgrade_py.D2(self.cube)

    def F(self):
        moves_upgrade_py.F(self.cube)

    def Fp(self):
        moves_upgrade_py.Fp(self.cube)

    def F2(self):
        moves_upgrade_py.F2(self.cube)

    def B(self):
        moves_upgrade_py.B(self.cube)

    def Bp(self):
        moves_upgrade_py.Bp(self.cube)

    def B2(self):
        moves_upgrade_py.B2(self.cube)

    def M(self):
        moves_upgrade_py.M(self.cube)

    def Mp(self):
        moves_upgrade_py.Mp(self.cube)

    def M2(self):
        moves_upgrade_py.M2(self.cube)

    def E(self):
        moves_upgrade_py.E(self.cube)

    def Ep(self):
        moves_upgrade_py.Ep(self.cube)

    def E2(self):
        moves_upgrade_py.E2(self.cube)

    def S(self):
        moves_upgrade_py.S(self.cube)

    def Sp(self):
        moves_upgrade_py.Sp(self.cube)

    def S2(self):
        moves_upgrade_py.S2(self.cube)

    def x(self):
        moves_upgrade_py.x(self.cube)

    def xp(self):
        moves_upgrade_py.xp(self.cube)

    def x2(self):
        moves_upgrade_py.x2(self.cube)

    def y(self):
        moves_upgrade_py.y(self.cube)

    def yp(self):
        moves_upgrade_py.yp(self.cube)

    def y2(self):
        moves_upgrade_py.y2(self.cube)

    def z(self):
        moves_upgrade_py.z(self.cube)

    def zp(self):
        moves_upgrade_py.zp(self.cube)

    def z2(self):
        moves_upgrade_py.z2(self.cube)

    def convert_moves_to_numbers(self):
        return {
            "R": 0,
            "R2": 1,
            "R'": 2,
            "L": 3,
            "L2": 4,
            "L'": 5,
            "U": 6,
            "U2": 7,
            "U'": 8,
            "D": 9,
            "D2": 10,
            "D'": 11,
            "F": 12,
            "F2": 13,
            "F'": 14,
            "B": 15,
            "B2": 16,
            "B'": 17
        }
