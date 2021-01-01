#!/usr/bin/env python3

import requests
import time

ip='192.168.0.101'
port='8080'

def makeurl(s):
    return "http://"+ip+":"+port+"/"+s


def light(onoff):
    cmd = "enabletorch" if onoff else "disabletorch"
    requests.get(makeurl(cmd))

light(True)
time.sleep(3)
light(False)
