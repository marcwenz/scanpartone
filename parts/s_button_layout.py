from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from parts.s_button import MainButton


class ButtonLayout(QtWidgets.QWidget):
    def __init__(self, parent=None, height=0, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setSizePolicy(QtWidgets.QSizePolicy.Maximum,
                           QtWidgets.QSizePolicy.Expanding)
        # Create vertical Layout
        self.setGeometry(
            QtCore.QRect(0, 0, 200, height))
        self.setStyleSheet("background:#1c1c1c")
        self.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 10, 0)
        self.verticalLayout.setSpacing(70)
        self.verticalLayout.setObjectName("verticalLayout")

        # Account Button
        self.pushButton_Account = MainButton("user.svg",
                                             parent=self)
        self.pushButton_Account.setObjectName("pushButton_Account")
        # Workflow button
        self.pushButton_Workflow = MainButton("workflow.svg",
                                              parent=self)
        self.pushButton_Workflow.setObjectName("pushButton_Workflow")
        # Scan Button
        self.pushButton_Scan = MainButton(
            "menu.svg", parent=self)
        self.pushButton_Scan.setObjectName("pushButton_Scan")
        # Settings button
        self.pushButton_Settings = MainButton("gear-option.svg",
                                              parent=self)
        self.pushButton_Settings.setObjectName("pushButton_Settings")
        # Quit button
        self.pushButton_Quit = MainButton(
            "off.svg", parent=self)
        self.pushButton_Quit.setObjectName("pushButton_Quit")

        # Add buttons to vert layout
        self.verticalLayout.addWidget(self.pushButton_Account)
        self.verticalLayout.addWidget(self.pushButton_Workflow)
        self.verticalLayout.addWidget(self.pushButton_Scan)
        self.verticalLayout.addWidget(self.pushButton_Settings)
        self.verticalLayout.addWidget(self.pushButton_Quit)

    def sizeHint(self):
        return QtCore.QSize(180, 0)
