# This Python file uses the following encoding: utf-8
from Finance2Go.task1.SimpleInterest import *
from Finance2Go.task4.ContinuousInterest import *

if __name__ == "__main__":
    print(get_interest(5, 100000, 0.25))
    print(get_increased_sum_with_changeable_growth_force(7, 0.05, 10000, 0.05,
                                                         "linear"))
