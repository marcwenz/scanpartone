from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from config.config import loadConfig
from utils import findMainWindow
# from twainhandle.scantwain import ScanManager


class WorkflowWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(objectName="cw_workflow", parent=parent, flags=flags)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding,
                           QtWidgets.QSizePolicy.Expanding)
        # self.wf = WorkflowSelection(self)
        self.gridLayout = QtWidgets.QGridLayout(self)
        # self.gridLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.wfItems = []
        cc = RowCol(3, 3)
        for wf in findMainWindow().configs["wf"]:
            wfi = WorkflowItem(wf, self)
            self.wfItems.append(wfi)
            self.gridLayout.addWidget(wfi, *cc.next())


class RowCol:
    def __init__(self, row_max=0, col_max=0):
        self.row = 0
        self.col = 0
        self.row_max = row_max
        self.col_max = col_max

    def next(self):
        if self.row == self.row_max:
            return None
        t = (self.row, self.col)
        self.col += 1
        if self.col == self.col_max:
            self.col = 0
            self.row += 1
        return t


"""
For selecting configured scan jobs.
Bottom right settings to edit jobs.
Top right questionmark for help.
Grid with 3 columns
"""


class WorkflowItem(QtWidgets.QWidget):
    def __init__(self, configItem, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        self.scanSettings = configItem
        self.iconContainer = QtWidgets.QWidget(self)
        dim = 125
        self.iconContainer.setContentsMargins(10, 10, 10, 10)
        self.iconContainer.setGeometry(QtCore.QRect(0, 0, dim, dim*.95))
        self.iconContainer.setStyleSheet(
            "background:#1c1c1c; border-radius:{}px".format(int(dim*.95/2)))
        self.svg = QtSvg.QSvgWidget("icons/document1.svg", self.iconContainer)
        im_size = int(dim * .53)
        self.svg.setGeometry(QtCore.QRect(
            int((dim-im_size)/2), int((dim*.95-im_size)/2), im_size, im_size))
        self.svg.setStyleSheet("background:transparent")

        lbl_dim = (dim*2.0, dim*.9)
        self.labelContainer = QtWidgets.QLabel(self)
        self.labelContainer.lower()
        self.labelContainer.setObjectName("labelContainer")
        self.labelContainer.setStyleSheet(
            "#labelContainer {\
            background:#bdbcb1;\
            padding-left: 70px; \
            border: 2px solid; \
            border-top-right-radius: 13px;\
            border-bottom-right-radius: 13px;\
            border-color:#1c1c1c;}")
        self.labelContainer.setGeometry(QtCore.QRect(
            int(dim/2), int((dim*.95-lbl_dim[1])/2), *lbl_dim))
        self.labelContainerLayout = QtWidgets.QVBoxLayout(self.labelContainer)
        self.labelContainerLayout.setContentsMargins(0, 0, 10, 0)
        self.labelContainerLayout.setSpacing(0)
        self.label = QtWidgets.QLabel(
            self.scanSettings["name"], self.labelContainer)
        self.label.setFont(QtGui.QFont("Raleway", 17, QtGui.QFont.Medium))
        self.label.setStyleSheet(
            "margin-right: 5px;\
            color: #1c1c1c;")
        self.label.setWordWrap(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignRight)
        self.labelContainerLayout.addWidget(self.label)

    def mouseReleaseEvent(self, QMouseEvent):
        # TODO change ui to display scanned documents
        if "css" in self.scanSettings.keys():
            self.window().setScannerConfig(self.scanSettings["css"])
        ims = self.window().startScan(True, False)
        print("Images received:")
        print(ims)


"""
Configure workflows.
Configures
    ** Scan destination - either UO or DMS (Posteingang)
    ** Basic twain settings (specifically dpi, color depth, duplex,)
    ** Qr detection
    ** Single or multipage
"""


class WorkflowConfig(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
