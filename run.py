from PyQt5 import QtWidgets
from main_window import MainWindow
from parts.scan_widget import ScanWidget
import sys


def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = MainWindow()
    GUI.show()
    app.exec_()


def icon_run():
    from parts.workflow_widget import WorkflowWidget
    app = QtWidgets.QApplication([])
    GUI = ScanWidget()
    GUI.show()
    app.exec_()


if __name__ == "__main__":
    run()
    # icon_run()
