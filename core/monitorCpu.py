#coding=utf-8
from monitorBase import MonitorBase
from .config import GC
from monitorData import CpuData
import os
import subprocess
import util
import time

class   MonitorCpu(MonitorBase):
    '''
    Cpu 监控
    '''
    def __init__(self,outFile,intervalTime):
        pass
        # MonitorBase(outFile,intervalTime)
        super(MonitorCpu,self).__init__(outFile,intervalTime)
        self.monitorData = CpuData()
        self._descrption="Monitor Cpu {}".format(outFile)


    def parseMonitorData(self,sampleTime,process_out):
        if(len(process_out)==0):
            return
        lines=process_out[0].split("%")
        line=lines[0].replace("\r\n","").strip()
        self.monitorData.append((sampleTime,line))
        # print(self.monitorData.data)
        pass

    def getCmd(self):
        cmd = "{} shell dumpsys cpuinfo | grep {}".format(GC.ADB,GC.APK)
        return cmd