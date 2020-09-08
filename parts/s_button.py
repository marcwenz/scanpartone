from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from os import scandir

# TODO dynamically change icon color

class BaseButton(QtWidgets.QPushButton):
    def __init__(self,  clicked=None, objectName="", text="", parent=None):
        super().__init__(text=text, clicked=clicked, objectName=objectName, parent=parent)


class MenuButton(BaseButton):
    def __init__(self, icon_path, clicked, objectName, text="", parent=None):
        super().__init__(text=text, clicked=clicked, objectName=objectName, parent=parent)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        self.setIcon(QtGui.QIcon("icons/" + icon_path))
        self.setIconSize(QtCore.QSize(100, 100))
        self.setStyleSheet("border: 0px; \
                           background-color: transparent")
        # self.resize(100, 100)

    def sizeHint(self):
        return QtCore.QSize(100, 150)
