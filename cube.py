import numpy as np
from moves.moves import Moves
from pll import PLL
import scramble
import convert
import visualization
from cross import Cross
from f2l import F2L
from oll import OLL
from solving_stage import Solving
from pprint import pprint



class Cube(Moves):
    """
    Reprezentuje stan kostki Rubika oraz operacje wykonywane na niej.

    Klasa przechowuje strukture kostki. Jest to zbiór rogów, krawędzi i centrów 
    oraz umozliwia wykonywanie ruchów na kostce.
    """
    def __init__(self, notation: str = None, state: str = None):
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
        self.reset()
        if notation: 
            convert.notation_to_moves(moves=notation, cube=self)
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
        return convert.replace_numbers_with_colors(convert.cube_to_color(self, show=True))

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
        self.centers = np.arange(6, dtype=np.uint8)


if __name__ == "__main__":
    # print(scramble.generate_scramble(10))
    # notation="B' U L' B2 R F2 L' R2 B2 U2 R2 D2 F2 D' B' U L2 B' D F"
    state = "305203242215110113300222024102334534110344044453555551"
    # notation="F' R2 F' U2 F R2 F' U2 R2 F U2 R U F L2 B D' B' R"
    # notation="F' B2 L F2 L D2 L2 U2 R D2 B2 L D' B2 F L' B L2 D U'"
    # notation = "R U R' L D2 F' B U' R2 L' F2 D' B2 U2 L2 D B' F"
    # notation = "U2 R' F D B2 L U' R2 F' D' L2 B U L' D2 R F2 B' U'"
    # notation = "L "#D2 B' R U2 F' L' B2 U R' D F2 L2 U' B R2 F D' U B'"

    # notation = "U2 D L2 B F2 R2 F B' D F' B' R' B F' U' R2 U2 B L D' R'"
    # notation = "B L B2 U' L' B L' R2 D' L B F2 L' B2 L U2 L F' U' R2 D2"
    # notation = "U' L F2 D' R2 D B L B R B D2 U' L B' D L' R' B' F' L2"


    # cube = Cube(notation = notation)

    notation = "B L B2 U' L' B L' R2 D' L B F2 L' B2 L U2 L F' U' R2 D2"

    # cube = Cube(state = state)


    cube = Cube(notation=notation)
    cube.get_state()
    print(cube)
    print(cube.corners)

    # print(cube.get_state())

    # L B R B' L U R2 D2 B2 F D2 L B2 R2 B D2 F B U' L' F2
