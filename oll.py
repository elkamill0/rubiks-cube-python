from tools import inverse, reduce
import json
from copy import deepcopy


class OLL():
    def __init__(self, cube, path="cases/oll_cases.json"):
        self.cube = deepcopy(cube)
        self.solved_cube = deepcopy(cube)
        self.solved_cube.reset()
        self.path = path


    def prepare_algs(self, path="algs/oll.json"):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        records = []        

        for i, case in enumerate(data):
            cube = deepcopy(self.solved_cube)
            cube.move(inverse(case))

            record = {
                "edges": [int(e[1]) for e in cube.edges[0:4]],
                "corners": [int(c[1]) for c in cube.corners[0:4]],
                "algorithm": case
            }
            records.append(record)

        with open(self.path, "w", encoding="utf-8") as f:
            f.write("[\n")
            for i, record in enumerate(records):
                line = json.dumps(record, ensure_ascii=False)
                if i < len(records) - 1:
                    line += ","
                f.write("\t" + line + "\n")
            f.write("]\n")

        print(f"Zapisano {len(records)} przypadków OLL do pliku: {self.path}")


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
            edges = tuple(int(e[1]) for e in cube.edges[0:4])
            corners = tuple(int(c[1]) for c in cube.corners[0:4])
            if (edges, corners) in self.cases:
                new_notation += self.cases.get((edges, corners))
                return reduce(new_notation)
            new_notation += "U "
            cube.U()
        return None
    
    def is_solved(self):
        for e in self.cube.edges[:4]:
            print(e)




if __name__ == "__main__":
    from cube import Cube
    oll = OLL(Cube()).prepare_algs()