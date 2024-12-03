from interfaces.day_interface import DayInterface
import re

class MullItOver(DayInterface):

    def __init__(self, day):
        super().__init__(day)

    def on_load(self):
        pass

    def do_puzzle(self):

        print("Day 2 Puzzle")
        print(f"Mul instructions result: {self._get_mul_instructions_result()}")
        print(f"Mul instructions result with conditions: {self._get_mul_instructions_result(True)}")

    def _find_correct_data(self, include_conditions):
        """
        Finds the correct data by regex
        When found exclude only numbers for later calculations
        """

        if include_conditions:
            self._find_with_conditions(self.puzzle_input)
            return
        
        self._correct_data += self._find_mul_instructions(self.puzzle_input)

    def _get_mul_instructions_result(self, include_conditions=False):
        self._correct_data = []
        result = 0

        self._find_correct_data(include_conditions)

        for line in self._correct_data:
            a, b = map(int, line.split(","))
            result += a * b
        
        return result
    
    def _find_mul_instructions(self, line):
        correct_data = []
        for data in re.findall(r"mul\(\d+,\d+\)", line):
                correct_data += re.findall(r"\d+,\d+", data)
        return correct_data  

    def _find_with_conditions(self, line):
        self._correct_data = []
        line_split_by_dont = line.split("don't()")

        for i in range(len(line_split_by_dont)):
            if i == 0:
                self._correct_data += self._find_mul_instructions(line_split_by_dont[i])
                continue
            
            instructions = line_split_by_dont[i].split("do()")
            for j in range(len(instructions)):
                if j == 0:
                    continue
                self._correct_data += self._find_mul_instructions(instructions[j])