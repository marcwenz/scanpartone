from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg


class AccountWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(objectName="cw_account", parent=parent, flags=flags)
