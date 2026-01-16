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
    def __init__(self, cube):
        """
        Inicjalizuje obiekt Cross.

        Args: 
            cube (Cube): Obiekt kostki Rubika, który ma być analizowany. 
        """

        self.cube = cube
        self.cross_edges = [4,5,6,7]
        self.start_state = convert.edges_to_binary(self.cube, self.cross_edges)
        from cube import Cube
        self.end_state = convert.edges_to_binary(Cube(), self.cross_edges)

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
            