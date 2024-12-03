from abc import ABC, abstractmethod
import os

class DayInterface(ABC):
    def __init__(self, day: int):
        with open(f"src/puzzles_by_day/day_{day}/puzzle_input.txt", 'r') as file:
            self.puzzle_input = file.read()

        self.on_load()

    @abstractmethod
    def on_load(self):
        pass

    @abstractmethod
    def do_puzzle(self):
        pass