from ..solvers import SimpleInterest


class SimpleInterestController:
    def __init__(self):
        pass

    def getInterest(self, n: float, p: float, i: float) -> float:
        return SimpleInterest.get_interest(n, p, i)

    def getAccumulatedSum(self, n: float, p: float, i: float) -> float:
        return SimpleInterest.get_accumulated_sum(n, p, i)