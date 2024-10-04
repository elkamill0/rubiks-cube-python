from cube import Cube

### CROSS LIST
a = Cube("R2 F' L2 B2 D' R2 F2 D' L2 U2 F2 L2 D B L2 R D R U L D2")
a.xp()
a.print_cube()
crosses = a.find_cross(6)
print(crosses[0])
