import numpy as np
from PySide6.QtCore import QObject, Slot


class Backend(QObject):
    def __init__(self, simpleInterestController):
        super().__init__()
        self.simpleInterestController = simpleInterestController

    def _handle_repeatable(self, params):
        if "_repeatable" not in params:
            return params
        keys = params["_repeatable"][0].keys()
        rep_params = {}
        for key in keys:
            rep_params[key] = np.array([x[key] for x in params["_repeatable"]])
        del params["_repeatable"]
        params.update(rep_params)
        return params

    @Slot(str, str, "QVariant", result=float)
    def dispatch(self, controllerName, handlerName, params):
        params = params.toVariant()
        params = self._handle_repeatable(params)
        controller = self.__getattribute__(controllerName + "Controller")
        return controller.__getattribute__(handlerName)(**params)
