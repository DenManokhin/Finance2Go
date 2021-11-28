from ..task1 import SimpleInterest

from PySide6.QtCore import QObject, Slot


class Backend(QObject):
    def __init__(self):
        super().__init__()

    def getInterest(self, n: float, p: float, i: float) -> float:
        return SimpleInterest.get_interest(n, p, i)

    @Slot(str, "QVariant", result=float)
    def dispatch(self, handlerName, params):
        variant = params.toVariant()
        return self.__getattribute__(handlerName)(**variant)
