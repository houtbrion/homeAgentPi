#!/usr/bin/env python
# -*- coding: utf-8 -*-

import grovepi
import math
import time
# デバッグ用モジュールのインポート
from logging import getLogger, StreamHandler, NullHandler, DEBUG

# 動作モード
#DEBUG_FLAG=False
DEBUG_FLAG=True

# センシングのインターバル
INTERVAL=2

#
# センサの設定情報を定義するグローバル変数
#
# 温度・湿度センサ
DHT_PIN = 4  # The Sensor goes on digital port 4.
DHT_TYPE=1 # DHT11 : 0 , DHT22 : 1

class RoomSensors:
    dhtPin=0
    dhtType=0
    dhtResult=False
    temperature=0.0
    humidity=0.0
    lightResult=False
    lux=0
    def getValues(self):
        global logger
        global grovepi
        try:
            [temp,hum] = grovepi.dht(sensor,tempSensorType)  
            if math.isnan(temp) == False and math.isnan(humidity) == False:
                self.temperature=temp
                self.humidity=hum
                self.dhtResult=True
                logger.debug("temperature = %.02f C humidity =%.02f%%"%(temp, hum))
            else:
                self.dhtResult=False
        except IOError:
            self.dhtResult=False
            logger.debug("DHT Error")



def setup(debugFlag, dhtPin, dhtType):
    global logger
    global sensor
    logger = getLogger(__name__)
    if debugFlag:
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        logger.setLevel(DEBUG)
    else:
        handler = NullHandler()
    logger.addHandler(handler)
    sensor.dhtPin=dhtPin
    sensor.dhtType=dhtType

def loop(interval):
    global logger
    global sensor
    while True:
        sensor.getValue()
        time.sleep(interval)
#
# メイン
#
if __name__ == '__main__':
    setup(DEBUG_FLAG,DHT_PIN, DHT_TYPE)
    loop(INTERVAL)

