from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
"""
Contains OK button to start scanning with set settings.
To be used in workflows and raw scan tabs.
"""


class BufferBar(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)

    def sizeHint(self):
        return QtCore.QSize(0, 120)
