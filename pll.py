from copy import deepcopy
import json
from tools import inverse, reduce

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
                notation = case+j
                cube = deepcopy(self.solved_cube)
                cube.move(inverse(notation))

                records.append({
                    "edges": [int(e[0]) for e in cube.edges[0:4]],
                    "corners": [int(c[0]) for c in cube.corners[0:4]],
                    "algorithm": notation
                })

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
            (tuple(item["edges"]), tuple(item["corners"])): item["algorithm"]
            for item in data
        }

        new_notation = ""
        cube = deepcopy(self.cube)
        for _ in range(4):
            edges = tuple(int(e[0]) for e in cube.edges[0:4])
            corners = tuple(int(c[0]) for c in cube.corners[0:4])
            
            if (edges, corners) in self.cases:
                new_notation += self.cases.get((edges, corners))
                return reduce(new_notation)
            new_notation += "U "
            cube.U()
        return None
    



if __name__ == "__main__":
    from cube import Cube
    pll = PLL(Cube()).prepare_algs()

