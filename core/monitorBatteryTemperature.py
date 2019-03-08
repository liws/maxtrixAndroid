 #coding=utf-8

from .config import GC
from .monitorData import BatteryData
from monitorBase import MonitorBase
import os
import sys
import subprocess
import time
import util


class MonitorBatteryTemperature(MonitorBase):
    '''
    电量监控
    '''
    def __init__(self,outFile,intervalTime):
        pass
        super(MonitorBatteryTemperature,self).__init__(outFile,intervalTime)
        self.monitorData = BatteryData()
    

    def parseMonitorData(self,sampleTime, process_out):
        if(len(process_out)==0):
            return
        level = 0
        temperature =0
        for line in process_out:
            if("level" in line):
                levelData=line.split(":")
                level=int(levelData[1].replace("\r\n","").strip())
            elif("temperature" in line):
                temperatureData=line.split(":")
                temperature=int(temperatureData[1].replace("\r\n","").strip())
            
            if(level != 0 and temperature != 0):
                break
        self.monitorData.append((level,temperature))
        print(self.monitorData.data)

    def getCmd(self):
        cmd = "{} shell dumpsys battery".format(GC.ADB)
        return cmd