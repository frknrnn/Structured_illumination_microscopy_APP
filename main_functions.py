import sys
import platform
import time
import threading
from PySide2 import  QtCore,QtGui,QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_main import Ui_MainWindow
from cncStage import cncPort
GLOBAL_STATE=0
import floresans_icons_rc
import arducam_config_parser
import ArducamSDK
from camera import cam
import numpy as np

#######################################
## QtDesignerda tasarım güncellenince ui_main.py üzerinden zoom.py klasörünü import edip picturebox objesini güncellemen gerekli.
## Result kısmında bulunan picturebox'ın güncellenmesi gerekli.
#######################################


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.__press_pos = QPoint()

        self.windowFlag=False #False minimize True maximize
        self.ui.pushButton_close.clicked.connect(self.APP_EXİT)
        self.ui.pushButton_minimized.clicked.connect(self.minimized_window)
        self.ui.pushButton_zStack.clicked.connect(self.showZStack)
        self.ui.pushButton_preview.clicked.connect(self.showPreview)
        self.ui.pushButton_timelapse.clicked.connect(self.showTimeLapse)
        self.ui.pushButton_zStackExtend.clicked.connect(self.showZStackExtend)
        self.ui.pushButton_result.clicked.connect(self.showResult)

        self.ui.pushButton_Z_up.pressed.connect(self.pushButtonZ_up_mouseDown)
        self.ui.pushButton_Z_up.released.connect(self.pushButtonZ_up_mouseUp)
        self.ui.pushButton_Z_down.pressed.connect(self.pushButtonZ_down_mouseDown)
        self.ui.pushButton_Z_down.released.connect(self.pushButtonZ_down_mouseUp)
        self.ui.pushButton_X_left.pressed.connect(self.pushButtonX_down_mouseDown)
        self.ui.pushButton_X_left.released.connect(self.pushButtonX_down_mouseUp)
        self.ui.pushButton_X_right.pressed.connect(self.pushButtonX_up_mouseDown)
        self.ui.pushButton_X_right.released.connect(self.pushButtonX_up_mouseUp)
        self.ui.pushButton_Y_up.pressed.connect(self.pushButtonY_up_mouseDown)
        self.ui.pushButton_Y_up.released.connect(self.pushButtonY_up_mouseUp)
        self.ui.pushButton_Y_down.pressed.connect(self.pushButtonY_down_mouseDown)
        self.ui.pushButton_Y_down.released.connect(self.pushButtonY_down_mouseUp)
        self.ui.horizontalSlider_red.valueChanged.connect(self.red_ledChannel_intensity)
        self.ui.horizontalSlider_green.valueChanged.connect(self.green_ledChannel_intensity)
        self.ui.horizontalSlider_blue.valueChanged.connect(self.blue_ledChannel_intensity)
        self.ui.horizontalSlider_uv.valueChanged.connect(self.uv_ledChannel_intensity)
        self.ui.horizontalSlider_white.valueChanged.connect(self.white_ledChannel_intensity)
        self.ui.horizontalSlider_exposure.valueChanged.connect(self.setExposure)
        self.ui.horizontalSlider_gain.valueChanged.connect(self.setGain)
        self.ui.pushButton_home.clicked.connect(self.goHome)
        self.ui.pushButton_red_intensity.clicked.connect(self.selected_Red)
        self.ui.pushButton_green_intensity.clicked.connect(self.selected_Green)
        self.ui.pushButton_blue_intensity.clicked.connect(self.selected_Blue)
        self.ui.pushButton_white_intensity.clicked.connect(self.selected_White)
        self.ui.pushButton_uv_intensity.clicked.connect(self.selected_Uv)
        self.ui.pushButton_red_capture.clicked.connect(self.selectCapture_led_Red)
        self.ui.pushButton_green_capture.clicked.connect(self.selectCapture_led_Green)
        self.ui.pushButton_blue_capture.clicked.connect(self.selectCapture_led_Blue)
        self.ui.pushButton_uv_capture.clicked.connect(self.selectCapture_led_Uv)
        self.ui.pushButton_white_capture.clicked.connect(self.selectCapture_led_White)

        self.ui.pushButton_red_zstack.clicked.connect(self.selectStack_led_Red)
        self.ui.pushButton_green_zstack.clicked.connect(self.selectStack_led_Green)
        self.ui.pushButton_blue_zstack.clicked.connect(self.selectStack_led_Blue)
        self.ui.pushButton_uv_zstack.clicked.connect(self.selectStack_led_Uv)
        self.ui.pushButton_white_zstack.clicked.connect(self.selectStack_led_White)
        self.ui.pushButton_zstack_flagSetSlices.clicked.connect(self.showZStackSlices)
        self.ui.pushButton_zstack_flagSetDistance.clicked.connect(self.showZStackDistance)

        self.ui.pushButton_zstack_setStart.clicked.connect(self.setZStackStart)
        self.ui.pushButton_zstack_setEnd.clicked.connect(self.setZStackEnd)
        self.ui.pushButton_zstack_setDistance.clicked.connect(self.setZStackDistance)
        self.ui.pushButton_zstack_setSlices.clicked.connect(self.setZStackSlices)
        self.ui.pushButton_zstack_clear.clicked.connect(self.clearZStackLabels)

        self.ui.pushButton_timelapse_setMeasurements.clicked.connect(self.timelapseSetMeasurement)
        self.ui.pushButton_timelapse_setInterval.clicked.connect(self.timelapseSetInterval)
        self.ui.pushButton_timelapse_clear.clicked.connect(self.timelapseClearLabels)
        self.ui.pushButton_timelapse_zstackSetStart.clicked.connect(self.timelapseZStackStart)
        self.ui.pushButton_timelapse_zstackSetEnd.clicked.connect(self.timelapseZStackEnd)
        self.ui.pushButton_timelapse_zstackSetDistance.clicked.connect(self.timelapseZStackDistance)
        self.ui.pushButton_timelapse_zstackSetSlices.clicked.connect(self.timelapseZStackSlices)
        self.ui.pushButton_timelapse_zstackClear.clicked.connect(self.timelapseZStackClearLabels)







        self.ui.pushButton_timelapse_flagSetSlices.clicked.connect(self.showTimelapseSlices)
        self.ui.pushButton_timelapse_flagSetDistance.clicked.connect(self.showTimelapseDistance)

        self.ui.pushButton_coarse.clicked.connect(self.selectedCoarse)
        self.ui.pushButton_fine.clicked.connect(self.selectedFine)
        self.ui.pushButton_stepMode.clicked.connect(self.selectedStepMode)
        self.ui.pushButton_goAbsulutePosition.clicked.connect(self.goAbsulutePosition)


        self.initialSettings()



        ######################## Variables

        self.cnc = cncPort()
        self.cnc.connectCnc()
        self.cnc.change_pixmap_signal.connect(self.update_position)
        self.cnc.start()
        self.homeFlag = False
        self.position=""
        self.old_position = ""

        self.zStackExtend_flag=False
        self.loadingProgressValue=0
        self.rightSide_tab_panel = 0 #### 0 preview 1 z-stack 2 timelapse 3 result
        self.rightSide_selected_led = 0 ##### 0 red 1 green 2 blue 3 uv 4 white
        self.flagCaptureRed=False
        self.flagCaptureGreen = False
        self.flagCaptureBlue = False
        self.flagCaptureUv = False
        self.flagCaptureWhite = False

        self.flagStackRed = False
        self.flagStackGreen = False
        self.flagStackBlue = False
        self.flagStackUv = False
        self.flagStackWhite = False

        #############################
        self.flagZp=False
        self.flagZn=False
        self.flagXp=False
        self.flagXn=False
        self.flagYp=False
        self.flagYn=False


        self.startCam()

        def moveWindow(event):
            if(self.windowFlag==True):
                self.showNormal()
                self.center()
                self.windowFlag = False

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.frame_titleBar.mouseMoveEvent=moveWindow

    def initialSettings(self):
        self.ui.stackedWidget_main.setCurrentIndex(0)
        self.ui.stackedWidget_zStack.setCurrentIndex(1)
        self.ui.stackedWidget_rightSide.setCurrentIndex(0)
        self.ui.stackedWidget_leftSide.setCurrentIndex(0)
        self.ui.stackedWidget_zstackExtend.setCurrentIndex(1)
        self.ui.stackedWidget_timelapseZstackExtend.setCurrentIndex(1)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.showMaximized()
        self.selectedCoarse()
        self.ui.pushButton_zstack_flagSetSlices.setStyleSheet(u"QPushButton{\n"
                                                              "	border:none;\n"
                                                              "\n"
                                                              "	background-image: url(:/floresansPrefix/whitePressed.png);\n"
                                                              "}")
        self.ui.pushButton_zstack_flagSetDistance.setStyleSheet(u"QPushButton{\n"
                                                              "	border:none;\n"
                                                              "\n"
                                                              "	background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                                              "}")

        self.ui.pushButton_timelapse_flagSetSlices.setStyleSheet(u"QPushButton{\n"
                                                              "	border:none;\n"
                                                              "\n"
                                                              "	background-image: url(:/floresansPrefix/whitePressed.png);\n"
                                                              "}")
        self.ui.pushButton_timelapse_flagSetDistance.setStyleSheet(u"QPushButton{\n"
                                                                "	border:none;\n"
                                                                "\n"
                                                                "	background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                                                "}")

        ################### Timelapse



    def startCam(self):
        self.cam = cam()
        self.cam.change_pixmap_signal.connect(self.update_image)
        self.cam.startCam(2)
        self.cam.start()

    def update_image(self,cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.ui.pictureBox.loadImageFromFile(qt_img)
        #self.ui.pictureBox.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        h, w, b= np.array(cv_img).shape
        bytes_per_line = w
        convert_to_Qt_format = QtGui.QImage(cv_img.data, w, h, bytes_per_line, QtGui.QImage.Format_Grayscale8)
        p = convert_to_Qt_format.scaled(self.ui.pictureBox.width(), self.ui.pictureBox.height(), Qt.KeepAspectRatio)
        return p     #QPixmap.fromImage(p)


    def center(self):
        screen = QtGui.QGuiApplication.screenAt(QtGui.QCursor().pos())
        fg = self.frameGeometry()
        fg.moveCenter(screen.geometry().center())
        self.move(fg.topLeft())




    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status==0:
            self.showMaximized()

            GLOBAL_STATE = 1
            self.ui.drop_shadow_frame.setContentsMargins(0,0,0,0)
            self.ui.pushButton_window.setToolTip("Restore")
        else:
            GLOBAL_STATE=0
            self.showNormal()
            self.resize(self.width()+1,self.height()+1)
            self.ui.drop_shadow_frame.setContentsMargins(10,10,10,10)
            self.ui.pushButton_window.setToolTip()

    def selected_Red(self):
        self.rightSide_selected_led=0
        self.change_rightSide_led_icons()

    def selected_Green(self):
        self.rightSide_selected_led = 1
        self.change_rightSide_led_icons()

    def selected_Blue(self):
        self.rightSide_selected_led = 2
        self.change_rightSide_led_icons()

    def selected_Uv(self):
        self.rightSide_selected_led = 3
        self.change_rightSide_led_icons()

    def selected_White(self):
        self.rightSide_selected_led = 4
        self.change_rightSide_led_icons()


    def showZStack(self):
        self.ui.stackedWidget_rightSide.setCurrentIndex(1)
        self.ui.stackedWidget_leftSide.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.rightSide_tab_panel =1
        self.change_rightSide_tab_icons()

    def showTimeLapse(self):
        self.ui.stackedWidget_rightSide.setCurrentIndex(2)
        self.ui.stackedWidget_leftSide.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.rightSide_tab_panel = 2
        self.change_rightSide_tab_icons()
    def showPreview(self):
        self.ui.stackedWidget_rightSide.setCurrentIndex(0)
        self.ui.stackedWidget_leftSide.setCurrentIndex(0)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.rightSide_tab_panel=0
        self.change_rightSide_tab_icons()

    def showResult(self):
        self.ui.stackedWidget_rightSide.setCurrentIndex(3)
        self.ui.stackedWidget_leftSide.setCurrentIndex(1)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.rightSide_tab_panel = 3
        self.change_rightSide_tab_icons()


    def showZStackExtend(self):
        if(self.zStackExtend_flag):
            self.ui.stackedWidget_zStack.setCurrentIndex(1)
            self.zStackExtend_flag=False
            self.ui.pushButton_zStackExtend.setStyleSheet(u"QPushButton{\n"
                                                             "background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                                             "border:none;\n"
                                                             "}\n"
                                                             "\n"
                                                             "")


        else:
            self.ui.stackedWidget_zStack.setCurrentIndex(0)
            self.zStackExtend_flag=True
            self.ui.pushButton_zStackExtend.setStyleSheet(u"QPushButton{\n"
                                                          "background-image: url(:/floresansPrefix/whitePressed.png);\n"
                                                          "border:none;\n"
                                                          "}\n"
                                                          "\n"
                                                          "")



    def APP_EXİT(self):
        self.cam.terminate()
        exit(0)

    def minimized_window(self):
        self.showMinimized()


    def goHome(self):
        self.timer_home = QtCore.QTimer()
        self.timer_home.timeout.connect(self.waitHome)
        self.loadingProgressValue=0
        self.countHome=0
        self.cnc.home()
        time.sleep(0.001)
        self.ui.stackedWidget_main.setCurrentIndex(1)
        self.stopHomeTimer = False
        self.timer_home.start(10)

    def waitHome(self):
        self.countHome=self.countHome+1
        self.loadingProgressValue = self.loadingProgressValue + 1
        if (self.loadingProgressValue == 100):
            self.loadingProgressValue = 0
        styleSheet1 = """
                QFrame{
                    border-radius:140px;
                    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP1_1} rgba(255, 0, 127, 0), stop:{STOP1_2} rgba(85, 170, 255, 255));

                }
                """
        progress = (100 - self.loadingProgressValue) / 100.0
        STOP1_1 = str(progress - 0.001)
        STOP1_2 = str(progress)

        newStyleSheet1 = styleSheet1.replace("{STOP1_1}", STOP1_1).replace("{STOP1_2}", STOP1_2)
        self.ui.circularProgress_loading1.setStyleSheet(newStyleSheet1)

        styleSheet2 = """
                        QFrame{
                            border-radius:120px;
                            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:{STOP2_1} rgba(255, 0, 127, 0), stop:{STOP2_2} rgba(85, 170, 255, 255));

                        }
                        """
        STOP2_1 = str(progress - 0.001)
        STOP2_2 = str(progress)

        newStyleSheet2 = styleSheet2.replace("{STOP2_1}", STOP2_1).replace("{STOP2_2}", STOP2_2)
        self.ui.circularProgress_loading2.setStyleSheet(newStyleSheet2)
        if(self.countHome>1000):
            self.homeFlag=True
            if(self.stopHomeTimer):
                self.timer_home.stop()
                self.ui.stackedWidget_main.setCurrentIndex(0)
                self.homeFlag=False
                self.stopHomeTimer=False



##########################################################
    ###################### Z ############################
    def goZp(self):
       if(self.activeStepMode):
           self.cnc.goZp_stepMode()
       else:
           self.cnc.goZp(self.zStackFeedRate)


    def pushButtonZ_up_mouseDown(self):
        self.cnc.resume()
        time.sleep(0.001)
        self.goZp()




    def pushButtonZ_up_mouseUp(self):
        self.cnc.hold()
        self.flagZp=False



    def goZn(self):
        if(self.activeStepMode):
            self.cnc.goZn_stepMode()
        else:
            self.cnc.goZn(self.zStackFeedRate)



    def pushButtonZ_down_mouseDown(self):
        self.cnc.resume()
        time.sleep(0.001)
        self.goZn()

    def pushButtonZ_down_mouseUp(self):
        self.cnc.hold()


##########################################################
    ########################### X ########################

    def goXp(self):
       if(self.activeStepMode):
           self.cnc.goXp_stepMode()
       else:
           self.cnc.goXp(self.xyStackFeedRate)


    def pushButtonX_up_mouseDown(self):
        self.cnc.resume()
        time.sleep(0.001)
        self.goXp()

    def pushButtonX_up_mouseUp(self):
        self.cnc.hold()


    def goXn(self):
       if(self.activeStepMode):
           self.cnc.goXn_stepMode()
       else:
           self.cnc.goXn(self.xyStackFeedRate)



    def pushButtonX_down_mouseDown(self):
        self.cnc.resume()
        time.sleep(0.001)
        self.goXn()


    def pushButtonX_down_mouseUp(self):
        self.cnc.hold()


##################################################################
########################## Y ############################

    def goYp(self):
       if(self.activeStepMode):
           self.cnc.goYp_stepMode()
       else:
           self.cnc.goYp(self.xyStackFeedRate)



    def pushButtonY_up_mouseDown(self):
        self.cnc.resume()
        time.sleep(0.001)
        self.goYp()


    def pushButtonY_up_mouseUp(self):
        self.cnc.hold()

    def goYn(self):
        if(self.activeStepMode):
            self.cnc.goYn_stepMode()
        else:
            self.cnc.goYn(self.xyStackFeedRate)



    def pushButtonY_down_mouseDown(self):
        self.cnc.resume()
        time.sleep(0.001)
        self.goYn()


    def pushButtonY_down_mouseUp(self):
        self.cnc.hold()


    def update_position(self,position):
        if(self.homeFlag):
            if (position.find("Idle") != -1):
                self.stopHomeTimer=True
        if (position.find("MPos:") != -1):
            pFrom = position.find("MPos:") + len("MPos:")
            pTo = position.rfind("FS:") - 1
            if (pTo != -2):
                result = position[pFrom:pTo]
                x_pFrom = 0
                x_to = result.find(',')
                x = result[x_pFrom:x_to]
                y_pFrom = result.find(",") + len(",")
                y_to = result.rfind(",")
                y = result[y_pFrom:y_to]
                z = result[y_to + 1:]

                if(result!=self.old_position):
                    self.old_position=result
                    self.ui.lineEdit_X_position.setText(x)
                    self.ui.lineEdit_Y_position.setText(y)
                    self.ui.lineEdit_Z_position.setText(z)


                    self.ui.lineEdit_zstack_zstackStart.setText(z)
                    self.ui.lineEdit_zstack_zstackEnd.setText(z)
                    self.ui.lineEdit_timelapse_zstackEnd.setText(z)
                    self.ui.lineEdit_timelapse_zstackStart.setText(z)



    def red_ledChannel_intensity(self):
        self.red_value = self.ui.horizontalSlider_red.value()
        styleSheet1 = """
               QFrame{
                   border-radius:50px;
                   background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP1_1} rgba(0, 0, 0, 9), stop:{STOP1_2} rgba(255, 255, 255, 255));

               }
               """
        progress = (100 - self.red_value) / 100.0
        STOP1_1 = str(progress - 0.001)
        STOP1_2 = str(progress)
        newStyleSheet1 = styleSheet1.replace("{STOP1_1}", STOP1_1).replace("{STOP1_2}", STOP1_2)
        self.ui.circularProgress_red.setStyleSheet(newStyleSheet1)
        self.ui.label_redChannel_led.setText(str(self.red_value))

    def green_ledChannel_intensity(self):
        self.green_value = self.ui.horizontalSlider_green.value()
        styleSheet1 = """
               QFrame{
                   border-radius:50px;
                   background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP1_1} rgba(0, 0, 0, 9), stop:{STOP1_2} rgba(255, 255, 255, 255));

               }
               """
        progress = (100 - self.green_value) / 100.0
        STOP1_1 = str(progress - 0.001)
        STOP1_2 = str(progress)
        newStyleSheet1 = styleSheet1.replace("{STOP1_1}", STOP1_1).replace("{STOP1_2}", STOP1_2)
        self.ui.circularProgress_green.setStyleSheet(newStyleSheet1)
        self.ui.label_greenChannel_led.setText(str(self.green_value))

    def blue_ledChannel_intensity(self):
        self.blue_value = self.ui.horizontalSlider_blue.value()
        styleSheet1 = """
                 QFrame{
                     border-radius:50px;
                     background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP1_1} rgba(0, 0, 0, 9), stop:{STOP1_2} rgba(255, 255, 255, 255));

                 }
                 """
        progress = (100 - self.blue_value) / 100.0
        STOP1_1 = str(progress - 0.001)
        STOP1_2 = str(progress)
        newStyleSheet1 = styleSheet1.replace("{STOP1_1}", STOP1_1).replace("{STOP1_2}", STOP1_2)
        self.ui.circularProgress_blue.setStyleSheet(newStyleSheet1)
        self.ui.label_blueChannel_led.setText(str(self.blue_value))

    def uv_ledChannel_intensity(self):
        self.uv_value = self.ui.horizontalSlider_uv.value()
        styleSheet1 = """
                 QFrame{
                     border-radius:50px;
                     background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP1_1} rgba(0, 0, 0, 9), stop:{STOP1_2} rgba(255, 255, 255, 255));

                 }
                 """
        progress = (100 - self.uv_value) / 100.0
        STOP1_1 = str(progress - 0.001)
        STOP1_2 = str(progress)
        newStyleSheet1 = styleSheet1.replace("{STOP1_1}", STOP1_1).replace("{STOP1_2}", STOP1_2)
        self.ui.circularProgress_uv.setStyleSheet(newStyleSheet1)
        self.ui.label_uvChannel_led.setText(str(self.uv_value))

    def white_ledChannel_intensity(self):
        self.white_value = self.ui.horizontalSlider_white.value()
        styleSheet1 = """
                 QFrame{
                     border-radius:50px;
                     background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP1_1} rgba(0, 0, 0, 9), stop:{STOP1_2} rgba(255, 255, 255, 255));

                 }
                 """
        progress = (100 - self.white_value) / 100.0
        STOP1_1 = str(progress - 0.001)
        STOP1_2 = str(progress)
        newStyleSheet1 = styleSheet1.replace("{STOP1_1}", STOP1_1).replace("{STOP1_2}", STOP1_2)
        self.ui.circularProgress_white.setStyleSheet(newStyleSheet1)
        self.ui.label_whiteChannel_led.setText(str(self.white_value))

    def setExposure(self):
        self.exposure_value = self.ui.horizontalSlider_exposure.value()
        self.cam.setExposure(self.exposure_value)
        styleSheet1 = """
                 QFrame{
                     border-radius:50px;
                     background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP1_1} rgba(0, 0, 0, 9), stop:{STOP1_2} rgba(255, 255, 255, 255));
                 }
                 """
        progress = (100 - self.exposure_value) / 100.0
        STOP1_1 = str(progress - 0.001)
        STOP1_2 = str(progress)
        newStyleSheet1 = styleSheet1.replace("{STOP1_1}", STOP1_1).replace("{STOP1_2}", STOP1_2)
        self.ui.circularProgress_exposure.setStyleSheet(newStyleSheet1)
        self.ui.label_exposure.setText(str(self.exposure_value))

    def setGain(self):
        self.gain_value = self.ui.horizontalSlider_gain.value()
        self.cam.setGain(self.gain_value)
        styleSheet1 = """
                  QFrame{
                      border-radius:50px;
                      background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP1_1} rgba(0, 0, 0, 9), stop:{STOP1_2} rgba(255, 255, 255, 255));
                  }
                  """

        progress = (100 - self.gain_value) / 100.0
        STOP1_1 = str(progress - 0.001)
        STOP1_2 = str(progress)
        newStyleSheet1 = styleSheet1.replace("{STOP1_1}", STOP1_1).replace("{STOP1_2}", STOP1_2)
        self.ui.circularProgress_gain.setStyleSheet(newStyleSheet1)
        self.ui.label_gain.setText(str(self.gain_value))
    def goAbsulutePosition(self):
        self.cnc.resume()
        time.sleep(0.001)
        x_location = self.ui.lineEdit_X_position.text()
        y_location = self.ui.lineEdit_Y_position.text()
        z_location = self.ui.lineEdit_Z_position.text()
        self.cnc.goAbsulutePosition(x_location,y_location,z_location)


    def selectedCoarse(self):
        self.activeStepMode = False
        self.zStackFeedRate = 10
        self.xyStackFeedRate = 50
        self.xyWaitTime = 0.00001

        self.ui.pushButton_coarse.setStyleSheet(u"QPushButton{\n"
                                                           "	border:none;\n"
                                                           "\n"
                                                           "	background-image: url(:/floresansPrefix/whitePressed.png);\n"
                                                           "}")
        self.ui.pushButton_fine.setStyleSheet(u"QPushButton{\n"
                                                           "	border:none;\n"
                                                           "\n"
                                                           "	background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                                           "}")
        self.ui.pushButton_stepMode.setStyleSheet(u"QPushButton{\n"
                                              "	border:none;\n"
                                              "\n"
                                              "	background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                              "}")

    def selectedFine(self):
        self.activeStepMode = False
        self.zStackFeedRate = 1
        self.xyStackFeedRate = 1


        self.ui.pushButton_fine.setStyleSheet(u"QPushButton{\n"
                                                "	border:none;\n"
                                                "\n"
                                                "	background-image: url(:/floresansPrefix/whitePressed.png);\n"
                                                "}")
        self.ui.pushButton_coarse.setStyleSheet(u"QPushButton{\n"
                                              "	border:none;\n"
                                              "\n"
                                              "	background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                              "}")
        self.ui.pushButton_stepMode.setStyleSheet(u"QPushButton{\n"
                                                  "	border:none;\n"
                                                  "\n"
                                                  "	background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                                  "}")

    def selectedStepMode(self):
        self.activeStepMode=True
        self.zStackFeedRate = 1
        self.xyStackFeedRate = 1

        self.ui.pushButton_stepMode.setStyleSheet(u"QPushButton{\n"
                                                "	border:none;\n"
                                                "\n"
                                                "	background-image: url(:/floresansPrefix/whitePressed.png);\n"
                                                "}")
        self.ui.pushButton_fine.setStyleSheet(u"QPushButton{\n"
                                              "	border:none;\n"
                                              "\n"
                                              "	background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                              "}")
        self.ui.pushButton_coarse.setStyleSheet(u"QPushButton{\n"
                                                  "	border:none;\n"
                                                  "\n"
                                                  "	background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                                  "}")


    def setZStackStart(self):
        text = self.ui.lineEdit_zstack_zstackStart.text()
        self.ui.label_zstack_start.setText(text)

    def setZStackEnd(self):
        text = self.ui.lineEdit_zstack_zstackEnd.text()
        self.ui.label_zstack_end.setText(text)


    def setZStackDistance(self):
        text = self.ui.lineEdit_zstack_distance.text()
        self.ui.label_zstack_distance.setText(text)

    def setZStackSlices(self):
        text = self.ui.lineEdit_zstack_slices.text()
        self.ui.label_zstack_slices.setText(text)

    def clearZStackLabels(self):
        self.ui.label_zstack_start.setText("0.000")
        self.ui.label_zstack_end.setText("0.000")
        self.ui.label_zstack_distance.setText("0.000")
        self.ui.label_zstack_slices.setText("0.000")


    def timelapseSetMeasurement(self):
        text = self.ui.lineEdit_timelapse_measurements.text()
        self.ui.label_timelapse_measurements.setText(text)
    def timelapseSetInterval(self):
        text = self.ui.lineEdit_timelapse_interval.text()
        self.ui.label_timelapse_interval.setText(text)
    def timelapseClearLabels(self):
        self.ui.label_timelapse_measurements.setText("0.000")
        self.ui.label_timelapse_interval.setText("0.000")
    def timelapseZStackStart(self):
        text = self.ui.lineEdit_timelapse_zstackStart.text()
        self.ui.label_timelapse_zstackStart.setText(text)
    def timelapseZStackEnd(self):
        text = self.ui.lineEdit_timelapse_zstackEnd.text()
        self.ui.label_timelapse_zstackEnd.setText(text)
    def timelapseZStackDistance(self):
        text = self.ui.lineEdit_timelapse_zstackDistance.text()
        self.ui.label_timelapse_zstackDistance.setText(text)
    def timelapseZStackSlices(self):
        text = self.ui.lineEdit_timelapse_zstackSlices.text()
        self.ui.label_timelapse_zstackSlices.setText(text)
    def timelapseZStackClearLabels(self):
        self.ui.label_timelapse_zstackStart.setText("0.000")
        self.ui.label_timelapse_zstackEnd.setText("0.000")
        self.ui.label_timelapse_zstackDistance.setText("0.000")
        self.ui.label_timelapse_zstackSlices.setText("0.000")



    def selectCapture_led_Red(self):
        if(self.flagCaptureRed==False):
            self.ui.pushButton_red_capture.setStyleSheet(u"QPushButton{\n"
                                                       "	border:none;\n"
                                                       "\n"
                                                       "	background-image: url(:/floresansPrefix/redPressed.png);\n"
                                                       "}")
            self.flagCaptureRed = True
        else:
            self.flagCaptureRed = False
            self.ui.pushButton_red_capture.setStyleSheet(u"QPushButton{\n"
                                                         "	border:none;\n"
                                                         "\n"
                                                         "	background-image: url(:/floresansPrefix/redUnPressed.png);\n"
                                                         "}")
    def selectCapture_led_Green(self):
        if (self.flagCaptureGreen == False):
            self.ui.pushButton_green_capture.setStyleSheet(u"QPushButton{\n"
                                                         "	border:none;\n"
                                                         "\n"
                                                         "	background-image: url(:/floresansPrefix/greenPressed.png);\n"
                                                         "}")
            self.flagCaptureGreen = True
        else:
            self.flagCaptureGreen = False
            self.ui.pushButton_green_capture.setStyleSheet(u"QPushButton{\n"
                                                         "	border:none;\n"
                                                         "\n"
                                                         "	background-image: url(:/floresansPrefix/greenUnPressed.png);\n"
                                                         "}")
    def selectCapture_led_Blue(self):
        if (self.flagCaptureBlue == False):
            self.ui.pushButton_blue_capture.setStyleSheet(u"QPushButton{\n"
                                                           "	border:none;\n"
                                                           "\n"
                                                           "	background-image: url(:/floresansPrefix/bluePressed.png);\n"
                                                           "}")
            self.flagCaptureBlue = True
        else:
            self.flagCaptureBlue = False
            self.ui.pushButton_blue_capture.setStyleSheet(u"QPushButton{\n"
                                                           "	border:none;\n"
                                                           "\n"
                                                           "	background-image: url(:/floresansPrefix/blueUnPressed.png);\n"
                                                           "}")
    def selectCapture_led_Uv(self):
        if (self.flagCaptureUv == False):
            self.ui.pushButton_uv_capture.setStyleSheet(u"QPushButton{\n"
                                                           "	border:none;\n"
                                                           "\n"
                                                           "	background-image: url(:/floresansPrefix/uv_button_pressed.png);\n"
                                                           "}")
            self.flagCaptureUv = True
        else:
            self.flagCaptureUv = False
            self.ui.pushButton_uv_capture.setStyleSheet(u"QPushButton{\n"
                                                           "	border:none;\n"
                                                           "\n"
                                                           "	background-image: url(:/floresansPrefix/uv_button_unpressed.png);\n"
                                                           "}")
    def selectCapture_led_White(self):
        if (self.flagCaptureWhite == False):
            self.ui.pushButton_white_capture.setStyleSheet(u"QPushButton{\n"
                                                          "	border:none;\n"
                                                          "\n"
                                                          "	background-image: url(:/floresansPrefix/whitePressed.png);\n"
                                                          "}")
            self.flagCaptureWhite = True
        else:
            self.flagCaptureWhite = False
            self.ui.pushButton_white_capture.setStyleSheet(u"QPushButton{\n"
                                                          "	border:none;\n"
                                                          "\n"
                                                          "	background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                                          "}")


    def selectStack_led_Red(self):
        if (self.flagStackRed == False):
            self.ui.pushButton_red_zstack.setStyleSheet(u"QPushButton{\n"
                                                         "	border:none;\n"
                                                         "\n"
                                                         "	background-image: url(:/floresansPrefix/redPressed.png);\n"
                                                         "}")
            self.flagStackRed = True
        else:
            self.flagStackRed = False
            self.ui.pushButton_red_zstack.setStyleSheet(u"QPushButton{\n"
                                                         "	border:none;\n"
                                                         "\n"
                                                         "	background-image: url(:/floresansPrefix/redUnPressed.png);\n"
                                                         "}")
    def selectStack_led_Green(self):
        if (self.flagStackGreen == False):
            self.ui.pushButton_green_zstack.setStyleSheet(u"QPushButton{\n"
                                                         "	border:none;\n"
                                                         "\n"
                                                         "	background-image: url(:/floresansPrefix/greenPressed.png);\n"
                                                         "}")
            self.flagStackGreen = True
        else:
            self.flagStackGreen = False
            self.ui.pushButton_green_zstack.setStyleSheet(u"QPushButton{\n"
                                                         "	border:none;\n"
                                                         "\n"
                                                         "	background-image: url(:/floresansPrefix/greenUnPressed.png);\n"
                                                         "}")

    def selectStack_led_Blue(self):
        if (self.flagStackBlue == False):
            self.ui.pushButton_blue_zstack.setStyleSheet(u"QPushButton{\n"
                                                           "	border:none;\n"
                                                           "\n"
                                                           "	background-image: url(:/floresansPrefix/bluePressed.png);\n"
                                                           "}")
            self.flagStackBlue = True
        else:
            self.flagStackBlue = False
            self.ui.pushButton_blue_zstack.setStyleSheet(u"QPushButton{\n"
                                                           "	border:none;\n"
                                                           "\n"
                                                           "	background-image: url(:/floresansPrefix/blueUnPressed.png);\n"
                                                           "}")

    def selectStack_led_Uv(self):
        if (self.flagStackUv == False):
            self.ui.pushButton_uv_zstack.setStyleSheet(u"QPushButton{\n"
                                                           "	border:none;\n"
                                                           "\n"
                                                           "	background-image: url(:/floresansPrefix/uv_button_pressed.png);\n"
                                                           "}")
            self.flagStackUv = True
        else:
            self.flagStackUv = False
            self.ui.pushButton_uv_zstack.setStyleSheet(u"QPushButton{\n"
                                                           "	border:none;\n"
                                                           "\n"
                                                           "	background-image: url(:/floresansPrefix/uv_button_unpressed.png);\n"
                                                           "}")

    def selectStack_led_White(self):
        if (self.flagStackWhite == False):
            self.ui.pushButton_white_zstack.setStyleSheet(u"QPushButton{\n"
                                                          "	border:none;\n"
                                                          "\n"
                                                          "	background-image: url(:/floresansPrefix/whitePressed.png);\n"
                                                          "}")
            self.flagStackWhite = True
        else:
            self.flagStackWhite = False
            self.ui.pushButton_white_zstack.setStyleSheet(u"QPushButton{\n"
                                                          "	border:none;\n"
                                                          "\n"
                                                          "	background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                                          "}")

    def showZStackSlices(self):
        self.ui.stackedWidget_zstackExtend.setCurrentIndex(1)
        self.ui.pushButton_zstack_flagSetSlices.setStyleSheet(u"QPushButton{\n"
                                                      "	border:none;\n"
                                                      "\n"
                                                      "	background-image: url(:/floresansPrefix/whitePressed.png);\n"
                                                      "}")
        self.ui.pushButton_zstack_flagSetDistance.setStyleSheet(u"QPushButton{\n"
                                                      "	border:none;\n"
                                                      "\n"
                                                      "	background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                                      "}")

    def showZStackDistance(self):
        self.ui.stackedWidget_zstackExtend.setCurrentIndex(0)
        self.ui.pushButton_zstack_flagSetDistance.setStyleSheet(u"QPushButton{\n"
                                                              "	border:none;\n"
                                                              "\n"
                                                              "	background-image: url(:/floresansPrefix/whitePressed.png);\n"
                                                              "}")
        self.ui.pushButton_zstack_flagSetSlices.setStyleSheet(u"QPushButton{\n"
                                                                "	border:none;\n"
                                                                "\n"
                                                                "	background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                                                "}")

    def showTimelapseSlices(self):
        self.ui.stackedWidget_timelapseZstackExtend.setCurrentIndex(1)
        self.ui.pushButton_timelapse_flagSetSlices.setStyleSheet(u"QPushButton{\n"
                                                                 "	border:none;\n"
                                                                 "\n"
                                                                 "	background-image: url(:/floresansPrefix/whitePressed.png);\n"
                                                                 "}")
        self.ui.pushButton_timelapse_flagSetDistance.setStyleSheet(u"QPushButton{\n"
                                                                   "	border:none;\n"
                                                                   "\n"
                                                                   "	background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                                                   "}")

    def showTimelapseDistance(self):
        self.ui.stackedWidget_timelapseZstackExtend.setCurrentIndex(0)
        self.ui.pushButton_timelapse_flagSetSlices.setStyleSheet(u"QPushButton{\n"
                                                                 "	border:none;\n"
                                                                 "\n"
                                                                 "	background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                                                 "}")
        self.ui.pushButton_timelapse_flagSetDistance.setStyleSheet(u"QPushButton{\n"
                                                                   "	border:none;\n"
                                                                   "\n"
                                                                   "	background-image: url(:/floresansPrefix/whitePressed.png);\n"
                                                                   "}")


    def change_rightSide_led_icons(self):
        if(self.rightSide_selected_led==0):
            self.ui.pushButton_red_intensity.setStyleSheet(u"QPushButton{\n"
                                                        "	border:none;\n"
                                                        "\n"
                                                        "	background-image: url(:/floresansPrefix/redPressed.png);\n"
                                                        "}")
            self.ui.pushButton_green_intensity.setStyleSheet(u"QPushButton{\n"
                                                          "	background-image: url(:/floresansPrefix/greenUnPressed.png);\n"
                                                          "	border:none;\n"
                                                          "}")
            self.ui.pushButton_blue_intensity.setStyleSheet(u"QPushButton{\n"
                                                         "	\n"
                                                         "	background-image: url(:/floresansPrefix/blueUnPressed.png);\n"
                                                         "	border:none;\n"
                                                         "}")
            self.ui.pushButton_uv_intensity.setStyleSheet(u"QPushButton{\n"
                                                       "	\n"
                                                       "	background-image: url(:/floresansPrefix/uv_button_unpressed.png);\n"
                                                       "	border:none;\n"
                                                       "}")
            self.ui.pushButton_white_intensity.setStyleSheet(u"QPushButton{\n"
                                                             "background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                                             "border:none;\n"
                                                             "}\n"
                                                             "\n"
                                                             "")
        if (self.rightSide_selected_led == 1):
            self.ui.pushButton_red_intensity.setStyleSheet(u"QPushButton{\n"
                                                           "	border:none;\n"
                                                           "\n"
                                                           "	background-image: url(:/floresansPrefix/redUnPressed.png);\n"
                                                           "}")
            self.ui.pushButton_green_intensity.setStyleSheet(u"QPushButton{\n"
                                                             "	background-image: url(:/floresansPrefix/greenPressed.png);\n"
                                                             "	border:none;\n"
                                                             "}")
            self.ui.pushButton_blue_intensity.setStyleSheet(u"QPushButton{\n"
                                                            "	\n"
                                                            "	background-image: url(:/floresansPrefix/blueUnPressed.png);\n"
                                                            "	border:none;\n"
                                                            "}")
            self.ui.pushButton_uv_intensity.setStyleSheet(u"QPushButton{\n"
                                                          "	\n"
                                                          "	background-image: url(:/floresansPrefix/uv_button_unpressed.png);\n"
                                                          "	border:none;\n"
                                                          "}")
            self.ui.pushButton_white_intensity.setStyleSheet(u"QPushButton{\n"
                                                             "background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                                             "border:none;\n"
                                                             "}\n"
                                                             "\n"
                                                             "")
        if (self.rightSide_selected_led == 2):
            self.ui.pushButton_red_intensity.setStyleSheet(u"QPushButton{\n"
                                                           "	border:none;\n"
                                                           "\n"
                                                           "	background-image: url(:/floresansPrefix/redUnPressed.png);\n"
                                                           "}")
            self.ui.pushButton_green_intensity.setStyleSheet(u"QPushButton{\n"
                                                             "	background-image: url(:/floresansPrefix/greenUnPressed.png);\n"
                                                             "	border:none;\n"
                                                             "}")
            self.ui.pushButton_blue_intensity.setStyleSheet(u"QPushButton{\n"
                                                            "	\n"
                                                            "	background-image: url(:/floresansPrefix/bluePressed.png);\n"
                                                            "	border:none;\n"
                                                            "}")
            self.ui.pushButton_uv_intensity.setStyleSheet(u"QPushButton{\n"
                                                          "	\n"
                                                          "	background-image: url(:/floresansPrefix/uv_button_unpressed.png);\n"
                                                          "	border:none;\n"
                                                          "}")
            self.ui.pushButton_white_intensity.setStyleSheet(u"QPushButton{\n"
                                                             "background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                                             "border:none;\n"
                                                             "}\n"
                                                             "\n"
                                                             "")
        if (self.rightSide_selected_led == 3):
            self.ui.pushButton_red_intensity.setStyleSheet(u"QPushButton{\n"
                                                           "	border:none;\n"
                                                           "\n"
                                                           "	background-image: url(:/floresansPrefix/redUnPressed.png);\n"
                                                           "}")
            self.ui.pushButton_green_intensity.setStyleSheet(u"QPushButton{\n"
                                                             "	background-image: url(:/floresansPrefix/greenUnPressed.png);\n"
                                                             "	border:none;\n"
                                                             "}")
            self.ui.pushButton_blue_intensity.setStyleSheet(u"QPushButton{\n"
                                                            "	\n"
                                                            "	background-image: url(:/floresansPrefix/blueUnPressed.png);\n"
                                                            "	border:none;\n"
                                                            "}")
            self.ui.pushButton_uv_intensity.setStyleSheet(u"QPushButton{\n"
                                                          "	\n"
                                                          "	background-image: url(:/floresansPrefix/uv_button_pressed.png);\n"
                                                          "	border:none;\n"
                                                          "}")
            self.ui.pushButton_white_intensity.setStyleSheet(u"QPushButton{\n"
                                                             "background-image: url(:/floresansPrefix/whiteUnpressed.png);\n"
                                                             "border:none;\n"
                                                             "}\n"
                                                             "\n"
                                                             "")
        if (self.rightSide_selected_led == 4):
            self.ui.pushButton_red_intensity.setStyleSheet(u"QPushButton{\n"
                                                           "	border:none;\n"
                                                           "\n"
                                                           "	background-image: url(:/floresansPrefix/redUnPressed.png);\n"
                                                           "}")
            self.ui.pushButton_green_intensity.setStyleSheet(u"QPushButton{\n"
                                                             "	background-image: url(:/floresansPrefix/greenUnPressed.png);\n"
                                                             "	border:none;\n"
                                                             "}")
            self.ui.pushButton_blue_intensity.setStyleSheet(u"QPushButton{\n"
                                                            "	\n"
                                                            "	background-image: url(:/floresansPrefix/blueUnPressed.png);\n"
                                                            "	border:none;\n"
                                                            "}")
            self.ui.pushButton_uv_intensity.setStyleSheet(u"QPushButton{\n"
                                                          "	\n"
                                                          "	background-image: url(:/floresansPrefix/uv_button_unpressed.png);\n"
                                                          "	border:none;\n"
                                                          "}")

            self.ui.pushButton_white_intensity.setStyleSheet(u"QPushButton{\n"
                                                          "background-image: url(:/floresansPrefix/whitePressed.png);\n"
                                                          "border:none;\n"
                                                          "}\n"
                                                          "\n"
                                                          "")



        pass

    def change_rightSide_tab_icons(self):
        if(self.rightSide_tab_panel==0):
            self.ui.pushButton_preview.setStyleSheet(u"QPushButton{\n"
                                                  "border:none;\n"
                                                  "background-image: url(:/floresansPrefix/preview_button_selected.png);\n"
                                                  "}\n"
                                                  "QPushButton::hover{\n"
                                                  "	background-color: rgba(255, 255, 255,150);\n"
                                                  "}")
            self.ui.pushButton_zStack.setStyleSheet(u"QPushButton{\n"
                                                    "border:none;\n"
                                                    "background-image: url(:/floresansPrefix/Zstack_button.png);\n"
                                                    "}\n"
                                                    "QPushButton::hover{\n"
                                                    "	background-color: rgba(255, 255, 255,150);\n"
                                                    "}")
            self.ui.pushButton_timelapse.setStyleSheet(u"QPushButton{\n"
                                                    "border:none;\n"
                                                    "	background-image: url(:/floresansPrefix/timelapse_button.png);\n"
                                                    "}\n"
                                                    "QPushButton::hover{\n"
                                                    "	background-color: rgba(255, 255, 255,150);\n"
                                                    "}")
            self.ui.pushButton_result.setStyleSheet(u"QPushButton{\n"
                                                 "border:none;\n"
                                                 "	background-image: url(:/floresansPrefix/result_button.png);\n"
                                                 "}\n"
                                                 "QPushButton::hover{\n"
                                                 "	background-color: rgba(255, 255, 255,150);\n"
                                                 "}")
        if (self.rightSide_tab_panel == 1):
            self.ui.pushButton_preview.setStyleSheet(u"QPushButton{\n"
                                                     "border:none;\n"
                                                     "background-image: url(:/floresansPrefix/preview_button.png);\n"
                                                     "}\n"
                                                     "QPushButton::hover{\n"
                                                     "	background-color: rgba(255, 255, 255,150);\n"
                                                     "}")
            self.ui.pushButton_zStack.setStyleSheet(u"QPushButton{\n"
                                                    "border:none;\n"
                                                    "background-image: url(:/floresansPrefix/Zstack_button_selected.png);\n"
                                                    "}\n"
                                                    "QPushButton::hover{\n"
                                                    "	background-color: rgba(255, 255, 255,150);\n"
                                                    "}")
            self.ui.pushButton_timelapse.setStyleSheet(u"QPushButton{\n"
                                                       "border:none;\n"
                                                       "	background-image: url(:/floresansPrefix/timelapse_button.png);\n"
                                                       "}\n"
                                                       "QPushButton::hover{\n"
                                                       "	background-color: rgba(255, 255, 255,150);\n"
                                                       "}")
            self.ui.pushButton_result.setStyleSheet(u"QPushButton{\n"
                                                    "border:none;\n"
                                                    "	background-image: url(:/floresansPrefix/result_button.png);\n"
                                                    "}\n"
                                                    "QPushButton::hover{\n"
                                                    "	background-color: rgba(255, 255, 255,150);\n"
                                                    "}")
        if (self.rightSide_tab_panel == 2):
            self.ui.pushButton_preview.setStyleSheet(u"QPushButton{\n"
                                                     "border:none;\n"
                                                     "background-image: url(:/floresansPrefix/preview_button.png);\n"
                                                     "}\n"
                                                     "QPushButton::hover{\n"
                                                     "	background-color: rgba(255, 255, 255,150);\n"
                                                     "}")
            self.ui.pushButton_zStack.setStyleSheet(u"QPushButton{\n"
                                                    "border:none;\n"
                                                    "background-image: url(:/floresansPrefix/Zstack_button.png);\n"
                                                    "}\n"
                                                    "QPushButton::hover{\n"
                                                    "	background-color: rgba(255, 255, 255,150);\n"
                                                    "}")
            self.ui.pushButton_timelapse.setStyleSheet(u"QPushButton{\n"
                                                       "border:none;\n"
                                                       "	background-image: url(:/floresansPrefix/timelapse_button_selected.png);\n"
                                                       "}\n"
                                                       "QPushButton::hover{\n"
                                                       "	background-color: rgba(255, 255, 255,150);\n"
                                                       "}")
            self.ui.pushButton_result.setStyleSheet(u"QPushButton{\n"
                                                    "border:none;\n"
                                                    "	background-image: url(:/floresansPrefix/result_button.png);\n"
                                                    "}\n"
                                                    "QPushButton::hover{\n"
                                                    "	background-color: rgba(255, 255, 255,150);\n"
                                                    "}")
        if (self.rightSide_tab_panel == 3):
            self.ui.pushButton_preview.setStyleSheet(u"QPushButton{\n"
                                                     "border:none;\n"
                                                     "background-image: url(:/floresansPrefix/preview_button.png);\n"
                                                     "}\n"
                                                     "QPushButton::hover{\n"
                                                     "	background-color: rgba(255, 255, 255,150);\n"
                                                     "}")
            self.ui.pushButton_zStack.setStyleSheet(u"QPushButton{\n"
                                                    "border:none;\n"
                                                    "background-image: url(:/floresansPrefix/Zstack_button.png);\n"
                                                    "}\n"
                                                    "QPushButton::hover{\n"
                                                    "	background-color: rgba(255, 255, 255,150);\n"
                                                    "}")
            self.ui.pushButton_timelapse.setStyleSheet(u"QPushButton{\n"
                                                       "border:none;\n"
                                                       "	background-image: url(:/floresansPrefix/timelapse_button.png);\n"
                                                       "}\n"
                                                       "QPushButton::hover{\n"
                                                       "	background-color: rgba(255, 255, 255,150);\n"
                                                       "}")
            self.ui.pushButton_result.setStyleSheet(u"QPushButton{\n"
                                                    "border:none;\n"
                                                    "	background-image: url(:/floresansPrefix/result_button_selected.png);\n"
                                                    "}\n"
                                                    "QPushButton::hover{\n"
                                                    "	background-color: rgba(255, 255, 255,150);\n"
                                                    "}")