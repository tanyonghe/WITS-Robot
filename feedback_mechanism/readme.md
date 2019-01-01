
# Table of Contents

1.  [Feedback Mechanism Module](#org1801c3e)
2.  [LED](#org4bd6630)
    1.  [Setup](#orgd922298)
        1.  [Physical Hardware](#org640b7cb)
        2.  [Software Installation](#org7647f83)
        3.  [how to use?](#orgffee343)
3.  [Speaker](#orgc7b7d7a)
    1.  [Setup](#org66c1a86)
        1.  [Physical Hardware](#org9c1d8f5)
        2.  [Software Installation](#orgc081707)
        3.  [Bluetooth Pairing](#org654a3a5)



<a id="org1801c3e"></a>

# Feedback Mechanism Module

feedback mechanism consist of:

-   speaker
-   led


<a id="org4bd6630"></a>

# LED


<a id="orgd922298"></a>

## Setup


<a id="org640b7cb"></a>

### Physical Hardware

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">LED</th>
<th scope="col" class="org-left">PI</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">+ve</td>
<td class="org-left">5v</td>
</tr>


<tr>
<td class="org-left">-ve</td>
<td class="org-left">ground</td>
</tr>


<tr>
<td class="org-left">data</td>
<td class="org-left">pin 18</td>
</tr>
</tbody>
</table>


<a id="org7647f83"></a>

### Software Installation

-   build tools, may be able to skip
    
        sudo apt-get install build-essential python-dev python-pip unzip wget scons swig
-   installation
    
        sudo pip install rpi_ws281x


<a id="orgffee343"></a>

### how to use?

-   this is helpful <https://github.com/jgarff/rpi_ws281x/blob/master/python/neopixel.py>
-   examples <https://github.com/jgarff/rpi_ws281x/tree/master/python/examples>
    -   strand test example useful <https://github.com/jgarff/rpi_ws281x/blob/master/python/examples/strandtest.py>

    from feedback_mechanism import led
    from neopixel import *
    
    # self defined colors
    # def Color(red, green, blue, white = 0):
    unicorn = Color(255,0,0,255)
    
    # you need to hold on to the strip object to tell it which led to change
    # take a look at neopixel.py for help 
    strip = led.init()
    # def setPixelColor(self, n, color):
    strip.setPixelColor(1, unicorn)
    # def setPixelColorRGB(self, n, red, green, blue, white = 0):
    strip.setPixelColorRGB(1, 255, 0, 0, 255)
    # def setBrightness(self, brightness):
    # def getBrightness(self):


<a id="orgc7b7d7a"></a>

# Speaker


<a id="org66c1a86"></a>

## Setup

We would go with the physical method first. However I have read
some blog post saying that its not possible to play music and
control the leds at the same time. This is due to the digital logic
output is based on the BCM-2835. If it cannot work then we have to
use bluetooth to pair it to the amplifier

-   might need to blacklist the BMC-2835


<a id="org9c1d8f5"></a>

### Physical Hardware

-   connect RCA jack on raspberrypi to TDA7492P amplifier
-   wire the speaker to the amplifier and bam.


<a id="orgc081707"></a>

### Software Installation

-   I have read some tutorials that say need to disable audio for

WS2812 to work, not sure

-   also audio might be routing through HDMI could try this to solve
    
        raspi-config
    
    -   Select 7 Advanced Options, then Audio.
    -   Select "Force 3.5mm ('headphone') jack".
    -   Then "OK".


<a id="org654a3a5"></a>

### Bluetooth Pairing

-   could probably use gui but if that fails we can use this <https://raspberrypi.stackexchange.com/questions/53408/automatically-connect-trusted-bluetooth-speaker/76288>

