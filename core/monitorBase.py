#coding=utf-8
import util
import subprocess
import time
from config import GC

class   MonitorBase(object):
    '''
    监控基类
    '''
    def __init__(self,outFile,intervalTime):
        self.outFile = outFile
        self.intervalTime=intervalTime
        self.exitFlag=False
        self.monitorData=None

    def endMonitor(self):
        self.exitFlag=True

    def startMonitor(self):
        self.exitFlag = False
        if(not GC.checkGC()):
            return
        cmd=self.getCmd()
        
        test = 1
        while(not self.exitFlag):
            nowTime=util.getCurTimeStr()
            process=subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            process.wait()
            process_out = process.stdout.readlines()
            process.stdout.close()
            self.parseMonitorData(nowTime, process_out)
            time.sleep(self.intervalTime)
            test+=1
            if(test == 10):
                break
        self.monitorData.save2Csv(self.outFile)

    
    def parseMonitorData(self,sampleTime, process_out):
        pass

    def getCmd(self):
        pass