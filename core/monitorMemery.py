#coding=utf-8

from .config import GC
from .monitorData import MemeryData
from monitorBase import MonitorBase
import os
import sys
import subprocess
import time
import util


class MonitorMemery(MonitorBase):
    '''
    内存监控
    '''
    def __init__(self,outFile,intervalTime):
        pass
        super(MonitorMemery,self).__init__(outFile,intervalTime)
        self.monitorData = MemeryData()

    def startMonitor(self):
        self.exitFlag = False
        if(not GC.checkGC()):
            return
        memeryCmd=self.getMemeryCmd()
        
        test = 1
        while(not self.exitFlag):
            nowTime=util.getCurTimeStr()
            process=subprocess.Popen(memeryCmd,shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            process.wait()
            process_out = process.stdout.readlines()
            process.stdout.close()
            self.parseMemery(nowTime, process_out)
            time.sleep(self.intervalTime)
            test+=1
            if(test == 10):
                break

        self.monitorData.save2Csv(self.outFile)

    def parseMemery(self,sampleTime, process_out):
        lists=[]
        for index in range(0,len(process_out)):
            if(process_out[index].startswith("  Native Heap")):
                lists.append(index)

        lines=process_out[lists[0]].split(' ')

        heap=[]
        for index in range(len(lines)):
            line=lines[index]
            if(line != '' or ('\r\n' in line)):
                heap.append(line.replace("\r\n",''))
        self.monitorData.append((sampleTime,float(heap[-3])/1024,float(heap[-2])/1024,float(heap[-1])/1024))
        print(self.monitorData.data)
        pass

    def getMemeryCmd(self):
        memeryCmd = "{} shell dumpsys meminfo -a {}".format(GC.ADB,GC.APK)
        return memeryCmd