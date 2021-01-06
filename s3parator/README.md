# S3PARATOR

...an idea to create LEGO brick separator from EV3 home edition.

# Current Best Proposed Design

## Considered Hardware

- Motor 1: (now not planning)
  - one belt to load stage
  - one belt to return failed bricks
- Motor 2 & 3:
  - Follow https://www.ev3dev.org/projects/2015/05/06/EV3-Print3rbot/
    to build a moving frame around the current element.
  - Still problematic because of the missing touch sensor.
    - Would need to calibrate via vision
  - Another problem could be the small range of movements (and the need to push the moving box very far)
    - So perhaps a better solution would be to simply *sink* the platform, dropping the brick into one of 8 directions
      - Sinking has the further advantage of an easy 'tare' of the scale
- cell phone with 2 cams
- possibly a digital scale

## Software

- RPyC ev3dev to operate the motors
- IP Webcam to scan the scene in video and then take pictures
- TF to recognize bricks (and weight digits if we use the scale)

## Intended Operation

- Drop a brick into the moving frame and touch a button.
- EV3 will move the brick to scanning area
- Take 2 pictures
- Predict object, decide on target direction
- Use the movable frame to shovel the object there

# Installation

Python again proved its flawed installation layout. I am absolutely struggling with getting a single version of python running which would have things like opencv, rpyc etc.

I damaged my python3 by custom-installing python 3.5.3 instead of the default 3.5.2. I reinstalled the default python3 with apt-get, further damaging things which relied on python3...

The only sensible way seems now:

```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 10
  # switch plain python to 3.7
pyvenv venv
source venv/bin/activate
# OR RATHER
virtualenv -p python3.7 venv379
source venv379/bin/activate

pip install -r requirements.txt
  # opencv will take ages
```

# Testing without EV3

An easy option to test your python code without EV3 is to use FakEV3dev, an API identical to ev3 module but with dummy operations.

To do so, simply put FakEV3dev into PYTHONPATH before regular modules. From this directory use:

```
export PYTHONPATH=$(pwd)/../fake3dev/:$PYTHONPATH
```

# Random Ideas on Lego Brick Recognition

## Links

https://www.instructables.com/id/Lego-Brick-Sorter/
...hardware pre-sorting

Large-scale sorters:

# Random Ideas on Lego Brick Recognition

## Links

https://www.instructables.com/id/Lego-Brick-Sorter/
...hardware pre-sorting

Large-scale sorters:
https://spectrum.ieee.org/geek-life/hands-on/how-i-built-an-ai-to-sort-2-tons-of-lego-pieces

https://www.youtube.com/watch?v=04JkdHEX3Yk&feature=youtu.be
...Universal Lego Sorting Machine

https://www.youtube.com/watch?v=fM9qGZCc4DY
...Axle Sorter

https://www.philohome.com/sort3r/sort3r.htm
https://www.eurobricks.com/forum/index.php?/forums/topic/83069-sort3r-my-first-ev3-robot/
...Color Sorter

http://ev3lessons.com/RobotDesigns/instructions/droidbot2instructions.pdf
...droid bot compact, better than tank

https://robo4you.at/publications/Lego.pdf
...2018 master thesis by Christine Zeh and Simon Babovic

## Catalogue of Parts and Sets

https://www.bricklink.com/catalogTree.asp?itemType=S

https://www.bricklink.com/catalogItemInv.asp?S=60198-1

https://www.kaggle.com/joosthazelzet/lego-brick-images
...dataset of 50 brick types rendered in angles

## Scales

Cheap scales with precision 0.001g:

https://www.amazon.com/Milligram-NEWACALOX-Rechargeable-Precision-Calibration/dp/B0813LPL4N/ref=sr_1_5?keywords=milligram+scale+usb+0.001&qid=1578254937&sr=8-5
18 USD + 7 shipment

https://www.mikrovahy.cz/mikrovahy-do-50g/123-kl-158-presna-digitalni-mikrovahy-do-50g-0-001g.html
650 CZK

https://www.profivahy.cz/profi-vahy/eshop/28-1-Vahy-podle-provozu/0/5/2027-LESAK-P058-500g-0-01g-miska-50x55mm?gclid=EAIaIQobChMIx_DFupyI7gIVhNCyCh2cXQjIEAQYAiABEgK33PD_BwE
300 CZK  but not sure if the precision is indeed 0.01g

## Motor-constrained design:

A motor to rotate triple wheel:
- load pieces, unload pieces, push away pieces from distribution belt

B motor to move distribution belt to appropriate position

C motor left to feed pieces

Process phases:

1. A rotates and:
  1.1. pushes old piece from belt to the bin
  1.2. (later)
       - pushes recognized piece to belt
       - pushes new piece on belt
2. - B rotates and positions recognized piece above its bin
   - camera takes picture of the new piece and its weight

3. new piece is put into the loading area


Limits:

pieces up to 8x2x2, larger won't be movable around
- sadly, no duplo

...should be 16x16


# IP Webcam

IP Webcam is a very nifty app.

http://192.168.10.243:8080/settings/ffc?set=off
...use on or off to swap the camera

http://192.168.10.243:8080/photoaf.jpg
...download to take an auto-focussed picture

http://192.168.10.243:8080/disabletorch
... switch led off

This can be easily utilized in openCV as in here:
https://medium.com/@jeppbautista/connect-android-camera-to-python-using-opencv-90fd19d838

# Relevant Tools

https://github.com/meganrapach/lego-image-recognition
...demo with 6 brick types

# Python Programming on Android

https://github.com/eliasdorneles/tictactoe-voc
...sample tic-tac-toe app


# RPyC

https://ev3dev-lang.readthedocs.io/projects/python-ev3dev/en/stable/rpyc.html
...run everything on laptop, remote-control the robot
