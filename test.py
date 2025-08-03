import cube_solver
from time import time

# print(cube_solver.__file__)

start = [104, 100, 98, 70]
end = [40, 9, 24, 10]
depth = 8
startt = time()
cube_solver.combinations(depth, start, end)
endt = time()
print(endt-startt)
