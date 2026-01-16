import convert
import cube_solver
from typing import List

class Cross:
    """
    Klasa odpowiedzialna za analizę i rozwiązywanie Cross na kostce Rubika.

    Attributes:
        cube (Cube): Obiekt reprezentujący aktualny stan kostki Rubika.
        start_state: Stan początkowy krawędzi Cross w postaci binarnej.
        end_state: Stan docelowy krawędzi Cross w postaci binarnej. 
    """
    def __init__(self, cube, color: str = "y"):
        """
        Inicjalizuje obiekt Cross.

        Args: 
            cube (Cube): Obiekt kostki Rubika, który ma być analizowany. 
        """
        self.cross_edges = {
            'w': [0, 1, 2, 3],
            'y': [4, 5, 6, 7],
            'r': [1, 5, 9, 10],
            'b': [0, 4, 8, 9],
            'g': [2, 6, 10, 11],
            'o': [3, 7, 8, 11],
        }[color]

        self.cube = cube

        COLOR_ROTATION = {
            'y': lambda: None,          # biały już na dole
            'w': lambda: self.cube.z2(),      # żółty na dół
            'r': lambda: self.cube.z(),       # czerwony na dół
            'o': lambda: self.cube.zp(),     # pomarańczowy na dół
            'b': lambda: self.cube.x(),       # niebieski na dół
            'g': lambda: self.cube.xp(),     # zielony na dół
        }[color]()

        # test = [0,1,2,3]#[4,5,6,7] [2,6,10,11] [0,4,8,9] [0,1,2,3] [3,7,8,11] [0,4,8,9]
        self.start_state = convert.edges_to_binary(self.cube, self.cross_edges)#[4,5,6,7])
        from cube import Cube
        self.end_state = convert.edges_to_binary(Cube(cube.rotation), self.cross_edges)

    def find_cross(self, length: int) -> List[str]:
        """
        Znajduje wszystkie możliwe algorytmy do utworzenia Cross o zadanej długości.
        Args:
            length (int): Maksymalna długość algorytmu Cross.

        Returns:
            List[str]: Lista algorytmów w notacji ruchów Rubika.
        """
        solutions = self.__find_solutions(length)
        return self.__convert_cross_numbers_to_notation(solutions)

    def __find_solutions(self, length: int) -> List[List[int]]:
        """
        Generuje wszystkie kombinacje ruchów prowadzące do Cross.

        Args: 
            length (int): Maksymalna długość algorytmu.

        Returns: 
            List[List[int]]: Lista kombinacji ruchów w formie numerycznej.
        """
        return cube_solver.combinations(length, self.start_state, self.end_state)

    def __convert_cross_numbers_to_notation(self, notation_int: List[List[int]]) -> List[str]:
        """
        Konwertuje kombinacje numeryczne ruchów Cross na standardową notację kostki Rubika.

        Args: 
            notation_int (List[List[int]]: notacja w formacie int, która potem będzie zmieniana na str.

        Returns:
            List[str]: Lista ruchów przekonwertowanych z liczb.
        """
        return [' '.join(convert.int_to_notation[x] for x in sol) for sol in notation_int]
    
    def is_cross_solved(self) -> bool:
        """
        Sprawdza, czy Cross jest już ułożony na kostce.

        Returns:
            bool: True jeśli Cross jest kompletny, False w przeciwnym wypadku.
        """
        for e in range(4,8):
            if not (self.cube.edges[e] == [e,0]).all():
                return False
        return True
            