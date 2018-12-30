#!/usr/bin/env bash

sudo apt-get install build-essential
sudo apt-get install python3-dev python3-pip
sudo apt-get install libfreetype6-dev libjpeg-dev

sudo apt-get install libcblas-dev
sudo apt-get install libhdf5-dev
sudo apt-get install libhdf5-serial-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev 
sudo apt-get install libqtgui4 
sudo apt-get install libqt4-test

sudo pip3 install opencv-python
sudo pip3 simpleaudio

git clone http://github.com/rm-hull/luma.led_matrix.git
sudo -H pip3 install luma.led_matrix

chmod 755 main.py
chmod 755 demo.py