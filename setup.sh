#!/usr/bin/env bash

sudo apt-get install build-essential
sudo apt-get install python3-dev python3-pip
sudo apt-get install libfreetype6-dev libjpeg-dev
git clone http://github.com/rm-hull/luma.led_matrix.git
sudo -H pip3 install luma.led_matrix

sudo pip3 simpleaudio

chmod 755 main.py
chmod 755 demo.py
