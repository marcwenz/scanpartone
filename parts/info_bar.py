from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

"""
Info header for every tab. Displays current tab name + info.
On right side is logo.
Same background color as everything.
"""

# TODO add content specific detail section
# TODO add logo to right side


class InfoBar(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        # self.setStyleSheet("background:#1c1c1c")
        # self.setGeometry(QtCore.QRect(0, 0, ))
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                           QtWidgets.QSizePolicy.Maximum)

        self.nameLabel = QtWidgets.QLabel("Workflows".upper(), parent=self)
        self.nameLabel.setStyleSheet(
                "font: 40pt SF New Republic; color:#bdbcb1; padding-top: 17px; padding-left: 15px; padding-right:15px")

    def sizeHint(self):
        return QtCore.QSize(0, 120)
