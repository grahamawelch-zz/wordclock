#!/bin/bash

git -C /home/pi/workspace/wordclock pull
screen -d -m -S clock bash /home/pi/workspace/wordclock/start_clock.sh

