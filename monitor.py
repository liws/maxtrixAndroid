from core import util
from core.monitorMemery import MonitorMemery
from core.monitorCpu import MonitorCpu
from core.monitorBatteryTemperature import MonitorBatteryTemperature
from core.config import GC;
import os;
import argparse
import threading
import time;


class   Monitor(object):

    @classmethod
    def useHelp(cls):
        pass
        msg ='''
        Monitor Param Prepare
        --pkg            pkgPath    required
        --adb            adb path
        --output         output path
        -a               Monitor All
        -m               Monitor Memory
        -c               Monitor Cpu
        -b               Monitor Battery

        sample1: monitor pkg for all
        startMonitor(-a,pkg="com.test.lgrass",outpath="/xxx/output") 
        
        sample2: monitor pkg for memory,cpu
        startMonitor(-m,-c,pkg="com.test.lgrass")
        '''
        print(msg)


    def __init__(self):
        pass
        self.pkg=None
        self.monitorList=[]
    

    def endMonitor(self):
        for subMonitor in self.monitorList:
            subMonitor.endMonitor()


    def startMonitor(self,*args,**argv):
        if(not self.checkParams(args,argv)):
            print("start monitor failed,param error")
            Monitor.useHelp()
            return

        print("<<<<<<Monitor Global Config")
        GC.printGCInfo()
        print("<<<<<<Monitor List Description")
        for subMonitor in self.monitorList:
            subMonitor.printDesc()

        for subMonitor in self.monitorList:
            handleThread = threading.Thread(target=self.monitorThread,args=(subMonitor,))
            handleThread.start()

    def monitorThread(self,monitor):
        monitor.startMonitor()
    
    def checkParams(self,args,argv):
        if(not args or not argv):
            return False
        
        for (key,value) in argv.items():
            if(key == "pkg"):
                GC.APK = value
            elif(key == "adb"):
                GC.ADB = value
            elif(key=="output"):
                GC.OUTPATH = value
        if(not GC.APK):
            return False

        curTime= util.getCurTimeStr()
        GC.OUTPATH = os.path.join(GC.OUTPATH,curTime)
        if( not os.path.exists(GC.OUTPATH)):
            os.makedirs(GC.OUTPATH)

        if("-a" in args):
            self.__addMemoMonitor()
            self.__addCpuMonitor()
            self.__addBatteryMonitor()
        else:
            for subParam in args:
                if(subParam == "-m"):
                    self.__addMemoMonitor()
                elif(subParam == "-c"):
                    self.__addCpuMonitor()
                elif(subParam == "-b"):
                    self.__addBatteryMonitor()
        
        if(len(self.monitorList)< 1):
            return False

        return True


    def __addMemoMonitor(self):
        outfile=os.path.join(GC.OUTPATH,"memory.csv")
        monitor = MonitorMemery(outfile,2)
        self.monitorList.append(monitor)

 
    def __addCpuMonitor(self):
        outfile=os.path.join(GC.OUTPATH,"cpu.csv")
        monitor = MonitorCpu(outfile,2)
        self.monitorList.append(monitor)

  
    def __addBatteryMonitor(self):
        outfile=os.path.join(GC.OUTPATH,"battery.csv")
        monitor = MonitorBatteryTemperature(outfile,2)
        self.monitorList.append(monitor)



if(__name__=="__main__"):
    pass
    monitor = Monitor()
    monitor.startMonitor("-m","-c","-b",pkg="cn.lemongrassmedia.loveworld.jrtt")
    import time
    time.sleep(20)
    monitor.endMonitor()