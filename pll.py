from copy import deepcopy
import json
from tools import inverse, reduce
import numpy as np

class PLL:
    def __init__(self, cube, path="cases/pll_cases.json"):
        self.cube = cube
        self.solved_cube = deepcopy(cube)
        self.solved_cube.reset()
        self.path = path

    def prepare_algs(self, path="algs/pll.json"):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        records = []

        for i, case in enumerate(data):
            for j in ["", " U", " U2", " U'"]:
                notation = case['alg']+" "+j
                cube = deepcopy(self.solved_cube)
                cube.move(inverse(notation))

                records.append({
                    "name": case['name'],
                    "edges": [int(e[0]) for e in cube.edges[0:4]],
                    "corners": [int(c[0]) for c in cube.corners[0:4]],
                    "alg": notation
                })
                if np.any(cube.edges[:4, 0] > 3) or np.any(cube.corners[:4, 0] > 3):
                    raise ValueError(f'Error with preparing on {case["name"]},\n {cube.edges[:4]}')

        with open(self.path, "w", encoding="utf-8") as f:
            f.write("[\n")
            for i, record in enumerate(records):
                line = json.dumps(record, ensure_ascii=False)
                if i < len(records) - 1:
                    line += ","
                f.write("\t" + line + "\n")
            f.write("]\n")

        

        print(f"Zapisano {len(records)} przypadków do {self.path}")

    
    def solve(self) -> str:
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        self.cases = {
            (tuple(item["edges"]), tuple(item["corners"])): (item["alg"], item["name"])
            for item in data
        }

        new_notation = ""
        cube = deepcopy(self.cube)
        for _ in range(4):
            edges = tuple(int(e[0]) for e in cube.edges[0:4])
            corners = tuple(int(c[0]) for c in cube.corners[0:4])
            
            if (edges, corners) in self.cases:
                alg, name = self.cases[(edges, corners)]
                new_notation += alg
                return reduce(new_notation), name
            new_notation += "U "
            cube.U()
        return "", ""

    def is_solved(self) -> bool:

        edges_ok = (np.array(self.cube.edges[0:4]) == np.array([[0,0],[1,0],[2,0],[3,0]])).all()
        corners_ok = (np.array(self.cube.corners[0:4]) == np.array([[0,0],[1,0],[2,0],[3,0]])).all()

        return edges_ok and corners_ok





if __name__ == "__main__":
    from cube import Cube
    pll = PLL(Cube()).prepare_algs()

