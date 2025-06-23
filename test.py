import mymodule
import numpy as np

arr = np.array([1.0, 2.0, 3.0], dtype=np.float64)
result = mymodule.double_array(arr)

print("Original:", arr)
print("Doubled: ", result)


import cross_c

from cube import Cube

cube = Cube("L2 D2 F2 L2 F L2 D2 L2 D2 B D F2 L F D R U F L2 D")

cross_c.inspect_cube(cube)


