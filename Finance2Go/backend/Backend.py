
from PySide6.QtCore import QObject, Slot


class Backend(QObject):
    def __init__(self, simpleInterestController):
        super().__init__()
        self.simpleInterestController = simpleInterestController

    @Slot(str, str, "QVariant", result=float)
    def dispatch(self, controllerName, handlerName, params):
        variant = params.toVariant()
        controller = self.__getattribute__(controllerName + "Controller")
        return controller.__getattribute__(handlerName)(**variant)
