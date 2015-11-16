#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *

import sys

import common
from constraint import Constraint

__all__ = ["PipelineTools"]


class PipelineTools(QMainWindow):
    """docstring for PipelineTools"""
    
    def __init__(self, parent=None):
        super(PipelineTools, self).__init__(parent)
        self.main_ui()

    def main_ui(self):
        self.setObjectName(Constraint.app_name)
        self.resize(600, 400)

        menu = self.menuBar()
        file = menu.addMenu("file")
        file.addAction(u"菜单A")
        file.addSeparator()
        file.addAction(u"菜单B")
        
        self.setWindowTitle(Constraint.window_name)  
        te=QTextEdit(self.tr(u"主窗口"))  
        # te.setAlignment(Qt.AlignCenter)  
        self.setCentralWidget(te)  
        
        # # add QToolBar
        # self.tool_bar = ToolBar()
        # self.addToolBar(self.tool_bar)

        # # Setting processing widget.
        # self.Application_Progress_Status_processing = Processing(self, Qt.Window)
        # self.statusBar.addPermanentWidget(self.Application_Progress_Status_processing)
        # self.Application_Progress_Status_processing.hide()
        self.statusBar().showMessage("this is status!") # statusBar() 创建，showMessage()显示
    
        self.set_center()
        self.show()

    def initialize_ui(self):
        '''创建各个控件
        '''
        pass

    def set_style(self):
        pass

    def set_shortcut(self):
        '''set shortcut
        '''
        self.exit = QAction(QIcon('icons/exit.png'), 'Exit', self)
        self.exit.setShortcut('Ctrl+q')
        self.exit.setStatusTip('Exit application')
        self.exit.connect(self.exit, SIGNAL('triggered()'), qApp, SLOT('quit()'))

        self.exit_bar = self.addToolBar("Exit Test")
        self.exit_bar.addAction(self.exit)

    def set_center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()

        self.move((screen.width() - size.width())/2,
                   (screen.height() - size.height())/2)

    def keyPressEvent(self, event):
        '''This method reimplements the "QWidget.keyPressEvent" method
        '''
        key = event.key()
        if key == Qt.Key_Escape:
            self.close()

    def closeEvent(self, event):
        '''可存储界面布局及位置等信息storeStartupLayout
        '''
        pass

# test 
if __name__ == '__main__':
    app = common.get_application_instance()

    win = PipelineTools()
    for widget in QApplication.allWidgets():
        if widget.objectName() == win:
            widget.close()
            
    win.show()
    sys.exit(app.exec_())