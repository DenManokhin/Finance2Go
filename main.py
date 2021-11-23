import sys

from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine

import resources

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon(':/icons/logo.png'))

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('qrc:/ui/main.qml')

    sys.exit(app.exec())
