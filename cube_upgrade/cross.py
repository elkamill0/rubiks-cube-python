from moves import Moves
import cube_upgrade


class Cross(Moves):
    def __init__(self, cube):
        super().__init__(cube)

    def find_cross(self, length):
        return cube_upgrade.combinations(length, self.cube, self.cube_copy)