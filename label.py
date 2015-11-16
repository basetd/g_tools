#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *

import sys

from constraint import Constraint
import common 

class Label(QLabel):
    """docstring for Label"""
    def __init__(self,
    			parent=None,
    			default_pixmap,
    			hover_pixmap,
    			active_pixmap):
        super(Label, self).__init__(parent)     

        # setting class attribtes
        self.default_pixmap = default_pixmap or QPixmap()
        self.hover_pixmap = hover_pixmap or QPixmap()
        self.active_pixmap = active_pixmap or QPixmap()

        # user args
        self.menu = None

    def set_menu(self, menu):
    	'''this method sets the widget menu
    	'''
    	self.__menu = menu

	def enterEvent(self, event):
		if self.__checkable:
			not self.__checked and self.setPixmap(self.__hoverPixmap)
		else:
			self.setPixmap(self.__hoverPixmap)

	def leaveEvent(self, event):
		if self.__checkable:
			not self.__checked and self.setPixmap(self.__defaultPixmap)
		else:
			self.setPixmap(self.__defaultPixmap)

	def mousePressEvent(self, event):
		self.setPixmap(self.__activePixmap)
		self.__menu and self.__menu.exec_(QCursor.pos())
		self.pressed.emit()

	def mouseReleaseEvent(self, event):
		if self.underMouse():
			if self.__checkable:
				self.setChecked(not self.__checked)
			else:
				self.setPixmap(self.__activePixmap)
		else:
			self.setPixmap(self.__defaultPixmap)
		self.released.emit()
		self.clicked.emit()

if __name__ == '__main__':
    app = common.get_application_instance()

    win = ToolBar()
    for widget in QApplication.allWidgets():
        if widget.objectName() == win:
            widget.close()
            
    win.show()
    sys.exit(app.exec_())