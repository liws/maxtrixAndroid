#coding=utf8

# cn.lemongrassmedia.loveworld.jrtt

import os

apk = "cn.lemongrassmedia.loveworld.jrtt"
cmd = "python ../run.py {} -a --len 60".format(apk)
print(cmd)
# os.popen(cmd)#error when exec
os.system(cmd)