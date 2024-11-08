import math
import statistics

def circle_area(r: float) -> float:
    return math.pi * math.pow(r, 2)

def average_score(grades: list[int]) -> int:
    return round(statistics.mean(grades))

def sber_count_securities(money: float) -> int:
    price: float = 317.20
    return math.floor(money // price)
