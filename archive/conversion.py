notation_map = {
    0: "R", 1: "R2", 2: "R'",
    3: "L", 4: "L2", 5: "L'",
    6: "U", 7: "U2", 8: "U'",
    9: "D", 10: "D2", 11: "D'",
    12: "F", 13: "F2", 14: "F'",
    15: "B", 16: "B2", 17: "B'"
}

def convert_and_reverse(input_string):
    # Podziel dane wejściowe na bloki oddzielone liniami '----------'
    blocks = input_string.strip().split("----------")

    results = []

    for block in blocks:
        block = block.strip()
        if not block:
            continue  # pomiń puste linie

        # Zamień string na listę liczb
        numbers = list(map(int, block.split()))
        # Odwróć kolejność
        reversed_numbers = numbers[::-1]
        # Zamień na notację ruchów
        moves = [notation_map[num] for num in reversed_numbers]

        # Zbuduj linię: oryginalne liczby -> ruchy
        line = f"{' '.join(map(str, numbers))} -> {' '.join(moves)}"
        results.append(line)

    return "\n----------\n".join(results)


# Przykład użycia – wklej swoje dane jako wieloliniowy string:
input_string = """
17 10 0 5 17 6 16
----------
17 10 5 0 17 6 16
----------
9 17 0 9 5 7 15
----------
9 1 15 2 9 5 15
----------
9 2 15 1 9 5 15
----------
9 15 0 9 5 15
----------
9 1 15 9 2 5 15
----------
9 15 1 9 2 5 15
----------
9 2 15 9 1 5 15
----------
9 15 2 9 1 5 15
----------
17 9 15 9 0 5 15
----------
9 1 15 9 5 2 15
----------
9 15 1 9 5 2 15
----------
9 2 15 9 5 1 15
----------
9 15 2 9 5 1 15
----------
17 9 15 9 5 0 15
----------
9 0 15 9 5 15 11
----------
3 10 14 5 8 15 9
----------
9 15 9 14 5 15 9
----------
2 15 3 14 9 4 8
----------
15 2 3 14 9 4 8
----------
15 3 2 14 9 4 8
----------
14 15 3 9 14 3 8
----------
15 14 3 9 14 3 8
----------
0 5 17 2 14 11 4
----------
5 0 17 2 14 11 4
----------
0 5 14 17 2 11 4
----------
5 0 14 17 2 11 4
----------
5 14 0 17 2 11 4
----------
0 5 17 14 2 11 4
----------
5 0 17 14 2 11 4
"""
input_string = """9 15 0 9 5 15
----------"""

result = convert_and_reverse(input_string)
print(result)
