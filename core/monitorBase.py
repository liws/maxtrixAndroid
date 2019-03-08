#coding=utf-8

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