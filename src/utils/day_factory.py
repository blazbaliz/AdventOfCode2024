from puzzles_by_day.day_1.hystorian_hysteria import HystorianHysteria
from puzzles_by_day.day_2.red_nosed_reports import RedNosedReports

def get_day_puzzle(day: int):
    match day:
        case 1:
            return HystorianHysteria(day)
        case 2:
            return RedNosedReports(day)
        case _:
            raise ValueError(f"No puzzle found for day {day}")