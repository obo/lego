# From https://github.com/magmax/python-readchar
# the source of pip module 'readkey'
# Using directly because pip on ev3dev is crazily slow

import sys
import tty
import termios


def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


# common
LF = '\x0d'
CR = '\x0a'
ENTER = '\x0d'
BACKSPACE = '\x7f'
SUPR = ''
SPACE = '\x20'
ESC = '\x1b'

# CTRL
CTRL_A = '\x01'
CTRL_B = '\x02'
CTRL_C = '\x03'
CTRL_D = '\x04'
CTRL_E = '\x05'
CTRL_F = '\x06'
CTRL_Z = '\x1a'

# ALT
ALT_A = '\x1b\x61'

# CTRL + ALT
CTRL_ALT_A = '\x1b\x01'

# cursors
UP = '\x1b\x5b\x41'
DOWN = '\x1b\x5b\x42'
LEFT = '\x1b\x5b\x44'
RIGHT = '\x1b\x5b\x43'

CTRL_ALT_SUPR = '\x1b\x5b\x33\x5e'

# other
F1 = '\x1b\x4f\x50'
F2 = '\x1b\x4f\x51'
F3 = '\x1b\x4f\x52'
F4 = '\x1b\x4f\x53'
F5 = '\x1b\x4f\x31\x35\x7e'
F6 = '\x1b\x4f\x31\x37\x7e'
F7 = '\x1b\x4f\x31\x38\x7e'
F8 = '\x1b\x4f\x31\x39\x7e'
F9 = '\x1b\x4f\x32\x30\x7e'
F10 = '\x1b\x4f\x32\x31\x7e'
F11 = '\x1b\x4f\x32\x33\x7e'
F12 = '\x1b\x4f\x32\x34\x7e'

PAGE_UP = '\x1b\x5b\x35\x7e'
PAGE_DOWN = '\x1b\x5b\x36\x7e'
HOME = '\x1b\x5b\x48'
END = '\x1b\x5b\x46'

INSERT = '\x1b\x5b\x32\x7e'
SUPR = '\x1b\x5b\x33\x7e'


ESCAPE_SEQUENCES = (
    ESC,
    ESC + '\x5b',
    ESC + '\x5b' + '\x31',
    ESC + '\x5b' + '\x32',
    ESC + '\x5b' + '\x33',
    ESC + '\x5b' + '\x35',
    ESC + '\x5b' + '\x36',
    ESC + '\x5b' + '\x31' + '\x35',
    ESC + '\x5b' + '\x31' + '\x36',
    ESC + '\x5b' + '\x31' + '\x37',
    ESC + '\x5b' + '\x31' + '\x38',
    ESC + '\x5b' + '\x31' + '\x39',
    ESC + '\x5b' + '\x32' + '\x30',
    ESC + '\x5b' + '\x32' + '\x31',
    ESC + '\x5b' + '\x32' + '\x32',
    ESC + '\x5b' + '\x32' + '\x33',
    ESC + '\x5b' + '\x32' + '\x34',
    ESC + '\x4f',
    ESC + ESC,
    ESC + ESC + '\x5b',
    ESC + ESC + '\x5b' + '\x32',
    ESC + ESC + '\x5b' + '\x33',
)


def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1 + c2
    c3 = getchar()
    if ord(c3) != 0x33:
        return c1 + c2 + c3
    c4 = getchar()
    return c1 + c2 + c3 + c4

# python print to stderr (most portable and flexible)
import sys
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def test():
    eprint("Hit various keys. Type 'q' to exit.")
    buffer = ""
    while True:
      key = readkey()
      if key == ESC:
        return
      if key == UP:
        eprint("UP")
      elif key == DOWN:
        eprint("DOWN")
      elif key == 'q':
        exit(0)
      elif key == 'a':
        eprint("a")
      elif key == 'Y':
        eprint("shift-Y")
      else:
        # Handle other text characters
        buffer += key
        print(buffer)
