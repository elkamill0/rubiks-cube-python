import json
import numpy as np
from convert import edges_to_binary, corners_to_binary
from typing import List
from tools import inverse, reduce
from copy import deepcopy

def load_f2l_from_json(path: str):
    """
    Wczytuje przypadki F2L z pliku JSON.

    Każdy rekord w plik powinien zawierać:
    - "pair": opis pary narożnik-krawędź w postaci binarnej,
    - "alg": algorytm rozwiązujący dany przypadek.

    Args:  
        path (str): Ścieżka do pliku JSON z przypadkami F2L.

    Returns:
        dict[tuple, str]: Słownik ma
    """
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {tuple(item["pair"]): item["alg"] for item in data}


class F2L:
    def __init__(self, cube):
        self.cube = deepcopy(cube)
        self.solved_cube = deepcopy(cube)
        self.solved_cube.reset()
        self.edges = edges_to_binary(self.cube, [10,11,8,9]) 
        self.corners = corners_to_binary(self.cube, [6,7,4,5])
        self.free_slots = self.check_free_slots()
        
        self.pairs = [
            load_f2l_from_json("cases/f2l1_cases.json") | load_f2l_from_json("cases/af2l1_cases.json"),
            load_f2l_from_json("cases/f2l2_cases.json") | load_f2l_from_json("cases/af2l2_cases.json"),
            load_f2l_from_json("cases/f2l3_cases.json") | load_f2l_from_json("cases/af2l3_cases.json"),
            load_f2l_from_json("cases/f2l4_cases.json") | load_f2l_from_json("cases/af2l4_cases.json")
        ]

    def prepare_algs(self) -> None:
        files = [
            ("algs/f2l1.json",  "test/f2l1_prepared.json", "f2l1", 0),
            ("algs/af2l1.json", "test/af2l1_prepared.json", "af2l1", 0),
            ("algs/f2l2.json",  "test/f2l2_prepared.json", "f2l2", 1),
            ("algs/af2l2.json", "test/af2l2_prepared.json", "af2l2", 1),
            ("algs/f2l3.json",  "test/f2l3_prepared.json", "f2l3", 2),
            ("algs/af2l3.json", "test/af2l3_prepared.json", "af2l3", 2),
            ("algs/f2l4.json",  "test/f2l4_prepared.json", "f2l4", 3),
            ("algs/af2l4.json", "test/af2l4_prepared.json", "af2l4", 3)
        ]

        for input_path, output_path, name, slot in files:
            with open(input_path, 'r', encoding="utf-8") as f:
                data = json.load(f)
            
            records = []

            for i, case in enumerate(data):
                if not case:
                    continue
                cube = deepcopy(self.solved_cube)
                cube.move(inverse(case))
                edges = edges_to_binary(cube, [10,11,8,9]) 
                corners = corners_to_binary(cube, [6,7,4,5])
                record = {
                    "name": f"{name}_{i+1}",
                    "pair": [corners[slot], edges[slot]],
                    "alg": case
                }
                records.append(record)

            with open(output_path, "w", encoding="utf-8") as f:
                f.write("[\n")
                for i, record in enumerate(records):
                    line = json.dumps(record, ensure_ascii=False)
                    if i < len(records) - 1:
                        line += ","
                    f.write("\t" + line + "\n")
                f.write("]\n")

            print(f"Zapisano {len(records)} przypadków do pliku: {output_path}")

    def check_free_slots(self) -> List[int]:
        edges = edges_to_binary(self.solved_cube, [10,11,8,9]) 
        corners = corners_to_binary(self.solved_cube, [6,7,4,5])

        solved_pairs = list(zip(edges, corners))
        pairs = list(zip(self.edges, self.corners))

        differences = []

        for i, (solved, current) in enumerate(zip(solved_pairs, pairs)):
            if solved != current:
                differences.append(i)

        return differences


    def solve(self, verbose:bool = False) -> list[str]:
        i = 0
        new_notation = ""
    
        final = []

        while i <= 4 and self.free_slots:
            for slot in self.free_slots:
                key = (self.corners[slot], self.edges[slot])
                if key in self.pairs[slot]:
                    alg = self.pairs[slot][key]
                    new_notation += alg
                    reduced = reduce(new_notation)
                    final.append(reduced)
                    new_notation = ""
                    if verbose:
                        print(reduced, f" # Slot {slot}")
                    self.cube.move(alg)
                    self.edges = edges_to_binary(self.cube, [10, 11, 8, 9])
                    self.corners = corners_to_binary(self.cube, [6, 7, 4, 5])
                    self.free_slots.remove(slot)
                    i = 0
                    break
            else:
                self.cube.U()
                new_notation+="U "
                self.edges = edges_to_binary(self.cube, [10, 11, 8, 9])
                self.corners = corners_to_binary(self.cube, [6, 7, 4, 5])
                i += 1
        return final


    def find_pairs(self) -> list[str]:
        i = 0
        final = []
        u_notation = ""

        while i <= 4 and self.free_slots:
            for slot in self.free_slots:
                key = (self.corners[slot], self.edges[slot])
                if key in self.pairs[slot]:
                    alg = self.pairs[slot][key]
                    reduced = reduce(u_notation + alg)
                    final.append(reduced)
                    self.free_slots.remove(slot)
                    break
            else:
                self.cube.U()
                u_notation+="U "
                self.edges = edges_to_binary(self.cube, [10, 11, 8, 9])
                self.corners = corners_to_binary(self.cube, [6, 7, 4, 5])
                i += 1
        return final
    
    def solve_slot(self, slot_number: int) -> None:
        for u in ["", "U ", "U2 ", "U' "]:
            key = (self.corners[slot_number], self.edges[slot_number])
            if key in self.pairs[slot_number]:
                alg = self.pairs[slot_number][key]
                return reduce(u + alg)
            else:
                self.cube.U()
                self.edges = edges_to_binary(self.cube, [10, 11, 8, 9])
                self.corners = corners_to_binary(self.cube, [6, 7, 4, 5])
        return None



if __name__ == "__main__":
    from cube import Cube

    F2L = F2L(Cube()).prepare_algs()

    # state = "144304304520113211220024422303331332514240540055555151"
    # state = "305203242215110113300222024102334534110344044453555551"
    # state = "404304022524314510100123323105032033113144542254555152"
    # state = "542400105114211014544023023330232534132140342152555350"
    # cube = Cube(state=state)
    # f2l = F2L(cube)
    # print(f2l.solve(verbose=True))