#!/bin/bash

git -C /home/pi/workspace/wordclock pull > /home/pi/workspace/wordclock/git_errors.txt 2>&1
screen -d -m -S clock bash /home/pi/workspace/wordclock/start_clock.sh

