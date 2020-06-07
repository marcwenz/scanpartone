from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

import twain


class SettingsWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
