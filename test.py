# -*- coding: utf-8 -*-   
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
import sys  
  
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  
  
class MyQQ(QToolBox):  
    def __init__(self,parent=None):  
        super(MyQQ,self).__init__(parent)  
          
        toolButton1_1=QToolButton()  
        toolButton1_1.setText(self.tr("好友1"))  
        toolButton1_1.setIcon(QIcon("images/example_6/1.jpg"))  
        toolButton1_1.setIconSize(QSize(60,60))  
        toolButton1_1.setAutoRaise(True)  
        toolButton1_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton1_2=QToolButton()  
        toolButton1_2.setText(self.tr("好友2"))  
        toolButton1_2.setIcon(QIcon("images/example_6/2.jpg"))  
        toolButton1_2.setIconSize(QSize(60,60))  
        toolButton1_2.setAutoRaise(True)  
        toolButton1_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton1_3=QToolButton()  
        toolButton1_3.setText(self.tr("好友3"))  
        toolButton1_3.setIcon(QIcon("images/example_6/3.jpg"))  
        toolButton1_3.setIconSize(QSize(60,60))  
        toolButton1_3.setAutoRaise(True)  
        toolButton1_3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
  
        toolButton2_1=QToolButton()  
        toolButton2_1.setText(self.tr("家人1"))  
        toolButton2_1.setIcon(QIcon("images/example_6/4.jpg"))  
        toolButton2_1.setIconSize(QSize(60,60))  
        toolButton2_1.setAutoRaise(True)  
        toolButton2_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton2_2=QToolButton()  
        toolButton2_2.setText(self.tr("家人2"))  
        toolButton2_2.setIcon(QIcon("images/example_6/5.jpg"))  
        toolButton2_2.setIconSize(QSize(60,60))  
        toolButton2_2.setAutoRaise(True)  
        toolButton2_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton3_1=QToolButton()  
        toolButton3_1.setText(self.tr("黑名单1"))  
        toolButton3_1.setIcon(QIcon("images/example_6/4.jpg"))  
        toolButton3_1.setIconSize(QSize(60,60))  
        toolButton3_1.setAutoRaise(True)  
        toolButton3_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton3_2=QToolButton()  
        toolButton3_2.setText(self.tr("黑名单2"))  
        toolButton3_2.setIcon(QIcon("images/example_6/2.jpg"))  
        toolButton3_2.setIconSize(QSize(60,60))  
        toolButton3_2.setAutoRaise(True)  
        toolButton3_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        groupbox1=QGroupBox()  
        vlayout1=QVBoxLayout(groupbox1)  
        vlayout1.setMargin(10)  
        vlayout1.setAlignment(Qt.AlignCenter)  
        vlayout1.addWidget(toolButton1_1)  
        vlayout1.addWidget(toolButton1_2)  
        vlayout1.addWidget(toolButton1_3)  
        
        # 按钮之后插入一个占位符，使得所有按钮能靠上对齐。并且在整个抽屉大小发生改变时，保证按钮的大小不发生变化
        vlayout1.addStretch()
  
        groupbox2=QGroupBox()  
        vlayout2=QVBoxLayout(groupbox2)  
        vlayout2.setMargin(10)  
        vlayout2.setAlignment(Qt.AlignCenter)  
        vlayout2.addWidget(toolButton2_1)  
        vlayout2.addWidget(toolButton2_2)  
           
        groupbox3=QGroupBox()  
        vlayout3=QVBoxLayout(groupbox3)  
        vlayout3.setMargin(10)  
        vlayout3.setAlignment(Qt.AlignCenter)  
        vlayout3.addWidget(toolButton3_1)  
        vlayout3.addWidget(toolButton3_2)  
        
        # 将QGroupBox控件添加到QToolBox父类上
        self.addItem(groupbox1,self.tr("我的好友"))  
        self.addItem(groupbox2,self.tr("同事"))  
        self.addItem(groupbox3,self.tr("黑名单"))  
  
app=QApplication(sys.argv)  
myqq=MyQQ()  
myqq.setWindowTitle("My QQ")  
myqq.show()  
app.exec_()  