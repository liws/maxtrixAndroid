#coding=utf-8
from core import util
from core.monitorMemery import MonitorMemery
from core.monitorCpu import MonitorCpu
from core.monitorBatteryTemperature import MonitorBatteryTemperature
from core.config import GC;
import os;
import argparse
import threading
import time;

def getArgParse():
    parser = argparse.ArgumentParser(description="Monitor Apk Performance ")
    parser.add_argument("pkg",help="Android package ")
    parser.add_argument("--adb",action="store",help="adb path")
    parser.add_argument("--len",action = "store",type=int,help="monitor second",default=30)
    parser.add_argument("--output",action="store",help="output path")
    parser.add_argument("-a",action="store_true", help="Monitor All ")
    parser.add_argument("-m",action="store_true", help="Monitor Memory ")
    parser.add_argument("-c",action="store_true", help="Monitor Cpu ")
    parser.add_argument("-b",action="store_true", help="Monitor Battery ")
    return parser

def parseArgsAndGenMonitorList(args):
    if(not args.a and not args.m and not args.c and not args.b):
        ap.print_help()
        exit(0)
    GC.APK=args.pkg
    if(args.adb):
        GC.ADB = args.adb
    
    if(args.output):
        GC.OUTPATH = args.output

    curTime= util.getCurTimeStr()
    GC.OUTPATH = os.path.join(GC.OUTPATH,curTime)
    if( not os.path.exists(GC.OUTPATH)):
        os.makedirs(GC.OUTPATH)

    monitorList=[]
    if(args.a):
        addMemoMonitor(monitorList)
        addCpuMonitor(monitorList)
        addBatteryMonitor(monitorList)
        pass
    else:
        if(args.m):
            addMemoMonitor(monitorList)
        if(args.c):
            addCpuMonitor(monitorList)
        if(args.b):
            addBatteryMonitor(monitorList)
        pass
    return monitorList

def addMemoMonitor(monitorList):
    outfile=os.path.join(GC.OUTPATH,"memory.csv")
    monitor = MonitorMemery(outfile,2)
    monitorList.append(monitor)

def addCpuMonitor(monitorList):
    outfile=os.path.join(GC.OUTPATH,"cpu.csv")
    monitor = MonitorCpu(outfile,2)
    monitorList.append(monitor)

def addBatteryMonitor(monitorList):
    outfile=os.path.join(GC.OUTPATH,"battery.csv")
    monitor = MonitorBatteryTemperature(outfile,2)
    monitorList.append(monitor)

def startMonitor(monitorList):
    for subMonitor in monitorList:
        handleThread = threading.Thread(target=monitorThread,args=(subMonitor,))
        handleThread.start()

def monitorThread(monitor):
    monitor.startMonitor()


def endMoitor(monitorList):
    for subMonitor in monitorList:
        subMonitor.endMonitor()

if(__name__=="__main__"):
    ap = getArgParse()
    args=ap.parse_args()
    
    monitorList = parseArgsAndGenMonitorList(args)
    len=args.len

    print("<<<<<<Monitor Global Config")
    GC.printGCInfo()
    print("<<<<<<Monitor List Description")
    for subMonitor in monitorList:
        subMonitor.printDesc()

    startMonitor(monitorList)
    time.sleep(len)
    endMoitor(monitorList)
    



    # outfile=os.path.join(GC.OUTPATH,"batteryoutput.csv")
    # batteryMonitor = MonitorBatteryTemperature(outfile,2)
    # batteryMonitor.startMonitor()

    # outfile=os.path.join(GC.OUTPATH,"cpuoutput.csv")
    # monitorCpu = MonitorCpu(outfile,2)
    # monitorCpu.startMonitor()

    # outfile=os.path.join(GC.OUTPATH,"memeryoutput.csv")
    # monitorMeme = MonitorMemery(outfile,2) 
    # monitorMeme.startMonitor()
    # print(outfile)
