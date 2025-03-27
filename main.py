from cube import Cube
import time


### CROSS LIST
# a = Cube("F2 U D2 L2 R2 B' D2 L2 F' D2 R2 U2 F L' U R' D R2 B' U'")
# a = Cube("F U2 B2 R2 D2 F2 U2 B' U2 L2 D L' D' R F' R2 B2 D' L'")
a = Cube("F' U2 L2 U2 R' F L F2 R2 L2 U R2 L2 U' F2 D' B2 U' L'")
# start = time.time()
crosses = a.find_cross(6)
# print(time.time() - start)
print(crosses)
a.sequence(crosses[0])
a.print_cube()


### MOVING
b = Cube()
b.R()
b.U()
b.x()
b.print_cube()
