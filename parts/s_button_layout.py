from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from parts.s_button import MenuButton
from utils import findMainWindow


class ButtonLayout(QtWidgets.QWidget):
    def __init__(self, cl, parent=None, height=0, flags=QtCore.Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.setSizePolicy(QtWidgets.QSizePolicy.Maximum,
                           QtWidgets.QSizePolicy.Expanding)
        # Create vertical Layout
        self.setGeometry(
            QtCore.QRect(0, 0, 200, height))
        self.setStyleSheet("background:#1c1c1c")
        self.setObjectName("verticalLayoutWidget")
        self.v_layout = QtWidgets.QVBoxLayout(self)
        self.v_layout.setContentsMargins(0, 0, 10, 0)
        self.v_layout.setSpacing(70)
        self.v_layout.setObjectName("verticalLayout")

        ii = [('user.svg', 'pb_Account', 'cw_account'),
                ('workflow.svg', 'pb_Workflow', 'cw_workflow'),
                ('menu.svg', 'pb_Scan', 'cw_scan'),
                ('gear-option.svg', 'pb_Settings', 'cw_settings')
            ]

        cc = [c.objectName() for c in cl.children()]
        for im, on, cn in ii:
            self.v_layout.addWidget(MenuButton(im, \
                    clicked=lambda _: \
                    findMainWindow().container_stack.setCurrentIndex(cc.index(cn)), \
                    objectName=on, parent=self))


        self.v_layout.addWidget(MenuButton('off.svg', \
                clicked=lambda _: QtCore.QCoreApplication.instance().quit(), \
                objectName='pb_Quit', parent=self))

    def sizeHint(self):
        return QtCore.QSize(180, 0)
