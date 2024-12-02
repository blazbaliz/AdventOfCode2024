from interfaces.day_interface import DayInterface


class RedNosedReports(DayInterface):
    reports = list()

    def __init__(self, day):
        super().__init__(day)

    def on_load(self):
        for line in self.puzzle_input:
            self.reports.append(list(map(int, line.split())))

    def do_puzzle(self):
        print("Day 2 Puzzle")
        print(f"Number of reports that are safe to send: {self._get_safe_reports_count()}")
        pass

    def _get_safe_reports_count(self):
        """
        Gets the number of reports that are safe to send.
        
        :return: Number of reports that are safe to send.
        """
        count = 0
        for report in self.reports:
            if self._isIncreasing(report) or self._isDecreasing(report):
                count += 1

        return count

    def _isDecreasing(self, list):
        """
        Checks if a list is decreasing (each element is less than or equal to the previous one).
        
        :param lst: List of numbers to check.
        :return: True if the list is declining, otherwise False.
        """
        return all(list[i] > list[i+1] and self._is_in_range(list[i], list[i+1]) for i in range(len(list) - 1))
    
    
    def _isIncreasing(self, list):
        """
        Checks if a list is increasing (each element is less than or equal to the previous one).
        
        :param lst: List of numbers to check.
        :return: True if the list is inclining, otherwise False.
        """
        return all(list[i] < list[i+1] and self._is_in_range(list[i], list[i+1]) for i in range(len(list) - 1)) 
    
    def _is_in_range(self, first_value, second_value):
        """
        Checks if the two values are in range.
        
        :param first_value: First value.
        :param second_value: Second value.
        :return: True if the two values are in range, otherwise False.
        """
        value_range = abs(first_value - second_value)

        return 1 <= value_range <= 3