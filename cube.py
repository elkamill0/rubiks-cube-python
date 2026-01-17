import numpy as np
from moves.moves import Moves
from pll import PLL
from scramble import remap_scramble_by_color
import convert
import visualization
from cross import Cross
from f2l import F2L
from oll import OLL
from solving_stage import Solving
from pprint import pprint
from tools import inverse



class Cube(Moves):
    """
    Reprezentuje stan kostki Rubika oraz operacje wykonywane na niej.

    Klasa przechowuje strukture kostki. Jest to zbiór rogów, krawędzi i centrów 
    oraz umozliwia wykonywanie ruchów na kostce.
    """
    def __init__(self, color="y", notation: str = None, state: str = None):
        """
        Inicjalizuje kostkę Rubika

        Kostka może zostać:
        - zainicjowana w stanie ułożonym (domyślnie)
        - przemieszana za pomocą notacji ruchów
        - odtworzona z zapisanego stanu

        Args:
            notation (str, optional): Sekwencja ruchów w notacji
            state (str, optional): Rozłożenie kostki według stanu (liczb od 0-5 
            symbolizujące kolory
            0-biały
            1-pomarańczowy
            2-zielony
            3-czerwony
            4-niebieski
            5-żółty)
        """
        self.color = color
        self.reset()
        if notation: 
            convert.notation_to_moves(moves=remap_scramble_by_color(notation, color=self.color), cube=self)
        elif state:
            self.corners, self.edges, self.centers = convert.state_to_cube(state=state)

    def move(self, notation: str) -> None:
        """
        Wykojnuje sekwecję ruchów na kostce.

        Args:
            notation (str): Sekwecja ruchów notacja.
        """
        convert.notation_to_moves(notation, self)

    def __str__(self):
        """
        Zwraca aktualny stan kostki rubika w formie kolorów.

        Returns:
            str: Tekstowa reprezentacja kostki Rubika w formie kolorów.
        """
        return convert.replace_numbers_with_colors(convert.cube_to_color(self, cross_color=self.color, show=True))

    def get_state(self)->str:
        """
        Zwraca aktualny stan kostki rubika w postaci notacji od 0-5 symbolizującą kolory.

        Returns:
            str: Tekstowa reprezentacja stanu kostki.

        """
        return convert.cube_to_color(self, show=False)

    def reset(self) -> None:
        """
        Resetuje kostkę do stanu ułożonego.

        Inicjalizuje:
        - narożniki, 
        - krawędzie,
        - środki kostki
        """
        
        self.corners = np.zeros((8, 2), dtype=np.int8)
        self.corners[:, 0] = np.arange(8)
        self.edges = np.zeros((12, 2), dtype=np.int8)
        self.edges[:, 0] = np.arange(12)
        self.centers = np.zeros(6, dtype=np.uint8)
        colors = {
            "y": [0, 1, 2, 3, 4, 5],
            "w": [5, 3, 2, 1, 4, 0],
            "r": [1, 5, 2, 0, 4, 3],
            "o": [3, 0, 2, 5, 4, 1],
            "g": [4, 1, 0, 3, 5, 2],
            "b": [2, 1, 5, 3, 0, 4]
        }
        self.centers[:] = colors[self.color]


if __name__ == "__main__":
    state = "305203242215110113300222024102334534110344044453555551"

    notation = "B L B2 U' L' B L' R2 D' L B F2 L' B2 L U2 L F' U' R2 D2"

    color = "y"
    print(notation)
    cube = Cube(notation=inverse(notation), color=color)


    # cross = Cross(cube).find_cross(6)
    # print(cross[0])
    # cube.move(cross[0])
    # f2l = F2L(cube).solve(verbose=True)
    # cube.move(f2l[0])
    # cube.move(f2l[1])
    # cube.move(f2l[2])
    # cube.move(f2l[3])
    # oll = OLL(cube).solve()
    # print(oll)
    # cube.move(oll)
    # pll = PLL(cube).solve()
    # print(pll)
    # cube.move(pll)
    # print(cube)


    # L B R B' L U R2 D2 B2 F D2 L B2 R2 B D2 F B U' L' F2
