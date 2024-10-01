from cube import Cube

### CROSS LIST
a = Cube("F2 U D2 L2 R2 B' D2 L2 F' D2 R2 U2 F L' U R' D R2 B' U'")
# a = Cube()
a.print_cube()
a.x()
crosses = a.find_cross(6)
print(crosses)