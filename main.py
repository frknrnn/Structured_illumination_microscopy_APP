import sys
import platform
from PySide2 import  QtCore,QtGui,QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


import cv2
import numpy as np

from main_functions import MainWindow
from ui_splash_screen import Ui_SplashScreen
import time
import serial
from serial.tools import list_ports

counter = 0

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.splash_ui = Ui_SplashScreen()
        self.splash_ui.setupUi(self)
        ## REMOVE TİTLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ##DropShadowEffect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,60))
        self.splash_ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ###QTİMER
        #self.connectSerial()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        self.show()
        ####Function


    def progress(self):
        global counter
        self.splash_ui.progressBar_2.setValue(counter)
        if counter > 100:
            self.timer.stop()
            ###Show MainWindow
            self.close()
            self.main = MainWindow()
            self.main.show()
        counter+=1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())