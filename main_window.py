from PyQt5 import QtCore, QtGui, QtWidgets
from parts.s_button_layout import ButtonLayout
from parts.info_bar import InfoBar
from parts.workflow_widget import WorkflowWidget
from parts.account_widget import AccountWidget
from parts.settings_widget import SettingsWidget
from parts.scan_widget import ScanWidget
from parts.info_bar import InfoBar
from parts.confirm_scan import BufferBar

# from twainhandle.scantwain import ScanManager
from config.config import loadConfig, saveConfig


class MainWindow(QtWidgets.QMainWindow):
    """
    This is the first part of the scanner application.
    It serves the purpose of initializing the scanning and its settings.
    Layout:
        - central_widget
            - content_h_layout
                - menu_buttons
                - content_container
                    - content_vlayout
                        - infobar
                        - container_stack
                        - buffer

    """

    def __init__(self, *a, **kw):
        QtGui.QFontDatabase.addApplicationFont("fonts/Raleway-Medium.ttf")
        super(MainWindow, self).__init__(*a, *kw)

        ### Initialize main window specifics ###
        self.initConfigs()
        self.init_window()
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("centralwidget")
        self.setCentralWidget(self.central_widget)

        ### HLayout containing Menu Buttons and Content Container ###
        self.content_h_layout = QtWidgets.QHBoxLayout(self.central_widget)
        self.content_h_layout.setContentsMargins(0, 0, 0, 0)
        self.content_h_layout.setSpacing(0)
        self.content_h_layout.setObjectName("centralLayout")

        # Main config specifies preferred scanner.
        # If not available display dialag to select.
        # self.scanManager = ScanManager()

        ### Initialize container for widgets ###
        self.content_container = QtWidgets.QWidget(self.central_widget)
        self.content_container.setObjectName("content_widget")
        self.content_container.setStyleSheet(
            "border-top-left-radius:3px; border-bottom-left-radius:3px"
        )
        self.content_container.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )

        ### VLayout containing InfoBar, Widget Content and Bottom Bar ###
        self.content_v_layout = QtWidgets.QVBoxLayout(self.content_container)
        self.content_v_layout.setContentsMargins(0, 0, 0, 0)
        self.content_v_layout.setSpacing(0)
        self.content_v_layout.setObjectName("contentVerticalLayout")

        ### Container Stack ###
        self.container_stack = QtWidgets.QStackedWidget(self.content_container)
        self.container_stack.setObjectName("containerWidget")
        self.container_stack.setStyleSheet("background:#bdbcb1")

        ### InfoBar and BufferBar ###
        self.infoBar = InfoBar(self.content_container)
        self.buffer = BufferBar(self.content_container)

        ### Init account, workflow, setting, scan widgets ###
        self.init_widgets()
        self.container_stack.addWidget(self.CW_account)
        self.container_stack.addWidget(self.CW_workflow)
        self.container_stack.addWidget(self.CW_scan)
        self.container_stack.addWidget(self.CW_setting)

        ### Create Menu Buttons ###
        self.menu_buttons = ButtonLayout(
            self.container_stack, self.central_widget, height=self.size().height()
        )

        # Populate content_v_layout
        self.content_v_layout.addWidget(self.infoBar)
        self.content_v_layout.addWidget(self.container_stack)
        self.content_v_layout.addWidget(self.buffer)

        # Populate content_h_layout
        self.content_h_layout.addWidget(self.menu_buttons)
        self.content_h_layout.addWidget(self.content_container)

        # self.container_stack.setCurrentWidget(self.container_stack.)

    def initConfigs(self):
        self.configs = {}
        self.configs["wf"] = loadConfig("wf")
        self.configs["sc"] = dict(
            [
                (k, dict([(int(kk), vv) for kk, vv in v.items()]))
                for k, v in loadConfig("sc").items()
            ]
        )

    def saveConfig(self):
        for i in self.configs.items():
            saveConfig(*i)

    def setScannerConfig(self, config):
        print("setScannerConfig")
        # return self.scanManager.loadConfig(config)

    def startScan(self, gui=True, modal=True):
        print("startScan")
        # return self.scanManager.acquire_images(ui=gui, modal=modal)

    def init_widgets(self):
        self.CW_workflow = WorkflowWidget()
        self.CW_account = AccountWidget()
        self.CW_scan = ScanWidget()
        self.CW_setting = SettingsWidget()

    def init_window(self):
        self.resize(1920, 1080)
        self.setStyleSheet("background:#1c1c1c")
        self.setWindowTitle("Scanner App")

    def closeEvent(self, event):
        self.saveConfig()
        return super().closeEvent()
