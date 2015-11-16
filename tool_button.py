#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *

import sys

from constraint import Constraint
import common 

class ToolButton(QToolButton):
    """docstring for QToolButton"""
    def __init__(self,
                parent=None,
                default_pixmap=None,
                hover_pixmap=None,
                active_pixmap=None,
                size=None,
                label=None,
                label_color=None):

        super(ToolButton, self).__init__(parent)     

        # setting class attribtes
        self.__default_pixmap = default_pixmap or QPixmap()
        self.__hover_pixmap = hover_pixmap or QPixmap()
        self.__active_pixmap = active_pixmap or QPixmap()

        self.__size = 500
        self.__label = label
        self.__label_color = label_color
        self.__label_color = QColor(250, 30, 30)

        self.__checkable = False
        self.__checked = True

        # user args
        self.__menu = None

        # init
        if self.__checked:
            self.set_icons(self.__active_pixmap)
        else:
            self.set_icons(self.__default_pixmap)


    def set_menu(self, menu):
        '''this method sets the widget menu
        '''
        self.__menu = menu

    def set_icons(self, pixmap):
        # 设置图标
        pixmap = QPixmap(QImage(pixmap))
        # pixmap = pixmap.scaled(self.__size, self.__size, Qt.IgnoreAspectRatio)
        # pixmap = pixmap.scaled(self.__size, self.__size, Qt.KeepAspectRatio, Qt.FastTransformation)

        iconPixmap = QIcon(pixmap)

        #设置图片及大小
        self.setIcon(iconPixmap)
        self.setIconSize(pixmap.size())
        # self.setIconSize(QSize(self.__size, self.__size))


        # # 匹配大小
        # self.setFixedSize(pixmap.size())
        self.setAutoRaise(True)

        #设置文本颜色
        text_palette = self.palette()
        text_palette.setColor(QPalette.ButtonText, self.__label_color)
        self.setPalette(text_palette)

        # # 设置文本粗体
        text_font = self.font()
        text_font.setWeight(QFont.Bold)

        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.setText(self.__label)

    def paintEvent(self, event):
        if self.underMouse():
            self.painterInfo(0,0,0)
        else:
            self.painterInfo(0,0,0)
        QToolButton.paintEvent(self, event)
    


    def painterInfo(self, topColor, middleColor, bottomColor):
        painter = QPainter(self)
        #Qpen是图标外侧的线框
        #pen = QPen(QColor(192, 192, 192))
        painter.setPen(Qt.NoPen)
        # painter.setRenderHint(QPainter.SmoothPixmapTransform)
        # painter.setRenderHint(QPainter.Antialiasing)

        linear = QLinearGradient(self.rect().topLeft(), self.rect().bottomLeft())

        linear.setColorAt(0, QColor(250, 250, 250, topColor))
        linear.setColorAt(0.5, QColor(160, 160, 160, middleColor))
        linear.setColorAt(1, QColor(0, 0, 0, bottomColor))

        painter.setBrush(linear)
        painter.drawRect(self.rect())
        painter.setRenderHint(painter.Antialiasing)


        text="GGGG"
        pointX = painter.fontMetrics().width(text) / 2
        pointY = pointX / 2
        painter.drawText(pointX, pointY, text)

    def enterEvent(self, event):
        if self.__checkable:
            not self.__checked and self.set_icons(self.__hover_pixmap)
        else:
            self.set_icons(self.__hover_pixmap)

    def leaveEvent(self, event):
        if self.__checkable:
            not self.__checked and self.set_icons(self.__default_pixmap)
        else:
            self.set_icons(self.__default_pixmap)

    def mousePressEvent(self, event):
        self.set_icons(self.__active_pixmap)
        self.__menu and self.__menu.exec_(QCursor.pos())
        self.pressed.emit()

    def mouseReleaseEvent(self, event):
        if self.underMouse():
            if self.__checkable:
                self.setChecked(not self.__checked)
            else:
                self.set_icons(self.__active_pixmap)
        else:
            self.set_icons(self.__default_pixmap)
        self.released.emit()
        self.clicked.emit()


if __name__ == '__main__':
    app = common.get_application_instance()

    # win = ToolBar()
    win = QWidget()
    layout = QHBoxLayout()
    win.setLayout(layout)

    for widget in QApplication.allWidgets():
        if widget.objectName() == win:
            widget.close()
    a = ToolButton(win,
                    "resouces/preferences.png",
                    "resouces/preferences_active.png",
                    "resouces/preferences_hover.png",
                    label = "test label")

    layout.addWidget(a)
    win.show()
    sys.exit(app.exec_())
