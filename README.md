# Lego: Random Ideas and Tools for EV3 Brick Running ev3dev Linux

This repository stores my personal experiments with ev3 brick running ev3dev
linux. Most of it is not sufficiently general but it may still serve as a
source of ideas for others.

The files ``.history-*`` are my local bash histories, for finding how I ran
what.

## Connecting via Bluetooth

brickman:
Wireless->Bluetooth->scroll to my paired NB
Network Connection -> Connect
...Bluetooth icon gets green instead of white in Mate side panel
...but leads to GDBus.Error:net.connman.Error.Failed: Input/output error

Remove devices from both devices
Switch off both bluetooths.
Fire up brick BT, Make brick visible
Open BT devices on NB
Search
Click on ev3dev
Pair
Confirm pairing on both devices
Then scroll to NB-device in brickman
click Network Connection
click Connect (*not* connect directly)
On NB **CONFIRM**. The window gets often hidden somewhere, so this tends to timeout...
Brickman should go over Associating to Connecting to Connected



## Basic Commands

```
ssh robot@ev3dev.local
# heslo maker
python3
ev3.Sound.speak('Welcome!').wait()
m = ev3.LargeMotor('outB')
m.run_timed(time_sp=1000,speed_sp=500)


```

## Creating a fresh robot card

Download from EV3DEV:

Find out the correct device (here ``/dev/mmcblk0``) e.g. by checking ``gnome-disks``.

Flash it simply with ``dd``:
```
sudo dd if=ev3dev-stretch-ev3-generic-2020-04-10.img of=/dev/mmcblk0 bs=4M && sync
```

## Populating fresh robot card

```
# connect, e.g.
ssh robot@192.168.0.105

# installing core packages I need
sudo apt-get update
sudo apt-get install gawk
sudo apt-get install python3-pip ## downloads 82 megs! Considering it for rpyc

# upgrading only ev3dev-python:
sudo apt-get update
sudo apt-get install --only-upgrade python3-ev3dev
```

```
git clone https://github.com/obo/lego.git
# use our bashrc and vimrc:
bash lego/environment/setup_environment.sh
```

## numpy and scipy on EV3

Highly recommended to use Debian pre-compiled packages, i.e.:

```
sudo apt install python3-numpy python3-scipy
```

## Interesting Ideas from ev3dev Python Demos

git clone https://github.com/ev3dev/ev3dev-lang-python-demo.git

ev3dev-lang-python-demo/robots/R3PTAR/r3ptar.py
... ukazuje vicevlaknovost
... cili tim by melo jit udelat rizeni a soucasne moznost zapnout sledovani cary

ev3dev-lang-python-demo/robots/EV3RSTORM/ev3rstorm.py
... zahrnuje kresleni na display! Cili tim by se dalo delat nejake malovani mapy, kudy projel

## Multipurpose Track3r Proposal

- vicevlaknova aplikace
- triggery na 4. kanalu IR pro ovladani nabidky
- tank na 1. kanalu
- pomalejsi tank na 2. kanalu
V nabidce:
- sleduj caru
  1. Rozhledne se vlevo a vpravo, tim pozna barvu cary a okoli, a taky tloustku cary.
  2. Vyrazi po care, zastavi na jakekoli jine barve nez cara nebo pozadi.


## Inspiring Youtube Videoss

http://www.mindcuber.com/mindcub3r/mindcub3r.html
http://www.mindcuber.com/mindcub3r/MindCub3r-v1p0.pdf


https://www.youtube.com/watch?v=JlWOKaxKrIE
...reptar a kocka

https://www.youtube.com/watch?v=uIPrN-b-Zb0
...spybot, dobry pasovy

https://www.youtube.com/watch?v=JOUGsgqYraE
...ruka

https://www.youtube.com/watch?v=bSmXZyNWm28
...tridic lentilek

https://www.youtube.com/watch?v=5VAhH7GUoks
...hledani veci

https://www.youtube.com/watch?v=cXgB3lIvPHI
...hraje na kytaru

https://www.youtube.com/watch?v=FCWNNk1G2UU
...had, slon

https://www.youtube.com/watch?v=6xCd55oSgO4
...hromska krabice

https://www.youtube.com/watch?v=dIgSKPzLC9g
...telegraf

https://www.youtube.com/watch?v=0d0ktACCwT4
...best of evdev

https://www.youtube.com/watch?v=LZYr646Ul4Q
...spirograph

https://www.youtube.com/watch?v=0Aw23jQkP2g
...gearbox


## Other interesting links:

Camera: https://siyahodacom.wordpress.com/2017/10/01/adding-webcam-to-ev3-ev3dev/

Camera-based line tracking:
http://karandashsamodelkin.blogspot.cz/

Pixy-camera: http://www.ev3dev.org/docs/tutorials/using-pixy-camera/

lejos opencv face recognition:
http://thinkbricks.net/face-tracking-on-ev3-using-lejos-0-9-1/

https://github.com/Klabbedi/ev3
...a better line follower, PID algorithm
(but this will not work on red lines, because in reflected-light scanning, red led is used, so red is the same as white)

http://pazhong.net/code/number_detect/number_detect.py
... number detection and draw it on screen

https://github.com/dlech/ev3dev-photo-booth

and a similar tutorial in C++:
https://github.com/FrankBau/raspi-repo-manifest/wiki/OpenCV


https://github.com/YuliangXiu/PoseFlow
... online pose tracking for human body



## Trying to get my old Logitech camera running

lsusb
Bus 001 Device 003: ID 046d:08ae Logitech, Inc. QuickCam for Notebooks

sudo hwinfo --usb
04: USB 00.0: 11200 TV Card
  [Created at usb.122]
  Unique ID: ADDn.elweGVRLXdD
  Parent ID: k4bc.BtRjRTLQ986
  SysFS ID: /devices/platform/ohci.0/usb1/1-1/1-1:1.0
  SysFS BusID: 1-1:1.0
  Hardware Class: tv card
  Model: "Logitech Camera"
  Hotplug: USB
  Vendor: usb 0x046d "Logitech, Inc."
  Device: usb 0x08ae "Camera"
  Revision: "1.00"
  Speed: 12 Mbps
  Module Alias: "usb:v046Dp08AEd0100dc00dsc00dp00icFFiscFFipFFin00"
  Driver Info #0:
    Driver Status: zc0301 is not active
    Driver Activation Cmd: "modprobe zc0301"
  Config Status: cfg=new, avail=yes, need=no, active=unknown
  Attached to: #3 (Hub)

dmesg
[ 4957.057832] usb 1-1: USB disconnect, device number 2
[ 4968.794243] usb 1-1: new full-speed USB device number 3 using ohci
[ 4969.013560] usb 1-1: New USB device found, idVendor=046d, idProduct=08ae
[ 4969.013649] usb 1-1: New USB device strings: Mfr=0, Product=2, SerialNumber=0
[ 4969.013705] usb 1-1: Product: Camera         

uname -r
4.4.87-22-ev3dev-ev3

The issue where I ask for help: https://github.com/ev3dev/ev3dev/issues/64

This is what could possibly help:
 I installed the kernel options: gspca (in v4l) and USB audio (in alsa USB devices) and then inserted the corresponding modules: zc3xx and snd_usb_audio. 


## Connecting via USB cable

There is a tutorial: http://www.ev3dev.org/docs/tutorials/connecting-to-the-internet-via-usb/

But it didn't really work for me.

When brickman connected to wired connection and has shown me its IP address, I manually configured my NB for that network:

ifconfig enp0s20f0u3 169.254.214.1
 
ssh robot@169.254.214.149

On the robot:
  sudo ifconfig
  myip=$(sudo ifconfig | sed -n 's/.*inet \([0-9][0-9.]*\).*/\1/p' | grep -v 127.0.0.1)
  sudo /sbin/route add default gw $(echo $myip | cut -d. -f1-3).1
  echo "nameserver 1.1.1.1" | sudo tee /etc/resolv.conf

And on my laptop: (this may have not been necessary, not sure)
echo 1 > /proc/sys/net/ipv4/ip_forward
sudo modprobe ip_tables
sudo modprobe ip_conntrack
sudo modprobe ip_conntrack_irc
sudo modprobe ip_conntrack_irc
sudo modprobe ip_conntrack_ftp
sudo iptables -t nat -A POSTROUTING -o wlp4s0 -j MASQUERADE
... to forward robot's network through my NB


### Still some problems:

[ 2540.370361] usb 1-1: new full-speed USB device number 2 using ohci-da8xx
[ 2540.643482] usb 1-1: New USB device found, idVendor=046d, idProduct=08ae
[ 2540.643546] usb 1-1: New USB device strings: Mfr=0, Product=2, SerialNumber=0
[ 2540.643581] usb 1-1: Product: Camera         
[ 2542.272748] Linux video capture interface: v2.00
[ 2542.395353] gspca_main: v2.14.0 registered
[ 2542.471259] gspca_main: gspca_zc3xx-2.14.0 probing 046d:08ae
[ 2543.313943] input: gspca_zc3xx as /devices/platform/soc@1c00000/ohci-da8xx/usb1/1-1/input/input2
[ 2543.344797] usbcore: registered new interface driver gspca_zc3xx
[ 2544.366522] usbcore: registered new interface driver snd-usb-audio

robot@ev3dev:~/lego$ streamer -f jpeg -o image.jpeg
files / video: JPEG (JFIF) / audio: none
fifo max fill: audio 0/0, video 1/16, convert 1/16  


## Taking pictured from camera

streamer -f jpeg -o image.jpeg

## Recording sound through USB camera

arecord -D plughw:1,0 -t wav --duration=5 test.wav
... worked out of the box

http://ofalcao.pt/blog/2017/lego-voice-control-ev3


## OpenCV links

https://www.pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles/

https://thecodacus.com/opencv-object-tracking-colour-detection-python/#.WuB4pta-lUA

## Connecting via wifi [solved]
https://github.com/ev3dev/ev3dev/issues/1082

lsusb:
Bus 001 Device 003: ID 083a:4505 Accton Technology Corp. SMCWUSB-G 802.11bg

hwinfo --usb
07: USB 00.0: 0000 Unclassified device
  [Created at usb.122]
  Unique ID: lfzD.wkm1Arvlfj3
  Parent ID: ADDn._cOmnuCBvb4
  SysFS ID: /devices/platform/soc@1c00000/ohci-da8xx/usb1/1-1/1-1.1/1-1.1:1.0
  SysFS BusID: 1-1.1:1.0
  Hardware Class: unknown
  Model: "Accton SMCWUSB-G 802.11bg"
  Hotplug: USB
  Vendor: usb 0x083a "Accton"
  Device: usb 0x4505 "SMCWUSB-G 802.11bg"
  Revision: "48.10"
  Speed: 12 Mbps
  Module Alias: "usb:v083Ap4505d4810dcFFdscFFdpFFicFFisc00ip00in00"
  Config Status: cfg=new, avail=yes, need=no, active=unknown
  Attached to: #8 (Hub)

ifconfig
usb1: flags=-28669<UP,BROADCAST,MULTICAST,DYNAMIC>  mtu 1500
        ether 22:16:53:5f:74:d2  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lsmod
Module                  Size  Used by
sr_mod                 12624  0
cdrom                  28732  1 sr_mod
snd_usb_audio         139864  0
snd_hwdep               5257  1 snd_usb_audio
snd_usbmidi_lib        19259  1 snd_usb_audio
snd_rawmidi            19974  1 snd_usbmidi_lib
snd_seq_device          4207  1 snd_rawmidi
gspca_zc3xx            41388  0
gspca_main             22080  1 gspca_zc3xx
v4l2_common             4978  1 gspca_main
videodev              127782  3 v4l2_common,gspca_zc3xx,gspca_main
iptable_nat             1728  0
nf_conntrack_ipv4       5927  1
nf_defrag_ipv4          1634  1 nf_conntrack_ipv4
nf_nat_ipv4             5140  1 iptable_nat
nf_nat                 14692  1 nf_nat_ipv4
nf_conntrack           87388  3 nf_conntrack_ipv4,nf_nat_ipv4,nf_nat
libcrc32c               1100  2 nf_conntrack,nf_nat
usb_f_rndis            15528  2
usb_f_ecm               6278  2
u_ether                12402  2 usb_f_ecm,usb_f_rndis
ev3_uart_sensor_ld      7767  2
ev3_uart_sensor        13506  1 ev3_uart_sensor_ld
nxt_i2c_sensor         35440  1 ev3_uart_sensor
servo_motor_class       6378  1 nxt_i2c_sensor
hci_uart               16410  0
serdev                  8117  1 hci_uart
suart_emu              23989  0
ev3_analog_sensor       5077  0
uinput                  8046  0
libcomposite           41550  16 usb_f_ecm,usb_f_rndis
configfs               28703  4 usb_f_ecm,usb_f_rndis,libcomposite
ip_tables              10235  1 iptable_nat
x_tables               19232  1 ip_tables


robot@ev3dev:~$ ev3dev-sysinfo -m
<!-- Copy everything between these lines -->
**System info (from `ev3dev-sysinfo`)**
```
Image file:         ev3dev-stretch-ev3-generic-2018-04-22
Kernel version:     4.14.35-ev3dev-2.0.0-ev3
Brickman:           0.10.0
ev3devKit:          0.5.2
Board:              board0
BOARD_INFO_HW_REV=8
BOARD_INFO_MODEL=LEGO MINDSTORMS EV3
BOARD_INFO_ROM_REV=6
BOARD_INFO_SERIAL_NUM=0016535F74D2
BOARD_INFO_TYPE=main
```
<!-- Copy everything between these lines -->


Brickman says Wifi: Not available

2018-05-08

After a kernel update, Brickman can power up wifi, but Start Scan says:
  DGBus.Error:net.connman.Error.NoCarrier. No carrier

Fixed by adding the correct firmware from:

https://sourceforge.net/projects/zd1211/files/zd1211-firmware/

After powering the wifi off and on, scan was possible.

However, picking my wifi and trying to connect failed with:
  GDBus.Error:net.connman.Error.OperationAborted: Operation aborted
...this was actually due to my MAC filter where I allowed a different MAC
address than the dongle presented now. I can't understand where I copied the
wrong MAC address from in at the first attempt.


## Mouse input?

ls /dev/input/by-id/
should say: usb-0461_USB_Optical_Mouse-event-mouse

Following mouse is implemented here:
follow_mouse:
  https://github.com/cavenel/ev3-print3rbot/blob/master/writer.py

## LCD

Use:
  brickrun ./command

sudo openvt -s -w -- sudo --user <user> -- COMMAND
...this should allow me to run the COMMAND with access to the screen

Another way to connect to the virtual console through ssh:
  sudo chvt 6
  # same as typing ctrl-alt-F6
  sudo conspy

http://www.ev3dev.org/docs/tutorials/using-ev3-lcd/
https://sites.google.com/site/ev3python/learn_ev3_python/screen

My issue: https://github.com/ev3dev/ev3dev-lang-python/issues/463
...should still confirm the booth

The photo booth works (gets pictures), but does not show them on screen.
This is probably the error message:
** (brickrun:1826): CRITICAL **: brickrun.vala:100: Failed to send signal: GDBus.Error:org.freedesktop.DBus.Error.UnknownMethod: No such method 'SignalGroup'


## QR code reader:

https://www.learnopencv.com/barcode-and-qr-code-scanner-using-zbar-and-opencv/

http://aishack.in/tutorials/scanning-qr-codes-2/

https://gist.github.com/mohankumargupta/243aeb6787123cc17f1c10338bd4a82f
...this seems to be all combined into one script

## Aruco Markers, better than QR codes:

https://www.sciencedirect.com/science/article/pii/S0031320317303151
...perhaps the best option
http://www.uco.es/investiga/grupos/ava/node/57
http://www.uco.es/grupos/ava/node/25

https://docs.opencv.org/3.4.1/d5/dae/tutorial_aruco_detection.html

PnP
OpenCV has method solvePnP

keywords: slam, simultaneous localization and mapping

https://openslam-org.github.io/

https://arxiv.org/pdf/1610.03660.pdf
Image Based Camera Localization: an Overview
Yihong Wu, Fulin Tang, Heping Li

## Installing Aruco:

get from here: https://sourceforge.net/projects/aruco/files/?source=navbar

cd aruco
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/home/bojar/opt/aruco-3.0.11 ..
make
make install

cd markermapper
mkdir build
cd build
export aruco_DIR=/home/bojar/opt/aruco-3.0.11/
cmake ..
make


## Simplest white balance:

https://gist.github.com/tomykaira/94472e9f4921ec2cf582
paper+code: http://www.ipol.im/pub/art/2011/llmps-scb/?utm_source=doi

## USB Camera button

https://unix.stackexchange.com/questions/398660/detecting-usb-camera-button-event

## Beacon Seeker

see random-bits/report-beacon-location.py

0 -128  ... means that no beacon is found
0 1     ... means that we are really really close

11 54   ... means that at "angle" 11, 54 "cm"

Note that it can't distinguish front and back, so we will have to realize that
when we try to roll towards but get further, we probably need to rotate...

Or put differently, we should first stabilize the angle and only then focus on the distance.

## Steering

steering3 doesn't work at all, ignores the change.

Course: 295.63783698408236 , Left: 40 , Right:  40.0
Course: 278.2177484737596 , Left: 40 , Right:  40.0
Course: 285.1530424270078 , Left: 40 , Right:  40.0
Course: 285.3336692939426 , Left: 40 , Right:  40.0
Course: 280.5610942447775 , Left: 40 , Right:  40.0
Course: 264.02855443500306 , Left: 40 , Right:  40.0
Course: 253.69647100177943 , Left: 40 , Right:  40.0
Course: 246.29642562886042 , Left: 40 , Right:  40.0
Course: 153.73717076689826 , Left: 40 , Right:  40.0
Course: 148.49593456078 , Left: 40 , Right:  40.0
Course: 160.43838775570993 , Left: 40 , Right:  40.0
Course: 203.88310612648385 , Left: 40 , Right:  40.0
Course: 162.86323496452164 , Left: 40 , Right:  40.0
Course: 118.7518368606886 , Left: 40 , Right:  40.0
Course: -27.32580003400672 , Left: -18.139359972794622 , Right:  40
Course: -193.01178484332874 , Left: 40.0 , Right:  40
Course: -208.61163282385814 , Left: 40.0 , Right:  40
Course: -199.13916193295287 , Left: 40.0 , Right:  40
Course: -167.95320071053493 , Left: 40.0 , Right:  40
Course: -145.75692942290914 , Left: 40.0 , Right:  40
Course: -150.46866580834674 , Left: 40.0 , Right:  40
Course: -166.23221224603807 , Left: 40.0 , Right:  40
Course: -172.32239497128228 , Left: 40.0 , Right:  40
Course: -206.31446988052232 , Left: 40.0 , Right:  40
Course: -235.97961153989553 , Left: 40.0 , Right:  40
Course: -229.70066500212323 , Left: 40.0 , Right:  40
Course: -213.9761825924693 , Left: 40.0 , Right:  40
Course: -203.31686643334615 , Left: 40.0 , Right:  40
Course: -193.18282078522884 , Left: 40.0 , Right:  40
Course: -184.6898381805486 , Left: 40.0 , Right:  40

## Testing new design of pen holder

import ev3dev.ev3 as ev3
from ev3dev.auto import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev.helper import MediumMotor
m=MediumMotor(OUTPUT_A)
m.run_to_abs_pos(speed_sp=80, position_sp=30, stop_action="hold")
# pens up
m.run_to_abs_pos(speed_sp=80, position_sp=0, stop_action="hold")
# left pen down
m.run_to_abs_pos(speed_sp=80, position_sp=60, stop_action="hold")
# right pen down



## Mouse in python:


>>> import evdev
>>> device = evdev.InputDevice('/dev/input/by-id/usb-04d9_0499-event-mouse')
>>> device.capabilities()
{0: [0, 1, 2, 4], 1: [272, 273, 274], 2: [0, 1, 8], 4: [4]}
>>> device.capabilities(verbose=True)
{('EV_REL', 2): [('REL_X', 0), ('REL_Y', 1), ('REL_WHEEL', 8)], ('EV_SYN', 0): [('SYN_REPORT', 0), ('SYN_CONFIG', 1), ('SYN_MT_REPORT', 2), ('?', 4)], ('EV_KEY', 1): [(['BTN_LEFT', 'BTN_MOUSE'], 272), ('BTN_RIGHT', 273), ('BTN_MIDDLE', 274)], ('EV_MSC', 4): [('MSC_SCAN', 4)]}

Further details: http://www.antony-jordan.co.uk/python-evdev.html?i=1

Working example: random-bits/report-mouse-moves.py

Possibly simpler solutions:
https://stackoverflow.com/questions/25848951/python-get-mouse-x-y-position-on-click

## Mouse Odometry:

http://www.ijcas.org/admin/paper/files/IJCAS_v2_n4_pp485-493.pdf
...one mice could be enough??

https://pdfs.semanticscholar.org/a219/ba7106fc63f4af5ddf7fac7b407c49af2b46.pdf
...two mice needed!

https://link.springer.com/chapter/10.1007/978-1-4020-5626-0_18
...precise, but even more mice needed

https://ieeexplore.ieee.org/document/1438090/
...one or two mice

## Visual Odometry:

http://www.instructables.com/id/ROS-Visual-Odometry/
...on raspberry pi

https://github.com/uoip/monoVO-python
...python and opencv2

https://github.com/Transportation-Inspection/visual_odometry
...another one in python

## Python Logo:
Standard python turtle graphics:
from turtle import *
forward(15)
...

https://stackoverflow.com/questions/4071633/python-turtle-module-saving-an-image
...a tip how to export the canvas as svg

...but none of this is what I need. I need Logo language interpreter where I
can 1) simply get the drawing as png, and 2) replace the commands with robot
moves


pylogo ... promising but the main project page was hacked
perhaps this fork?
  https://github.com/gldnspud/pylogo

export PYTHONPATH=/home/bojar/notes/lego/pylogo:/home/bojar/notes/lego/pylogo/Pmw.1.3:
python
import pylogo.script
pylogo.script.main()
... basic programs work but the for [ i ... ] syntax is not recognized

jslogo: for [l 10 80 5] [print :l]
...means 10 15 20 25 ... 80
pylogo: for "l (gen 10 80 5) [print :l]
...with my own generator:
to gen :lo :hi :step
  make "x []
  while [ :lo < (:hi+1) ] [ make "x lput :lo :x make "lo :lo + :step ]
  output :x
end

http://www.calormen.com/jslogo/language.html
...jslogo syntax


Simpler:

https://github.com/dominoanty/Logo-Interpreter
...works but python2 and pygame needed
... and it takes 87% CPU when idle, probably due to pygame
... but does not support procedures

here:
cd Logo-Interpreter
python main.py
repeat 10 [ lt 60 fd 20 rt 120 fd 20 lt 60 ]

Could be also used to record turtle moves from mouse drawing.

http://www.calormen.com/jslogo/
... nice javascript interpreter, for testing, with examples
source:
https://github.com/inexorabletash/jslogo

### Great Logo One-Liners

http://www.mathcats.com/gallery/15wordcontest.html
http://www.mathcats.com/gallery/15wordcontest.html#squarespiralvariations

And other nice drawings:
http://www.pool-rnd.com/en/Kafelka.aspx?artID=5

## Web servers:

https://www.youtube.com/watch?v=x5VauXr7W4A
...demos the standard EV3D4:
https://github.com/ev3dev/ev3dev-lang-python/tree/jessie/demo/EV3D4

## Pylogo on robot:

pylogo needs tkinter which in turn needs X display.
xvfb-run from xvfb resolved the limitation:

robot@ev3dev:~/lego/pylogo$ xvfb-run ./start.py 
...no more complaints, so it hopefully works. (Can't see anything in xvfb...)

...well, not really sure, after killing the silent process, I got:
IO:  fatal IO error 11 (Resource temporarily unavailable) on X server ":99"
      after 1632 requests (668 known processed) with 0 events remaining.

## Battery Voltage in bash

cat /sys/class/power_supply/lego-ev3-battery/voltage_now
# divide by 10^6

## Overloaded on Stretch
https://github.com/ev3dev/ev3dev/issues/1022

top - 17:01:17 up  1:31,  3 users,  load average: 3.06, 2.83, 2.59
Tasks:  73 total,   2 running,  45 sleeping,   0 stopped,   0 zombie
%Cpu(s): 74.1 us, 23.7 sy,  0.0 ni,  0.0 id,  0.3 wa,  0.0 hi,  2.0 si,  0.0 st
KiB Mem :    57180 total,     1532 free,    24700 used,    30948 buff/cache
KiB Swap:    98300 total,    84988 free,    13312 used.    28968 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S %CPU %MEM     TIME+ COMMAND      
 2606 robot     20   0   12276   8308   4804 R 49.8 14.5   0:06.25 run_ev3.py   
 2348 root      20   0       0      0      0 I 14.5  0.0   1:40.79 kworker/0:0  
   71 root     -51   0       0      0      0 S 13.8  0.0  12:25.19 irq/245-ti-+ 


## Trying to figure out the distance needed for 360 degree tank rotation

random-bits/find_angle_speed.py

The following generally reports how much needs to be travelled with the left
and right motors to get 180 degree of rotation.

The average is around 402, as detailed below.
To travel 1 degree, we need to travel 402/180 steps


carpet:
At 100 , travel for 1/2circ  403 L and 400 R; absL: 805 , absR: 800
At 100 , travel for 1/2circ  401 L and 399 R; absL: 1206 , absR: 1199
At 100 , travel for 1/2circ  401 L and 400 R; absL: 1607 , absR: 1599
At 100 , travel for 1/2circ  403 L and 399 R; absL: 2010 , absR: 1998
At 100 , travel for 1/2circ  401 L and 398 R; absL: 2411 , absR: 2396
At 100 , travel for 1/2circ  402 L and 399 R; absL: 804 , absR: 796
At 100 , travel for 1/2circ  404 L and 405 R; absL: 1208 , absR: 1201
At 100 , travel for 1/2circ  403 L and 398 R; absL: 1611 , absR: 1599
At 100 , travel for 1/2circ  403 L and 404 R; absL: 2014 , absR: 2003
At 100 , travel for 1/2circ  402 L and 398 R; absL: 2416 , absR: 2401
At 150 , travel for 1/2circ  405 L and 404 R; absL: 2821 , absR: 2805
At 150 , travel for 1/2circ  401 L and 398 R; absL: 3222 , absR: 3203
At 150 , travel for 1/2circ  401 L and 398 R; absL: 3623 , absR: 3601
At 150 , travel for 1/2circ  402 L and 402 R; absL: 4025 , absR: 4003
At 150 , travel for 1/2circ  403 L and 402 R; absL: 4428 , absR: 4405
At -180 , travel for 1/2circ  401 L and 404 R; absL: 4027 , absR: 4001
At -180 , travel for 1/2circ  408 L and 408 R; absL: 3619 , absR: 3593
At -180 , travel for 1/2circ  403 L and 404 R; absL: 3216 , absR: 3189
At -180 , travel for 1/2circ  403 L and 405 R; absL: 2813 , absR: 2784
At -180 , travel for 1/2circ  402 L and 405 R; absL: 2411 , absR: 2379
At 150 , travel for 1/2circ  402 L and 398 R; absL: 2813 , absR: 2777
At 150 , travel for 1/2circ  401 L and 399 R; absL: 3214 , absR: 3176
At 150 , travel for 1/2circ  401 L and 399 R; absL: 3615 , absR: 3575
At 150 , travel for 1/2circ  401 L and 401 R; absL: 4016 , absR: 3976
At 150 , travel for 1/2circ  404 L and 403 R; absL: 4420 , absR: 4379
At -90 , travel for 1/2circ  402 L and 399 R; absL: 4018 , absR: 3980
At -90 , travel for 1/2circ  403 L and 401 R; absL: 3615 , absR: 3579
At -90 , travel for 1/2circ  402 L and 400 R; absL: 3213 , absR: 3179
At -90 , travel for 1/2circ  401 L and 399 R; absL: 2812 , absR: 2780
At -90 , travel for 1/2circ  401 L and 401 R; absL: 2411 , absR: 2379
At -180 , travel for 1/2circ  403 L and 404 R; absL: 2008 , absR: 1975
At -180 , travel for 1/2circ  405 L and 409 R; absL: 1603 , absR: 1566
At -180 , travel for 1/2circ  403 L and 405 R; absL: 1200 , absR: 1161
At -180 , travel for 1/2circ  403 L and 404 R; absL: 797 , absR: 757
At -180 , travel for 1/2circ  401 L and 405 R; absL: 396 , absR: 352
At 90 , travel for 1/2circ  403 L and 401 R; absL: 799 , absR: 753
At 90 , travel for 1/2circ  401 L and 401 R; absL: 1200 , absR: 1154
At 90 , travel for 1/2circ  401 L and 398 R; absL: 1601 , absR: 1552
At 90 , travel for 1/2circ  403 L and 404 R; absL: 2004 , absR: 1956
At 90 , travel for 1/2circ  403 L and 404 R; absL: 2407 , absR: 2360
At -120 , travel for 1/2circ  402 L and 399 R; absL: 2005 , absR: 1961
At -120 , travel for 1/2circ  403 L and 399 R; absL: 1602 , absR: 1562
At -120 , travel for 1/2circ  402 L and 403 R; absL: 1200 , absR: 1159
At -120 , travel for 1/2circ  402 L and 402 R; absL: 798 , absR: 757
At -120 , travel for 1/2circ  403 L and 400 R; absL: 395 , absR: 357
At -180 , travel for 1/2circ  405 L and 408 R; absL: 10 , absR: 51
At -180 , travel for 1/2circ  405 L and 409 R; absL: 415 , absR: 460
At -180 , travel for 1/2circ  401 L and 405 R; absL: 816 , absR: 865
At -180 , travel for 1/2circ  402 L and 405 R; absL: 1218 , absR: 1270
At -180 , travel for 1/2circ  404 L and 407 R; absL: 1622 , absR: 1677
At -180 , travel for 1/2circ  401 L and 404 R; absL: 2023 , absR: 2081
At -180 , travel for 1/2circ  404 L and 407 R; absL: 2427 , absR: 2488
At -180 , travel for 1/2circ  403 L and 407 R; absL: 2830 , absR: 2895
At -180 , travel for 1/2circ  403 L and 404 R; absL: 3233 , absR: 3299

Solid floor:

At 100 , travel for 1/2circ  402 L and 399 R; absL: 804 , absR: 797
At 100 , travel for 1/2circ  406 L and 406 R; absL: 1210 , absR: 1203
At 100 , travel for 1/2circ  401 L and 400 R; absL: 1611 , absR: 1603
At 100 , travel for 1/2circ  402 L and 398 R; absL: 2013 , absR: 2001
At 100 , travel for 1/2circ  402 L and 398 R; absL: 2415 , absR: 2399
At 90 , travel for 1/2circ  402 L and 398 R; absL: 2817 , absR: 2797
At 90 , travel for 1/2circ  403 L and 401 R; absL: 3220 , absR: 3198
At 90 , travel for 1/2circ  402 L and 401 R; absL: 3622 , absR: 3599
At 90 , travel for 1/2circ  402 L and 400 R; absL: 4024 , absR: 3999
At 90 , travel for 1/2circ  402 L and 401 R; absL: 4426 , absR: 4400
At -90 , travel for 1/2circ  401 L and 397 R; absL: 4025 , absR: 4003
At -90 , travel for 1/2circ  401 L and 400 R; absL: 3624 , absR: 3603
At -90 , travel for 1/2circ  402 L and 401 R; absL: 3222 , absR: 3202
At -90 , travel for 1/2circ  401 L and 400 R; absL: 2821 , absR: 2802
At -90 , travel for 1/2circ  402 L and 399 R; absL: 2419 , absR: 2403
At 150 , travel for 1/2circ  401 L and 398 R; absL: 2820 , absR: 2801
At 150 , travel for 1/2circ  403 L and 402 R; absL: 3223 , absR: 3203
At 150 , travel for 1/2circ  404 L and 404 R; absL: 3627 , absR: 3607
At 150 , travel for 1/2circ  401 L and 398 R; absL: 4028 , absR: 4005
At 150 , travel for 1/2circ  402 L and 398 R; absL: 4430 , absR: 4403
At 120 , travel for 1/2circ  403 L and 402 R; absL: 4833 , absR: 4805
At 120 , travel for 1/2circ  403 L and 399 R; absL: 5236 , absR: 5204
At 120 , travel for 1/2circ  403 L and 398 R; absL: 5639 , absR: 5602
At 120 , travel for 1/2circ  403 L and 400 R; absL: 6042 , absR: 6002
At 120 , travel for 1/2circ  402 L and 400 R; absL: 6444 , absR: 6402
At -180 , travel for 1/2circ  404 L and 405 R; absL: 6040 , absR: 5997
At -180 , travel for 1/2circ  403 L and 408 R; absL: 5637 , absR: 5589
At -180 , travel for 1/2circ  403 L and 403 R; absL: 5234 , absR: 5186
At -180 , travel for 1/2circ  402 L and 405 R; absL: 4832 , absR: 4781
At -180 , travel for 1/2circ  404 L and 407 R; absL: 4428 , absR: 4374
At -150 , travel for 1/2circ  404 L and 401 R; absL: 4024 , absR: 3973
At -150 , travel for 1/2circ  401 L and 400 R; absL: 3623 , absR: 3573
At -150 , travel for 1/2circ  402 L and 402 R; absL: 3221 , absR: 3171
At -150 , travel for 1/2circ  401 L and 400 R; absL: 2820 , absR: 2771
At -150 , travel for 1/2circ  402 L and 400 R; absL: 2418 , absR: 2371
At 180 , travel for 1/2circ  403 L and 404 R; absL: 2821 , absR: 2775
At 180 , travel for 1/2circ  401 L and 404 R; absL: 3222 , absR: 3179
At 180 , travel for 1/2circ  404 L and 402 R; absL: 3626 , absR: 3581
At 180 , travel for 1/2circ  402 L and 404 R; absL: 4028 , absR: 3985
At 180 , travel for 1/2circ  401 L and 405 R; absL: 4429 , absR: 4390
At -180 , travel for 1/2circ  403 L and 406 R; absL: 4026 , absR: 3984
At -180 , travel for 1/2circ  402 L and 405 R; absL: 3624 , absR: 3579
At -180 , travel for 1/2circ  404 L and 409 R; absL: 3220 , absR: 3170
At -180 , travel for 1/2circ  404 L and 407 R; absL: 2816 , absR: 2763
At -180 , travel for 1/2circ  404 L and 407 R; absL: 2412 , absR: 2356
At 90 , travel for 1/2circ  401 L and 397 R; absL: 2813 , absR: 2753
At 90 , travel for 1/2circ  405 L and 405 R; absL: 3218 , absR: 3158
At 90 , travel for 1/2circ  402 L and 400 R; absL: 3620 , absR: 3558
At 90 , travel for 1/2circ  402 L and 400 R; absL: 4022 , absR: 3958
At 90 , travel for 1/2circ  403 L and 401 R; absL: 4425 , absR: 4359
At -90 , travel for 1/2circ  411 L and 408 R; absL: 4014 , absR: 3951
At -90 , travel for 1/2circ  402 L and 401 R; absL: 3612 , absR: 3550
At -90 , travel for 1/2circ  401 L and 399 R; absL: 3211 , absR: 3151
At -90 , travel for 1/2circ  403 L and 403 R; absL: 2808 , absR: 2748
At -90 , travel for 1/2circ  401 L and 399 R; absL: 2407 , absR: 2349
At -90 , travel for 1/2circ  401 L and 399 R; absL: 2006 , absR: 1950
At -90 , travel for 1/2circ  401 L and 399 R; absL: 1605 , absR: 1551
At -90 , travel for 1/2circ  401 L and 400 R; absL: 1204 , absR: 1151



...strangely, when I set these values, the robot rotated *much* less with run_to_rel_pos, although the tacho counters seemed to report the correct 200 of delta for 90 degrees turn:

Left -90 called, going for -201 from 20768 L, -28889 R.
  Left -90 done, going for -201 to 20971 L, -29090 R.

Left -90 called, going for -201 from 20570 L, -29893 R.
  Left -90 done, going for -201 to 20773 L, -30093 R.

Left -90 called, going for -201 from 20470 L, -30394 R.
  Left -90 done, going for -201 to 20674 L, -30594 R.


180 seems like 14 degrees

full circle seems like 2098


## 2018-05-25 Navrh zastavitelneho weboveho interpretru loga

- webserver:
  - nabizi kod k editaci [done]
  - pri stisku preview to vrati nakreslene SVG (nebo error log) [done]
  - po uspesnem preview je mozne spustit kod [done]
  - propagace stavu robota do webu, aby se vedelo, jestli je mozny run nebo stop
  - tlacitko na robotovi udela stop
  - kdyz vyjede mimo bile, udela stop
  - infra se da jezdit nezavisle, ale smysl to ma jen, kdyz to nic nemaluje [done]

Now the basic things work:

```
cd loev3go
./run_webserver.py [--no-robot]
```

TODO:
- stav baterky
- prepinac dry-run, aby obrazek projel bez pokladani pera [done]
- stop_motors nejak otoci polaritu, zkousim tedy pridat reset
  .... fixed, ale je prohozeny levy a pravy motor
  ... pero je spravne leve je cerne a je to LEFT
- speed choice in logo code ("speed 200") [done]
- motor polarity (jezdi pozadu) [done]
- ladici robot, tj. jako ev3dev, ale jen ladici vypisy, aby se testovalo
  zastavovani ap. [done]
- web-based "pen release" and "pen fix" (staci jedna vec: stop_motors, clovek ji zmackne jednou, nastavi vypnuta pera, zmackne podruhe, aby zresetoval stav, musi se asi taky zmenit stav na PEN_UP
- IR-follow
- left and right pens are swapped [done]
- inaccuracies:
  - should wait after pendown, this is critical!
  - dangerous are also rotations there and immediately back
  - the 20 degrees themselves are probably OK
  - unclear that the squares seem sort of OK and the rotation by 20 degrees
    between each red or black square does not add up 9*20*2 = 360
    - should check level of shaking due to pen movements, once we have mouse in
    - should check non-linearity of robot rotation, perhaps 90 degrees work
      well but 20 do not.

Code to check the non-linearity of rotation:
... first a circle in one color, then a circle of alternating colors
penwidth 2
pencolor "right
pd
repeat 18 [ fd 10 lt 20 ]
rt 180
repeat 9 [
  pencolor "right
  fd 10 lt 20
  pencolor "left
  fd 10 lt 20
]


## Setting up robot as wifi accesspoint

Maybe this tip contains everything that is needed:

https://superuser.com/questions/748455/how-to-setup-access-point-wifi-hotspot-on-debian
https://superuser.com/questions/437137/how-to-turn-my-linux-netbook-into-wifi-ap

## Tips for power supply

http://www.mindstormsrobots.com/lego-mindstorms/mindstorms-robots/mindstorms-ev3-robots/
...napajeni ze site

https://zbozi.mobilmania.cz/ostatni-baterie-a-prislusenstvi/napajeci-adapter-230v-3-12v-600ma/
...194Kc
https://www.softcom.cz/eshop/napajeci-adapter-230v-3-12v-stejnosmerny-600ma_d107596.html

## Bootstrap web layout
https://getbootstrap.com/docs/3.3/css/

### Switch off color sensor

# switch it off
echo other-uart >  /sys/class/lego-port/port1/mode
# and back on
echo auto >  /sys/class/lego-port/port1/mode

### Nice figures:

# jewels:
penwidth 2
to square
  repeat 4 [ fd 10 rt 90 ]
end
repeat 9 [
pencolor "left
pd
square pu fd 10 lt 20
pencolor "right
pd
square pu fd 10 lt 20
]


## Colors of carpet etc

v seru v zelenem pokoji:

tmavy kusovy koberec:
Sum: 68, Red: 28, Green: 34, Blue: 6

bily papir
Sum: 616, Red: 233, Green: 259, Blue: 124

cara na bilem papire:
Sum: 588, Red: 221, Green: 248, Blue: 119

svetly zeleny koberec:
Sum: 182, Red: 76, Green: 82, Blue: 24

koberec v obyvaku:
  svetly bod:
  Sum: 78, Red: 42, Green: 29, Blue: 7
  tmavsi cast:
  Sum: 35, Red: 18, Green: 13, Blue: 4
  Sum: 24, Red: 11, Green: 10, Blue: 3
  Sum: 9, Red: 3, Green: 4, Blue: 2
  nejtmavsi cast:
  Sum: 12, Red: 4, Green: 5, Blue: 3
  svetla cast koberce:
  Sum: 111, Red: 56, Green: 44, Blue: 11

bily papir ve svetle v obyvaku:
  Sum: 582, Red: 222, Green: 247, Blue: 113

  a hneda caranice na nem:
  Sum: 254, Red: 117, Green: 97, Blue: 40


### Mouse in USB hub:

Mouse devices: /dev/input/by-id/usb-13ba_Barcode_Reader-if01-event-mouse

15:30 [644] random-bits$./report-mouse-moves.py 
Device:  Barcode Reader 
D:  device /dev/input/event3, name "Barcode Reader ", phys "usb-ohci-da8xx-1.4/input1"
Device:  Barcode Reader 
D:  device /dev/input/event2, name "Barcode Reader ", phys "usb-ohci-da8xx-1.4/input0"
Device:  EV3 Brick Buttons
D:  device /dev/input/event1, name "EV3 Brick Buttons", phys "gpio-keys/input0"
Device:  LEGO MINDSTORMS EV3 Speaker
D:  device /dev/input/event0, name "LEGO MINDSTORMS EV3 Speaker", phys ""



## Which old sets I used to have:

6932 Futuron
6750  Sonic Robot

6780 ... possibly, but quite unsure
https://brickset.com/sets/6783-1 ...rather not

## Slowness:

https://github.com/ev3dev/ev3dev/issues/1199
...IR sensor contact?
...IR sensor in wrong port?

## Strange random segfaults


00:16 obonb ~$ssh robot@robot
Linux ev3dev 4.14.38-ev3dev-2.0.1-ev3 #1 PREEMPT Sat May 5 13:15:45 CDT 2018 armv5tejl
             _____     _
   _____   _|___ /  __| | _____   __
  / _ \ \ / / |_ \ / _` |/ _ \ \ / /
 |  __/\ V / ___) | (_| |  __/\ V /
  \___| \_/ |____/ \__,_|\___| \_/

Debian stretch on LEGO MINDSTORMS EV3!
Last login: Mon Feb  3 23:09:29 2020 from 192.168.10.110
05:30 [734] ~$sudo apt-get update
[sudo] password for robot: 
Hit:1 http://security.debian.org stretch/updates InRelease                     
Ign:2 http://httpredir.debian.org/debian stretch InRelease                     
Hit:3 http://httpredir.debian.org/debian stretch Release                  
Hit:4 http://archive.ev3dev.org/debian stretch InRelease                 
Reading package lists... Done                      
awk: cmd. line:1: fatal error: internal error: segfault
Aborted
05:35 [728] ~$sudo apt-get install --reinstall awk
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Package awk is a virtual package provided by:
  original-awk 2012-12-20-6
  mawk 1.3.3-17+b3
  gawk 1:4.1.4+dfsg-1
You should explicitly select one to install.

E: Package 'awk' has no installation candidate
05:36 [728] ~$sudo apt-get install --reinstall gawk
Reading package lists... Done
Building dependency tree       
Reading state information... Done
0 upgraded, 0 newly installed, 1 reinstalled, 0 to remove and 184 not upgraded.
Need to get 0 B/533 kB of archives.
After this operation, 0 B of additional disk space will be used.
(Reading database ... 49440 files and directories currently installed.)
Preparing to unpack .../gawk_1%3a4.1.4+dfsg-1_armel.deb ...
Unpacking gawk (1:4.1.4+dfsg-1) over (1:4.1.4+dfsg-1) ...
Setting up gawk (1:4.1.4+dfsg-1) ...
05:39 [728] ~$sudo apt-get install strace
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  strace
0 upgraded, 1 newly installed, 0 to remove and 184 not upgraded.
Need to get 478 kB of archives.
After this operation, 854 kB of additional disk space will be used.
Get:1 http://httpredir.debian.org/debian stretch/main armel strace armel 4.15-2 [478 kB]
Fetched 478 kB in 2s (189 kB/s) 
Selecting previously unselected package strace.
(Reading database ... 49440 files and directories currently installed.)
Preparing to unpack .../strace_4.15-2_armel.deb ...
Unpacking strace (4.15-2) ...
Setting up strace (4.15-2) ...
awk: cmd. line:1: (FILENAME=- FNR=1) fatal: field.c:111: erealloc called with zero bytes
05:44 [724] ~$sudo apt-get install memtester
eading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  memtester
0 upgraded, 1 newly installed, 0 to remove and 184 not upgraded.
Need to get 18.7 kB of archives.
After this operation, 45.1 kB of additional disk space will be used.
Get:1 http://httpredir.debian.org/debian stretch/main armel memtester armel 4.3.0-4+b1 [18.7 kB]
Fetched 18.7 kB in 1s (12.5 kB/s)      
Selecting previously unselected package memtester.
(Reading database ... 49449 files and directories currently installed.)
Preparing to unpack .../memtester_4.3.0-4+b1_armel.deb ...
Unpacking memtester (4.3.0-4+b1) ...
Setting up memtester (4.3.0-4+b1) ...
05:49 [725] ~$memtester 1024 5
-bash: memtester: command not found
05:50 [723] ~$sudo memtester 1024 5
memtester version 4.3.0 (32-bit)
Copyright (C) 2001-2012 Charles Cazabon.
Licensed under the GNU General Public License version 2 (only).

pagesize is 4096
pagesizemask is 0xfffff000
want 1024MB (1073741824 bytes)
got  121MB (127242240 bytes), trying mlock ...Killed
awk: cmd. line:1: fatal error: internal error: segfault
Aborted
ter version 4.3.0 (32-bit)
Copyright (C) 2001-2012 Charles Cazabon.
Licensed under the GNU General Public License version 2 (only).

pagesize is 4096
pagesizemask is 0xfffff000
want 30MB (31457280 bytes)
got  30MB (31457280 bytes), trying mlock ...locked.
Loop 1/2:
  Stuck Address       : ok         
  Random Value        : ok
  Compare XOR         : ok
  Compare SUB         : ok
  Compare MUL         : ok
  Compare DIV         : ok
  Compare OR          : ok
  Compare AND         : ok
  Sequential Increment: ok
  Solid Bits          : ok         
  Block Sequential    : setting 200^C
supoawk: cmd. line:1: (FILENAME=- FNR=1) warning: gensub: third argument 0 treated as 1
awk: cmd. line:1: (FILENAME=- FNR=1) warning: gensub: third argument 0 treated as 1


strace: bugs/strace-test-python-tk-segfaulting.stderr


top dies with segfault:

07:55 [822] ~$cat /proc/meminfo 
MemTotal:          57180 kB
MemFree:            6244 kB
MemAvailable:      36932 kB
Buffers:            4700 kB
Cached:            27764 kB
SwapCached:         1624 kB
Active:            15376 kB
Inactive:          20744 kB
Active(anon):       2308 kB
Inactive(anon):     1360 kB
Active(file):      13068 kB
Inactive(file):    19384 kB
Unevictable:           0 kB
Mlocked:               0 kB
SwapTotal:         98300 kB
SwapFree:          89340 kB
Dirty:                 4 kB
Writeback:             0 kB
AnonPages:          3076 kB
Mapped:            12332 kB
Shmem:                12 kB
Slab:               6172 kB
SReclaimable:       1692 kB
SUnreclaim:         4480 kB
KernelStack:         552 kB
PageTables:          680 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:      126888 kB
Committed_AS:     103200 kB
VmallocTotal:     966656 kB
VmallocUsed:           0 kB
VmallocChunk:          0 kB


07:56 [822] ~$top
Segmentation fault


Failing to apt-get:
07:42 [835] ~$sudo apt-get install --reinstall libtk8.6  tk8.6-blt2.5
[sudo] password for robot: 
Reading package lists... Done
Building dependency tree        
Reading state information... Done
0 upgraded, 0 newly installed, 2 reinstalled, 0 to remove and 184 not upgraded.
Need to get 0 B/1,156 kB of archives.
After this operation, 0 B of additional disk space will be used.
(Reading database ... 49459 files and directories currently installed.)
Preparing to unpack .../libtk8.6_8.6.6-1+b1_armel.deb ...
Unpacking libtk8.6:armel (8.6.6-1+b1) over (8.6.6-1+b1) ...
Preparing to unpack .../tk8.6-blt2.5_2.5.3+dfsg-3_armel.deb ...
Unpacking tk8.6-blt2.5 (2.5.3+dfsg-3) over (2.5.3+dfsg-3) ...
Setting up libtk8.6:armel (8.6.6-1+b1) ...
Processing triggers for libc-bin (2.24-11+deb9u3) ...
Setting up tk8.6-blt2.5 (2.5.3+dfsg-3) ...
Processing triggers for libc-bin (2.24-11+deb9u3) ...
awk: cmd. line:1: fatal error: internal error: segfault
Aborted


Memory was not full, I do not see much change in: (when apt-get was already stopped)
07:44 [831] ~$cat /proc/meminfo 
MemTotal:          57180 kB
MemFree:            2008 kB
MemAvailable:      36616 kB
Buffers:            5740 kB
Cached:            30644 kB
SwapCached:         1780 kB
Active:            18940 kB
Inactive:          21460 kB
Active(anon):       1676 kB
Inactive(anon):     2364 kB
Active(file):      17264 kB
Inactive(file):    19096 kB
Unevictable:           0 kB
Mlocked:               0 kB
SwapTotal:         98300 kB
SwapFree:          89340 kB
Dirty:                 0 kB
Writeback:             0 kB
AnonPages:          3344 kB
Mapped:            13928 kB
Shmem:                24 kB
Slab:               6208 kB
SReclaimable:       1716 kB
SUnreclaim:         4492 kB
KernelStack:         552 kB
PageTables:          680 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:      126888 kB
Committed_AS:     103200 kB
VmallocTotal:     966656 kB
VmallocUsed:           0 kB
VmallocChunk:          0 kB

08:07 [814] ~$sudo apt-get install --reinstall  procps
Reading package lists... Done
Building dependency tree        
Reading state information... Done
The following packages will be upgraded:
  procps
1 upgraded, 0 newly installed, 0 to remove and 183 not upgraded.
Need to get 244 kB of archives.
After this operation, 0 B of additional disk space will be used.
Get:1 http://httpredir.debian.org/debian stretch/main armel procps armel 2:3.3.12-3+deb9u1 [244 kB]
Fetched 244 kB in 1s (152 kB/s)        
(Reading database ... 49459 files and directories currently installed.)
Preparing to unpack .../procps_2%3a3.3.12-3+deb9u1_armel.deb ...
Unpacking procps (2:3.3.12-3+deb9u1) over (2:3.3.12-3) ...
Setting up procps (2:3.3.12-3+deb9u1) ...
Processing triggers for systemd (232-25+deb9u2) ...
topawk: cmd. line:1: fatal error: internal error: segfault
Aborted
08:09 [813] ~$top

	signal 11 (SEGV) was caught by top, please
	see http://www.debian.org/Bugs/Reporting
Segmentation fault


...it is not bad blocks:
On main machine:
/dev/mmcblk0p2   3785840   2493144   1105064  70% /media/bojar/EV3DEV_ROOTFS
/dev/mmcblk0p1     49038      7322     41716  15% /media/bojar/EV3DEV_BOOT
09:35 obonb ~$sudo umount /media/bojar/EV3DEV_ROOTFS
[sudo] password for bojar: 
09:35 obonb ~$sudo umount /media/bojar/EV3DEV_BOOT
09:35 obonb ~$badblocks -n -v /dev/mmcblk0p1
badblocks: Permission denied while trying to determine device size
09:35 obonb ~$sudo badblocks -n -v /dev/mmcblk0p1
Checking for bad blocks in non-destructive read-write mode
From block 0 to 49151
Testing with random pattern: Pass completed, 0 bad blocks found. (0/0/0 errors)
09:36 obonb ~$sudo badblocks -n -v /dev/mmcblk0p2
Checking for bad blocks in non-destructive read-write mode
From block 0 to 3878911
Testing with random pattern: Pass completed, 0 bad blocks found. (0/0/0 errors)


...I filed an issue on this:
https://github.com/ev3dev/ev3dev/issues/1374


Other good links:
http://www.legoengineering.com/ev3-gone-wrong/
