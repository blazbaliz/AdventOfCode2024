import os

class HystorianHysteria():

    _first_list = []
    _second_list = []

    def __init__(self):
        # Change working directory
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        with open('puzzle_input.txt', 'r') as file:
            for line in file.readlines():
                rows = line.split()
                self._first_list.append(rows[0])
                self._second_list.append(rows[1])
                
        self._first_list = sorted(self._first_list, key=int)
        self._second_list = sorted(self._second_list, key=int)

    def do_puzzle(self):
        distance = 0

        for id in range(len(self._first_list)):
            distance += abs(int(self._second_list[id]) - int(self._first_list[id])) 

        return distance
    
    