import json
from copy import deepcopy

import numpy as np

from src.tools import inverse, reduce


class OLL:
    def __init__(self, cube, path="data/cases/oll_cases.json"):
        self.cube = deepcopy(cube)
        self.solved_cube = deepcopy(cube)
        self.solved_cube.reset()
        self.path = path

    def prepare_algs(self, path="algs/oll.json") -> None:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        records = []

        for i, case in enumerate(data):
            cube = deepcopy(self.solved_cube)
            cube.move(inverse(case["alg"]))

            record = {
                "name": case["name"],
                "edges": [int(e[1]) for e in cube.edges[0:4]],
                "corners": [int(c[1]) for c in cube.corners[0:4]],
                "alg": case["alg"],
            }
            records.append(record)
            print(case["name"])
            print(record["edges"], record["corners"])
            print(cube, "\n---------------------------------------------\n")

            if np.any(cube.edges[:4, 0] > 3) or np.any(cube.corners[:4, 0] > 3):
                raise ValueError(
                    f"Error with preparing on {case['name']},\n {cube.edges[:4]}"
                )

        with open(self.path, "w", encoding="utf-8") as f:
            f.write("[\n")
            for i, record in enumerate(records):
                line = json.dumps(record, ensure_ascii=False)
                if i < len(records) - 1:
                    line += ","
                f.write("\t" + line + "\n")
            f.write("]\n")

        print(f"Zapisano {len(records)} przypadków OLL do pliku: {self.path}")

    def solve(self) -> tuple[str, str]:
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.cases = {
            (tuple(item["edges"]), tuple(item["corners"])): (item["alg"], item["name"])
            for item in data
        }

        new_notation = ""
        cube = deepcopy(self.cube)

        for _ in range(4):
            edges = tuple(int(e[1]) for e in cube.edges[0:4])
            corners = tuple(int(c[1]) for c in cube.corners[0:4])

            if (edges, corners) in self.cases:
                alg, name = self.cases[(edges, corners)]
                new_notation += alg
                return reduce(new_notation), name

            new_notation += "U "
            cube.U()

        return "", ""

    def is_solved(self):
        edges_ok = all(e[1] == 0 for e in self.cube.edges[0:4])
        corners_ok = all(c[1] == 0 for c in self.cube.corners[0:4])
        return edges_ok and corners_ok


if __name__ == "__main__":
    from src.cube import Cube

    oll = OLL(Cube()).prepare_algs()
