
# -*- coding: utf-8 -*-
import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QCheckBox, QRadioButton)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"窗口6")
        MainWindow.resize(400, 360)
        MainWindow.setWindowTitle(u"窗口6")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.复选框1 = QCheckBox(self.centralwidget)
        self.复选框1.setObjectName(u"复选框1")
        self.复选框1.setGeometry(QRect(128, 122, 125, 63))
        self.复选框1.setText("复选框1")
        self.单选框1 = QRadioButton(self.centralwidget)
        self.单选框1.setObjectName(u"单选框1")
        self.单选框1.setGeometry(QRect(307, 106, 84, 84))
        self.单选框1.setText("单选框1")
        MainWindow.setCentralWidget(self.centralwidget)
        QMetaObject.connectSlotsByName(MainWindow)

class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    sys.exit(app.exec())
