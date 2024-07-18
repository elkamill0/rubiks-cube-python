from moves import Moves


class Scramble(Moves):
    def __init__(self, cube, moves: str):
        super().__init__(cube)
        self.moves = moves
        self.execute_moves()

    def execute_moves(self):
        for move in self.moves.split(" "):
            self.move_mapping().get(move)() if True else print(f"Unknown move: {move}")
