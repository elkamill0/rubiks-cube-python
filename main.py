from cube import Cube

### CROSS LIST
a = Cube("F2 U D2 L2 R2 B' D2 L2 F' D2 R2 U2 F L' U R' D R2 B' U'")
crosses = a.find_cross(6)
print(crosses)
a.sequence(crosses[0])
a.print_cube()


### MOVING
b = Cube()
b.R()
b.U()
b.x()
b.print_cube()

