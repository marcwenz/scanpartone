from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

# import twain


class SettingsWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(objectName="cw_settings", parent=parent, flags=flags)
