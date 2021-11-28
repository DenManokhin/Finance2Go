import sys

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine

from Finance2Go.backend import Backend

import resources

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon(':/icons/logo.png'))

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('ui/main.qml')

    backend = Backend.Backend()
    engine.rootObjects()[0].setProperty("backend", backend)

    sys.exit(app.exec())
