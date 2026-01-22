import cube_solver
from convert import int_to_notation


start_state = [20, 74, 100, 40]
final_state = [40, 9, 24, 10]

solutions = cube_solver.combinations(8, start_state, final_state)
for sol in solutions:
    print([int_to_notation[x] for x in sol])

