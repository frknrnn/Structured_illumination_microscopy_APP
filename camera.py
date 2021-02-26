import sys
import os
import time
import cv2
import threading
import numpy as np
import signal
import json
from PySide2 import  QtCore,QtGui,QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ImageConvert import *
import arducam_config_parser
import ArducamSDK

class cam(QThread):
    change_pixmap_signal = Signal(np.ndarray)
    ımage_ = ""
    getFlag = False
    camFlag = True
    save_flag = False
    save_raw = False
    cfg = {}
    handle = {}
    def camera_initFromFile(self,fileName):
        config = arducam_config_parser.LoadConfigFile(fileName)

        camera_parameter = config.camera_param.getdict()
        self.Width = camera_parameter["WIDTH"]
        self.Height = camera_parameter["HEIGHT"]

        BitWidth = camera_parameter["BIT_WIDTH"]
        ByteLength = 1
        if BitWidth > 8 and BitWidth <= 16:
            ByteLength = 2
            self.save_raw = True
        FmtMode = camera_parameter["FORMAT"][0]
        self.color_mode = camera_parameter["FORMAT"][1]

        I2CMode = camera_parameter["I2C_MODE"]
        I2cAddr = camera_parameter["I2C_ADDR"]
        TransLvl = camera_parameter["TRANS_LVL"]
        self.cfg = {"u32CameraType": 0x00,
               "u32Width": self.Width, "u32Height": self.Height,
               "usbType": 0,
               "u8PixelBytes": ByteLength,
               "u16Vid": 0,
               "u32Size": 0,
               "u8PixelBits": BitWidth,
               "u32I2cAddr": I2cAddr,
               "emI2cMode": I2CMode,
               "emImageFmtMode": FmtMode,
               "u32TransLvl": TransLvl}

        # ret,handle,rtn_cfg = ArducamSDK.Py_ArduCam_open(cfg,0)
        ret, self.handle, rtn_cfg = ArducamSDK.Py_ArduCam_autoopen(self.cfg)
        if ret == 0:

            # ArducamSDK.Py_ArduCam_writeReg_8_8(handle,0x46,3,0x00)
            usb_version = rtn_cfg['usbType']
            configs = config.configs
            configs_length = config.configs_length
            for i in range(configs_length):
                type = configs[i].type
                if ((type >> 16) & 0xFF) != 0 and ((type >> 16) & 0xFF) != usb_version:
                    continue
                if type & 0xFFFF == arducam_config_parser.CONFIG_TYPE_REG:
                    ArducamSDK.Py_ArduCam_writeSensorReg(self.handle, configs[i].params[0], configs[i].params[1])
                elif type & 0xFFFF == arducam_config_parser.CONFIG_TYPE_DELAY:
                    time.sleep(float(configs[i].params[0]) / 1000)
                elif type & 0xFFFF == arducam_config_parser.CONFIG_TYPE_VRCMD:
                    self.configBoard(configs[i])

            ArducamSDK.Py_ArduCam_registerCtrls(self.handle, config.controls, config.controls_length)
            ArducamSDK.Py_ArduCam_setCtrl(self.handle, "setFramerate", 5)

            rtn_val, datas = ArducamSDK.Py_ArduCam_readUserData(self.handle, 0x400 - 16, 16)
            print("Serial: %c%c%c%c-%c%c%c%c-%c%c%c%c" % (datas[0], datas[1], datas[2], datas[3],
                                                          datas[4], datas[5], datas[6], datas[7],
                                                          datas[8], datas[9], datas[10], datas[11]))
            return True
        else:
            print("open fail,rtn_val = ", ret)
            return False


    def configBoard(self,config):
        ArducamSDK.Py_ArduCam_setboardConfig(self.handle, config.params[0], \
                                                 config.params[1], config.params[2], config.params[3], \
                                                 config.params[4:config.params_length])

    def captureImage_thread(self):
        rtn_val = ArducamSDK.Py_ArduCam_beginCaptureImage(self.handle)
        if rtn_val != 0:
            print("Error beginning capture, rtn_val = ", rtn_val)
            self.camFlag = False
            return
        else:
            print("Capture began, rtn_val = ", rtn_val)

        while self.camFlag:
            # print "capture"
            rtn_val = ArducamSDK.Py_ArduCam_captureImage(self.handle)
            if rtn_val > 255:
                print("Error capture image, rtn_val = ", rtn_val)
                if rtn_val == ArducamSDK.USB_CAMERA_USB_TASK_ERROR:
                    break
            time.sleep(0.005)

        self.camFlag = False
        ArducamSDK.Py_ArduCam_endCaptureImage(self.handle)


    def readImage_thread(self):
        global COLOR_BayerGB2BGR, COLOR_BayerRG2BGR, COLOR_BayerGR2BGR, COLOR_BayerBG2BGR
        data = {}
        #ArducamSDK.Py_ArduCam_writeSensorReg(handle,12328,200)
        if not os.path.exists("images"):
            os.makedirs("images")
        while self.camFlag:
            if ArducamSDK.Py_ArduCam_availableImage(self.handle) > 0:
                rtn_val, data, rtn_cfg = ArducamSDK.Py_ArduCam_readImage(self.handle)
                datasize = rtn_cfg['u32Size']
                if rtn_val != 0 or datasize == 0:
                    ArducamSDK.Py_ArduCam_del(self.handle)
                    print("read data fail!")
                    continue
                image = convert_image(data, rtn_cfg, self.color_mode)
                self.getFlag=True
                self.ımage_=image
                ArducamSDK.Py_ArduCam_del(self.handle)
                # print("------------------------display time:",(time.time() - display_time))
            else:
                time.sleep(0.001)
                self.getFlag=False

    def setExposure(self,value):
        ArducamSDK.Py_ArduCam_writeSensorReg(self.handle,12306,value)

    def setGain(self,value):
        ArducamSDK.Py_ArduCam_writeSensorReg(self.handle, 12328, value)

    def getImage(self):
        a=self.getFlag
        b=self.ımage_
        return a,b

    def startCam(self,resolution):
        if resolution==1:
            if self.camera_initFromFile("MT9J001_MONO_8b_640x480_27fps.cfg"):
                ArducamSDK.Py_ArduCam_setMode(self.handle, ArducamSDK.CONTINUOUS_MODE)
        if resolution==2:
            if self.camera_initFromFile("MT9J001_MONO_8b_1280x720_20fps.cfg"):
                ArducamSDK.Py_ArduCam_setMode(self.handle, ArducamSDK.CONTINUOUS_MODE)
        if resolution==3:
            if self.camera_initFromFile("MT9J001_MONO_8b_1920x1080_20fps.cfg"):
                ArducamSDK.Py_ArduCam_setMode(self.handle, ArducamSDK.CONTINUOUS_MODE)
        if resolution==4:
            if self.camera_initFromFile("MT9J001_MONO_8b_1920x1080_subsampling_20fps.cfg"):
                ArducamSDK.Py_ArduCam_setMode(self.handle, ArducamSDK.CONTINUOUS_MODE)
        if resolution==5:
            if self.camera_initFromFile("MT9J001_MONO_8b_3664x2748_4fps.cfg"):
                ArducamSDK.Py_ArduCam_setMode(self.handle, ArducamSDK.CONTINUOUS_MODE)
        if resolution==6:
            if self.camera_initFromFile("MT9J001_MONO_12b_3664x2748_2fps.cfg"):
                ArducamSDK.Py_ArduCam_setMode(self.handle, ArducamSDK.CONTINUOUS_MODE)

    def run(self):
        global COLOR_BayerGB2BGR, COLOR_BayerRG2BGR, COLOR_BayerGR2BGR, COLOR_BayerBG2BGR
        data = {}
        rtn_val = ArducamSDK.Py_ArduCam_beginCaptureImage(self.handle)
        if rtn_val != 0:
            print("Error beginning capture, rtn_val = ", rtn_val)
            self.camFlag = False
            return
        else:
            print("Capture began, rtn_val = ", rtn_val)
        while self.camFlag:
            rtn_val = ArducamSDK.Py_ArduCam_captureImage(self.handle)
            if rtn_val > 255:
                print("Error capture image, rtn_val = ", rtn_val)
                if rtn_val == ArducamSDK.USB_CAMERA_USB_TASK_ERROR:
                    break
            time.sleep(0.005)
            if ArducamSDK.Py_ArduCam_availableImage(self.handle) > 0:
                rtn_val, data, rtn_cfg = ArducamSDK.Py_ArduCam_readImage(self.handle)
                datasize = rtn_cfg['u32Size']
                if rtn_val != 0 or datasize == 0:
                    ArducamSDK.Py_ArduCam_del(self.handle)
                    print("read data fail!")
                    continue
                image = convert_image(data, rtn_cfg, self.color_mode)
                self.change_pixmap_signal.emit(image)
                ArducamSDK.Py_ArduCam_del(self.handle)
                # print("------------------------display time:",(time.time() - display_time))
            else:
                time.sleep(0.001)


    def terminate(self):
        self.camFlag = False

