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
        print (f"Number of reports that are safe to send with Problem Dampener: {self._get_safe_reports_count(use_problem_dampener=True)}")
        pass

    def _get_safe_reports_count(self, use_problem_dampener=False):
        """
        Gets the number of reports that are safe to send.
        
        :param use_problem_dampener: Use the problem dampener to make the report safe to send.
        :return: Number of reports that are safe to send.
        """

        count = 0

        for report in self.reports:
            if not self._is_report_safe(report):
                if not use_problem_dampener:
                    continue
                if not self._is_report_safe_with_dampener(report):
                    continue
            count += 1    

        return count
    
    def _is_report_safe(self, report):
        """
        Checks if a report is safe to send.
        
        :param report: Report to check.
        :return: True if the report is safe to send, otherwise False.
        """
        return ((all(self._is_increasing(report[i], report[i+1]) for i in range(len(report) - 1)) or
                all(self._is_decreasing(report[i], report[i+1]) for i in range(len(report) - 1))) and
                all(self._is_in_range(report[i], report[i+1]) for i in range(len(report) - 1)))

    def _is_report_safe_with_dampener(self, report: list ):
        """
        Use the problem dampener to make the report safe to send 
        Remove first value that is not in range 
        Remove first value that is not increasing or decreasing 

        param report: Report to make safe to send 
        return: True if the report is safe to send, otherwise False 
        """
        for i in range(len(report)):
            report_ref = report.copy()
            del report_ref[i]
            
            if self._is_report_safe(report_ref):
                return True
      
    def _is_decreasing(self, first_value, second_value):
        """
        Checks if a list is decreasing (each element is less than or equal to the previous one).
        
        :param first_value: First value.
        :param second_value: Second value.
        :return: True if the list is declining, otherwise False.
        """
        return first_value > second_value
    
    
    def _is_increasing(self, first_value, second_value):
        """
        Checks if a list is increasing (each element is less than or equal to the previous one).
        
        :param first_value: First value.
        :param second_value: Second value.
        :return: True if the list is inclining, otherwise False.
        """
        return first_value < second_value
    
    def _is_in_range(self, first_value, second_value):
        """
        Checks if the two values are in range.
        
        :param first_value: First value.
        :param second_value: Second value.
        :return: True if the two values are in range, otherwise False.
        """
        value_range = abs(first_value - second_value)

        return 1 <= value_range <= 3
