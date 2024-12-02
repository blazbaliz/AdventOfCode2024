from interfaces.day_interface import DayInterface

class HystorianHysteria(DayInterface):

    _first_list = []
    _second_list = []

    def __init__(self, day):
        super().__init__(day)

    def on_load(self):
        ''' Load the puzzle input '''
        
        for line in self.puzzle_input:
            rows = line.split()
            self._first_list.append(rows[0])
            self._second_list.append(rows[1])
                    
        self._first_list = sorted(self._first_list, key=int)
        self._second_list = sorted(self._second_list, key=int)

    def do_puzzle(self):
        ''' Do the puzzle '''

        distance, similarity = self._get_distance_and_similarity()

        print("Day 1 Puzzle")
        print(f"Distance between the two lists: {distance}")
        print(f"Similarity: {similarity}")
    
    def _get_distance_and_similarity(self):
        ''' Get the distance and similarity between two lists '''
        
        distance = 0
        similarity = 0

        for id in range(len(self._first_list)):
            distance += abs(int(self._second_list[id]) - int(self._first_list[id]))

            # Count occurrences of each element in list2
            similarity += int(self._first_list[id]) *  self._second_list.count(self._first_list[id])

        return distance, similarity
    