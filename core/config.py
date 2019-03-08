#coding=utf-8
import os;

class   GC(object):
    '''
     全局变量
    '''
    APK=None
    ADB=None
    OUTPATH=None

    @classmethod
    def InitDefaultParam(cls):
        result=os.popen("which adb")
        cmdAdb = result.read()
        if cmdAdb:
            GC.ADB = cmdAdb.replace("\n","")
        GC.OUTPATH=os.path.abspath("./")

    @classmethod
    def checkGC(cls):
        if(not GC.APK )or (not GC.ADB )or (not GC.OUTPATH):
            GC.printGCInfo()
            return False
        return True

    @classmethod    
    def printGCInfo(cls):
        print("-----GCInfo------")
        print("GC.APK",GC.APK)
        print("GC.ADB",GC.ADB)
        print("GC.OUTPATH",GC.OUTPATH)
