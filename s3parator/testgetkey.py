#!/usr/bin/env python3
# https://pypi.org/project/getkey/


# python print to stderr (most portable and flexible)
import sys
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

buffer = ""

from getkey import getkey, keys
while True:
  key = getkey()
  if key == keys.ESC:
    exit(0)
  if key == keys.UP:
    eprint("UP")
  elif key == keys.DOWN:
    eprint("DOWN")
  elif key == 'a':
    eprint("a")
  elif key == 'Y':
    eprint("shift-Y")
  else:
    # Handle other text characters
    buffer += key
    print(buffer)

