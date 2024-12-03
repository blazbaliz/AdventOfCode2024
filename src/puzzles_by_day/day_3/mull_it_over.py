from interfaces.day_interface import DayInterface
import re

class MullItOver(DayInterface):

    _correct_data = list()
    
    def __init__(self, day):
        super().__init__(day)

    def on_load(self):
        self._find_correct_data()

    def do_puzzle(self):

        print("Day 2 Puzzle")
        print(f"Mul instructions result: {self._get_mul_instructions_result()}")

    def _find_correct_data(self):
        """
        Finds the correct data by regex
        When found exclude only numbers for later calculations
        """

        for line in self.puzzle_input:
            for data in re.findall(r"mul\(\d+,\d+\)", line):
                self._correct_data += re.findall(r"\d+,\d+", data)

    def _get_mul_instructions_result(self):
        result = 0
        for line in self._correct_data:
            a, b = map(int, line.split(","))
            result += a * b
        
        return result