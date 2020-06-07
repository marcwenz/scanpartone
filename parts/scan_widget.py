from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from PyQt5.QtWidgets import QSizePolicy


class ScanWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)
        self.configTabWidget = ConfigTabWidget(self)
        self.configLayout = ConfigBarWidget(self)
        self.mainLayout.addWidget(self.configLayout)
        self.mainLayout.addWidget(QHSeperationLine(self))
        self.mainLayout.addWidget(self.configTabWidget)

    def updateConfig(self, text):
        # TODO problem with popup window
        self.configTabWidget.updateConfig(self.window().configs["sc"][text])


class QHSeperationLine(QtWidgets.QFrame):
    '''
    a horizontal seperation line
    '''

    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setMinimumWidth(1)
        self.setFixedHeight(1)
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setLineWidth(1)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred,
                           QtWidgets.QSizePolicy.Minimum)
        self.setStyleSheet("border:1px solid #1c1c1c")
        self.setFrameShadow(QtWidgets.QFrame.Sunken)


class ConfigBarWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        self.configLayout = QtWidgets.QHBoxLayout(self)
        self.setSizePolicy(QSizePolicy.Expanding,
                           QSizePolicy.Maximum)
        self.configLayout.setContentsMargins(30, 0, 30, 0)
        self.configLayout.setSpacing(40)
        self.comboBox_config = C_ComboBox(self)
        # TODO problem with popup window
        self.comboBox_config.addItems(self.window().configs["sc"].keys())
        self.comboBox_config.currentTextChanged.connect(
            lambda _: self.parent().updateConfig(self.comboBox_config.currentText()))
        # self.comboBox_config.addItems(["item", "item", "item", "item"])
        self.pushButton_Save = C_PushButton("Save", self)
        self.pushButton_New = C_PushButton("New", self)
        self.pushButton_Delete = C_PushButton("Delete", self)
        self.pushButton_Default = C_PushButton("Default", self)
        self.pushButton_Prescan = C_PushButton("Prescan", self)
        self.pushButton_Scan = C_PushButton("Scan", self)

        self.configLayout.addWidget(self.comboBox_config)
        self.configLayout.addSpacerItem(QtWidgets.QSpacerItem(
            320, 0, QSizePolicy.Preferred, QSizePolicy.Expanding))
        self.configLayout.addWidget(self.pushButton_Save)
        self.configLayout.addWidget(self.pushButton_New)
        self.configLayout.addWidget(self.pushButton_Delete)
        self.configLayout.addWidget(self.pushButton_Default)
        self.configLayout.addWidget(self.pushButton_Prescan)
        self.configLayout.addWidget(self.pushButton_Scan)
        self.configLayout.addSpacerItem(QtWidgets.QSpacerItem(
            120, 0, QSizePolicy.Preferred, QSizePolicy.Expanding))
        self.parent().updateConfig(self.comboBox_config.currentText())

    def sizeHint(self):
        return QtCore.QSize(0, 50)


class ConfigTabWidget(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.tab_Bar = ConfigTabBar(self)
        self.setTabBar(self.tab_Bar)
        self.setTabPosition(QtWidgets.QTabWidget.West)
        self.setStyleSheet("QTabWidget::pane { border: 0; }")

        self.setSizePolicy(QSizePolicy.Expanding,
                           QSizePolicy.Expanding)

        self.basicTab = BasicTab(self)
        self.commonTab = CommonTab(self)
        self.qrTab = QRTab(self)
        self.colorTab = ColorTab(self)
        self.addTab(self.basicTab, "Basic")
        self.addTab(self.commonTab, "Common")
        self.addTab(self.qrTab, "QR Code")
        self.addTab(self.colorTab, "Color")

    def updateConfig(self, conf):
        print(conf)
        self.tmp_conf = self.window().setScannerConfig(conf)

        print(conf)
        self.window().configs["sc"]["dbw1"] = self.tmp_conf
        print("updating...")


class ConfigTabBar(QtWidgets.QTabBar):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setMinimumWidth(200)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        # self.setStyleSheet("text-align:left")
        self.setFont(QtGui.QFont("Raleway", 15, QtGui.QFont.Medium))

    def sizeHint(self):
        return QtCore.QSize(200, 350)

    def tabSizeHint(self, index):
        s = QtWidgets.QTabBar.tabSizeHint(self, index)
        s.transpose()
        return QtCore.QSize(self.sizeHint().width(), s.height())

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        opt = QtWidgets.QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
            painter.save()

            tabRect = self.tabRect(i)
            tabRect.moveLeft(10)
            painter.drawText(tabRect, QtCore.Qt.AlignVCenter |
                             QtCore.Qt.TextDontClip,
                             self.tabText(i))
            painter.restore()


class SettingsLayout(QtWidgets.QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        QtWidgets.QScroller.grabGesture(
            self, QtWidgets.QScroller.LeftMouseButtonGesture)
        self.widget = QtWidgets.QWidget()
        self.container = QtWidgets.QVBoxLayout(self.widget)
        self.widgetLayout = QtWidgets.QVBoxLayout()
        self.widgetLayout.setSpacing(13)
        self.widgetLayout.setContentsMargins(0, 0, 0, 0)
        self.container.addLayout(self.widgetLayout)
        self.setWidget(self.widget)
        spacer = QtWidgets.QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        spacer.setContentsMargins(0, 0, 0, 0)
        self.container.addWidget(spacer)

        self.setWidgetResizable(True)

    def addItem(self, label, description, setting):
        self.widgetLayout.addWidget(SettingUnit(
            label, description, setting, parent=self.widget))

    def addSection(self, section):
        section.finish()
        self.widgetLayout.addWidget(section)

    def getColumn(self, col=0):
        lab = []
        for r in range(self.gridLayout.rowCount()):
            i = self.gridLayout.itemAtPosition(r, 0)
            if isinstance(i, QtWidgets.QLayoutItem):
                lab.append(i.widget())
                print("item")
        return lab

    def pair(self, index):
        return [self.gridLayout.itemAtPosition(index, 0),
                self.gridLayout.itemAtPosition(index, 1)]


class SettingEnforcer:
    def __init__(self):
        pass


class SettingUnitSection(QtWidgets.QWidget):
    def __init__(self, header, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.finished = 0
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.addWidget(QHSeperationLine(self))
        self.layout.addWidget(SettingUnitSectionHeader(header))

    def addItem(self, label, description, setting):
        self.layout.addWidget(SettingUnit(
            label, description, setting, parent=self))

    def finish(self):
        if not self.finished:
            self.layout.addWidget(QHSeperationLine(self))
            self.finished = 1


class SettingUnitSectionHeader(QtWidgets.QLabel):
    def __init__(self, str, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(str, parent=parent, flags=flags)
        self.setFont(QtGui.QFont("Raleway", 14, QtGui.QFont.Medium))


class SettingUnit(QtWidgets.QWidget):
    def __init__(self, label, description, widget, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.label = SettingUnitLabel(label)
        self.description = SettingUnitDescription(description)
        self.widget = widget
        self.layout.addWidget(self.label, QtCore.Qt.AlignTop)
        if isinstance(self.widget, SettingUnitCheckbox):
            widget.setText(description)
        else:
            self.layout.addWidget(self.description, QtCore.Qt.AlignTop)
        self.layout.addWidget(self.widget, QtCore.Qt.AlignTop)

    def getValue(self):
        return self.widget.getValue()


class SettingUnitLabel(QtWidgets.QLabel):
    def __init__(self, str, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(str, parent=parent, flags=flags)
        self.setFont(QtGui.QFont("Raleway", 12, QtGui.QFont.Medium))
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)


class SettingUnitDescription(QtWidgets.QLabel):
    def __init__(self, str, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(str, parent=parent, flags=flags)
        self.setFont(QtGui.QFont("Raleway", 8, QtGui.QFont.Medium))
        self.setWordWrap(True)


class SettingUnitCheckbox(QtWidgets.QWidget):
    def __init__(self, text="", parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.col1 = QtWidgets.QVBoxLayout()
        self.col1.setAlignment(QtCore.Qt.AlignTop)
        self.col1.setContentsMargins(0, 1, 0, 0)
        self.col1.setDirection(0)
        self.col2 = QtWidgets.QVBoxLayout()
        self.col2.setAlignment(QtCore.Qt.AlignTop)
        self.col2.setContentsMargins(0, 0, 0, 0)
        self.col2.setDirection(0)
        self.layout.addLayout(self.col1)
        self.layout.addLayout(self.col2)
        self.checkBox = QtWidgets.QCheckBox()
        self.checkBox.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.checkLabel = QtWidgets.QLabel(text)
        self.checkLabel.setWordWrap(True)
        self.checkLabel.setSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.col1.addWidget(self.checkBox)
        self.col2.addWidget(self.checkLabel)
        self.setFont(QtGui.QFont("Raleway", 10, QtGui.QFont.Medium))

    def isChecked(self):
        return self.checkBox.isChecked()

    def setText(self, text):
        self.checkLabel.setText(text)

    def getValue(self):
        return self.isChecked()


class SettingUnitInput(QtWidgets.QLineEdit):
    def __init__(self, init, string=1, parent=None):
        super().__init__(str(init), parent=parent)
        self.setFont(QtGui.QFont("Raleway", 11, QtGui.QFont.Medium))
        self.setMaximumWidth(100 + string * 200)

    def getValue(self):
        if not self.string:
            return int(self.text())
        return str(self.string)


class C_ComboBox(QtWidgets.QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.setFont(QtGui.QFont("Raleway", 14, QtGui.QFont.Medium))
        self.delegate = QtWidgets.QStyledItemDelegate()
        self.setItemDelegate(self.delegate)


class SettingUnitCBox(C_ComboBox):
    def __init__(self, items=None, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet("padding:5;margin-right:10px;")
        self.setMaximumHeight(50)
        self.setMaximumWidth(350)
        self.setFont(QtGui.QFont("Raleway", 10, QtGui.QFont.Medium))
        # self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        if items:
            for i in items:
                self.addItem(i)

    def getValue(self):
        # numeric value?
        return str(self.currentText())


class BasicTab(SettingsLayout):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.addItem("Duplex", "Controls whether the scanner scans both sides of the document.",
                     SettingUnitCBox(["Duplex", "Simplex"]))
        self.addItem("Color Depth", "Select the scanning color.",
                     SettingUnitCBox(["Black and White", "Gray", "24 bit color"]))
        self.addItem("Output Filetype", "Controls the filetype of the output scan.",
                     SettingUnitCBox(["BMP", "TIFF", "JPG", "PDF"]))
        self.addItem("Scanning Resolution",
                     "Sets the resolution for the scan", SettingUnitInput("300", 0))
        self.addItem(
            "Auto Rotate", "Automatically rotate the scan based on its content.", SettingUnitCheckbox())
        self.addItem("Deskew", "Automatically deskews the image.",
                     SettingUnitCheckbox())
        self.addItem(
            "Auto Crop", "Automatically crops the scan to the paper size.", SettingUnitCheckbox())


class CommonTab(SettingsLayout):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.addItem(
            "Auto Crop", "Automatically crops the scan to the paper size.", SettingUnitCheckbox())
        self.addItem("Deskew", "Automatically deskews the image.",
                     SettingUnitCheckbox())
        self.addItem("Hole Removal", "Remove holes in the scan.",
                     SettingUnitCheckbox())
        # Turn this into section w/ checkbox and input
        section = SettingUnitSection("Blank Page Removal")
        section.addItem("Blank Page Removal", "Remove blank pages.",
                        SettingUnitCheckbox())
        section.addItem("Blank Page Threshold",
                        "Set the threshold for blank pixels", SettingUnitInput(0.05, string=0))
        self.addSection(section)


class QRTab(SettingsLayout):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.addItem(
            "Enable QR Code", "Begin a new document each time a QR code is detected on the page.", SettingUnitCheckbox())
        self.addItem("Detection side", "Detect QR Codes on the front, back or both sides",
                     SettingUnitCBox(["Both", "Front", "Back"]))
        section = SettingUnitSection("Information Requirement")
        section.addItem("Enable Information Requirement",
                        "Only split the document if the detected code matches the requirement.", SettingUnitCheckbox())
        section.addItem(
            "Text Requirement", "Specify the information requirement for the decoded QR Code.", SettingUnitInput(""))
        self.addSection(section)
        self.addItem(
            "Remove QR Code", "Remove detected QR Codes from the scan", SettingUnitCheckbox())


class ColorTab(QtWidgets.QWidget):
    def __init__(self, parent=None, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        self.setStyleSheet("background:red")
        self.btn = QtWidgets.QPushButton("test", self)


class C_PushButton(QtWidgets.QPushButton):
    def __init__(self, str, parent=None):
        super().__init__(str, parent=parent)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        self.setFont(QtGui.QFont("Raleway", 10, QtGui.QFont.Medium))
        self.setStyleSheet(
            "padding: 3px; border:1px solid #1c1c1c;border-radius:5px;")
        self.setMaximumWidth(100)
