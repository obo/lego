#!/bin/bash
# launcher which first quickly check motors

echo "Motors:"
cat /sys/class/tacho-motor/*/address | sed 's/^/  /'

mots=$(cat /sys/class/tacho-motor/*/address | sort)
echo "Got: '$mots'"
if [ "$(echo $mots)" == "ev3-ports:outA ev3-ports:outD" ]; then
  ./manual-mover.py
else
  echo "Some motors missing"
fi
