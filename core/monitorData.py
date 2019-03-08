#coding=utf-8

import csv

class MonitorData:
    def __init__(self):
        self.data=[]
        pass

    def append(self,value):
        self.data.append(value)
    
    def save2Csv(self,outfile):
        csvFile = open(outfile,'wb')
        writer = csv.writer(csvFile)
        writer.writerows(self.data)
        csvFile.close()


class MemeryData(MonitorData):
    def __init__(self):
        MonitorData()
        self.clear()

    def clear(self):
        self.data=[("sampleTime","Native Heap Size","Native Heap Alloc","Native Heap Free")]
        pass
    
    

class CpuData(MonitorData):
    def __init__(self):
        MonitorData()
        self.clear()

    def clear(self):
        self.data=[("sampleTime","cpuValue")]

        