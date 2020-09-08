from PyQt5 import QtWidgets

def findMainWindow():
    # Global function to find the (open) QMainWindow in application
    app = QtWidgets.QApplication.instance()
    for widget in app.topLevelWidgets():
        if isinstance(widget, QtWidgets.QMainWindow):
            return widget
    return None
