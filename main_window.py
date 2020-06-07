from PyQt5 import QtCore, QtGui, QtWidgets
from parts.s_button_layout import ButtonLayout
from parts.info_bar import InfoBar
from parts.workflow_widget import WorkflowWidget
from parts.account_widget import AccountWidget
from parts.settings_widget import SettingsWidget
from parts.scan_widget import ScanWidget
from parts.info_bar import InfoBar
from parts.confirm_scan import BufferBar
from twainhandle.scantwain import ScanManager
from config.config import loadConfig, saveConfig


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *a, **kw):
        QtGui.QFontDatabase.addApplicationFont(
            "fonts/Raleway-Medium.ttf")
        super(MainWindow, self).__init__(*a, *kw)
        self.initConfigs()
        self.init_window()
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("centralwidget")
        self.setCentralWidget(self.central_widget)
        self.centralLayout = QtWidgets.QHBoxLayout(self.central_widget)
        self.centralLayout.setContentsMargins(0, 0, 0, 0)
        self.centralLayout.setSpacing(0)
        self.centralLayout.setObjectName("centralLayout")

        # Main config specifies preferred scanner.
        # If not available display dialag to select.
        self.scanManager = ScanManager()

        # Create Main Button Layout
        self.verticalLayoutWidget = ButtonLayout(
            self.central_widget, height=self.size().height())
        self.centralLayout.addWidget(self.verticalLayoutWidget)

        # Content widget
        self.content_widget = QtWidgets.QWidget(self.central_widget)
        # self.content_widget.setGeometry(QtCore.QRect(200, 10, 1651, 1021))
        self.content_widget.setObjectName("content_widget")
        self.content_widget.setStyleSheet(
            "border-top-left-radius:3px; border-bottom-left-radius:3px")
        self.content_widget.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        self.contentVerticalLayout = QtWidgets.QVBoxLayout(self.content_widget)
        self.contentVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.contentVerticalLayout.setSpacing(0)
        self.contentVerticalLayout.setObjectName("contentVerticalLayout")
        self.centralLayout.addWidget(self.content_widget)

        # Container widget
        self.containerWidget = QtWidgets.QWidget(self.content_widget)
        self.containerWidget.setObjectName("containerWidget")
        self.containerWidget.setStyleSheet("background:#bdbcb1")
        # self.containerWidget.setGeometry(QtCore.QRect(200, 10, 1651, 1021))
        # self.containerWidget.setSizePolicy()
        self.containerLayout = QtWidgets.QVBoxLayout(self.containerWidget)
        self.containerLayout.setContentsMargins(0, 0, 0, 0)
        self.containerLayout.setSpacing(0)
        self.containerLayout.setObjectName("containerLayout")

        self.init_widgets()

        self.containerLayout.addWidget(self.workflowWidget)

        # Add infobar to vert layout
        self.infoBar = InfoBar(self.content_widget)
        self.buffer = BufferBar(self.content_widget)
        self.contentVerticalLayout.addWidget(self.infoBar)
        self.contentVerticalLayout.addWidget(self.containerWidget)
        self.contentVerticalLayout.addWidget(self.buffer)

        self.init_button_press()
        self.displayScanWidget()

    def initConfigs(self):
        self.configs = {}
        self.configs["wf"] = loadConfig("wf")
        self.configs["sc"] = dict(
            [(k, dict([(int(kk), vv) for kk, vv in v.items()])) for k, v in loadConfig("sc").items()])

    def saveConfig(self):
        for i in self.configs.items():
            saveConfig(*i)

    def setScannerConfig(self, config):
        return self.scanManager.loadConfig(config)

    def startScan(self, gui=True, modal=True):
        return self.scanManager.acquire_images(ui=gui, modal=modal)

    def init_button_press(self):
        actionButton = self.verticalLayoutWidget.findChild(
            QtWidgets.QPushButton, "pushButton_Account")
        actionButton.clicked.connect(self.displayAccountWidget)
        actionButton = self.verticalLayoutWidget.findChild(
            QtWidgets.QPushButton, "pushButton_Workflow")
        actionButton.clicked.connect(self.displayWorkflowWidget)
        actionButton = self.verticalLayoutWidget.findChild(
            QtWidgets.QPushButton, "pushButton_Scan")
        actionButton.clicked.connect(self.displayScanWidget)
        actionButton = self.verticalLayoutWidget.findChild(
            QtWidgets.QPushButton, "pushButton_Settings")
        actionButton.clicked.connect(self.displaySettingsWidget)
        actionButton = self.verticalLayoutWidget.findChild(
            QtWidgets.QPushButton, "pushButton_Quit")
        actionButton.clicked.connect(
            lambda _: QtCore.QCoreApplication.instance().quit())

    def init_widgets(self):
        self.workflowWidget = WorkflowWidget(self.containerWidget)
        self.accountWidget = AccountWidget(self.containerWidget)
        self.scanWidget = ScanWidget(self.containerWidget)
        self.settingsWidget = SettingsWidget(self.containerWidget)

    def displayAccountWidget(self):
        # print(self.containerLayout.itemAt(0).widget())
        if self.infoBar.nameLabel.text() != "Account":
            self.infoBar.nameLabel.setText("Account".upper())
            ss = self.containerLayout.itemAt(0).widget()
            ss.hide()
            self.accountWidget.show()
            self.containerLayout.replaceWidget(ss, self.accountWidget)

    def displayWorkflowWidget(self):
        if self.infoBar.nameLabel.text() != "Workflows":
            self.infoBar.nameLabel.setText("Workflows".upper())
            ss = self.containerLayout.itemAt(0).widget()
            ss.hide()
            self.workflowWidget.show()
            self.containerLayout.replaceWidget(ss, self.workflowWidget)

    def displayScanWidget(self):
        if self.infoBar.nameLabel.text() != "Scanning":
            self.infoBar.nameLabel.setText("Scanning".upper())
            ss = self.containerLayout.itemAt(0).widget()
            ss.hide()
            self.scanWidget.show()
            self.containerLayout.replaceWidget(ss, self.scanWidget)

    def displaySettingsWidget(self):
        if self.infoBar.nameLabel.text() != "Settings":
            self.infoBar.nameLabel.setText("Settings".upper())
            ss = self.containerLayout.itemAt(0).widget()
            ss.hide()
            self.settingsWidget.show()
            self.containerLayout.replaceWidget(ss, self.settingsWidget)

    def init_window(self):
        self.resize(1920, 1080)
        self.setStyleSheet("background:#1c1c1c")
        self.setWindowTitle("Scanner App")

    def closeEvent(self, event):
        self.saveConfig()
        return super().closeEvent()
