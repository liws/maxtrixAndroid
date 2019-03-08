#coding=utf-8

import time

def getCurTimeStr():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))