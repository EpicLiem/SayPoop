#!/bin/bash

cd -- "$(dirname "$BASH_SOURCE")"
python install_cron.py
diskutil unmount /Volumes/Augie
killall Terminal