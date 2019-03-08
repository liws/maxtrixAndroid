#coding=utf-8
from core import * 
from core.monitorMemery import MonitorMemery
from core.monitorCpu import MonitorCpu
from core.monitorBatteryTemperature import MonitorBatteryTemperature
from core.config import GC;
import os;

if(__name__=="__main__"):
    print("run.py")

    GC.APK="com.tencent.tmgp.loveworld.lgrass"

    outfile=os.path.join(GC.OUTPATH,"batteryoutput.csv")
    batteryMonitor = MonitorBatteryTemperature(outfile,2)
    batteryMonitor.startMonitor()

    
    # outfile=os.path.join(GC.OUTPATH,"cpuoutput.csv")
    # monitorCpu = MonitorCpu(outfile,2)
    # monitorCpu.startMonitor()

    # outfile=os.path.join(GC.OUTPATH,"memeryoutput.csv")
    # monitorMeme = MonitorMemery(outfile,2) 
    # monitorMeme.startMonitor()
    # print(outfile)
