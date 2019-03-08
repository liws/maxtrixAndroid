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

    def startMonitor(self):
        self.exitFlag = False
        if(not GC.checkGC()):
            return
        
        cpuCmd = self.getCpuCmd()
        test = 1
        while(not self.exitFlag):
            sampleTime = util.getCurTimeStr()
            process=subprocess.Popen(cpuCmd,shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            process.wait()
            process_out = process.stdout.readlines()
            process.stdout.close()
            self.parseCpu(sampleTime, process_out)
            time.sleep(self.intervalTime)
            test+=1
            if(test == 10):
                break

        self.monitorData.save2Csv(self.outFile)


    def parseCpu(self,sampleTime,process_out):
        if(len(process_out)==0):
            return
        lines=process_out[0].split("%")
        line=lines[0].replace("\r\n","").strip()
        self.monitorData.append((sampleTime,line))
        print(self.monitorData.data)
        pass


    def getCpuCmd(self):
        cmd = "{} shell dumpsys cpuinfo | grep {}".format(GC.ADB,GC.APK)
        return cmd