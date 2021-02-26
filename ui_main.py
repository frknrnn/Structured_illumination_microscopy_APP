# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainkfYGFJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from zoom import QtImageViewer
import floresans_icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1499, 941)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"background-color: rgb(49, 51, 50);")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_titleBar = QFrame(self.drop_shadow_frame)
        self.frame_titleBar.setObjectName(u"frame_titleBar")
        self.frame_titleBar.setMinimumSize(QSize(0, 40))
        self.frame_titleBar.setMaximumSize(QSize(16777215, 40))
        self.frame_titleBar.setFrameShape(QFrame.NoFrame)
        self.frame_titleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_titleBar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_titleBar)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(250, 40))
        self.frame_4.setStyleSheet(u"background-image: url(:/floresansPrefix/nanaFluor_pageLogo.png);")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_5 = QFrame(self.frame_titleBar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setSpacing(30)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 10, 0)
        self.pushButton_minimized = QPushButton(self.frame_11)
        self.pushButton_minimized.setObjectName(u"pushButton_minimized")
        self.pushButton_minimized.setMinimumSize(QSize(20, 20))
        self.pushButton_minimized.setMaximumSize(QSize(20, 20))
        self.pushButton_minimized.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_minimized.setAutoFillBackground(False)
        self.pushButton_minimized.setStyleSheet(u"QPushButton{\n"
"    border:none;\n"
"	image: url(:/floresansPrefix/minimizeButtonIcon.png);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255,150);\n"
"}")
        self.pushButton_minimized.setAutoRepeat(False)
        self.pushButton_minimized.setAutoExclusive(False)
        self.pushButton_minimized.setAutoDefault(False)
        self.pushButton_minimized.setFlat(False)

        self.horizontalLayout_7.addWidget(self.pushButton_minimized, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.pushButton_close = QPushButton(self.frame_11)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setMinimumSize(QSize(20, 20))
        self.pushButton_close.setMaximumSize(QSize(20, 20))
        self.pushButton_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_close.setAutoFillBackground(False)
        self.pushButton_close.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/floresansPrefix/closeButtonIcon.png);\n"
"border:none;\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255,150);\n"
"}")
        self.pushButton_close.setAutoRepeat(False)
        self.pushButton_close.setAutoExclusive(False)
        self.pushButton_close.setAutoDefault(False)
        self.pushButton_close.setFlat(False)

        self.horizontalLayout_7.addWidget(self.pushButton_close, 0, Qt.AlignRight)


        self.horizontalLayout_6.addWidget(self.frame_11, 0, Qt.AlignRight)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_titleBar)

        self.frame_3 = QFrame(self.drop_shadow_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_main = QStackedWidget(self.frame_3)
        self.stackedWidget_main.setObjectName(u"stackedWidget_main")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_4 = QHBoxLayout(self.page)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(250, 0))
        self.frame_7.setMaximumSize(QSize(250, 16777215))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_leftSide = QStackedWidget(self.frame_7)
        self.stackedWidget_leftSide.setObjectName(u"stackedWidget_leftSide")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.horizontalLayout_10 = QHBoxLayout(self.page_5)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 5, 0, 0)
        self.frame_14 = QFrame(self.page_5)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_14)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 50))
        self.frame_16.setMaximumSize(QSize(16777215, 50))
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_20 = QFrame(self.frame_16)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.pushButton_home = QPushButton(self.frame_20)
        self.pushButton_home.setObjectName(u"pushButton_home")
        self.pushButton_home.setGeometry(QRect(40, 0, 150, 30))
        self.pushButton_home.setMinimumSize(QSize(150, 30))
        self.pushButton_home.setMaximumSize(QSize(30, 16777215))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_home.setFont(font)
        self.pushButton_home.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_11.addWidget(self.frame_20)


        self.verticalLayout_4.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 200))
        self.frame_17.setMaximumSize(QSize(16777215, 200))
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_17)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_23 = QFrame(self.frame_17)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_24)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 171, 51))
        self.label_3.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(60, 0))
        self.frame_25.setMaximumSize(QSize(60, 16777215))
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_25)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_coarse = QPushButton(self.frame_25)
        self.pushButton_coarse.setObjectName(u"pushButton_coarse")
        self.pushButton_coarse.setMinimumSize(QSize(25, 25))
        self.pushButton_coarse.setMaximumSize(QSize(25, 25))
        self.pushButton_coarse.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/floresansPrefix/whitePressed.png);\n"
"border:none;\n"
"}")

        self.verticalLayout_6.addWidget(self.pushButton_coarse, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_12.addWidget(self.frame_25)


        self.verticalLayout_5.addWidget(self.frame_23)

        self.frame_22 = QFrame(self.frame_17)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_22)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_26)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 6, 171, 41))
        self.label_2.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_22)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMaximumSize(QSize(60, 16777215))
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_30 = QFrame(self.frame_27)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.pushButton_fine = QPushButton(self.frame_30)
        self.pushButton_fine.setObjectName(u"pushButton_fine")
        self.pushButton_fine.setMinimumSize(QSize(25, 25))
        self.pushButton_fine.setMaximumSize(QSize(25, 25))
        self.pushButton_fine.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
"border:none;\n"
"}")

        self.horizontalLayout_17.addWidget(self.pushButton_fine)


        self.horizontalLayout_16.addWidget(self.frame_30, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_14.addWidget(self.frame_27)


        self.verticalLayout_5.addWidget(self.frame_22)

        self.frame_21 = QFrame(self.frame_17)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_29 = QFrame(self.frame_21)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_29)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 0, 171, 51))
        self.label_4.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.frame_29)

        self.frame_28 = QFrame(self.frame_21)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(60, 16777215))
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.frame_31 = QFrame(self.frame_28)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.pushButton_stepMode = QPushButton(self.frame_31)
        self.pushButton_stepMode.setObjectName(u"pushButton_stepMode")
        self.pushButton_stepMode.setMinimumSize(QSize(25, 25))
        self.pushButton_stepMode.setMaximumSize(QSize(25, 25))
        self.pushButton_stepMode.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
"border:none;\n"
"}")

        self.horizontalLayout_18.addWidget(self.pushButton_stepMode)


        self.horizontalLayout_19.addWidget(self.frame_31, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_15.addWidget(self.frame_28)


        self.verticalLayout_5.addWidget(self.frame_21)


        self.verticalLayout_4.addWidget(self.frame_17)

        self.frame_19 = QFrame(self.frame_14)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_19)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_38 = QFrame(self.frame_19)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setMinimumSize(QSize(0, 200))
        self.frame_38.setMaximumSize(QSize(16777215, 200))
        self.frame_38.setFrameShape(QFrame.NoFrame)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_38)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_18 = QFrame(self.frame_38)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.pushButton_Z_up = QPushButton(self.frame_18)
        self.pushButton_Z_up.setObjectName(u"pushButton_Z_up")
        self.pushButton_Z_up.setGeometry(QRect(170, 20, 45, 41))
        self.pushButton_Z_up.setMinimumSize(QSize(45, 41))
        self.pushButton_Z_up.setMaximumSize(QSize(45, 41))
        self.pushButton_Z_up.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	\n"
"	background-image: url(:/floresansPrefix/upBtn.png);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255,150);\n"
"}")
        self.pushButton_Z_down = QPushButton(self.frame_18)
        self.pushButton_Z_down.setObjectName(u"pushButton_Z_down")
        self.pushButton_Z_down.setGeometry(QRect(170, 120, 45, 41))
        self.pushButton_Z_down.setMinimumSize(QSize(45, 41))
        self.pushButton_Z_down.setMaximumSize(QSize(45, 41))
        self.pushButton_Z_down.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	image: url(:/floresansPrefix/downBtn.png);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255,150);\n"
"}")
        self.pushButton_Y_up = QPushButton(self.frame_18)
        self.pushButton_Y_up.setObjectName(u"pushButton_Y_up")
        self.pushButton_Y_up.setGeometry(QRect(50, 20, 45, 41))
        self.pushButton_Y_up.setMinimumSize(QSize(45, 41))
        self.pushButton_Y_up.setMaximumSize(QSize(45, 41))
        self.pushButton_Y_up.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	\n"
"	background-image: url(:/floresansPrefix/upBtn.png);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255,150);\n"
"}")
        self.pushButton_Y_down = QPushButton(self.frame_18)
        self.pushButton_Y_down.setObjectName(u"pushButton_Y_down")
        self.pushButton_Y_down.setGeometry(QRect(50, 120, 45, 41))
        self.pushButton_Y_down.setMinimumSize(QSize(45, 41))
        self.pushButton_Y_down.setMaximumSize(QSize(45, 41))
        self.pushButton_Y_down.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	image: url(:/floresansPrefix/downBtn.png);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255,150);\n"
"}")
        self.pushButton_X_left = QPushButton(self.frame_18)
        self.pushButton_X_left.setObjectName(u"pushButton_X_left")
        self.pushButton_X_left.setGeometry(QRect(0, 70, 45, 41))
        self.pushButton_X_left.setMinimumSize(QSize(45, 41))
        self.pushButton_X_left.setMaximumSize(QSize(45, 41))
        self.pushButton_X_left.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	image: url(:/floresansPrefix/leftBtn.png);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255,150);\n"
"}")
        self.pushButton_X_right = QPushButton(self.frame_18)
        self.pushButton_X_right.setObjectName(u"pushButton_X_right")
        self.pushButton_X_right.setGeometry(QRect(100, 70, 45, 41))
        self.pushButton_X_right.setMinimumSize(QSize(45, 41))
        self.pushButton_X_right.setMaximumSize(QSize(45, 41))
        self.pushButton_X_right.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	image: url(:/floresansPrefix/rightBtn.png);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255,150);\n"
"}")

        self.verticalLayout_10.addWidget(self.frame_18)


        self.verticalLayout_9.addWidget(self.frame_38)

        self.frame_37 = QFrame(self.frame_19)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.NoFrame)
        self.frame_37.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame_37)


        self.verticalLayout_4.addWidget(self.frame_19)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 300))
        self.frame_15.setMaximumSize(QSize(16777215, 300))
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_15)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.frame_33 = QFrame(self.frame_15)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_33)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_34 = QFrame(self.frame_33)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.NoFrame)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_9 = QLabel(self.frame_34)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 75 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_20.addWidget(self.label_9)

        self.lineEdit_X_position = QLineEdit(self.frame_34)
        self.lineEdit_X_position.setObjectName(u"lineEdit_X_position")
        self.lineEdit_X_position.setMinimumSize(QSize(150, 30))
        self.lineEdit_X_position.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_X_position.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_X_position.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 3px;\n"
"border-style:inset;")
        self.lineEdit_X_position.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.lineEdit_X_position)


        self.verticalLayout_8.addWidget(self.frame_34)

        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_7 = QLabel(self.frame_35)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 75 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_21.addWidget(self.label_7)

        self.lineEdit_Y_position = QLineEdit(self.frame_35)
        self.lineEdit_Y_position.setObjectName(u"lineEdit_Y_position")
        self.lineEdit_Y_position.setMinimumSize(QSize(150, 30))
        self.lineEdit_Y_position.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_Y_position.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 3px;\n"
"border-style:inset;")
        self.lineEdit_Y_position.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.lineEdit_Y_position)


        self.verticalLayout_8.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_33)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.NoFrame)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_8 = QLabel(self.frame_36)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 75 18pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_22.addWidget(self.label_8)

        self.lineEdit_Z_position = QLineEdit(self.frame_36)
        self.lineEdit_Z_position.setObjectName(u"lineEdit_Z_position")
        self.lineEdit_Z_position.setMinimumSize(QSize(150, 30))
        self.lineEdit_Z_position.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_Z_position.setStyleSheet(u"font: 75 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 3px;\n"
"border-style:inset;")
        self.lineEdit_Z_position.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.lineEdit_Z_position)


        self.verticalLayout_8.addWidget(self.frame_36)


        self.verticalLayout_7.addWidget(self.frame_33)

        self.frame_32 = QFrame(self.frame_15)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 50))
        self.frame_32.setMaximumSize(QSize(16777215, 50))
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.pushButton_goAbsulutePosition = QPushButton(self.frame_32)
        self.pushButton_goAbsulutePosition.setObjectName(u"pushButton_goAbsulutePosition")
        self.pushButton_goAbsulutePosition.setGeometry(QRect(40, 10, 150, 30))
        self.pushButton_goAbsulutePosition.setMinimumSize(QSize(150, 30))
        self.pushButton_goAbsulutePosition.setMaximumSize(QSize(30, 16777215))
        self.pushButton_goAbsulutePosition.setFont(font)
        self.pushButton_goAbsulutePosition.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.verticalLayout_7.addWidget(self.frame_32)


        self.verticalLayout_4.addWidget(self.frame_15)


        self.horizontalLayout_10.addWidget(self.frame_14)

        self.stackedWidget_leftSide.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_53 = QVBoxLayout(self.page_6)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.frame_77 = QFrame(self.page_6)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.NoFrame)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_77)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.frame_80 = QFrame(self.frame_77)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.NoFrame)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_80)
        self.verticalLayout_55.setSpacing(0)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_126 = QFrame(self.frame_80)
        self.frame_126.setObjectName(u"frame_126")
        self.frame_126.setFrameShape(QFrame.NoFrame)
        self.frame_126.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_126)
        self.horizontalLayout_58.setSpacing(0)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_149 = QFrame(self.frame_126)
        self.frame_149.setObjectName(u"frame_149")
        self.frame_149.setFrameShape(QFrame.NoFrame)
        self.frame_149.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_66 = QHBoxLayout(self.frame_149)
        self.horizontalLayout_66.setSpacing(0)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalLayout_66.setContentsMargins(0, 0, 0, 0)
        self.result_left_picturebox1 = QLabel(self.frame_149)
        self.result_left_picturebox1.setObjectName(u"result_left_picturebox1")

        self.horizontalLayout_66.addWidget(self.result_left_picturebox1)


        self.horizontalLayout_58.addWidget(self.frame_149)

        self.frame_150 = QFrame(self.frame_126)
        self.frame_150.setObjectName(u"frame_150")
        self.frame_150.setMinimumSize(QSize(30, 0))
        self.frame_150.setMaximumSize(QSize(30, 16777215))
        self.frame_150.setFrameShape(QFrame.NoFrame)
        self.frame_150.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_59 = QHBoxLayout(self.frame_150)
        self.horizontalLayout_59.setSpacing(0)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.pushButton_color_1 = QPushButton(self.frame_150)
        self.pushButton_color_1.setObjectName(u"pushButton_color_1")
        self.pushButton_color_1.setMinimumSize(QSize(23, 23))
        self.pushButton_color_1.setMaximumSize(QSize(23, 23))
        self.pushButton_color_1.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"\n"
"	background-image: url(:/floresansPrefix/redUnPressed.png);\n"
"}")

        self.horizontalLayout_59.addWidget(self.pushButton_color_1)


        self.horizontalLayout_58.addWidget(self.frame_150)


        self.verticalLayout_55.addWidget(self.frame_126)

        self.frame_127 = QFrame(self.frame_80)
        self.frame_127.setObjectName(u"frame_127")
        self.frame_127.setMinimumSize(QSize(0, 15))
        self.frame_127.setMaximumSize(QSize(16777215, 15))
        self.frame_127.setFrameShape(QFrame.NoFrame)
        self.frame_127.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frame_127)
        self.horizontalLayout_67.setSpacing(0)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.horizontalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.horizontalSlider_result_1 = QSlider(self.frame_127)
        self.horizontalSlider_result_1.setObjectName(u"horizontalSlider_result_1")
        self.horizontalSlider_result_1.setStyleSheet(u"QSlider{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"	border-radius:3px;\n"
"    }")
        self.horizontalSlider_result_1.setMaximum(99)
        self.horizontalSlider_result_1.setPageStep(1)
        self.horizontalSlider_result_1.setValue(25)
        self.horizontalSlider_result_1.setOrientation(Qt.Horizontal)

        self.horizontalLayout_67.addWidget(self.horizontalSlider_result_1)


        self.verticalLayout_55.addWidget(self.frame_127)


        self.verticalLayout_54.addWidget(self.frame_80)

        self.frame_133 = QFrame(self.frame_77)
        self.frame_133.setObjectName(u"frame_133")
        self.frame_133.setFrameShape(QFrame.NoFrame)
        self.frame_133.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_133)
        self.verticalLayout_56.setSpacing(0)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.frame_134 = QFrame(self.frame_133)
        self.frame_134.setObjectName(u"frame_134")
        self.frame_134.setFrameShape(QFrame.NoFrame)
        self.frame_134.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frame_134)
        self.horizontalLayout_69.setSpacing(0)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.horizontalLayout_69.setContentsMargins(0, 0, 0, 0)
        self.frame_152 = QFrame(self.frame_134)
        self.frame_152.setObjectName(u"frame_152")
        self.frame_152.setFrameShape(QFrame.NoFrame)
        self.frame_152.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_70 = QHBoxLayout(self.frame_152)
        self.horizontalLayout_70.setSpacing(0)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.horizontalLayout_70.setContentsMargins(0, 0, 0, 0)
        self.result_left_picturebox2 = QLabel(self.frame_152)
        self.result_left_picturebox2.setObjectName(u"result_left_picturebox2")

        self.horizontalLayout_70.addWidget(self.result_left_picturebox2)


        self.horizontalLayout_69.addWidget(self.frame_152)

        self.frame_153 = QFrame(self.frame_134)
        self.frame_153.setObjectName(u"frame_153")
        self.frame_153.setMinimumSize(QSize(30, 0))
        self.frame_153.setMaximumSize(QSize(30, 16777215))
        self.frame_153.setFrameShape(QFrame.NoFrame)
        self.frame_153.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_77 = QHBoxLayout(self.frame_153)
        self.horizontalLayout_77.setSpacing(0)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.pushButton_color_2 = QPushButton(self.frame_153)
        self.pushButton_color_2.setObjectName(u"pushButton_color_2")
        self.pushButton_color_2.setMinimumSize(QSize(23, 23))
        self.pushButton_color_2.setMaximumSize(QSize(23, 23))
        self.pushButton_color_2.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"\n"
"	background-image: url(:/floresansPrefix/redUnPressed.png);\n"
"}")

        self.horizontalLayout_77.addWidget(self.pushButton_color_2)


        self.horizontalLayout_69.addWidget(self.frame_153)


        self.verticalLayout_56.addWidget(self.frame_134)

        self.frame_154 = QFrame(self.frame_133)
        self.frame_154.setObjectName(u"frame_154")
        self.frame_154.setMinimumSize(QSize(0, 15))
        self.frame_154.setMaximumSize(QSize(16777215, 15))
        self.frame_154.setFrameShape(QFrame.NoFrame)
        self.frame_154.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_154)
        self.horizontalLayout_78.setSpacing(0)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.horizontalSlider_result_2 = QSlider(self.frame_154)
        self.horizontalSlider_result_2.setObjectName(u"horizontalSlider_result_2")
        self.horizontalSlider_result_2.setStyleSheet(u"QSlider{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"	border-radius:3px;\n"
"    }")
        self.horizontalSlider_result_2.setMaximum(99)
        self.horizontalSlider_result_2.setPageStep(1)
        self.horizontalSlider_result_2.setValue(25)
        self.horizontalSlider_result_2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_78.addWidget(self.horizontalSlider_result_2)


        self.verticalLayout_56.addWidget(self.frame_154)


        self.verticalLayout_54.addWidget(self.frame_133)

        self.frame_174 = QFrame(self.frame_77)
        self.frame_174.setObjectName(u"frame_174")
        self.frame_174.setFrameShape(QFrame.NoFrame)
        self.frame_174.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_174)
        self.verticalLayout_60.setSpacing(0)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(0, 0, 0, 0)
        self.frame_175 = QFrame(self.frame_174)
        self.frame_175.setObjectName(u"frame_175")
        self.frame_175.setFrameShape(QFrame.NoFrame)
        self.frame_175.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_175)
        self.horizontalLayout_91.setSpacing(0)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.frame_176 = QFrame(self.frame_175)
        self.frame_176.setObjectName(u"frame_176")
        self.frame_176.setFrameShape(QFrame.NoFrame)
        self.frame_176.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_176)
        self.horizontalLayout_92.setSpacing(0)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.result_left_picturebox3 = QLabel(self.frame_176)
        self.result_left_picturebox3.setObjectName(u"result_left_picturebox3")

        self.horizontalLayout_92.addWidget(self.result_left_picturebox3)


        self.horizontalLayout_91.addWidget(self.frame_176)

        self.frame_177 = QFrame(self.frame_175)
        self.frame_177.setObjectName(u"frame_177")
        self.frame_177.setMinimumSize(QSize(30, 0))
        self.frame_177.setMaximumSize(QSize(30, 16777215))
        self.frame_177.setFrameShape(QFrame.NoFrame)
        self.frame_177.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_177)
        self.horizontalLayout_93.setSpacing(0)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.pushButton_color_3 = QPushButton(self.frame_177)
        self.pushButton_color_3.setObjectName(u"pushButton_color_3")
        self.pushButton_color_3.setMinimumSize(QSize(23, 23))
        self.pushButton_color_3.setMaximumSize(QSize(23, 23))
        self.pushButton_color_3.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"\n"
"	background-image: url(:/floresansPrefix/redUnPressed.png);\n"
"}")

        self.horizontalLayout_93.addWidget(self.pushButton_color_3)


        self.horizontalLayout_91.addWidget(self.frame_177)


        self.verticalLayout_60.addWidget(self.frame_175)

        self.frame_178 = QFrame(self.frame_174)
        self.frame_178.setObjectName(u"frame_178")
        self.frame_178.setMinimumSize(QSize(0, 15))
        self.frame_178.setMaximumSize(QSize(16777215, 15))
        self.frame_178.setFrameShape(QFrame.NoFrame)
        self.frame_178.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_178)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.horizontalSlider_result_3 = QSlider(self.frame_178)
        self.horizontalSlider_result_3.setObjectName(u"horizontalSlider_result_3")
        self.horizontalSlider_result_3.setStyleSheet(u"QSlider{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"	border-radius:3px;\n"
"    }")
        self.horizontalSlider_result_3.setMaximum(99)
        self.horizontalSlider_result_3.setPageStep(1)
        self.horizontalSlider_result_3.setValue(25)
        self.horizontalSlider_result_3.setOrientation(Qt.Horizontal)

        self.horizontalLayout_94.addWidget(self.horizontalSlider_result_3)


        self.verticalLayout_60.addWidget(self.frame_178)


        self.verticalLayout_54.addWidget(self.frame_174)

        self.frame_159 = QFrame(self.frame_77)
        self.frame_159.setObjectName(u"frame_159")
        self.frame_159.setFrameShape(QFrame.NoFrame)
        self.frame_159.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_159)
        self.verticalLayout_57.setSpacing(0)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_160 = QFrame(self.frame_159)
        self.frame_160.setObjectName(u"frame_160")
        self.frame_160.setFrameShape(QFrame.NoFrame)
        self.frame_160.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_160)
        self.horizontalLayout_79.setSpacing(0)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalLayout_79.setContentsMargins(0, 0, 0, 0)
        self.frame_161 = QFrame(self.frame_160)
        self.frame_161.setObjectName(u"frame_161")
        self.frame_161.setFrameShape(QFrame.NoFrame)
        self.frame_161.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_161)
        self.horizontalLayout_80.setSpacing(0)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalLayout_80.setContentsMargins(0, 0, 0, 0)
        self.result_left_picturebox4 = QLabel(self.frame_161)
        self.result_left_picturebox4.setObjectName(u"result_left_picturebox4")

        self.horizontalLayout_80.addWidget(self.result_left_picturebox4)


        self.horizontalLayout_79.addWidget(self.frame_161)

        self.frame_162 = QFrame(self.frame_160)
        self.frame_162.setObjectName(u"frame_162")
        self.frame_162.setMinimumSize(QSize(30, 0))
        self.frame_162.setMaximumSize(QSize(30, 16777215))
        self.frame_162.setFrameShape(QFrame.NoFrame)
        self.frame_162.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_162)
        self.horizontalLayout_81.setSpacing(0)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.pushButton_color_4 = QPushButton(self.frame_162)
        self.pushButton_color_4.setObjectName(u"pushButton_color_4")
        self.pushButton_color_4.setMinimumSize(QSize(23, 23))
        self.pushButton_color_4.setMaximumSize(QSize(23, 23))
        self.pushButton_color_4.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"\n"
"	background-image: url(:/floresansPrefix/redUnPressed.png);\n"
"}")

        self.horizontalLayout_81.addWidget(self.pushButton_color_4)


        self.horizontalLayout_79.addWidget(self.frame_162)


        self.verticalLayout_57.addWidget(self.frame_160)

        self.frame_163 = QFrame(self.frame_159)
        self.frame_163.setObjectName(u"frame_163")
        self.frame_163.setMinimumSize(QSize(0, 15))
        self.frame_163.setMaximumSize(QSize(16777215, 15))
        self.frame_163.setFrameShape(QFrame.NoFrame)
        self.frame_163.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_163)
        self.horizontalLayout_82.setSpacing(0)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.horizontalSlider_result_4 = QSlider(self.frame_163)
        self.horizontalSlider_result_4.setObjectName(u"horizontalSlider_result_4")
        self.horizontalSlider_result_4.setStyleSheet(u"QSlider{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"	border-radius:3px;\n"
"    }")
        self.horizontalSlider_result_4.setMaximum(99)
        self.horizontalSlider_result_4.setPageStep(1)
        self.horizontalSlider_result_4.setValue(25)
        self.horizontalSlider_result_4.setOrientation(Qt.Horizontal)

        self.horizontalLayout_82.addWidget(self.horizontalSlider_result_4)


        self.verticalLayout_57.addWidget(self.frame_163)


        self.verticalLayout_54.addWidget(self.frame_159)

        self.frame_169 = QFrame(self.frame_77)
        self.frame_169.setObjectName(u"frame_169")
        self.frame_169.setFrameShape(QFrame.NoFrame)
        self.frame_169.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_169)
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.frame_170 = QFrame(self.frame_169)
        self.frame_170.setObjectName(u"frame_170")
        self.frame_170.setFrameShape(QFrame.NoFrame)
        self.frame_170.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.frame_170)
        self.horizontalLayout_87.setSpacing(0)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.horizontalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.frame_171 = QFrame(self.frame_170)
        self.frame_171.setObjectName(u"frame_171")
        self.frame_171.setFrameShape(QFrame.NoFrame)
        self.frame_171.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_88 = QHBoxLayout(self.frame_171)
        self.horizontalLayout_88.setSpacing(0)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalLayout_88.setContentsMargins(0, 0, 0, 0)
        self.result_left_picturebox5 = QLabel(self.frame_171)
        self.result_left_picturebox5.setObjectName(u"result_left_picturebox5")

        self.horizontalLayout_88.addWidget(self.result_left_picturebox5)


        self.horizontalLayout_87.addWidget(self.frame_171)

        self.frame_172 = QFrame(self.frame_170)
        self.frame_172.setObjectName(u"frame_172")
        self.frame_172.setMinimumSize(QSize(30, 0))
        self.frame_172.setMaximumSize(QSize(30, 16777215))
        self.frame_172.setFrameShape(QFrame.NoFrame)
        self.frame_172.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.frame_172)
        self.horizontalLayout_89.setSpacing(0)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.horizontalLayout_89.setContentsMargins(0, 0, 0, 0)
        self.pushButton_color_5 = QPushButton(self.frame_172)
        self.pushButton_color_5.setObjectName(u"pushButton_color_5")
        self.pushButton_color_5.setMinimumSize(QSize(23, 23))
        self.pushButton_color_5.setMaximumSize(QSize(23, 23))
        self.pushButton_color_5.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"\n"
"	background-image: url(:/floresansPrefix/redUnPressed.png);\n"
"}")

        self.horizontalLayout_89.addWidget(self.pushButton_color_5)


        self.horizontalLayout_87.addWidget(self.frame_172)


        self.verticalLayout_59.addWidget(self.frame_170)

        self.frame_173 = QFrame(self.frame_169)
        self.frame_173.setObjectName(u"frame_173")
        self.frame_173.setMinimumSize(QSize(0, 15))
        self.frame_173.setMaximumSize(QSize(16777215, 15))
        self.frame_173.setFrameShape(QFrame.NoFrame)
        self.frame_173.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_173)
        self.horizontalLayout_90.setSpacing(0)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.horizontalSlider_result_5 = QSlider(self.frame_173)
        self.horizontalSlider_result_5.setObjectName(u"horizontalSlider_result_5")
        self.horizontalSlider_result_5.setStyleSheet(u"QSlider{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"	border-radius:3px;\n"
"    }")
        self.horizontalSlider_result_5.setMaximum(99)
        self.horizontalSlider_result_5.setPageStep(1)
        self.horizontalSlider_result_5.setValue(25)
        self.horizontalSlider_result_5.setOrientation(Qt.Horizontal)

        self.horizontalLayout_90.addWidget(self.horizontalSlider_result_5)


        self.verticalLayout_59.addWidget(self.frame_173)


        self.verticalLayout_54.addWidget(self.frame_169)


        self.verticalLayout_53.addWidget(self.frame_77)

        self.stackedWidget_leftSide.addWidget(self.page_6)

        self.horizontalLayout_9.addWidget(self.stackedWidget_leftSide)


        self.horizontalLayout_4.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_6)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.horizontalLayout_83 = QHBoxLayout(self.page_14)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.pictureBox = QtImageViewer()
        self.pictureBox.setObjectName(u"pictureBox")
        self.pictureBox.setStyleSheet(u"QGraphicsView{\n"
"\n"
"border:none;\n"
"\n"
"}\n"
"\n"
" QScrollBar:horizontal\n"
"\n"
" {\n"
"\n"
"     height: 15px;\n"
"\n"
"     margin: 3px 15px 3px 15px;\n"
"\n"
"     border: 1px transparent #2A2929;\n"
"\n"
"     border-radius: 4px;\n"
"\n"
"     background-color:rgb(49, 51, 50) ;  \n"
"\n"
"	\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::handle:horizontal\n"
"\n"
" {\n"
"\n"
"     background-color: white;      /* #605F5F; */\n"
"\n"
"     min-width: 5px;\n"
"\n"
"     border-radius: 4px;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::add-line:horizontal\n"
"\n"
" {\n"
"\n"
"     margin: 0px 3px 0px 3px;\n"
"\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"\n"
"     width: 10px;\n"
"\n"
"     height: 10px;\n"
"\n"
"     subcontrol-position: right;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
"\n"
" {\n"
"\n"
"     margin: 0px 3px 0px 3px;\n"
"\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"\n"
""
                        "     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: left;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"\n"
" {\n"
"\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: right;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"\n"
" {\n"
"\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: left;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"\n"
" {\n"
"\n"
"     background: none;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizonta"
                        "l\n"
"\n"
" {\n"
"\n"
"     background: none;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar:vertical\n"
"\n"
" {\n"
"\n"
"     \n"
"\n"
"	background-color: rgb(49, 51, 50);\n"
"\n"
"     width: 15px;\n"
"\n"
"     margin: 15px 3px 15px 3px;\n"
"\n"
"     border: 1px transparent #2A2929;\n"
"\n"
"     border-radius: 4px;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::handle:vertical\n"
"\n"
" {\n"
"\n"
"     background-color: white;         /* #605F5F; */\n"
"\n"
"     min-height: 5px;\n"
"\n"
"     border-radius: 4px;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::sub-line:vertical\n"
"\n"
" {\n"
"\n"
"     margin: 3px 0px 3px 0px;\n"
"\n"
"     border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: top;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::add-line:vertical\n"
"\n"
" {\n"
"\n"
"     margin: 3px 0px 3px 0px;\n"
"\n"
"     border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
""
                        "\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: bottom;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"\n"
" {\n"
"\n"
"\n"
"\n"
"     border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: top;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"\n"
" {\n"
"\n"
"     border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: bottom;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"\n"
" {\n"
"\n"
"     background: none;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
""
                        "\n"
" {\n"
"\n"
"     background: none;\n"
"\n"
" }")
        self.pictureBox.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_83.addWidget(self.pictureBox)

        self.stackedWidget.addWidget(self.page_14)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.horizontalLayout_84 = QHBoxLayout(self.page_15)
        self.horizontalLayout_84.setSpacing(0)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalLayout_84.setContentsMargins(0, 0, 0, 0)
        self.frame_164 = QFrame(self.page_15)
        self.frame_164.setObjectName(u"frame_164")
        self.frame_164.setFrameShape(QFrame.NoFrame)
        self.frame_164.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_164)
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.verticalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.frame_165 = QFrame(self.frame_164)
        self.frame_165.setObjectName(u"frame_165")
        self.frame_165.setFrameShape(QFrame.NoFrame)
        self.frame_165.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.frame_165)
        self.horizontalLayout_85.setSpacing(0)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.pictureBox_result = QtImageViewer()
        self.pictureBox_result.setObjectName(u"pictureBox_result")
        self.pictureBox_result.setStyleSheet(u"QGraphicsView{\n"
"\n"
"border:none;\n"
"\n"
"}\n"
"\n"
" QScrollBar:horizontal\n"
"\n"
" {\n"
"\n"
"     height: 15px;\n"
"\n"
"     margin: 3px 15px 3px 15px;\n"
"\n"
"     border: 1px transparent #2A2929;\n"
"\n"
"     border-radius: 4px;\n"
"\n"
"     background-color:rgb(49, 51, 50) ;  \n"
"\n"
"	\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::handle:horizontal\n"
"\n"
" {\n"
"\n"
"     background-color: white;      /* #605F5F; */\n"
"\n"
"     min-width: 5px;\n"
"\n"
"     border-radius: 4px;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::add-line:horizontal\n"
"\n"
" {\n"
"\n"
"     margin: 0px 3px 0px 3px;\n"
"\n"
"     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);\n"
"\n"
"     width: 10px;\n"
"\n"
"     height: 10px;\n"
"\n"
"     subcontrol-position: right;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal\n"
"\n"
" {\n"
"\n"
"     margin: 0px 3px 0px 3px;\n"
"\n"
"     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);\n"
"\n"
""
                        "     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: left;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
"\n"
" {\n"
"\n"
"     border-image: url(:/qss_icons/rc/right_arrow.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: right;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
"\n"
" {\n"
"\n"
"     border-image: url(:/qss_icons/rc/left_arrow.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: left;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"\n"
" {\n"
"\n"
"     background: none;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizonta"
                        "l\n"
"\n"
" {\n"
"\n"
"     background: none;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar:vertical\n"
"\n"
" {\n"
"\n"
"     \n"
"\n"
"	background-color: rgb(49, 51, 50);\n"
"\n"
"     width: 15px;\n"
"\n"
"     margin: 15px 3px 15px 3px;\n"
"\n"
"     border: 1px transparent #2A2929;\n"
"\n"
"     border-radius: 4px;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::handle:vertical\n"
"\n"
" {\n"
"\n"
"     background-color: white;         /* #605F5F; */\n"
"\n"
"     min-height: 5px;\n"
"\n"
"     border-radius: 4px;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::sub-line:vertical\n"
"\n"
" {\n"
"\n"
"     margin: 3px 0px 3px 0px;\n"
"\n"
"     border-image: url(:/qss_icons/rc/up_arrow_disabled.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: top;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::add-line:vertical\n"
"\n"
" {\n"
"\n"
"     margin: 3px 0px 3px 0px;\n"
"\n"
"     border-image: url(:/qss_icons/rc/down_arrow_disabled.png);\n"
""
                        "\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: bottom;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
"\n"
" {\n"
"\n"
"\n"
"\n"
"     border-image: url(:/qss_icons/rc/up_arrow.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: top;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"\n"
" {\n"
"\n"
"     border-image: url(:/qss_icons/rc/down_arrow.png);\n"
"\n"
"     height: 10px;\n"
"\n"
"     width: 10px;\n"
"\n"
"     subcontrol-position: bottom;\n"
"\n"
"     subcontrol-origin: margin;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"\n"
" {\n"
"\n"
"     background: none;\n"
"\n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
""
                        "\n"
" {\n"
"\n"
"     background: none;\n"
"\n"
" }")
        self.pictureBox_result.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_85.addWidget(self.pictureBox_result)


        self.verticalLayout_58.addWidget(self.frame_165)

        self.frame_166 = QFrame(self.frame_164)
        self.frame_166.setObjectName(u"frame_166")
        self.frame_166.setMinimumSize(QSize(0, 100))
        self.frame_166.setMaximumSize(QSize(16777215, 100))
        self.frame_166.setFrameShape(QFrame.NoFrame)
        self.frame_166.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_166)
        self.verticalLayout_61.setSpacing(0)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.frame_167 = QFrame(self.frame_166)
        self.frame_167.setObjectName(u"frame_167")
        self.frame_167.setFrameShape(QFrame.StyledPanel)
        self.frame_167.setFrameShadow(QFrame.Raised)

        self.verticalLayout_61.addWidget(self.frame_167)

        self.frame_168 = QFrame(self.frame_166)
        self.frame_168.setObjectName(u"frame_168")
        self.frame_168.setFrameShape(QFrame.NoFrame)
        self.frame_168.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.frame_168)
        self.horizontalLayout_86.setSpacing(0)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.frame_181 = QFrame(self.frame_168)
        self.frame_181.setObjectName(u"frame_181")
        self.frame_181.setMinimumSize(QSize(70, 0))
        self.frame_181.setMaximumSize(QSize(70, 16777215))
        self.frame_181.setFrameShape(QFrame.StyledPanel)
        self.frame_181.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_86.addWidget(self.frame_181)

        self.frame_179 = QFrame(self.frame_168)
        self.frame_179.setObjectName(u"frame_179")
        self.frame_179.setFrameShape(QFrame.StyledPanel)
        self.frame_179.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_179)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.horizontalSlider_result_6 = QSlider(self.frame_179)
        self.horizontalSlider_result_6.setObjectName(u"horizontalSlider_result_6")
        self.horizontalSlider_result_6.setStyleSheet(u"QSlider{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"	border-radius:3px;\n"
"    }")
        self.horizontalSlider_result_6.setMaximum(99)
        self.horizontalSlider_result_6.setPageStep(1)
        self.horizontalSlider_result_6.setValue(0)
        self.horizontalSlider_result_6.setOrientation(Qt.Horizontal)

        self.verticalLayout_62.addWidget(self.horizontalSlider_result_6)


        self.horizontalLayout_86.addWidget(self.frame_179)

        self.frame_180 = QFrame(self.frame_168)
        self.frame_180.setObjectName(u"frame_180")
        self.frame_180.setMinimumSize(QSize(70, 0))
        self.frame_180.setMaximumSize(QSize(70, 16777215))
        self.frame_180.setFrameShape(QFrame.NoFrame)
        self.frame_180.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_180)
        self.horizontalLayout_95.setSpacing(0)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_180)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"font: 75 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_95.addWidget(self.label_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_86.addWidget(self.frame_180)


        self.verticalLayout_61.addWidget(self.frame_168)


        self.verticalLayout_58.addWidget(self.frame_166)


        self.horizontalLayout_84.addWidget(self.frame_164)

        self.stackedWidget.addWidget(self.page_15)

        self.horizontalLayout_23.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(300, 0))
        self.frame_8.setMaximumSize(QSize(300, 16777215))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 10, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(25, 0))
        self.frame_9.setMaximumSize(QSize(25, 16777215))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_9)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_preview = QPushButton(self.frame_9)
        self.pushButton_preview.setObjectName(u"pushButton_preview")
        self.pushButton_preview.setMinimumSize(QSize(25, 150))
        self.pushButton_preview.setAutoFillBackground(False)
        self.pushButton_preview.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"background-image: url(:/floresansPrefix/preview_button_selected.png);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255,150);\n"
"}")
        self.pushButton_preview.setAutoRepeat(False)
        self.pushButton_preview.setAutoExclusive(False)
        self.pushButton_preview.setAutoDefault(False)
        self.pushButton_preview.setFlat(False)

        self.verticalLayout_2.addWidget(self.pushButton_preview)

        self.pushButton_zStack = QPushButton(self.frame_9)
        self.pushButton_zStack.setObjectName(u"pushButton_zStack")
        self.pushButton_zStack.setMinimumSize(QSize(25, 150))
        self.pushButton_zStack.setAutoFillBackground(False)
        self.pushButton_zStack.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"background-image: url(:/floresansPrefix/Zstack_button.png);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255,150);\n"
"}")
        self.pushButton_zStack.setAutoRepeat(False)
        self.pushButton_zStack.setAutoExclusive(False)
        self.pushButton_zStack.setAutoDefault(False)
        self.pushButton_zStack.setFlat(False)

        self.verticalLayout_2.addWidget(self.pushButton_zStack)

        self.pushButton_timelapse = QPushButton(self.frame_9)
        self.pushButton_timelapse.setObjectName(u"pushButton_timelapse")
        self.pushButton_timelapse.setMinimumSize(QSize(25, 150))
        self.pushButton_timelapse.setAutoFillBackground(False)
        self.pushButton_timelapse.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	background-image: url(:/floresansPrefix/timelapse_button.png);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255,150);\n"
"}")
        self.pushButton_timelapse.setAutoRepeat(False)
        self.pushButton_timelapse.setAutoExclusive(False)
        self.pushButton_timelapse.setAutoDefault(False)
        self.pushButton_timelapse.setFlat(False)

        self.verticalLayout_2.addWidget(self.pushButton_timelapse)

        self.pushButton_result = QPushButton(self.frame_9)
        self.pushButton_result.setObjectName(u"pushButton_result")
        self.pushButton_result.setMinimumSize(QSize(25, 150))
        self.pushButton_result.setAutoFillBackground(False)
        self.pushButton_result.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"	background-image: url(:/floresansPrefix/result_button.png);\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255,150);\n"
"}")
        self.pushButton_result.setAutoRepeat(False)
        self.pushButton_result.setAutoExclusive(False)
        self.pushButton_result.setAutoDefault(False)
        self.pushButton_result.setFlat(False)

        self.verticalLayout_2.addWidget(self.pushButton_result)


        self.horizontalLayout_5.addWidget(self.frame_9, 0, Qt.AlignTop)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_10)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_rightSide = QStackedWidget(self.frame_10)
        self.stackedWidget_rightSide.setObjectName(u"stackedWidget_rightSide")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_8 = QHBoxLayout(self.page_3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.page_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_13)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, -1, 5, 5)
        self.frame_39 = QFrame(self.frame_13)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setMinimumSize(QSize(0, 600))
        self.frame_39.setMaximumSize(QSize(16777215, 800))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_39)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_43 = QFrame(self.frame_39)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.NoFrame)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.circularProgressBarBase_5 = QFrame(self.frame_43)
        self.circularProgressBarBase_5.setObjectName(u"circularProgressBarBase_5")
        self.circularProgressBarBase_5.setMinimumSize(QSize(100, 100))
        self.circularProgressBarBase_5.setMaximumSize(QSize(100, 100))
        self.circularProgressBarBase_5.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase_5.setFrameShadow(QFrame.Raised)
        self.circularProgress_red = QFrame(self.circularProgressBarBase_5)
        self.circularProgress_red.setObjectName(u"circularProgress_red")
        self.circularProgress_red.setGeometry(QRect(0, 0, 100, 100))
        self.circularProgress_red.setStyleSheet(u"QFrame{\n"
"border-radius:50px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.748 rgba(0, 0, 0, 9), stop:0.749 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        self.circularProgress_red.setFrameShape(QFrame.NoFrame)
        self.circularProgress_red.setFrameShadow(QFrame.Raised)
        self.container_8 = QFrame(self.circularProgress_red)
        self.container_8.setObjectName(u"container_8")
        self.container_8.setGeometry(QRect(10, 10, 81, 81))
        self.container_8.setStyleSheet(u"QFrame{\n"
"	border-radius:40px;\n"
"	\n"
"	background-color: rgb(238, 29, 37);\n"
"}\n"
"")
        self.container_8.setFrameShape(QFrame.NoFrame)
        self.container_8.setFrameShadow(QFrame.Raised)
        self.label_redChannel_led = QLabel(self.container_8)
        self.label_redChannel_led.setObjectName(u"label_redChannel_led")
        self.label_redChannel_led.setGeometry(QRect(0, 20, 81, 31))
        self.label_redChannel_led.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"font: 75 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_redChannel_led.setAlignment(Qt.AlignCenter)
        self.horizontalSlider_red = QSlider(self.container_8)
        self.horizontalSlider_red.setObjectName(u"horizontalSlider_red")
        self.horizontalSlider_red.setGeometry(QRect(12, 50, 60, 10))
        self.horizontalSlider_red.setStyleSheet(u"QSlider{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"	border-radius:3px;\n"
"    }")
        self.horizontalSlider_red.setMaximum(99)
        self.horizontalSlider_red.setPageStep(1)
        self.horizontalSlider_red.setValue(25)
        self.horizontalSlider_red.setOrientation(Qt.Horizontal)
        self.circularBg_6 = QFrame(self.circularProgressBarBase_5)
        self.circularBg_6.setObjectName(u"circularBg_6")
        self.circularBg_6.setGeometry(QRect(0, 0, 100, 100))
        self.circularBg_6.setStyleSheet(u"QFrame{\n"
"border-radius:50px;\n"
"	background-color: rgba(238, 29, 37, 120);\n"
"}\n"
"")
        self.circularBg_6.setFrameShape(QFrame.NoFrame)
        self.circularBg_6.setFrameShadow(QFrame.Raised)
        self.circularBg_6.raise_()
        self.circularProgress_red.raise_()

        self.horizontalLayout_13.addWidget(self.circularProgressBarBase_5)

        self.label_14 = QLabel(self.frame_43)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(50, 0))
        self.label_14.setMaximumSize(QSize(50, 16777215))
        self.label_14.setStyleSheet(u"font: 75 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.label_14)

        self.pushButton_red_intensity = QPushButton(self.frame_43)
        self.pushButton_red_intensity.setObjectName(u"pushButton_red_intensity")
        self.pushButton_red_intensity.setMinimumSize(QSize(23, 23))
        self.pushButton_red_intensity.setMaximumSize(QSize(23, 23))
        self.pushButton_red_intensity.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background-image: url(:/floresansPrefix/redPressed.png);\n"
"}")

        self.horizontalLayout_13.addWidget(self.pushButton_red_intensity)


        self.verticalLayout_12.addWidget(self.frame_43)

        self.frame_44 = QFrame(self.frame_39)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.NoFrame)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.circularProgressBarBase_2 = QFrame(self.frame_44)
        self.circularProgressBarBase_2.setObjectName(u"circularProgressBarBase_2")
        self.circularProgressBarBase_2.setMinimumSize(QSize(100, 100))
        self.circularProgressBarBase_2.setMaximumSize(QSize(100, 100))
        self.circularProgressBarBase_2.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase_2.setFrameShadow(QFrame.Raised)
        self.circularProgress_green = QFrame(self.circularProgressBarBase_2)
        self.circularProgress_green.setObjectName(u"circularProgress_green")
        self.circularProgress_green.setGeometry(QRect(0, 0, 100, 100))
        self.circularProgress_green.setStyleSheet(u"QFrame{\n"
"border-radius:50px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.748 rgba(0, 0, 0, 0), stop:0.749 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        self.circularProgress_green.setFrameShape(QFrame.NoFrame)
        self.circularProgress_green.setFrameShadow(QFrame.Raised)
        self.container_5 = QFrame(self.circularProgress_green)
        self.container_5.setObjectName(u"container_5")
        self.container_5.setGeometry(QRect(10, 10, 80, 80))
        self.container_5.setStyleSheet(u"QFrame{\n"
"	border-radius:40px;\n"
"	\n"
"	\n"
"	background-color: rgb(81, 166, 0);\n"
"}\n"
"")
        self.container_5.setFrameShape(QFrame.NoFrame)
        self.container_5.setFrameShadow(QFrame.Raised)
        self.label_greenChannel_led = QLabel(self.container_5)
        self.label_greenChannel_led.setObjectName(u"label_greenChannel_led")
        self.label_greenChannel_led.setGeometry(QRect(0, 20, 81, 31))
        self.label_greenChannel_led.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"font: 75 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_greenChannel_led.setAlignment(Qt.AlignCenter)
        self.horizontalSlider_green = QSlider(self.container_5)
        self.horizontalSlider_green.setObjectName(u"horizontalSlider_green")
        self.horizontalSlider_green.setGeometry(QRect(12, 50, 60, 10))
        self.horizontalSlider_green.setStyleSheet(u"QSlider{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"	border-radius:3px;\n"
"    }")
        self.horizontalSlider_green.setPageStep(1)
        self.horizontalSlider_green.setValue(25)
        self.horizontalSlider_green.setOrientation(Qt.Horizontal)
        self.circularBg_4 = QFrame(self.circularProgressBarBase_2)
        self.circularBg_4.setObjectName(u"circularBg_4")
        self.circularBg_4.setGeometry(QRect(0, 0, 100, 100))
        self.circularBg_4.setStyleSheet(u"QFrame{\n"
"border-radius:50px;\n"
"	\n"
"	background-color: rgba(81, 166, 0, 120);\n"
"}\n"
"")
        self.circularBg_4.setFrameShape(QFrame.NoFrame)
        self.circularBg_4.setFrameShadow(QFrame.Raised)
        self.circularBg_4.raise_()
        self.circularProgress_green.raise_()

        self.horizontalLayout_24.addWidget(self.circularProgressBarBase_2)

        self.label_13 = QLabel(self.frame_44)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(50, 0))
        self.label_13.setMaximumSize(QSize(50, 16777215))
        self.label_13.setStyleSheet(u"font: 75 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_24.addWidget(self.label_13)

        self.pushButton_green_intensity = QPushButton(self.frame_44)
        self.pushButton_green_intensity.setObjectName(u"pushButton_green_intensity")
        self.pushButton_green_intensity.setMinimumSize(QSize(23, 23))
        self.pushButton_green_intensity.setMaximumSize(QSize(23, 23))
        self.pushButton_green_intensity.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/floresansPrefix/greenUnPressed.png);\n"
"	border:none;\n"
"}")

        self.horizontalLayout_24.addWidget(self.pushButton_green_intensity)


        self.verticalLayout_12.addWidget(self.frame_44)

        self.frame_45 = QFrame(self.frame_39)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.NoFrame)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.circularProgressBarBase_3 = QFrame(self.frame_45)
        self.circularProgressBarBase_3.setObjectName(u"circularProgressBarBase_3")
        self.circularProgressBarBase_3.setMinimumSize(QSize(100, 100))
        self.circularProgressBarBase_3.setMaximumSize(QSize(100, 100))
        self.circularProgressBarBase_3.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase_3.setFrameShadow(QFrame.Raised)
        self.circularProgress_blue = QFrame(self.circularProgressBarBase_3)
        self.circularProgress_blue.setObjectName(u"circularProgress_blue")
        self.circularProgress_blue.setGeometry(QRect(0, 0, 100, 100))
        self.circularProgress_blue.setStyleSheet(u"QFrame{\n"
"border-radius:50px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.748 rgba(0, 0, 0, 9), stop:0.749 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        self.circularProgress_blue.setFrameShape(QFrame.NoFrame)
        self.circularProgress_blue.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgress_blue)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(10, 10, 80, 80))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius:40px;\n"
"	\n"
"	background-color: rgb(0, 173, 238);\n"
"}\n"
"")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.label_blueChannel_led = QLabel(self.container)
        self.label_blueChannel_led.setObjectName(u"label_blueChannel_led")
        self.label_blueChannel_led.setGeometry(QRect(0, 20, 81, 31))
        self.label_blueChannel_led.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"font: 75 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_blueChannel_led.setAlignment(Qt.AlignCenter)
        self.horizontalSlider_blue = QSlider(self.container)
        self.horizontalSlider_blue.setObjectName(u"horizontalSlider_blue")
        self.horizontalSlider_blue.setGeometry(QRect(12, 50, 60, 10))
        self.horizontalSlider_blue.setStyleSheet(u"QSlider{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"	border-radius:3px;\n"
"    }")
        self.horizontalSlider_blue.setPageStep(1)
        self.horizontalSlider_blue.setValue(25)
        self.horizontalSlider_blue.setOrientation(Qt.Horizontal)
        self.circularBg = QFrame(self.circularProgressBarBase_3)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(0, 0, 100, 100))
        self.circularBg.setStyleSheet(u"QFrame{\n"
"border-radius:50px;\n"
"	background-color: rgba(0, 173, 238, 120);\n"
"}\n"
"")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.circularBg.raise_()
        self.circularProgress_blue.raise_()

        self.horizontalLayout_25.addWidget(self.circularProgressBarBase_3)

        self.label_12 = QLabel(self.frame_45)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(50, 0))
        self.label_12.setMaximumSize(QSize(50, 16777215))
        self.label_12.setStyleSheet(u"font: 75 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_25.addWidget(self.label_12)

        self.pushButton_blue_intensity = QPushButton(self.frame_45)
        self.pushButton_blue_intensity.setObjectName(u"pushButton_blue_intensity")
        self.pushButton_blue_intensity.setMinimumSize(QSize(23, 23))
        self.pushButton_blue_intensity.setMaximumSize(QSize(23, 23))
        self.pushButton_blue_intensity.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-image: url(:/floresansPrefix/blueUnPressed.png);\n"
"	border:none;\n"
"}")

        self.horizontalLayout_25.addWidget(self.pushButton_blue_intensity)


        self.verticalLayout_12.addWidget(self.frame_45)

        self.frame_46 = QFrame(self.frame_39)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.NoFrame)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.circularProgressBarBase_4 = QFrame(self.frame_46)
        self.circularProgressBarBase_4.setObjectName(u"circularProgressBarBase_4")
        self.circularProgressBarBase_4.setMinimumSize(QSize(100, 100))
        self.circularProgressBarBase_4.setMaximumSize(QSize(100, 100))
        self.circularProgressBarBase_4.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase_4.setFrameShadow(QFrame.Raised)
        self.circularProgress_uv = QFrame(self.circularProgressBarBase_4)
        self.circularProgress_uv.setObjectName(u"circularProgress_uv")
        self.circularProgress_uv.setGeometry(QRect(0, 0, 100, 100))
        self.circularProgress_uv.setStyleSheet(u"QFrame{\n"
"border-radius:50px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.748 rgba(0, 0, 0, 9), stop:0.749 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        self.circularProgress_uv.setFrameShape(QFrame.NoFrame)
        self.circularProgress_uv.setFrameShadow(QFrame.Raised)
        self.container_6 = QFrame(self.circularProgress_uv)
        self.container_6.setObjectName(u"container_6")
        self.container_6.setGeometry(QRect(10, 10, 81, 81))
        self.container_6.setStyleSheet(u"QFrame{\n"
"	border-radius:40px;\n"
"	\n"
"	background-color: rgb(170, 0, 255);\n"
"}\n"
"")
        self.container_6.setFrameShape(QFrame.NoFrame)
        self.container_6.setFrameShadow(QFrame.Raised)
        self.label_uvChannel_led = QLabel(self.container_6)
        self.label_uvChannel_led.setObjectName(u"label_uvChannel_led")
        self.label_uvChannel_led.setGeometry(QRect(0, 20, 81, 31))
        self.label_uvChannel_led.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"font: 75 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_uvChannel_led.setAlignment(Qt.AlignCenter)
        self.horizontalSlider_uv = QSlider(self.container_6)
        self.horizontalSlider_uv.setObjectName(u"horizontalSlider_uv")
        self.horizontalSlider_uv.setGeometry(QRect(12, 50, 60, 10))
        self.horizontalSlider_uv.setStyleSheet(u"QSlider{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"	border-radius:3px;\n"
"    }")
        self.horizontalSlider_uv.setPageStep(1)
        self.horizontalSlider_uv.setValue(25)
        self.horizontalSlider_uv.setOrientation(Qt.Horizontal)
        self.circularBg_5 = QFrame(self.circularProgressBarBase_4)
        self.circularBg_5.setObjectName(u"circularBg_5")
        self.circularBg_5.setGeometry(QRect(0, 0, 100, 100))
        self.circularBg_5.setStyleSheet(u"QFrame{\n"
"border-radius:50px;\n"
"	background-color: rgba(170, 0, 255, 120);\n"
"}\n"
"")
        self.circularBg_5.setFrameShape(QFrame.NoFrame)
        self.circularBg_5.setFrameShadow(QFrame.Raised)
        self.circularBg_5.raise_()
        self.circularProgress_uv.raise_()

        self.horizontalLayout_26.addWidget(self.circularProgressBarBase_4)

        self.label_11 = QLabel(self.frame_46)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(50, 0))
        self.label_11.setMaximumSize(QSize(50, 16777215))
        self.label_11.setStyleSheet(u"font: 75 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_26.addWidget(self.label_11)

        self.pushButton_uv_intensity = QPushButton(self.frame_46)
        self.pushButton_uv_intensity.setObjectName(u"pushButton_uv_intensity")
        self.pushButton_uv_intensity.setMinimumSize(QSize(23, 24))
        self.pushButton_uv_intensity.setMaximumSize(QSize(23, 24))
        self.pushButton_uv_intensity.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-image: url(:/floresansPrefix/uv_button_unpressed.png);\n"
"	border:none;\n"
"}")

        self.horizontalLayout_26.addWidget(self.pushButton_uv_intensity)


        self.verticalLayout_12.addWidget(self.frame_46)

        self.frame_40 = QFrame(self.frame_39)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.NoFrame)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.circularProgressBarBase_6 = QFrame(self.frame_40)
        self.circularProgressBarBase_6.setObjectName(u"circularProgressBarBase_6")
        self.circularProgressBarBase_6.setMinimumSize(QSize(100, 100))
        self.circularProgressBarBase_6.setMaximumSize(QSize(100, 100))
        self.circularProgressBarBase_6.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase_6.setFrameShadow(QFrame.Raised)
        self.circularProgress_white = QFrame(self.circularProgressBarBase_6)
        self.circularProgress_white.setObjectName(u"circularProgress_white")
        self.circularProgress_white.setGeometry(QRect(0, 0, 100, 100))
        self.circularProgress_white.setStyleSheet(u"QFrame{\n"
"border-radius:50px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.748 rgba(0, 0, 0, 9), stop:0.749 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        self.circularProgress_white.setFrameShape(QFrame.NoFrame)
        self.circularProgress_white.setFrameShadow(QFrame.Raised)
        self.container_9 = QFrame(self.circularProgress_white)
        self.container_9.setObjectName(u"container_9")
        self.container_9.setGeometry(QRect(10, 10, 80, 80))
        self.container_9.setStyleSheet(u"QFrame{\n"
"	border-radius:40px;\n"
"	\n"
"	background-color: rgb(150, 150, 150);\n"
"}\n"
"")
        self.container_9.setFrameShape(QFrame.NoFrame)
        self.container_9.setFrameShadow(QFrame.Raised)
        self.label_whiteChannel_led = QLabel(self.container_9)
        self.label_whiteChannel_led.setObjectName(u"label_whiteChannel_led")
        self.label_whiteChannel_led.setGeometry(QRect(0, 20, 81, 31))
        self.label_whiteChannel_led.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"font: 75 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_whiteChannel_led.setAlignment(Qt.AlignCenter)
        self.horizontalSlider_white = QSlider(self.container_9)
        self.horizontalSlider_white.setObjectName(u"horizontalSlider_white")
        self.horizontalSlider_white.setGeometry(QRect(12, 50, 60, 10))
        self.horizontalSlider_white.setStyleSheet(u"QSlider{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"	border-radius:3px;\n"
"    }")
        self.horizontalSlider_white.setPageStep(1)
        self.horizontalSlider_white.setValue(25)
        self.horizontalSlider_white.setOrientation(Qt.Horizontal)
        self.circularBg_7 = QFrame(self.circularProgressBarBase_6)
        self.circularBg_7.setObjectName(u"circularBg_7")
        self.circularBg_7.setGeometry(QRect(0, 0, 100, 100))
        self.circularBg_7.setStyleSheet(u"QFrame{\n"
"border-radius:50px;\n"
"	background-color: rgba(211, 211, 211, 120);\n"
"}\n"
"")
        self.circularBg_7.setFrameShape(QFrame.NoFrame)
        self.circularBg_7.setFrameShadow(QFrame.Raised)
        self.circularBg_7.raise_()
        self.circularProgress_white.raise_()

        self.horizontalLayout_27.addWidget(self.circularProgressBarBase_6)

        self.label = QLabel(self.frame_40)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 0))
        self.label.setMaximumSize(QSize(50, 16777215))
        self.label.setStyleSheet(u"font: 75 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_27.addWidget(self.label)

        self.pushButton_white_intensity = QPushButton(self.frame_40)
        self.pushButton_white_intensity.setObjectName(u"pushButton_white_intensity")
        self.pushButton_white_intensity.setMinimumSize(QSize(25, 25))
        self.pushButton_white_intensity.setMaximumSize(QSize(25, 25))
        self.pushButton_white_intensity.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
"border:none;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_27.addWidget(self.pushButton_white_intensity)


        self.verticalLayout_12.addWidget(self.frame_40)


        self.verticalLayout_11.addWidget(self.frame_39)

        self.frame_41 = QFrame(self.frame_13)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setFrameShape(QFrame.NoFrame)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_41)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_42 = QFrame(self.frame_41)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.NoFrame)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_42)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.frame_42)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line)

        self.frame_48 = QFrame(self.frame_42)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.NoFrame)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 3, 0, 0)
        self.circularProgressBarBase_7 = QFrame(self.frame_48)
        self.circularProgressBarBase_7.setObjectName(u"circularProgressBarBase_7")
        self.circularProgressBarBase_7.setMinimumSize(QSize(100, 100))
        self.circularProgressBarBase_7.setMaximumSize(QSize(100, 100))
        self.circularProgressBarBase_7.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase_7.setFrameShadow(QFrame.Raised)
        self.circularProgress_exposure = QFrame(self.circularProgressBarBase_7)
        self.circularProgress_exposure.setObjectName(u"circularProgress_exposure")
        self.circularProgress_exposure.setGeometry(QRect(0, 0, 101, 101))
        self.circularProgress_exposure.setStyleSheet(u"QFrame{\n"
"border-radius:50px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.748 rgba(0, 0, 0, 9), stop:0.749 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        self.circularProgress_exposure.setFrameShape(QFrame.NoFrame)
        self.circularProgress_exposure.setFrameShadow(QFrame.Raised)
        self.container_10 = QFrame(self.circularProgress_exposure)
        self.container_10.setObjectName(u"container_10")
        self.container_10.setGeometry(QRect(10, 10, 80, 80))
        self.container_10.setStyleSheet(u"QFrame{\n"
"	border-radius:40px;\n"
"	\n"
"	background-color: rgb(100,100, 100);\n"
"}\n"
"")
        self.container_10.setFrameShape(QFrame.NoFrame)
        self.container_10.setFrameShadow(QFrame.Raised)
        self.label_exposure = QLabel(self.container_10)
        self.label_exposure.setObjectName(u"label_exposure")
        self.label_exposure.setGeometry(QRect(0, 20, 81, 31))
        self.label_exposure.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"font: 75 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_exposure.setAlignment(Qt.AlignCenter)
        self.horizontalSlider_exposure = QSlider(self.container_10)
        self.horizontalSlider_exposure.setObjectName(u"horizontalSlider_exposure")
        self.horizontalSlider_exposure.setGeometry(QRect(12, 50, 60, 10))
        self.horizontalSlider_exposure.setStyleSheet(u"QSlider{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"	border-radius:3px;\n"
"    }")
        self.horizontalSlider_exposure.setPageStep(1)
        self.horizontalSlider_exposure.setValue(25)
        self.horizontalSlider_exposure.setOrientation(Qt.Horizontal)
        self.circularBg_8 = QFrame(self.circularProgressBarBase_7)
        self.circularBg_8.setObjectName(u"circularBg_8")
        self.circularBg_8.setGeometry(QRect(0, 0, 101, 101))
        self.circularBg_8.setStyleSheet(u"QFrame{\n"
"border-radius:50px;\n"
"	background-color: rgba(100, 100, 100,120);\n"
"}\n"
"")
        self.circularBg_8.setFrameShape(QFrame.NoFrame)
        self.circularBg_8.setFrameShadow(QFrame.Raised)
        self.circularBg_8.raise_()
        self.circularProgress_exposure.raise_()

        self.horizontalLayout_28.addWidget(self.circularProgressBarBase_7)

        self.circularProgressBarBase_8 = QFrame(self.frame_48)
        self.circularProgressBarBase_8.setObjectName(u"circularProgressBarBase_8")
        self.circularProgressBarBase_8.setMinimumSize(QSize(100, 100))
        self.circularProgressBarBase_8.setMaximumSize(QSize(100, 100))
        self.circularProgressBarBase_8.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase_8.setFrameShadow(QFrame.Raised)
        self.circularProgress_gain = QFrame(self.circularProgressBarBase_8)
        self.circularProgress_gain.setObjectName(u"circularProgress_gain")
        self.circularProgress_gain.setGeometry(QRect(0, 0, 101, 101))
        self.circularProgress_gain.setStyleSheet(u"QFrame{\n"
"border-radius:50px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.748 rgba(0, 0, 0, 9), stop:0.749 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        self.circularProgress_gain.setFrameShape(QFrame.NoFrame)
        self.circularProgress_gain.setFrameShadow(QFrame.Raised)
        self.container_11 = QFrame(self.circularProgress_gain)
        self.container_11.setObjectName(u"container_11")
        self.container_11.setGeometry(QRect(10, 10, 80, 80))
        self.container_11.setStyleSheet(u"QFrame{\n"
"	border-radius:40px;\n"
"	\n"
"	background-color: rgb(100,100, 100);\n"
"}\n"
"")
        self.container_11.setFrameShape(QFrame.NoFrame)
        self.container_11.setFrameShadow(QFrame.Raised)
        self.label_gain = QLabel(self.container_11)
        self.label_gain.setObjectName(u"label_gain")
        self.label_gain.setGeometry(QRect(0, 20, 81, 31))
        self.label_gain.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"font: 75 14pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_gain.setAlignment(Qt.AlignCenter)
        self.horizontalSlider_gain = QSlider(self.container_11)
        self.horizontalSlider_gain.setObjectName(u"horizontalSlider_gain")
        self.horizontalSlider_gain.setGeometry(QRect(12, 50, 60, 10))
        self.horizontalSlider_gain.setStyleSheet(u"QSlider{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: white;\n"
"	border-radius:3px;\n"
"    }")
        self.horizontalSlider_gain.setPageStep(1)
        self.horizontalSlider_gain.setValue(25)
        self.horizontalSlider_gain.setOrientation(Qt.Horizontal)
        self.circularBg_9 = QFrame(self.circularProgressBarBase_8)
        self.circularBg_9.setObjectName(u"circularBg_9")
        self.circularBg_9.setGeometry(QRect(0, 0, 101, 101))
        self.circularBg_9.setStyleSheet(u"QFrame{\n"
"border-radius:50px;\n"
"	background-color: rgba(100, 100, 100,120);\n"
"}\n"
"")
        self.circularBg_9.setFrameShape(QFrame.NoFrame)
        self.circularBg_9.setFrameShadow(QFrame.Raised)
        self.circularBg_9.raise_()
        self.circularProgress_gain.raise_()

        self.horizontalLayout_28.addWidget(self.circularProgressBarBase_8)


        self.verticalLayout_14.addWidget(self.frame_48)

        self.frame_49 = QFrame(self.frame_42)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMinimumSize(QSize(0, 20))
        self.frame_49.setMaximumSize(QSize(16777215, 20))
        self.frame_49.setFrameShape(QFrame.NoFrame)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_49)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font: 75 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_21, 0, Qt.AlignTop)

        self.label_22 = QLabel(self.frame_49)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font: 75 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_22, 0, Qt.AlignTop)


        self.verticalLayout_14.addWidget(self.frame_49)


        self.verticalLayout_13.addWidget(self.frame_42)

        self.frame_47 = QFrame(self.frame_41)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.NoFrame)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_47)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.frame_47)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_2)

        self.frame_50 = QFrame(self.frame_47)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setFrameShape(QFrame.NoFrame)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.pushButton_red_capture = QPushButton(self.frame_50)
        self.pushButton_red_capture.setObjectName(u"pushButton_red_capture")
        self.pushButton_red_capture.setMinimumSize(QSize(23, 23))
        self.pushButton_red_capture.setMaximumSize(QSize(23, 23))
        self.pushButton_red_capture.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"\n"
"	background-image: url(:/floresansPrefix/redUnPressed.png);\n"
"}")

        self.horizontalLayout_30.addWidget(self.pushButton_red_capture)

        self.pushButton_green_capture = QPushButton(self.frame_50)
        self.pushButton_green_capture.setObjectName(u"pushButton_green_capture")
        self.pushButton_green_capture.setMinimumSize(QSize(23, 23))
        self.pushButton_green_capture.setMaximumSize(QSize(23, 23))
        self.pushButton_green_capture.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/floresansPrefix/greenUnPressed.png);\n"
"	border:none;\n"
"}")

        self.horizontalLayout_30.addWidget(self.pushButton_green_capture)

        self.pushButton_blue_capture = QPushButton(self.frame_50)
        self.pushButton_blue_capture.setObjectName(u"pushButton_blue_capture")
        self.pushButton_blue_capture.setMinimumSize(QSize(23, 23))
        self.pushButton_blue_capture.setMaximumSize(QSize(23, 23))
        self.pushButton_blue_capture.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-image: url(:/floresansPrefix/blueUnPressed.png);\n"
"	border:none;\n"
"}")

        self.horizontalLayout_30.addWidget(self.pushButton_blue_capture)

        self.pushButton_uv_capture = QPushButton(self.frame_50)
        self.pushButton_uv_capture.setObjectName(u"pushButton_uv_capture")
        self.pushButton_uv_capture.setMinimumSize(QSize(23, 24))
        self.pushButton_uv_capture.setMaximumSize(QSize(23, 24))
        self.pushButton_uv_capture.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-image: url(:/floresansPrefix/uv_button_unpressed.png);\n"
"	border:none;\n"
"}")

        self.horizontalLayout_30.addWidget(self.pushButton_uv_capture)

        self.pushButton_white_capture = QPushButton(self.frame_50)
        self.pushButton_white_capture.setObjectName(u"pushButton_white_capture")
        self.pushButton_white_capture.setMinimumSize(QSize(25, 25))
        self.pushButton_white_capture.setMaximumSize(QSize(25, 25))
        self.pushButton_white_capture.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
"border:none;\n"
"}")

        self.horizontalLayout_30.addWidget(self.pushButton_white_capture)


        self.verticalLayout_15.addWidget(self.frame_50)

        self.frame_51 = QFrame(self.frame_47)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.NoFrame)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.pushButton_17 = QPushButton(self.frame_51)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(60, 10, 150, 30))
        self.pushButton_17.setMinimumSize(QSize(150, 30))
        self.pushButton_17.setMaximumSize(QSize(30, 16777215))
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.verticalLayout_15.addWidget(self.frame_51)


        self.verticalLayout_13.addWidget(self.frame_47)


        self.verticalLayout_11.addWidget(self.frame_41)


        self.horizontalLayout_8.addWidget(self.frame_13)

        self.stackedWidget_rightSide.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_31 = QHBoxLayout(self.page_4)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_52 = QFrame(self.page_4)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_52)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_53 = QFrame(self.frame_52)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.NoFrame)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_53)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_60 = QFrame(self.frame_53)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.NoFrame)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.label_23 = QLabel(self.frame_60)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(0, 0, 251, 51))
        self.label_23.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.frame_53)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.NoFrame)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.frame_62 = QFrame(self.frame_61)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.NoFrame)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_62)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.pushButton_red_zstack = QPushButton(self.frame_62)
        self.pushButton_red_zstack.setObjectName(u"pushButton_red_zstack")
        self.pushButton_red_zstack.setMinimumSize(QSize(23, 23))
        self.pushButton_red_zstack.setMaximumSize(QSize(23, 23))
        self.pushButton_red_zstack.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"\n"
"	background-image: url(:/floresansPrefix/redUnPressed.png);\n"
"}")

        self.horizontalLayout_32.addWidget(self.pushButton_red_zstack)

        self.pushButton_green_zstack = QPushButton(self.frame_62)
        self.pushButton_green_zstack.setObjectName(u"pushButton_green_zstack")
        self.pushButton_green_zstack.setMinimumSize(QSize(23, 23))
        self.pushButton_green_zstack.setMaximumSize(QSize(23, 23))
        self.pushButton_green_zstack.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/floresansPrefix/greenUnPressed.png);\n"
"	border:none;\n"
"}")

        self.horizontalLayout_32.addWidget(self.pushButton_green_zstack)

        self.pushButton_blue_zstack = QPushButton(self.frame_62)
        self.pushButton_blue_zstack.setObjectName(u"pushButton_blue_zstack")
        self.pushButton_blue_zstack.setMinimumSize(QSize(23, 23))
        self.pushButton_blue_zstack.setMaximumSize(QSize(23, 23))
        self.pushButton_blue_zstack.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-image: url(:/floresansPrefix/blueUnPressed.png);\n"
"	border:none;\n"
"}")

        self.horizontalLayout_32.addWidget(self.pushButton_blue_zstack)

        self.pushButton_uv_zstack = QPushButton(self.frame_62)
        self.pushButton_uv_zstack.setObjectName(u"pushButton_uv_zstack")
        self.pushButton_uv_zstack.setMinimumSize(QSize(23, 24))
        self.pushButton_uv_zstack.setMaximumSize(QSize(23, 24))
        self.pushButton_uv_zstack.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-image: url(:/floresansPrefix/uv_button_unpressed.png);\n"
"	border:none;\n"
"}")

        self.horizontalLayout_32.addWidget(self.pushButton_uv_zstack)

        self.pushButton_white_zstack = QPushButton(self.frame_62)
        self.pushButton_white_zstack.setObjectName(u"pushButton_white_zstack")
        self.pushButton_white_zstack.setMinimumSize(QSize(25, 25))
        self.pushButton_white_zstack.setMaximumSize(QSize(25, 25))
        self.pushButton_white_zstack.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
"border:none;\n"
"}")

        self.horizontalLayout_32.addWidget(self.pushButton_white_zstack)


        self.horizontalLayout_33.addWidget(self.frame_62)


        self.verticalLayout_17.addWidget(self.frame_61)


        self.verticalLayout_16.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.frame_52)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.NoFrame)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_54)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_83 = QFrame(self.frame_54)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setFrameShape(QFrame.NoFrame)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_83)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_84 = QFrame(self.frame_83)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.NoFrame)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.frame_85 = QFrame(self.frame_84)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setMinimumSize(QSize(140, 0))
        self.frame_85.setFrameShape(QFrame.NoFrame)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.pushButton_zstack_setStart = QPushButton(self.frame_85)
        self.pushButton_zstack_setStart.setObjectName(u"pushButton_zstack_setStart")
        self.pushButton_zstack_setStart.setGeometry(QRect(10, 10, 120, 35))
        self.pushButton_zstack_setStart.setMinimumSize(QSize(120, 35))
        self.pushButton_zstack_setStart.setMaximumSize(QSize(120, 35))
        self.pushButton_zstack_setStart.setFont(font)
        self.pushButton_zstack_setStart.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_41.addWidget(self.frame_85)

        self.frame_86 = QFrame(self.frame_84)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setFrameShape(QFrame.NoFrame)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.lineEdit_zstack_zstackStart = QLineEdit(self.frame_86)
        self.lineEdit_zstack_zstackStart.setObjectName(u"lineEdit_zstack_zstackStart")
        self.lineEdit_zstack_zstackStart.setGeometry(QRect(20, 10, 80, 35))
        self.lineEdit_zstack_zstackStart.setMinimumSize(QSize(80, 35))
        self.lineEdit_zstack_zstackStart.setMaximumSize(QSize(80, 35))
        self.lineEdit_zstack_zstackStart.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_zstack_zstackStart.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.lineEdit_zstack_zstackStart.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.frame_86)


        self.verticalLayout_23.addWidget(self.frame_84)

        self.frame_87 = QFrame(self.frame_83)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.NoFrame)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_88 = QFrame(self.frame_87)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMinimumSize(QSize(140, 0))
        self.frame_88.setFrameShape(QFrame.NoFrame)
        self.frame_88.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_42.addWidget(self.frame_88)

        self.frame_89 = QFrame(self.frame_87)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setFrameShape(QFrame.NoFrame)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.label_zstack_start = QLabel(self.frame_89)
        self.label_zstack_start.setObjectName(u"label_zstack_start")
        self.label_zstack_start.setGeometry(QRect(0, 0, 121, 51))
        self.label_zstack_start.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(0, 170, 0);")
        self.label_zstack_start.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.frame_89)


        self.verticalLayout_23.addWidget(self.frame_87)


        self.verticalLayout_24.addWidget(self.frame_83)


        self.verticalLayout_16.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.frame_52)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.NoFrame)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_55)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_64 = QFrame(self.frame_55)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.NoFrame)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_65 = QFrame(self.frame_64)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setMinimumSize(QSize(140, 0))
        self.frame_65.setFrameShape(QFrame.NoFrame)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.pushButton_zstack_setEnd = QPushButton(self.frame_65)
        self.pushButton_zstack_setEnd.setObjectName(u"pushButton_zstack_setEnd")
        self.pushButton_zstack_setEnd.setGeometry(QRect(10, 10, 120, 35))
        self.pushButton_zstack_setEnd.setMinimumSize(QSize(120, 35))
        self.pushButton_zstack_setEnd.setMaximumSize(QSize(120, 35))
        self.pushButton_zstack_setEnd.setFont(font)
        self.pushButton_zstack_setEnd.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_35.addWidget(self.frame_65)

        self.frame_66 = QFrame(self.frame_64)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.NoFrame)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.lineEdit_zstack_zstackEnd = QLineEdit(self.frame_66)
        self.lineEdit_zstack_zstackEnd.setObjectName(u"lineEdit_zstack_zstackEnd")
        self.lineEdit_zstack_zstackEnd.setGeometry(QRect(20, 10, 80, 35))
        self.lineEdit_zstack_zstackEnd.setMinimumSize(QSize(80, 35))
        self.lineEdit_zstack_zstackEnd.setMaximumSize(QSize(80, 35))
        self.lineEdit_zstack_zstackEnd.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_zstack_zstackEnd.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.lineEdit_zstack_zstackEnd.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.frame_66)


        self.verticalLayout_18.addWidget(self.frame_64)

        self.frame_63 = QFrame(self.frame_55)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.NoFrame)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_67 = QFrame(self.frame_63)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setMinimumSize(QSize(140, 0))
        self.frame_67.setFrameShape(QFrame.NoFrame)
        self.frame_67.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_36.addWidget(self.frame_67)

        self.frame_68 = QFrame(self.frame_63)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.NoFrame)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.label_zstack_end = QLabel(self.frame_68)
        self.label_zstack_end.setObjectName(u"label_zstack_end")
        self.label_zstack_end.setGeometry(QRect(0, 0, 121, 51))
        self.label_zstack_end.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(0, 170, 0);")
        self.label_zstack_end.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.frame_68)


        self.verticalLayout_18.addWidget(self.frame_63)


        self.verticalLayout_16.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.frame_52)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setMaximumSize(QSize(16777215, 60))
        self.frame_56.setFrameShape(QFrame.NoFrame)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.pushButton_zstack_flagSetSlices = QPushButton(self.frame_56)
        self.pushButton_zstack_flagSetSlices.setObjectName(u"pushButton_zstack_flagSetSlices")
        self.pushButton_zstack_flagSetSlices.setMinimumSize(QSize(25, 25))
        self.pushButton_zstack_flagSetSlices.setMaximumSize(QSize(25, 25))
        self.pushButton_zstack_flagSetSlices.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
"border:none;\n"
"}")

        self.horizontalLayout_40.addWidget(self.pushButton_zstack_flagSetSlices)

        self.label_24 = QLabel(self.frame_56)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.label_24)

        self.pushButton_zstack_flagSetDistance = QPushButton(self.frame_56)
        self.pushButton_zstack_flagSetDistance.setObjectName(u"pushButton_zstack_flagSetDistance")
        self.pushButton_zstack_flagSetDistance.setMinimumSize(QSize(25, 25))
        self.pushButton_zstack_flagSetDistance.setMaximumSize(QSize(25, 25))
        self.pushButton_zstack_flagSetDistance.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/floresansPrefix/whitePressed.png);\n"
"border:none;\n"
"}")

        self.horizontalLayout_40.addWidget(self.pushButton_zstack_flagSetDistance)

        self.label_25 = QLabel(self.frame_56)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.label_25)


        self.verticalLayout_16.addWidget(self.frame_56)

        self.frame_59 = QFrame(self.frame_52)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setMaximumSize(QSize(16777215, 119))
        self.frame_59.setFrameShape(QFrame.NoFrame)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_59)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_zstackExtend = QStackedWidget(self.frame_59)
        self.stackedWidget_zstackExtend.setObjectName(u"stackedWidget_zstackExtend")
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.horizontalLayout_39 = QHBoxLayout(self.page_10)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_69 = QFrame(self.page_10)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.NoFrame)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_69)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_70 = QFrame(self.frame_69)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.NoFrame)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.pushButton_zstack_setDistance = QPushButton(self.frame_70)
        self.pushButton_zstack_setDistance.setObjectName(u"pushButton_zstack_setDistance")
        self.pushButton_zstack_setDistance.setMinimumSize(QSize(130, 35))
        self.pushButton_zstack_setDistance.setMaximumSize(QSize(130, 35))
        self.pushButton_zstack_setDistance.setFont(font)
        self.pushButton_zstack_setDistance.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_37.addWidget(self.pushButton_zstack_setDistance)

        self.lineEdit_zstack_distance = QLineEdit(self.frame_70)
        self.lineEdit_zstack_distance.setObjectName(u"lineEdit_zstack_distance")
        self.lineEdit_zstack_distance.setMinimumSize(QSize(80, 35))
        self.lineEdit_zstack_distance.setMaximumSize(QSize(80, 35))
        self.lineEdit_zstack_distance.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_zstack_distance.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.lineEdit_zstack_distance.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.lineEdit_zstack_distance)


        self.verticalLayout_19.addWidget(self.frame_70)

        self.frame_73 = QFrame(self.frame_69)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.NoFrame)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_74 = QFrame(self.frame_73)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setMinimumSize(QSize(120, 0))
        self.frame_74.setFrameShape(QFrame.NoFrame)
        self.frame_74.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_38.addWidget(self.frame_74)

        self.frame_75 = QFrame(self.frame_73)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setFrameShape(QFrame.NoFrame)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_75)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_zstack_distance = QLabel(self.frame_75)
        self.label_zstack_distance.setObjectName(u"label_zstack_distance")
        self.label_zstack_distance.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(0, 170, 0);")
        self.label_zstack_distance.setAlignment(Qt.AlignCenter)

        self.verticalLayout_44.addWidget(self.label_zstack_distance)


        self.horizontalLayout_38.addWidget(self.frame_75)


        self.verticalLayout_19.addWidget(self.frame_73)


        self.horizontalLayout_39.addWidget(self.frame_69)

        self.stackedWidget_zstackExtend.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.verticalLayout_21 = QVBoxLayout(self.page_11)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_78 = QFrame(self.page_11)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setFrameShape(QFrame.NoFrame)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_78)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.frame_79 = QFrame(self.frame_78)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.NoFrame)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_73 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_73.setSpacing(0)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.horizontalLayout_73.setContentsMargins(0, 0, 0, 0)
        self.pushButton_zstack_setSlices = QPushButton(self.frame_79)
        self.pushButton_zstack_setSlices.setObjectName(u"pushButton_zstack_setSlices")
        self.pushButton_zstack_setSlices.setMinimumSize(QSize(130, 35))
        self.pushButton_zstack_setSlices.setMaximumSize(QSize(130, 35))
        self.pushButton_zstack_setSlices.setFont(font)
        self.pushButton_zstack_setSlices.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_73.addWidget(self.pushButton_zstack_setSlices)

        self.lineEdit_zstack_slices = QLineEdit(self.frame_79)
        self.lineEdit_zstack_slices.setObjectName(u"lineEdit_zstack_slices")
        self.lineEdit_zstack_slices.setMinimumSize(QSize(80, 35))
        self.lineEdit_zstack_slices.setMaximumSize(QSize(80, 35))
        self.lineEdit_zstack_slices.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_zstack_slices.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.lineEdit_zstack_slices.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_73.addWidget(self.lineEdit_zstack_slices)


        self.verticalLayout_42.addWidget(self.frame_79)

        self.frame_122 = QFrame(self.frame_78)
        self.frame_122.setObjectName(u"frame_122")
        self.frame_122.setFrameShape(QFrame.NoFrame)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_74 = QHBoxLayout(self.frame_122)
        self.horizontalLayout_74.setSpacing(0)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalLayout_74.setContentsMargins(0, 0, 0, 0)
        self.frame_123 = QFrame(self.frame_122)
        self.frame_123.setObjectName(u"frame_123")
        self.frame_123.setMinimumSize(QSize(120, 0))
        self.frame_123.setFrameShape(QFrame.NoFrame)
        self.frame_123.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_74.addWidget(self.frame_123)

        self.frame_129 = QFrame(self.frame_122)
        self.frame_129.setObjectName(u"frame_129")
        self.frame_129.setFrameShape(QFrame.NoFrame)
        self.frame_129.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_129)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_zstack_slices = QLabel(self.frame_129)
        self.label_zstack_slices.setObjectName(u"label_zstack_slices")
        self.label_zstack_slices.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(0, 170, 0);")
        self.label_zstack_slices.setAlignment(Qt.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_zstack_slices)


        self.horizontalLayout_74.addWidget(self.frame_129)


        self.verticalLayout_42.addWidget(self.frame_122)


        self.verticalLayout_21.addWidget(self.frame_78)

        self.stackedWidget_zstackExtend.addWidget(self.page_11)

        self.verticalLayout_22.addWidget(self.stackedWidget_zstackExtend)


        self.verticalLayout_16.addWidget(self.frame_59)

        self.frame_57 = QFrame(self.frame_52)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.NoFrame)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_90 = QFrame(self.frame_57)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setFrameShape(QFrame.NoFrame)
        self.frame_90.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_34.addWidget(self.frame_90)

        self.frame_91 = QFrame(self.frame_57)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setFrameShape(QFrame.NoFrame)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.pushButton_zstack_clear = QPushButton(self.frame_91)
        self.pushButton_zstack_clear.setObjectName(u"pushButton_zstack_clear")
        self.pushButton_zstack_clear.setMinimumSize(QSize(80, 35))
        self.pushButton_zstack_clear.setMaximumSize(QSize(120, 35))
        self.pushButton_zstack_clear.setFont(font)
        self.pushButton_zstack_clear.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_43.addWidget(self.pushButton_zstack_clear)


        self.horizontalLayout_34.addWidget(self.frame_91, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.frame_52)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.NoFrame)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.pushButton_zstack_goStack = QPushButton(self.frame_58)
        self.pushButton_zstack_goStack.setObjectName(u"pushButton_zstack_goStack")
        self.pushButton_zstack_goStack.setGeometry(QRect(60, 40, 150, 50))
        self.pushButton_zstack_goStack.setMinimumSize(QSize(150, 50))
        self.pushButton_zstack_goStack.setMaximumSize(QSize(30, 16777215))
        self.pushButton_zstack_goStack.setFont(font)
        self.pushButton_zstack_goStack.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.verticalLayout_16.addWidget(self.frame_58)


        self.horizontalLayout_31.addWidget(self.frame_52)

        self.stackedWidget_rightSide.addWidget(self.page_4)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.horizontalLayout_44 = QHBoxLayout(self.page_7)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.frame_92 = QFrame(self.page_7)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_92)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_93 = QFrame(self.frame_92)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setFrameShape(QFrame.NoFrame)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_93)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_99 = QFrame(self.frame_93)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setMinimumSize(QSize(0, 90))
        self.frame_99.setFrameShape(QFrame.NoFrame)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_99)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_100 = QFrame(self.frame_99)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFrameShape(QFrame.NoFrame)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.label_28 = QLabel(self.frame_100)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(0, 0, 251, 21))
        self.label_28.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.frame_100)

        self.frame_101 = QFrame(self.frame_99)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setFrameShape(QFrame.NoFrame)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.frame_102 = QFrame(self.frame_101)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFrameShape(QFrame.NoFrame)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.pushButton_red_timelapse = QPushButton(self.frame_102)
        self.pushButton_red_timelapse.setObjectName(u"pushButton_red_timelapse")
        self.pushButton_red_timelapse.setMinimumSize(QSize(23, 23))
        self.pushButton_red_timelapse.setMaximumSize(QSize(23, 23))
        self.pushButton_red_timelapse.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"\n"
"	background-image: url(:/floresansPrefix/redUnPressed.png);\n"
"}")

        self.horizontalLayout_46.addWidget(self.pushButton_red_timelapse)

        self.pushButton_green_timelapse = QPushButton(self.frame_102)
        self.pushButton_green_timelapse.setObjectName(u"pushButton_green_timelapse")
        self.pushButton_green_timelapse.setMinimumSize(QSize(23, 23))
        self.pushButton_green_timelapse.setMaximumSize(QSize(23, 23))
        self.pushButton_green_timelapse.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/floresansPrefix/greenUnPressed.png);\n"
"	border:none;\n"
"}")

        self.horizontalLayout_46.addWidget(self.pushButton_green_timelapse)

        self.pushButton_blue_timelapse = QPushButton(self.frame_102)
        self.pushButton_blue_timelapse.setObjectName(u"pushButton_blue_timelapse")
        self.pushButton_blue_timelapse.setMinimumSize(QSize(23, 23))
        self.pushButton_blue_timelapse.setMaximumSize(QSize(23, 23))
        self.pushButton_blue_timelapse.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-image: url(:/floresansPrefix/blueUnPressed.png);\n"
"	border:none;\n"
"}")

        self.horizontalLayout_46.addWidget(self.pushButton_blue_timelapse)

        self.pushButton_uv_timelapse = QPushButton(self.frame_102)
        self.pushButton_uv_timelapse.setObjectName(u"pushButton_uv_timelapse")
        self.pushButton_uv_timelapse.setMinimumSize(QSize(23, 24))
        self.pushButton_uv_timelapse.setMaximumSize(QSize(23, 24))
        self.pushButton_uv_timelapse.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-image: url(:/floresansPrefix/uv_button_unpressed.png);\n"
"	border:none;\n"
"}")

        self.horizontalLayout_46.addWidget(self.pushButton_uv_timelapse)

        self.pushButton_white_timelapse = QPushButton(self.frame_102)
        self.pushButton_white_timelapse.setObjectName(u"pushButton_white_timelapse")
        self.pushButton_white_timelapse.setMinimumSize(QSize(25, 25))
        self.pushButton_white_timelapse.setMaximumSize(QSize(25, 25))
        self.pushButton_white_timelapse.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
"border:none;\n"
"}")

        self.horizontalLayout_46.addWidget(self.pushButton_white_timelapse)


        self.horizontalLayout_45.addWidget(self.frame_102)


        self.verticalLayout_26.addWidget(self.frame_101)


        self.verticalLayout_27.addWidget(self.frame_99)


        self.verticalLayout_25.addWidget(self.frame_93)

        self.frame_94 = QFrame(self.frame_92)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setMinimumSize(QSize(0, 100))
        self.frame_94.setFrameShape(QFrame.NoFrame)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_94)
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_103 = QFrame(self.frame_94)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setFrameShape(QFrame.NoFrame)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_103)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_104 = QFrame(self.frame_103)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setFrameShape(QFrame.NoFrame)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_47.setSpacing(0)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_105 = QFrame(self.frame_104)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setMinimumSize(QSize(140, 0))
        self.frame_105.setFrameShape(QFrame.NoFrame)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.pushButton_timelapse_setMeasurements = QPushButton(self.frame_105)
        self.pushButton_timelapse_setMeasurements.setObjectName(u"pushButton_timelapse_setMeasurements")
        self.pushButton_timelapse_setMeasurements.setGeometry(QRect(10, 10, 120, 35))
        self.pushButton_timelapse_setMeasurements.setMinimumSize(QSize(120, 35))
        self.pushButton_timelapse_setMeasurements.setMaximumSize(QSize(120, 35))
        self.pushButton_timelapse_setMeasurements.setFont(font)
        self.pushButton_timelapse_setMeasurements.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_47.addWidget(self.frame_105)

        self.frame_106 = QFrame(self.frame_104)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setFrameShape(QFrame.NoFrame)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.lineEdit_timelapse_measurements = QLineEdit(self.frame_106)
        self.lineEdit_timelapse_measurements.setObjectName(u"lineEdit_timelapse_measurements")
        self.lineEdit_timelapse_measurements.setGeometry(QRect(20, 10, 80, 35))
        self.lineEdit_timelapse_measurements.setMinimumSize(QSize(80, 35))
        self.lineEdit_timelapse_measurements.setMaximumSize(QSize(80, 35))
        self.lineEdit_timelapse_measurements.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_timelapse_measurements.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1px;\n"
"border-style:inset;\n"
"")
        self.lineEdit_timelapse_measurements.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.frame_106)


        self.verticalLayout_28.addWidget(self.frame_104)

        self.frame_107 = QFrame(self.frame_103)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setFrameShape(QFrame.NoFrame)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_107)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.frame_108 = QFrame(self.frame_107)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setMinimumSize(QSize(140, 0))
        self.frame_108.setFrameShape(QFrame.NoFrame)
        self.frame_108.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_48.addWidget(self.frame_108)

        self.frame_109 = QFrame(self.frame_107)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setFrameShape(QFrame.NoFrame)
        self.frame_109.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_71 = QHBoxLayout(self.frame_109)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_timelapse_measurements = QLabel(self.frame_109)
        self.label_timelapse_measurements.setObjectName(u"label_timelapse_measurements")
        self.label_timelapse_measurements.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(0, 170, 0);")
        self.label_timelapse_measurements.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_71.addWidget(self.label_timelapse_measurements)


        self.horizontalLayout_48.addWidget(self.frame_109)


        self.verticalLayout_28.addWidget(self.frame_107)


        self.verticalLayout_29.addWidget(self.frame_103)


        self.verticalLayout_25.addWidget(self.frame_94)

        self.frame_95 = QFrame(self.frame_92)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMinimumSize(QSize(0, 100))
        self.frame_95.setFrameShape(QFrame.NoFrame)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.frame_95)
        self.horizontalLayout_51.setSpacing(0)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.frame_110 = QFrame(self.frame_95)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setFrameShape(QFrame.NoFrame)
        self.frame_110.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_110)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_111 = QFrame(self.frame_110)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setFrameShape(QFrame.NoFrame)
        self.frame_111.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_111)
        self.horizontalLayout_49.setSpacing(0)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_112 = QFrame(self.frame_111)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setMinimumSize(QSize(140, 0))
        self.frame_112.setFrameShape(QFrame.NoFrame)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.pushButton_timelapse_setInterval = QPushButton(self.frame_112)
        self.pushButton_timelapse_setInterval.setObjectName(u"pushButton_timelapse_setInterval")
        self.pushButton_timelapse_setInterval.setGeometry(QRect(10, 10, 120, 35))
        self.pushButton_timelapse_setInterval.setMinimumSize(QSize(120, 35))
        self.pushButton_timelapse_setInterval.setMaximumSize(QSize(120, 35))
        self.pushButton_timelapse_setInterval.setFont(font)
        self.pushButton_timelapse_setInterval.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_49.addWidget(self.frame_112)

        self.frame_113 = QFrame(self.frame_111)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setFrameShape(QFrame.NoFrame)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.lineEdit_timelapse_interval = QLineEdit(self.frame_113)
        self.lineEdit_timelapse_interval.setObjectName(u"lineEdit_timelapse_interval")
        self.lineEdit_timelapse_interval.setGeometry(QRect(20, 10, 80, 35))
        self.lineEdit_timelapse_interval.setMinimumSize(QSize(80, 35))
        self.lineEdit_timelapse_interval.setMaximumSize(QSize(80, 35))
        self.lineEdit_timelapse_interval.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_timelapse_interval.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.lineEdit_timelapse_interval.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.frame_113)


        self.verticalLayout_30.addWidget(self.frame_111)

        self.frame_114 = QFrame(self.frame_110)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setFrameShape(QFrame.NoFrame)
        self.frame_114.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_50 = QHBoxLayout(self.frame_114)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.frame_115 = QFrame(self.frame_114)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setMinimumSize(QSize(140, 0))
        self.frame_115.setFrameShape(QFrame.NoFrame)
        self.frame_115.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_50.addWidget(self.frame_115)

        self.frame_116 = QFrame(self.frame_114)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setFrameShape(QFrame.NoFrame)
        self.frame_116.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_72 = QHBoxLayout(self.frame_116)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_timelapse_interval = QLabel(self.frame_116)
        self.label_timelapse_interval.setObjectName(u"label_timelapse_interval")
        self.label_timelapse_interval.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(0, 170, 0);")
        self.label_timelapse_interval.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_72.addWidget(self.label_timelapse_interval)


        self.horizontalLayout_50.addWidget(self.frame_116)


        self.verticalLayout_30.addWidget(self.frame_114)


        self.horizontalLayout_51.addWidget(self.frame_110)


        self.verticalLayout_25.addWidget(self.frame_95)

        self.frame_71 = QFrame(self.frame_92)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_71)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.pushButton_timelapse_clear = QPushButton(self.frame_71)
        self.pushButton_timelapse_clear.setObjectName(u"pushButton_timelapse_clear")
        self.pushButton_timelapse_clear.setMinimumSize(QSize(80, 35))
        self.pushButton_timelapse_clear.setMaximumSize(QSize(120, 35))
        self.pushButton_timelapse_clear.setFont(font)
        self.pushButton_timelapse_clear.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.verticalLayout_20.addWidget(self.pushButton_timelapse_clear)


        self.verticalLayout_25.addWidget(self.frame_71, 0, Qt.AlignRight)

        self.frame_96 = QFrame(self.frame_92)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFrameShape(QFrame.NoFrame)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_64 = QHBoxLayout(self.frame_96)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.pushButton_zStackExtend = QPushButton(self.frame_96)
        self.pushButton_zStackExtend.setObjectName(u"pushButton_zStackExtend")
        self.pushButton_zStackExtend.setMinimumSize(QSize(25, 25))
        self.pushButton_zStackExtend.setMaximumSize(QSize(25, 25))
        self.pushButton_zStackExtend.setStyleSheet(u"QPushButton{\n"
"background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
"border:none;\n"
"}")

        self.horizontalLayout_64.addWidget(self.pushButton_zStackExtend)

        self.label_35 = QLabel(self.frame_96)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(150, 0))
        self.label_35.setMaximumSize(QSize(150, 16777215))
        self.label_35.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_35.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_64.addWidget(self.label_35)


        self.verticalLayout_25.addWidget(self.frame_96, 0, Qt.AlignLeft)

        self.frame_97 = QFrame(self.frame_92)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setMinimumSize(QSize(0, 350))
        self.frame_97.setMaximumSize(QSize(16777215, 350))
        self.frame_97.setFrameShape(QFrame.NoFrame)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_97)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_140 = QFrame(self.frame_97)
        self.frame_140.setObjectName(u"frame_140")
        self.frame_140.setFrameShape(QFrame.NoFrame)
        self.frame_140.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_140)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_144 = QFrame(self.frame_140)
        self.frame_144.setObjectName(u"frame_144")
        self.frame_144.setFrameShape(QFrame.NoFrame)
        self.frame_144.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_61 = QHBoxLayout(self.frame_144)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_zStack = QStackedWidget(self.frame_144)
        self.stackedWidget_zStack.setObjectName(u"stackedWidget_zStack")
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.horizontalLayout_54 = QHBoxLayout(self.page_8)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.frame_117 = QFrame(self.page_8)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setFrameShape(QFrame.NoFrame)
        self.frame_117.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_117)
        self.verticalLayout_49.setSpacing(0)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.frame_121 = QFrame(self.frame_117)
        self.frame_121.setObjectName(u"frame_121")
        self.frame_121.setMaximumSize(QSize(16777215, 60))
        self.frame_121.setFrameShape(QFrame.NoFrame)
        self.frame_121.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_121)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_124 = QFrame(self.frame_121)
        self.frame_124.setObjectName(u"frame_124")
        self.frame_124.setMinimumSize(QSize(0, 60))
        self.frame_124.setFrameShape(QFrame.NoFrame)
        self.frame_124.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_124)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_125 = QFrame(self.frame_124)
        self.frame_125.setObjectName(u"frame_125")
        self.frame_125.setMinimumSize(QSize(0, 25))
        self.frame_125.setMaximumSize(QSize(16777215, 25))
        self.frame_125.setFrameShape(QFrame.NoFrame)
        self.frame_125.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_56 = QHBoxLayout(self.frame_125)
        self.horizontalLayout_56.setSpacing(0)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.pushButton_timelapse_zstackSetStart = QPushButton(self.frame_125)
        self.pushButton_timelapse_zstackSetStart.setObjectName(u"pushButton_timelapse_zstackSetStart")
        self.pushButton_timelapse_zstackSetStart.setMinimumSize(QSize(130, 25))
        self.pushButton_timelapse_zstackSetStart.setMaximumSize(QSize(130, 25))
        self.pushButton_timelapse_zstackSetStart.setFont(font)
        self.pushButton_timelapse_zstackSetStart.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_56.addWidget(self.pushButton_timelapse_zstackSetStart)

        self.lineEdit_timelapse_zstackStart = QLineEdit(self.frame_125)
        self.lineEdit_timelapse_zstackStart.setObjectName(u"lineEdit_timelapse_zstackStart")
        self.lineEdit_timelapse_zstackStart.setMinimumSize(QSize(80, 25))
        self.lineEdit_timelapse_zstackStart.setMaximumSize(QSize(80, 25))
        self.lineEdit_timelapse_zstackStart.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_timelapse_zstackStart.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.lineEdit_timelapse_zstackStart.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_56.addWidget(self.lineEdit_timelapse_zstackStart)


        self.verticalLayout_33.addWidget(self.frame_125)

        self.frame_128 = QFrame(self.frame_124)
        self.frame_128.setObjectName(u"frame_128")
        self.frame_128.setMinimumSize(QSize(0, 25))
        self.frame_128.setMaximumSize(QSize(16777215, 25))
        self.frame_128.setFrameShape(QFrame.NoFrame)
        self.frame_128.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_128)
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.frame_130 = QFrame(self.frame_128)
        self.frame_130.setObjectName(u"frame_130")
        self.frame_130.setMinimumSize(QSize(140, 0))
        self.frame_130.setMaximumSize(QSize(16777215, 100))
        self.frame_130.setFrameShape(QFrame.NoFrame)
        self.frame_130.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_57.addWidget(self.frame_130)

        self.frame_131 = QFrame(self.frame_128)
        self.frame_131.setObjectName(u"frame_131")
        self.frame_131.setFrameShape(QFrame.NoFrame)
        self.frame_131.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_131)
        self.verticalLayout_51.setSpacing(0)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_timelapse_zstackStart = QLabel(self.frame_131)
        self.label_timelapse_zstackStart.setObjectName(u"label_timelapse_zstackStart")
        self.label_timelapse_zstackStart.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(0, 170, 0);")
        self.label_timelapse_zstackStart.setAlignment(Qt.AlignCenter)

        self.verticalLayout_51.addWidget(self.label_timelapse_zstackStart)


        self.horizontalLayout_57.addWidget(self.frame_131)


        self.verticalLayout_33.addWidget(self.frame_128)


        self.verticalLayout_32.addWidget(self.frame_124)


        self.verticalLayout_49.addWidget(self.frame_121)

        self.frame_72 = QFrame(self.frame_117)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMinimumSize(QSize(0, 50))
        self.frame_72.setMaximumSize(QSize(16777215, 60))
        self.frame_72.setFrameShape(QFrame.NoFrame)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_72)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_76 = QFrame(self.frame_72)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.NoFrame)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_53.setSpacing(0)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.pushButton_timelapse_zstackSetEnd = QPushButton(self.frame_76)
        self.pushButton_timelapse_zstackSetEnd.setObjectName(u"pushButton_timelapse_zstackSetEnd")
        self.pushButton_timelapse_zstackSetEnd.setMinimumSize(QSize(130, 25))
        self.pushButton_timelapse_zstackSetEnd.setMaximumSize(QSize(130, 25))
        self.pushButton_timelapse_zstackSetEnd.setFont(font)
        self.pushButton_timelapse_zstackSetEnd.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_53.addWidget(self.pushButton_timelapse_zstackSetEnd)

        self.lineEdit_timelapse_zstackEnd = QLineEdit(self.frame_76)
        self.lineEdit_timelapse_zstackEnd.setObjectName(u"lineEdit_timelapse_zstackEnd")
        self.lineEdit_timelapse_zstackEnd.setMinimumSize(QSize(80, 25))
        self.lineEdit_timelapse_zstackEnd.setMaximumSize(QSize(80, 25))
        self.lineEdit_timelapse_zstackEnd.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_timelapse_zstackEnd.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.lineEdit_timelapse_zstackEnd.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.lineEdit_timelapse_zstackEnd)


        self.verticalLayout_31.addWidget(self.frame_76)

        self.frame_81 = QFrame(self.frame_72)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMinimumSize(QSize(0, 40))
        self.frame_81.setMaximumSize(QSize(16777215, 16777215))
        self.frame_81.setFrameShape(QFrame.NoFrame)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_55.setSpacing(0)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.frame_82 = QFrame(self.frame_81)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setMinimumSize(QSize(140, 30))
        self.frame_82.setMaximumSize(QSize(16777215, 30))
        self.frame_82.setFrameShape(QFrame.NoFrame)
        self.frame_82.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_55.addWidget(self.frame_82)

        self.frame_120 = QFrame(self.frame_81)
        self.frame_120.setObjectName(u"frame_120")
        self.frame_120.setMinimumSize(QSize(0, 0))
        self.frame_120.setMaximumSize(QSize(16777215, 16777215))
        self.frame_120.setFrameShape(QFrame.NoFrame)
        self.frame_120.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_120)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_timelapse_zstackEnd = QLabel(self.frame_120)
        self.label_timelapse_zstackEnd.setObjectName(u"label_timelapse_zstackEnd")
        self.label_timelapse_zstackEnd.setMinimumSize(QSize(0, 0))
        self.label_timelapse_zstackEnd.setMaximumSize(QSize(16777215, 16777215))
        self.label_timelapse_zstackEnd.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(0, 170, 0);")
        self.label_timelapse_zstackEnd.setAlignment(Qt.AlignCenter)

        self.verticalLayout_52.addWidget(self.label_timelapse_zstackEnd)


        self.horizontalLayout_55.addWidget(self.frame_120)


        self.verticalLayout_31.addWidget(self.frame_81)


        self.verticalLayout_49.addWidget(self.frame_72)

        self.frame_135 = QFrame(self.frame_117)
        self.frame_135.setObjectName(u"frame_135")
        self.frame_135.setMinimumSize(QSize(0, 40))
        self.frame_135.setMaximumSize(QSize(16777215, 40))
        self.frame_135.setFrameShape(QFrame.NoFrame)
        self.frame_135.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_60 = QHBoxLayout(self.frame_135)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.pushButton_timelapse_flagSetSlices = QPushButton(self.frame_135)
        self.pushButton_timelapse_flagSetSlices.setObjectName(u"pushButton_timelapse_flagSetSlices")
        self.pushButton_timelapse_flagSetSlices.setMinimumSize(QSize(25, 25))
        self.pushButton_timelapse_flagSetSlices.setMaximumSize(QSize(25, 25))
        self.pushButton_timelapse_flagSetSlices.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
"border:none;\n"
"}")

        self.horizontalLayout_60.addWidget(self.pushButton_timelapse_flagSetSlices)

        self.label_26 = QLabel(self.frame_135)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.label_26)

        self.pushButton_timelapse_flagSetDistance = QPushButton(self.frame_135)
        self.pushButton_timelapse_flagSetDistance.setObjectName(u"pushButton_timelapse_flagSetDistance")
        self.pushButton_timelapse_flagSetDistance.setMinimumSize(QSize(25, 25))
        self.pushButton_timelapse_flagSetDistance.setMaximumSize(QSize(25, 25))
        self.pushButton_timelapse_flagSetDistance.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/floresansPrefix/whitePressed.png);\n"
"border:none;\n"
"}")

        self.horizontalLayout_60.addWidget(self.pushButton_timelapse_flagSetDistance)

        self.label_27 = QLabel(self.frame_135)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.label_27)


        self.verticalLayout_49.addWidget(self.frame_135)

        self.frame_136 = QFrame(self.frame_117)
        self.frame_136.setObjectName(u"frame_136")
        self.frame_136.setMaximumSize(QSize(16777215, 60))
        self.frame_136.setFrameShape(QFrame.NoFrame)
        self.frame_136.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_136)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_timelapseZstackExtend = QStackedWidget(self.frame_136)
        self.stackedWidget_timelapseZstackExtend.setObjectName(u"stackedWidget_timelapseZstackExtend")
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.horizontalLayout_62 = QHBoxLayout(self.page_12)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.frame_137 = QFrame(self.page_12)
        self.frame_137.setObjectName(u"frame_137")
        self.frame_137.setFrameShape(QFrame.NoFrame)
        self.frame_137.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_137)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.frame_138 = QFrame(self.frame_137)
        self.frame_138.setObjectName(u"frame_138")
        self.frame_138.setFrameShape(QFrame.NoFrame)
        self.frame_138.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_138)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.pushButton_timelapse_zstackSetDistance = QPushButton(self.frame_138)
        self.pushButton_timelapse_zstackSetDistance.setObjectName(u"pushButton_timelapse_zstackSetDistance")
        self.pushButton_timelapse_zstackSetDistance.setMinimumSize(QSize(130, 25))
        self.pushButton_timelapse_zstackSetDistance.setMaximumSize(QSize(130, 25))
        self.pushButton_timelapse_zstackSetDistance.setFont(font)
        self.pushButton_timelapse_zstackSetDistance.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_63.addWidget(self.pushButton_timelapse_zstackSetDistance)

        self.lineEdit_timelapse_zstackDistance = QLineEdit(self.frame_138)
        self.lineEdit_timelapse_zstackDistance.setObjectName(u"lineEdit_timelapse_zstackDistance")
        self.lineEdit_timelapse_zstackDistance.setMinimumSize(QSize(80, 25))
        self.lineEdit_timelapse_zstackDistance.setMaximumSize(QSize(80, 25))
        self.lineEdit_timelapse_zstackDistance.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_timelapse_zstackDistance.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.lineEdit_timelapse_zstackDistance.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.lineEdit_timelapse_zstackDistance)


        self.verticalLayout_37.addWidget(self.frame_138)

        self.frame_139 = QFrame(self.frame_137)
        self.frame_139.setObjectName(u"frame_139")
        self.frame_139.setFrameShape(QFrame.NoFrame)
        self.frame_139.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_65 = QHBoxLayout(self.frame_139)
        self.horizontalLayout_65.setSpacing(0)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.frame_141 = QFrame(self.frame_139)
        self.frame_141.setObjectName(u"frame_141")
        self.frame_141.setMinimumSize(QSize(140, 0))
        self.frame_141.setMaximumSize(QSize(16777215, 140))
        self.frame_141.setFrameShape(QFrame.NoFrame)
        self.frame_141.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_65.addWidget(self.frame_141)

        self.frame_142 = QFrame(self.frame_139)
        self.frame_142.setObjectName(u"frame_142")
        self.frame_142.setFrameShape(QFrame.NoFrame)
        self.frame_142.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_142)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_timelapse_zstackDistance = QLabel(self.frame_142)
        self.label_timelapse_zstackDistance.setObjectName(u"label_timelapse_zstackDistance")
        self.label_timelapse_zstackDistance.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(0, 170, 0);")
        self.label_timelapse_zstackDistance.setAlignment(Qt.AlignCenter)

        self.verticalLayout_45.addWidget(self.label_timelapse_zstackDistance)


        self.horizontalLayout_65.addWidget(self.frame_142)


        self.verticalLayout_37.addWidget(self.frame_139)


        self.horizontalLayout_62.addWidget(self.frame_137)

        self.stackedWidget_timelapseZstackExtend.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.verticalLayout_46 = QVBoxLayout(self.page_13)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.frame_143 = QFrame(self.page_13)
        self.frame_143.setObjectName(u"frame_143")
        self.frame_143.setFrameShape(QFrame.NoFrame)
        self.frame_143.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_143)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_145 = QFrame(self.frame_143)
        self.frame_145.setObjectName(u"frame_145")
        self.frame_145.setFrameShape(QFrame.NoFrame)
        self.frame_145.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_75 = QHBoxLayout(self.frame_145)
        self.horizontalLayout_75.setSpacing(0)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.horizontalLayout_75.setContentsMargins(0, 0, 0, 0)
        self.pushButton_timelapse_zstackSetSlices = QPushButton(self.frame_145)
        self.pushButton_timelapse_zstackSetSlices.setObjectName(u"pushButton_timelapse_zstackSetSlices")
        self.pushButton_timelapse_zstackSetSlices.setMinimumSize(QSize(130, 25))
        self.pushButton_timelapse_zstackSetSlices.setMaximumSize(QSize(130, 25))
        self.pushButton_timelapse_zstackSetSlices.setFont(font)
        self.pushButton_timelapse_zstackSetSlices.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_75.addWidget(self.pushButton_timelapse_zstackSetSlices)

        self.lineEdit_timelapse_zstackSlices = QLineEdit(self.frame_145)
        self.lineEdit_timelapse_zstackSlices.setObjectName(u"lineEdit_timelapse_zstackSlices")
        self.lineEdit_timelapse_zstackSlices.setMinimumSize(QSize(80, 25))
        self.lineEdit_timelapse_zstackSlices.setMaximumSize(QSize(80, 25))
        self.lineEdit_timelapse_zstackSlices.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit_timelapse_zstackSlices.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1px;\n"
"border-style:inset;")
        self.lineEdit_timelapse_zstackSlices.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_75.addWidget(self.lineEdit_timelapse_zstackSlices)


        self.verticalLayout_47.addWidget(self.frame_145)

        self.frame_146 = QFrame(self.frame_143)
        self.frame_146.setObjectName(u"frame_146")
        self.frame_146.setFrameShape(QFrame.NoFrame)
        self.frame_146.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_76 = QHBoxLayout(self.frame_146)
        self.horizontalLayout_76.setSpacing(0)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.frame_147 = QFrame(self.frame_146)
        self.frame_147.setObjectName(u"frame_147")
        self.frame_147.setMinimumSize(QSize(140, 0))
        self.frame_147.setFrameShape(QFrame.NoFrame)
        self.frame_147.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_76.addWidget(self.frame_147)

        self.frame_148 = QFrame(self.frame_146)
        self.frame_148.setObjectName(u"frame_148")
        self.frame_148.setFrameShape(QFrame.NoFrame)
        self.frame_148.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_148)
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_timelapse_zstackSlices = QLabel(self.frame_148)
        self.label_timelapse_zstackSlices.setObjectName(u"label_timelapse_zstackSlices")
        self.label_timelapse_zstackSlices.setStyleSheet(u"font: 75 16pt \"Segoe UI\";\n"
"color: rgb(0, 170, 0);")
        self.label_timelapse_zstackSlices.setAlignment(Qt.AlignCenter)

        self.verticalLayout_48.addWidget(self.label_timelapse_zstackSlices)


        self.horizontalLayout_76.addWidget(self.frame_148)


        self.verticalLayout_47.addWidget(self.frame_146)


        self.verticalLayout_46.addWidget(self.frame_143)

        self.stackedWidget_timelapseZstackExtend.addWidget(self.page_13)

        self.verticalLayout_36.addWidget(self.stackedWidget_timelapseZstackExtend)


        self.verticalLayout_49.addWidget(self.frame_136)

        self.frame_132 = QFrame(self.frame_117)
        self.frame_132.setObjectName(u"frame_132")
        self.frame_132.setMinimumSize(QSize(0, 30))
        self.frame_132.setMaximumSize(QSize(16777215, 30))
        self.frame_132.setFrameShape(QFrame.NoFrame)
        self.frame_132.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_132)
        self.verticalLayout_50.setSpacing(0)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.pushButton_timelapse_zstackClear = QPushButton(self.frame_132)
        self.pushButton_timelapse_zstackClear.setObjectName(u"pushButton_timelapse_zstackClear")
        self.pushButton_timelapse_zstackClear.setMinimumSize(QSize(80, 25))
        self.pushButton_timelapse_zstackClear.setMaximumSize(QSize(120, 25))
        self.pushButton_timelapse_zstackClear.setFont(font)
        self.pushButton_timelapse_zstackClear.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.verticalLayout_50.addWidget(self.pushButton_timelapse_zstackClear)


        self.verticalLayout_49.addWidget(self.frame_132, 0, Qt.AlignRight)


        self.horizontalLayout_54.addWidget(self.frame_117)

        self.stackedWidget_zStack.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.verticalLayout_39 = QVBoxLayout(self.page_9)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.frame_155 = QFrame(self.page_9)
        self.frame_155.setObjectName(u"frame_155")
        self.frame_155.setFrameShape(QFrame.StyledPanel)
        self.frame_155.setFrameShadow(QFrame.Raised)

        self.verticalLayout_39.addWidget(self.frame_155)

        self.stackedWidget_zStack.addWidget(self.page_9)

        self.horizontalLayout_61.addWidget(self.stackedWidget_zStack)


        self.verticalLayout_34.addWidget(self.frame_144)


        self.verticalLayout_35.addWidget(self.frame_140)


        self.verticalLayout_25.addWidget(self.frame_97)

        self.frame_98 = QFrame(self.frame_92)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMinimumSize(QSize(0, 60))
        self.frame_98.setFrameShape(QFrame.NoFrame)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_98)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.frame_151 = QFrame(self.frame_98)
        self.frame_151.setObjectName(u"frame_151")
        self.frame_151.setFrameShape(QFrame.NoFrame)
        self.frame_151.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_68 = QHBoxLayout(self.frame_151)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.pushButton_goTimelapse = QPushButton(self.frame_151)
        self.pushButton_goTimelapse.setObjectName(u"pushButton_goTimelapse")
        self.pushButton_goTimelapse.setMinimumSize(QSize(150, 50))
        self.pushButton_goTimelapse.setMaximumSize(QSize(50, 16777215))
        self.pushButton_goTimelapse.setFont(font)
        self.pushButton_goTimelapse.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(49, 51, 50);\n"
"border-radius:8px;\n"
"border-color: rgb(255,255, 255);\n"
"border-width : 1.2px;\n"
"border-style:inset;\n"
"color:rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")

        self.horizontalLayout_68.addWidget(self.pushButton_goTimelapse)


        self.verticalLayout_38.addWidget(self.frame_151)


        self.verticalLayout_25.addWidget(self.frame_98)


        self.horizontalLayout_44.addWidget(self.frame_92)

        self.stackedWidget_rightSide.addWidget(self.page_7)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.horizontalLayout_96 = QHBoxLayout(self.page_16)
        self.horizontalLayout_96.setSpacing(0)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.frame_182 = QFrame(self.page_16)
        self.frame_182.setObjectName(u"frame_182")
        self.frame_182.setFrameShape(QFrame.NoFrame)
        self.frame_182.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_96.addWidget(self.frame_182)

        self.stackedWidget_rightSide.addWidget(self.page_16)

        self.verticalLayout_3.addWidget(self.stackedWidget_rightSide)


        self.horizontalLayout_5.addWidget(self.frame_10)


        self.horizontalLayout_4.addWidget(self.frame_8)

        self.stackedWidget_main.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_40 = QVBoxLayout(self.page_2)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_52 = QHBoxLayout(self.frame)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.frame_119 = QFrame(self.frame)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setFrameShape(QFrame.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_52.addWidget(self.frame_119)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_2)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_158 = QFrame(self.frame_2)
        self.frame_158.setObjectName(u"frame_158")
        self.frame_158.setFrameShape(QFrame.StyledPanel)
        self.frame_158.setFrameShadow(QFrame.Raised)

        self.verticalLayout_41.addWidget(self.frame_158)

        self.frame_118 = QFrame(self.frame_2)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setMinimumSize(QSize(0, 400))
        self.frame_118.setFrameShape(QFrame.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Raised)
        self.circularProgressBarBase = QFrame(self.frame_118)
        self.circularProgressBarBase.setObjectName(u"circularProgressBarBase")
        self.circularProgressBarBase.setGeometry(QRect(90, 10, 300, 300))
        self.circularProgressBarBase.setFrameShape(QFrame.NoFrame)
        self.circularProgressBarBase.setFrameShadow(QFrame.Raised)
        self.circularProgress_loading1 = QFrame(self.circularProgressBarBase)
        self.circularProgress_loading1.setObjectName(u"circularProgress_loading1")
        self.circularProgress_loading1.setGeometry(QRect(10, 10, 280, 280))
        self.circularProgress_loading1.setStyleSheet(u"QFrame{\n"
"border-radius:140px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"\n"
"}")
        self.circularProgress_loading1.setFrameShape(QFrame.NoFrame)
        self.circularProgress_loading1.setFrameShadow(QFrame.Raised)
        self.circularBg_2 = QFrame(self.circularProgressBarBase)
        self.circularBg_2.setObjectName(u"circularBg_2")
        self.circularBg_2.setGeometry(QRect(10, 10, 280, 280))
        self.circularBg_2.setStyleSheet(u"QFrame{\n"
"border-radius:140px;\n"
"background-color: rgba(77, 77, 127,100);\n"
"}\n"
"")
        self.circularBg_2.setFrameShape(QFrame.NoFrame)
        self.circularBg_2.setFrameShadow(QFrame.Raised)
        self.container_2 = QFrame(self.circularProgressBarBase)
        self.container_2.setObjectName(u"container_2")
        self.container_2.setGeometry(QRect(20, 20, 260, 260))
        self.container_2.setStyleSheet(u"QFrame{\n"
"	border-radius:130px;\n"
"	background-color: rgb(77, 77, 127);	\n"
"}\n"
"")
        self.container_2.setFrameShape(QFrame.NoFrame)
        self.container_2.setFrameShadow(QFrame.Raised)
        self.circularProgress_loading2 = QFrame(self.circularProgressBarBase)
        self.circularProgress_loading2.setObjectName(u"circularProgress_loading2")
        self.circularProgress_loading2.setGeometry(QRect(30, 30, 241, 241))
        self.circularProgress_loading2.setStyleSheet(u"QFrame{\n"
"border-radius:120px;\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"\n"
"}")
        self.circularProgress_loading2.setFrameShape(QFrame.NoFrame)
        self.circularProgress_loading2.setFrameShadow(QFrame.Raised)
        self.container2 = QFrame(self.circularProgressBarBase)
        self.container2.setObjectName(u"container2")
        self.container2.setGeometry(QRect(40, 40, 220, 220))
        self.container2.setStyleSheet(u"QFrame{\n"
"	border-radius:110px;\n"
"	background-color: rgb(77, 77, 127);	\n"
"}")
        self.container2.setFrameShape(QFrame.NoFrame)
        self.container2.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.container2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 60, 171, 81))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color:none;\n"
"color:rgb(255,255,255);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.circularBg_2.raise_()
        self.circularProgress_loading1.raise_()
        self.container_2.raise_()
        self.circularProgress_loading2.raise_()
        self.container2.raise_()

        self.verticalLayout_41.addWidget(self.frame_118)

        self.frame_157 = QFrame(self.frame_2)
        self.frame_157.setObjectName(u"frame_157")
        self.frame_157.setFrameShape(QFrame.StyledPanel)
        self.frame_157.setFrameShadow(QFrame.Raised)

        self.verticalLayout_41.addWidget(self.frame_157)


        self.horizontalLayout_52.addWidget(self.frame_2)

        self.frame_156 = QFrame(self.frame)
        self.frame_156.setObjectName(u"frame_156")
        self.frame_156.setFrameShape(QFrame.StyledPanel)
        self.frame_156.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_52.addWidget(self.frame_156)


        self.verticalLayout_40.addWidget(self.frame)

        self.stackedWidget_main.addWidget(self.page_2)

        self.horizontalLayout_3.addWidget(self.stackedWidget_main)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_minimized.setDefault(False)
        self.pushButton_close.setDefault(False)
        self.stackedWidget_main.setCurrentIndex(0)
        self.stackedWidget_leftSide.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_preview.setDefault(False)
        self.pushButton_zStack.setDefault(False)
        self.pushButton_timelapse.setDefault(False)
        self.pushButton_result.setDefault(False)
        self.stackedWidget_rightSide.setCurrentIndex(1)
        self.stackedWidget_zstackExtend.setCurrentIndex(1)
        self.stackedWidget_zStack.setCurrentIndex(0)
        self.stackedWidget_timelapseZstackExtend.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.pushButton_minimized.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_minimized.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_close.setText("")
        self.pushButton_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Coarse", None))
        self.pushButton_coarse.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Fine", None))
        self.pushButton_fine.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Step Mode", None))
        self.pushButton_stepMode.setText("")
        self.pushButton_Z_up.setText("")
        self.pushButton_Z_down.setText("")
        self.pushButton_Y_up.setText("")
        self.pushButton_Y_down.setText("")
        self.pushButton_X_left.setText("")
        self.pushButton_X_right.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"X :", None))
        self.lineEdit_X_position.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Y :", None))
        self.lineEdit_Y_position.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Z :", None))
        self.lineEdit_Z_position.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.pushButton_goAbsulutePosition.setText(QCoreApplication.translate("MainWindow", u"GO", None))
        self.result_left_picturebox1.setText("")
        self.pushButton_color_1.setText("")
        self.result_left_picturebox2.setText("")
        self.pushButton_color_2.setText("")
        self.result_left_picturebox3.setText("")
        self.pushButton_color_3.setText("")
        self.result_left_picturebox4.setText("")
        self.pushButton_color_4.setText("")
        self.result_left_picturebox5.setText("")
        self.pushButton_color_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.pushButton_preview.setText("")
        self.pushButton_zStack.setText("")
        self.pushButton_timelapse.setText("")
        self.pushButton_result.setText("")
        self.label_redChannel_led.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"RED", None))
        self.pushButton_red_intensity.setText("")
        self.label_greenChannel_led.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"GREEN", None))
        self.pushButton_green_intensity.setText("")
        self.label_blueChannel_led.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"BLUE", None))
        self.pushButton_blue_intensity.setText("")
        self.label_uvChannel_led.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"UV", None))
        self.pushButton_uv_intensity.setText("")
        self.label_whiteChannel_led.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"WHITE", None))
        self.pushButton_white_intensity.setText("")
        self.label_exposure.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_gain.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Exposure", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.pushButton_red_capture.setText("")
        self.pushButton_green_capture.setText("")
        self.pushButton_blue_capture.setText("")
        self.pushButton_uv_capture.setText("")
        self.pushButton_white_capture.setText("")
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"CAPTURE", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Emission Colors", None))
        self.pushButton_red_zstack.setText("")
        self.pushButton_green_zstack.setText("")
        self.pushButton_blue_zstack.setText("")
        self.pushButton_uv_zstack.setText("")
        self.pushButton_white_zstack.setText("")
        self.pushButton_zstack_setStart.setText(QCoreApplication.translate("MainWindow", u"Set Stack Start", None))
        self.lineEdit_zstack_zstackStart.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_zstack_start.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.pushButton_zstack_setEnd.setText(QCoreApplication.translate("MainWindow", u"Set Stack End", None))
        self.lineEdit_zstack_zstackEnd.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_zstack_end.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.pushButton_zstack_flagSetSlices.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Slice", None))
        self.pushButton_zstack_flagSetDistance.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Distance", None))
        self.pushButton_zstack_setDistance.setText(QCoreApplication.translate("MainWindow", u"Set Distance (mm)", None))
        self.lineEdit_zstack_distance.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_zstack_distance.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.pushButton_zstack_setSlices.setText(QCoreApplication.translate("MainWindow", u"# Slices", None))
        self.lineEdit_zstack_slices.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_zstack_slices.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.pushButton_zstack_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_zstack_goStack.setText(QCoreApplication.translate("MainWindow", u"START STACK", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Emission Colors", None))
        self.pushButton_red_timelapse.setText("")
        self.pushButton_green_timelapse.setText("")
        self.pushButton_blue_timelapse.setText("")
        self.pushButton_uv_timelapse.setText("")
        self.pushButton_white_timelapse.setText("")
        self.pushButton_timelapse_setMeasurements.setText(QCoreApplication.translate("MainWindow", u"# Measurements", None))
        self.lineEdit_timelapse_measurements.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_timelapse_measurements.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.pushButton_timelapse_setInterval.setText(QCoreApplication.translate("MainWindow", u"Set Interval (min)", None))
        self.lineEdit_timelapse_interval.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_timelapse_interval.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.pushButton_timelapse_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_zStackExtend.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Z-Stack", None))
        self.pushButton_timelapse_zstackSetStart.setText(QCoreApplication.translate("MainWindow", u"Set Stack Start", None))
        self.lineEdit_timelapse_zstackStart.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_timelapse_zstackStart.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.pushButton_timelapse_zstackSetEnd.setText(QCoreApplication.translate("MainWindow", u"Set Stack End", None))
        self.lineEdit_timelapse_zstackEnd.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_timelapse_zstackEnd.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.pushButton_timelapse_flagSetSlices.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Slice", None))
        self.pushButton_timelapse_flagSetDistance.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Distance", None))
        self.pushButton_timelapse_zstackSetDistance.setText(QCoreApplication.translate("MainWindow", u"Set Distance (mm)", None))
        self.lineEdit_timelapse_zstackDistance.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_timelapse_zstackDistance.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.pushButton_timelapse_zstackSetSlices.setText(QCoreApplication.translate("MainWindow", u"# Slices", None))
        self.lineEdit_timelapse_zstackSlices.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.label_timelapse_zstackSlices.setText(QCoreApplication.translate("MainWindow", u"0.000", None))
        self.pushButton_timelapse_zstackClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_goTimelapse.setText(QCoreApplication.translate("MainWindow", u"START TIMELAPSE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<strong>Loading</strong>...", None))
    # retranslateUi

