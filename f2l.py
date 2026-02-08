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
        self.e = [
            [10,11,8,9], 
            [9,10,11,8],
            [8,9,10,11],
            [11,8,9,10]
        ]
        self.c = [
            [6,7,4,5],
            [5,6,7,4],
            [4,5,6,7],
            [7,4,5,6]
        ]
        self.rotate_edges = False
        self.cube = deepcopy(cube)
        self.solved_cube = deepcopy(cube)
        self.solved_cube.reset()
        self.edges = edges_to_binary(self.cube, self.e[self.cube.y_rotate]) 
        self.corners = corners_to_binary(self.cube, self.c[self.cube.y_rotate])
        self.free_slots = self.check_free_slots()
        
        self.pairs = [
            # load_f2l_from_json("cases/new_f2l1_cases.json"), # | load_f2l_from_json("cases/af2l1_cases.json"),
            # load_f2l_from_json("cases/new_f2l2_cases.json"), # | load_f2l_from_json("cases/af2l2_cases.json"),
            # load_f2l_from_json("cases/new_f2l3_cases.json"), # | load_f2l_from_json("cases/af2l3_cases.json"),
            # load_f2l_from_json("cases/new_f2l4_cases.json"), # | load_f2l_from_json("cases/af2l4_cases.json")
            load_f2l_from_json("test/f2l1_prepared.json") | load_f2l_from_json("test/af2l1_prepared.json"),
            load_f2l_from_json("test/f2l2_prepared.json") | load_f2l_from_json("test/af2l2_prepared.json"),
            load_f2l_from_json("test/f2l3_prepared.json") | load_f2l_from_json("test/af2l3_prepared.json"),
            load_f2l_from_json("test/f2l4_prepared.json") | load_f2l_from_json("test/af2l4_prepared.json")
        ]

    def prepare_algs(self, prepare_pairs = False) -> None:
        files = [
            ("algs/new_f2l1.json",  "test/f2l1_prepared.json",  0),
            ("algs/new_af2l1.json", "test/af2l1_prepared.json", 0),
            ("algs/new_f2l2.json",  "test/f2l2_prepared.json",  1),
            ("algs/new_af2l2.json", "test/af2l2_prepared.json", 1),
            ("algs/new_f2l3.json",  "test/f2l3_prepared.json",  2),
            ("algs/new_af2l3.json", "test/af2l3_prepared.json", 2),
            ("algs/new_f2l4.json",  "test/f2l4_prepared.json",  3),
            ("algs/new_af2l4.json", "test/af2l4_prepared.json", 3)
        ]

        for input_path, output_path, slot in files:
            with open(input_path, 'r', encoding="utf-8") as f:
                in_data = json.load(f)

            with open(output_path, 'r', encoding="utf-8") as f:
                out_data = json.load(f)

            
            records = []

            for in_case, out_case in zip(in_data, out_data):
                if not in_case:
                    continue
                alg = in_case["alg"]
                name = in_case["name"]
                pair = out_case["pair"]
                cube = deepcopy(self.solved_cube)
                cube.move(inverse(alg))
                edges = edges_to_binary(cube, self.e[self.cube.y_rotate]) 
                corners = corners_to_binary(cube, self.c[self.cube.y_rotate])

                if prepare_pairs:                    
                    record = {
                        "name": f"{name}",
                        "pair": [corners[slot], edges[slot]],
                        "alg": alg
                    }
                else:
                    record = {
                        "name": f"{name}",
                        "pair": pair,
                        "alg": alg
                    }                    
                records.append(record)


            PAIR_COL = 22
            ALG_COL = 46

            with open(output_path, "w", encoding="utf-8") as f:
                f.write("[\n")

                for i, record in enumerate(records):
                    name = f'"name": {json.dumps(record["name"], ensure_ascii=False)},'
                    pair = f'"pair": {json.dumps(record["pair"], ensure_ascii=False)},'
                    alg  = f'"alg": {json.dumps(record["alg"],  ensure_ascii=False)}'

                    line = "\t{"
                    line += name

                    line += " " * max(1, PAIR_COL - len(line))
                    line += pair

                    line += " " * max(1, ALG_COL - len(line))
                    line += alg

                    line += "}"

                    if i < len(records) - 1:
                        line += ","

                    f.write(line + "\n")

                f.write("]\n")



    def check_free_slots(self) -> List[int]:
        edges = edges_to_binary(self.solved_cube, self.e[self.cube.y_rotate]) 
        corners = corners_to_binary(self.solved_cube, self.c[self.cube.y_rotate])

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
                key = (self.cube.corners[slot], self.cube.edges[slot] ^ (64 * (self.cube.y_rotate % 2)))
                if key in self.pairs[slot]:
                    prev_y_rotate = self.cube.y_rotate
                    alg = self.pairs[slot][key]
                    new_notation += alg
                    reduced = reduce(new_notation)
                    final.append(reduced)
                    new_notation = ""
                    if verbose:
                        print(reduced, f" # Slot {slot}")
                    self.cube.move(alg)
                    self.edges = edges_to_binary(self.cube, self.e[self.cube.y_rotate])
                    self.corners = corners_to_binary(self.cube, self.c[self.cube.y_rotate])
                    self.free_slots.remove(slot)
                    delta = (self.cube.y_rotate - prev_y_rotate) % 4
                    if delta:
                        self.free_slots = [(slot + delta) % 4 for slot in self.free_slots]
                        
                    i = 0
                    break
            else:
                self.cube.U()
                new_notation+="U "
                self.edges = edges_to_binary(self.cube, self.e[self.cube.y_rotate])
                self.corners = corners_to_binary(self.cube, self.c[self.cube.y_rotate])
                i += 1
        return final


    def find_pairs(self) -> list[str]:
        i = 0
        final = []
        u_notation = ""

        while i <= 4 and self.free_slots:
            for slot in self.free_slots:
                key = (self.corners[slot], self.edges[slot] ^ (64 * (self.cube.y_rotate % 2)))
                if key in self.pairs[slot]:
                    # prev_y_rotate = self.cube.y_rotate
                    # print(key)
                    alg = self.pairs[slot][key]
                    reduced = reduce(u_notation + alg)
                    final.append(reduced)
                    self.free_slots.remove(slot)
                    # delta = (self.cube.y_rotate - prev_y_rotate) % 4
                    # if delta:
                    #     self.free_slots = [(slot + delta) % 4 for slot in self.free_slots]
                    # break
            else:
                self.cube.U()
                u_notation+="U "
                self.edges = edges_to_binary(self.cube, self.e[self.cube.y_rotate])
                self.corners = corners_to_binary(self.cube, self.c[self.cube.y_rotate])
                i += 1
        return final
    
    def solve_slot(self, slot_number: int) -> None:
        for u in ["", "U ", "U2 ", "U' "]:
            key = (self.corners[slot_number], self.edges[slot_number] ^ (64 * (self.cube.y_rotate % 2)))
            if key in self.pairs[slot_number]:
                prev_y_rotate = self.cube.y_rotate
                alg = self.pairs[slot_number][key]
                delta = (self.cube.y_rotate - prev_y_rotate) % 4
                if delta:
                    self.free_slots = [(slot + delta) % 4 for slot in self.free_slots]
                return reduce(u + alg)
            else:
                self.cube.U()
                self.edges = edges_to_binary(self.cube, self.e[self.cube.y_rotate])
                self.corners = corners_to_binary(self.cube, self.c[self.cube.y_rotate])
        return None



if __name__ == "__main__":
    from cube import Cube

    F2L = F2L(Cube()).prepare_algs()

    # import json

    # input_path = "test/f2l4_prepared.json"
    # output_path = "test/f2l4_pair.json"

    # with open(input_path, "r", encoding="utf-8") as f:
    #     data = json.load(f)

    # with open(output_path, "w", encoding="utf-8") as f:
    #     f.write("[\n")  # początek tablicy

    #     for i, item in enumerate(data):
    #         out = {"name": item["name"], "pair": item["pair"]}
    #         line = "\t" + json.dumps(out, ensure_ascii=False)
    #         if i < len(data) - 1:  # przecinek tylko jeśli to nie ostatni
    #             line += ","
    #         f.write(line + "\n")

    #     f.write("]\n")  # koniec tablicy





    # state = "144304304520113211220024422303331332514240540055555151"
    # state = "305203242215110113300222024102334534110344044453555551"
    # state = "404304022524314510100123323105032033113144542254555152"
    # state = "542400105114211014544023023330232534132140342152555350"
    # cube = Cube(state=state)
    # f2l = F2L(cube)
    # print(f2l.solve(verbose=True))