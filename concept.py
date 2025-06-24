from cube import Cube
import numpy as np

class BinaryRepresentation:
    def __init__(self, cube: Cube):
        self.cross = self.find_cross_blocks(cube=cube)
        self.color_to_binary = {
            0: 36,
            1: 5,
            2: 20,
            3: 6,
            4: 40,
            5: 9,
            6: 24,
            7: 10,
            8: 34,
            9: 33,
            10: 17,
            11: 18,
        }
    def find_cross_blocks(self, cube: Cube):
        target_values = [4, 5, 6, 7]
        print(cube.edges[:, 0])
        return [np.where(cube.edges == val)[0][0] for val in target_values]

    def conversion(self, numbers):
        return [self.color_to_binary[n] for n in numbers]

    def binary_or_number(self, list_of_biaries):
        result = list_of_biaries[0]
        for val in list_of_biaries[1:]:
            result |= val
        return result

class Cross:
    def __init__(self, cross_slots):
        self.cross_slots = cross_slots

    def combinations(cross_slots):
        iterator = 0
        for i in range(x.bit_length()):

            
            if (x >> i) & 1:
                self.map_moves[i]()  # wywołaj tylko jeśli bit == 1
            for _ in range(3):
                map_move_from_numbers(cube,i)
                for j in range(6):
                    if i == j:
                        continue
                    for _ in range(3):
                        map_move_from_numbers(cube,j)
                        for k in range(6):
                            if is_invalid(k, j, i) or j == k:
                                continue
                            for _ in range(3):
                                map_move_from_numbers(cube,k)
                                for l in range(6):
                                    if is_invalid(l, k, j) or k == l:
                                        continue
                                    for _ in range(3):
                                        map_move_from_numbers(cube,l)
                                        # for m in range(6):
                                        #     if is_invalid(m, l, k) or l == m:
                                        #         continue
                                        #     for _ in range(3):
                                        #         map_move_from_numbers(cube,m)
                                        #         # print(i,j,k,l,m)
                                        iterator += 1
                                    map_move_from_numbers(cube,l)
                            map_move_from_numbers(cube, k)
                    map_move_from_numbers(cube,j)
            map_move_from_numbers(cube,i)

        print(iterator)


    def combinations(self):
        for i in range(6):
            for j in range(3):
                pass





class Moves:
    def __init__(self):
        self.map_moves = {
            0: lambda: self.R(x),
            1: lambda: self.L(x),
            2: lambda: self.U(x),
            3: lambda: self.D(x),
            4: lambda: self.F(x),
            5: lambda: self.B(x)
        }


    def R(x):
        return (
        ((x == 5)   * (x ^ 36)) +  # 5 → 33
        ((x == 33)  * (x ^ 40)) +  # 33 → 9
        ((x == 9)   * (x ^ 24)) +  # 9 → 17
        ((x == 17)  * (x ^ 20))    # 17 → 5
        )

    def Rp(x):
        return (
            ((x == 33) * (x ^ 36)) +  # 33 → 5
            ((x == 9)  * (x ^ 40)) +  # 9  → 33
            ((x == 17) * (x ^ 24)) +  # 17 → 9
            ((x == 5)  * (x ^ 20))    # 5  → 17
        )
    
    def R2(x):
        return (
            ((x == 33) * (x ^ 48)) +  # 33 → 17
            ((x == 17) * (x ^ 48)) +  # 17 → 33
            ((x == 5)  * (x ^ 12)) +  # 5 → 9
            ((x == 9)  * (x ^ 12))    # 9 → 5
        )
    
    def L(x):
        return (
            ((x == 6)  * (x ^ 20)) +  # 6 → 18
            ((x == 18) * (x ^ 24)) +  # 18 → 10
            ((x == 10) * (x ^ 40)) +  # 10 → 34
            ((x == 34) * (x ^ 36))    # 34 → 6
        )

    def Lp(x):
        return (
            ((x == 6)  * (x ^ 36)) +  # 6 ← 34
            ((x == 18) * (x ^ 20)) +  # 18 ← 6
            ((x == 10) * (x ^ 24)) +  # 10 ← 18
            ((x == 34) * (x ^ 40))    # 34 ← 10
        )


    def L2(x):
        return (
            ((x == 6)  * (x ^ 12)) +  # 6 ↔ 10
            ((x == 10) * (x ^ 12)) +  # 10 ↔ 6
            ((x == 18) * (x ^ 48)) +  # 18 ↔ 34
            ((x == 34) * (x ^ 48))    # 34 ↔ 18
        )
    
    def U(x):
        return (
            ((x == 36) * (x ^ 33)) +  # 36 → 5
            ((x == 5)  * (x ^ 17)) +  # 5 → 20
            ((x == 20) * (x ^ 18)) +  # 20 → 6
            ((x == 6)  * (x ^ 34))    # 6 → 36
        )

    def Up(x):
        return (
            ((x == 36) * (x ^ 33)) +  # 36 ← 5
            ((x == 5)  * (x ^ 17)) +  # 5 ← 20
            ((x == 20) * (x ^ 18)) +  # 20 ← 6
            ((x == 6)  * (x ^ 34))    # 6 ← 36
        )

    def U2(x):
        return (
            ((x == 36) * (x ^ 48)) +  # 36 ↔ 20
            ((x == 20) * (x ^ 48)) +  # 20 ↔ 36
            ((x == 5)  * (x ^ 3))  +  # 5 ↔ 6
            ((x == 6)  * (x ^ 3))     # 6 ↔ 5
        )

    def D(x):
        return (
            ((x == 40) * (x ^ 34)) +  # 40 → 10
            ((x == 10) * (x ^ 18)) +  # 10 → 24
            ((x == 24) * (x ^ 17)) +  # 24 → 9
            ((x == 9)  * (x ^ 33))    # 9 → 40
        )
    
    def Dp(x):
        return (
            ((x == 40) * (x ^ 33)) +  # 40 ← 9
            ((x == 10) * (x ^ 34)) +  # 10 ← 40
            ((x == 24) * (x ^ 18)) +  # 24 ← 10
            ((x == 9)  * (x ^ 17))    # 9 ← 24
        )

    def D2(x):
        return (
            ((x == 40) * (x ^ 48)) +  # 40 ↔ 24
            ((x == 24) * (x ^ 48)) +  # 24 ↔ 40
            ((x == 10) * (x ^ 3))  +  # 10 ↔ 9
            ((x == 9)  * (x ^ 3))     # 9 ↔ 10
        )
    
    def F(x):
        return (
            ((x == 20) * (x ^ 5)) +   # 20 → 17
            ((x == 17) * (x ^ 9)) +   # 17 → 24
            ((x == 24) * (x ^ 10)) +  # 24 → 18
            ((x == 18) * (x ^ 6))     # 18 → 20
        )
    def Fp(x):
        return (
            ((x == 20) * (x ^ 6)) +    # 20 ← 18
            ((x == 17) * (x ^ 5)) +    # 17 ← 20
            ((x == 24) * (x ^ 9)) +    # 24 ← 17
            ((x == 18) * (x ^ 10))     # 18 ← 24
        )

    def F2(x):
        return (
            ((x == 20) * (x ^ 12)) +  # 20 ↔ 24
            ((x == 24) * (x ^ 12)) +  # 24 ↔ 20
            ((x == 17) * (x ^ 3)) +   # 17 ↔ 18
            ((x == 18) * (x ^ 3))     # 18 ↔ 17
        )
    def B(x):
        return (
            ((x == 36) * (x ^ 2)) +   # 36 → 34
            ((x == 34) * (x ^ 3)) +   # 34 → 33
            ((x == 33) * (x ^ 9)) +   # 33 → 40
            ((x == 40) * (x ^ 12))    # 40 → 36
        )
    def Bp(x):
        return (
            ((x == 36) * (x ^ 12)) +  # 36 ← 40
            ((x == 34) * (x ^ 2)) +   # 34 ← 36
            ((x == 33) * (x ^ 3)) +   # 33 ← 34
            ((x == 40) * (x ^ 9))     # 40 ← 33
        )
    def B2(x):
        return (
            ((x == 36) * (x ^ 12)) +  # 36 ↔ 24
            ((x == 24) * (x ^ 12)) +  # 24 ↔ 36
            ((x == 34) * (x ^ 3))  +  # 34 ↔ 33
            ((x == 33) * (x ^ 3))     # 33 ↔ 34
        )




    


if __name__ == "__main__":
    # cube = Cube("L2 B2 L2 U' B2 L2 U' R2 D' L2 U B2 R B' D F L F2 D F2")
    # b = BinaryRepresentation(cube)
    # print(b.cross)
    # conversion = b.conversion(b.cross)
    # print(bin(b.binary_or_number(conversion)))

    moves = Moves()
    x = 36
    print(bin(x))
    x = moves.U(x)
    print(bin(x))