
# Table of Contents

1.  [Feedback Mechanism Module](#org69014da)
2.  [LED](#org077f3f8)
    1.  [Setup](#org563dae6)
        1.  [Physical Hardware](#org6f54b7f)
        2.  [Software Installation](#orgd68d534)
        3.  [how to use?](#orge0e8af4)
3.  [Speaker](#org18e141c)
    1.  [Setup](#org0ee6211)
        1.  [Physical Hardware](#org0139f31)
        2.  [Software Installation](#org2be10aa)
        3.  [Bluetooth Pairing](#org2a9858a)



<a id="org69014da"></a>

# Feedback Mechanism Module

feedback mechanism consist of:

-   speaker
-   led


<a id="org077f3f8"></a>

# LED


<a id="org563dae6"></a>

## Setup


<a id="org6f54b7f"></a>

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


<a id="orgd68d534"></a>

### Software Installation

-   build tools, may be able to skip
    
        sudo apt-get install build-essential python-dev python-pip unzip wget scons swig
-   installation
    
        sudo pip install rpi_ws281x


<a id="orge0e8af4"></a>

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


<a id="org18e141c"></a>

# Speaker


<a id="org0ee6211"></a>

## Setup

We would go with the physical method first. However I have read
some blog post saying that its not possible to play music and
control the leds at the same time. This is due to the digital logic
output is based on the BCM-2835. If it cannot work then we have to
use bluetooth to pair it to the amplifier

-   might need to blacklist the BMC-2835


<a id="org0139f31"></a>

### Physical Hardware

-   connect RCA jack on raspberrypi to TDA7492P amplifier
-   wire the speaker to the amplifier and bam.


<a id="org2be10aa"></a>

### Software Installation

-   I have read some tutorials that say need to disable audio for

WS2812 to work, not sure

-   also audio might be routing through HDMI could try this to solve
    
        raspi-config
    
    -   Select 7 Advanced Options, then Audio.
    -   Select "Force 3.5mm ('headphone') jack".
    -   Then "OK".


<a id="org2a9858a"></a>

### Bluetooth Pairing

-   could probably use gui but if that fails we can use this <https://raspberrypi.stackexchange.com/questions/53408/automatically-connect-trusted-bluetooth-speaker/76288>

