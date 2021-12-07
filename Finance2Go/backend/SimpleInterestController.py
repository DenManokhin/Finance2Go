import numpy as np
from ..solvers import SimpleInterest


class SimpleInterestController:
    def __init__(self):
        pass

    def getInterest(self, n: float, p: float, i: float) -> float:
        return SimpleInterest.get_interest(n, p, i/100)

    def getAccumulatedSum(self, n: float, p: float, i: float) -> float:
        return SimpleInterest.get_accumulated_sum(n, p, i/100)

    def getAccumulatedValueForDifferentPeriods(self, n: np.array, p: float, i: np.array) -> float:
        return SimpleInterest.get_increased_sum_for_different_periods(n, p, i/100)