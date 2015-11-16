#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *

import sys

from constraint import Constraint
import common 
from tool_button import ToolButton

class ToolBar(QToolBar):
    """docstring for ToolBar"""
    def __init__(self, parent=None):
        super(ToolBar, self).__init__(parent)        
        # self.__container = parent
        # self.__settings = self.__container.settings


        # init ui
        self.initialize_ui()

    def initialize_ui(self):
        self.setObjectName("toolBar")

        self.setAllowedAreas(Qt.TopToolBarArea) # 停靠QToolBar顶部
        self.setFloatable(False)
        self.setMovable(False)

        self.setWindowTitle("%s toolBar" % Constraint.window_name)

        vision = QLabel()
        vision.setText(Constraint.version)
        vision.setToolTip(self.tr("Version"))

        self.__user_layouts=[]

        self.set_children_widgets()
        # logoLabel = self.getApplicationLogoLabel()

        self.resize(500, 300)
        # self.setGeometry(500,500, 600,400)
        self.show()

    def set_children_widgets(self):
        test = ToolButton(self,
                            "resouces/preferences.png",
                            "resouces/preferences_active.png",
                            "resouces/preferences_hover.png")

        self.addWidget(test)
        # self.setIconSize(QSize(UiConstants.defaultToolbarIconSize, UiConstants.defaultToolbarIconSize))
        self.setIconSize(test.size())
        
    def keyPressEvent(self, event):
        '''This method reimplements the "QWidget.keyPressEvent" method
        '''
        key = event.key()
        if key == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = common.get_application_instance()

    win = ToolBar()
    for widget in QApplication.allWidgets():
        if widget.objectName() == win:
            widget.close()
            
    win.show()
    sys.exit(app.exec_())