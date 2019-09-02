from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget,QApplication,QLCDNumber,QVBoxLayout,QMessageBox,QPushButton
import sys
import time

class MyTime(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init_timer()
        #UI界面搭建
    def update_time(self):
        self.lcd.display(time.strftime('%X', time.localtime()))

    def init_timer(self):
        self.timer=QTimer()
        self.timer.setInterval(1000)#设置定时器 1S触发一次
        self.timer.start()#启动定时器
        self.timer.timeout.connect(self.update_time)

    def  initUI(self):
        self.resize(400,200)
        self.setWindowTitle("创意时钟")
        self.setWindowIcon(QIcon('xiaomayun.jpg'))

        #初始化  调色板
        self.pl=QPalette()
        self.pl.setColor(QPalette.Background,Qt.darkYellow)
        self.setAutoFillBackground(True)
        self.setPalette(self.pl)#设置顶层布局

        self.lcd=QLCDNumber() #初始化lcd
        self.lcd.setDigitCount(10)#设置数字个数
        self.lcd.setMode(QLCDNumber.Dec)#数字十进制
        self.lcd.setSegmentStyle(QLCDNumber.Flat)#平面模式
        self.lcd.display(time.strftime('%X',time.localtime()))

        ##初始化盒子布局
        self.box_layout=QVBoxLayout()
        self.box_layout.addWidget(self.lcd)#添加LCD组件

        self.box_layout.setAlignment(Qt.AlignCenter)#设置组件在布局中间
        self.setLayout(self.box_layout)#设置窗体布局

        self.btn = QPushButton('Button', self)
        self.btn.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.on_click)
        self.box_layout.addWidget(self.btn)
        # btn.move(50, 50)

        self.qbtn = QPushButton('Quit', self)
        self.qbtn.clicked.connect(QCoreApplication.instance().quit)
        self.qbtn.resize(self.qbtn.sizeHint())
        self.qbtn.move(300, 150)

        self.show()


    """创建鼠标点击事件"""
    def on_click(self):
        print("PyQt5 button click")


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        # 第一个字符串的内容被显示在标题栏上。第二个字符串是对话框上显示的文本。第三个参数指定了显示在对话框上的按钮集合。最后一个参数是默认选中的按钮。
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app=QApplication(sys.argv)
    mt=MyTime()
    app.exec_()
