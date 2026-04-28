class MovesBase:
    def _cycle_right(self, arr, elements: list[int]) -> None:
        arr[elements] = arr[[elements[-1]] + elements[:-1]]

    def _cycle_left(self, arr, elements: list[int]) -> None:
        arr[elements] = arr[elements[1:] + [elements[0]]]

    def _swap_pairs(self, arr, elements: list[int]) -> None:
        arr[elements] = arr[[elements[2], elements[3], elements[0], elements[1]]]
