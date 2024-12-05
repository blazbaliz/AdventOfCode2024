from puzzles_by_day.day_1.hystorian_hysteria import HystorianHysteria
from puzzles_by_day.day_2.red_nosed_reports import RedNosedReports
from puzzles_by_day.day_3.mull_it_over import MullItOver
from puzzles_by_day.day_4.ceres_search import CeresSearch

def get_day_puzzle(day: int):
    match day:
        case 1:
            return HystorianHysteria(day)
        case 2:
            return RedNosedReports(day)
        case 3:
            return MullItOver(day)
        case 4:
            return CeresSearch(day)
        case _:
            raise ValueError(f"No puzzle found for day {day}")