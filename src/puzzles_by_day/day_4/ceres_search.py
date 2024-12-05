from interfaces.day_interface import DayInterface
import re

class CeresSearch(DayInterface):
    """
    Ceres Search
    """

    XMAS_CONST = "XMAS"

    _lines = []

    _number_of_occurrences = 0

    def __init__(self, day):
        super().__init__(day)

    def on_load(self):
        """
        Load the puzzle input
        """

        self._get_all_lines()
    
    def do_puzzle(self):
        """
        Do the puzzle
        """

        print("Day 3 Puzzle")
        print(f"Number of occurences: {self._calculate_number_of_occurrences()}")

    def _get_all_lines(self):
        """
        Find all horizontal, vertical, diagonal up and diagonal down lines
        """

        input = self.puzzle_input.splitlines()
        rows = len(input)
        cols = len(input[0])

        self._horizontal_lines = input
        self._vertical_lines = [''.join(row[j] for row in input) for j in range(len(input[0]))]

        self._diagonal_up_lines  = [
            ''.join(input[r + i][c + i] for i in range(min(rows - r, cols - c)))
            for r, c in [(0, col) for col in range(cols)] + [(row, 0) for row in range(1, rows)]
        ]

        self._diagonal_down_lines = [
            ''.join(input[r + i][c - i] for i in range(min(rows - r, c + 1)))
            for r, c in [(0, col) for col in range(cols - 1, -1, -1)] + [(row, cols - 1) for row in range(1, rows)]
        ]


    def _calculate_number_of_occurrences(self) -> int:
        """
        Calculate the number of occurrences of a substring in a string
        """
        return self._get_number_of_occurrences_in_lines(self._horizontal_lines) + \
               self._get_number_of_occurrences_in_lines(self._vertical_lines) + \
               self._get_number_of_occurrences_in_lines(self._diagonal_up_lines) + \
               self._get_number_of_occurrences_in_lines(self._diagonal_down_lines)
    
    
    def _get_count_by_regex(self, line):
        """
        Get the count by regex
        """
        return len(re.findall(rf"{self.XMAS_CONST}", line))
    
    def _get_number_of_occurrences_in_lines(self, lines):
        """
        Get the number of occurrences in a line
        Search in both ways forward and backward
        """
        return sum(self._get_count_by_regex(line) for line in lines) + sum(self._get_count_by_regex(line[::-1]) for line in lines)
