#!/usr/bin/env python3

import requests
import time

import cv2
import numpy as np

# python print to stderr (most portable and flexible)
import sys
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

ip='192.168.0.103'
port='8080'

class IPWebCam:
    def __init__(self, ip, port, force_set=False):
        self.ip = ip
        self.port = port
        self.url = "http://"+self.ip+":"+self.port+"/"
        self.force_set = force_set
          # before every image, choose main or front camera
    
    def set_light(self, onoff):
        cmd = "enabletorch" if onoff else "disabletorch"
        requests.get(self.url+cmd)
    
    def test_set_light(self):
        self.set_light(True)
        time.sleep(3)
        self.set_light(False)
    
    def get_image(self, main_camera=True):
        onoff = "off" if main_camera else "on"
        if self.force_set or onoff is not self.lastonoff:
            requests.get(self.url+"settings/ffc?set="+onoff)
        self.lastonoff = onoff
        # get auto-focussed image
        resp = requests.get(self.url+"photoaf.jpg", stream=True).raw
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image

## OpenCV missing routine:
def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)
## end of ResizeWithAspectRatio

cam = IPWebCam(ip, port, True)
eprint("Testing light on and off")
cam.test_set_light()
eprint("Light tested.")

# for testing
for pair in [(False, True), (True, True), (False, False), (True, False)]:
    light = pair[0]
    maincam = pair[1]
    eprint("Taking picture "+("with" if light else "without")
      +" light from "+("main" if maincam else "front")+" camera.")
    cam.set_light(light)
    i = cam.get_image(maincam)
    r = ResizeWithAspectRatio(i, width=300)
    cv2.imshow('image',r)
    cv2.waitKey(0)

cam.set_light(False)
cv2.destroyAllWindows()
