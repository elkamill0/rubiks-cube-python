from moves import Moves
import scramble


class Cross(Moves):
    def __init__(self, cube):
        super().__init__(cube)

    def find_cross(self, length):
        return scramble.combinations(length, self.cube)