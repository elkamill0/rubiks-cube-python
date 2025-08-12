# from cube import Cube
import time


### CROSS LIST
# a = Cube("F2 U D2 L2 R2 B' D2 L2 F' D2 R2 U2 F L' U R' D R2 B' U'")
# a = Cube("F U2 B2 R2 D2 F2 U2 B' U2 L2 D L' D' R F' R2 B2 D' L'")
# state = "000000000111111111222222222333333333444444444555555550" 
# a = Cube(state=state)
# print(a)
# start = time.time()
# crosses = a.find_cross(6)
# print(time.time() - start)
# print(crosses)
# a.sequence(crosses[0])
# a.print_cube()


### MOVING
# b = Cube()
# b.R()
# b.U()
# b.x()
# b.print_cube()

import numpy as np

corners = np.zeros((8, 2), dtype=np.uint8)
corners[:, 0] = np.arange(8, dtype=np.uint8)
corners[:, 1] = 0

edges = np.zeros((12, 2), dtype=np.uint16)
edges[:, 0] = np.arange(12, dtype=np.uint16)
edges[:, 1] = 0

centers = np.arange(6, dtype=np.uint8)

print(corners)

corners[[0,3]] = corners[[3,0]]

print(corners)