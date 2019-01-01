
# Table of Contents

1.  [Feedback Mechanism Module](#org4807db9)
2.  [LED](#org61ee650)
    1.  [Setup](#org4b47418)
        1.  [Physical Hardware](#org3d4c88f)
        2.  [Software Installation](#org0bef282)
3.  [Speaker](#org51c3572)
    1.  [Setup](#orgea86e34)
        1.  [Physical Hardware](#org30a3b4d)
        2.  [Software Installation](#org79e3370)
        3.  [Bluetooth Pairing](#orgbfe5967)



<a id="org4807db9"></a>

# Feedback Mechanism Module

feedback mechanism consist of:

-   speaker
-   led


<a id="org61ee650"></a>

# LED


<a id="org4b47418"></a>

## Setup


<a id="org3d4c88f"></a>

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


<a id="org0bef282"></a>

### Software Installation

-   build tools, may be able to skip
    
        sudo apt-get install build-essential python-dev python-pip unzip wget scons swig
-   installation
    
        sudo pip install rpi_ws281x


<a id="org51c3572"></a>

# Speaker


<a id="orgea86e34"></a>

## Setup

We would go with the physical method first. However I have read
some blog post saying that its not possible to play music and
control the leds at the same time. This is due to the digital logic
output is based on the BCM-2835. If it cannot work then we have to
use bluetooth to pair it to the amplifier

-   might need to blacklist the BMC-2835


<a id="org30a3b4d"></a>

### Physical Hardware

-   connect RCA jack on raspberrypi to TDA7492P amplifier
-   wire the speaker to the amplifier and bam.


<a id="org79e3370"></a>

### Software Installation

-   I have read some tutorials that say need to disable audio for

WS2812 to work, not sure

-   also audio might be routing through HDMI could try this to solve
    
        raspi-config
    
    -   Select 7 Advanced Options, then Audio.
    -   Select "Force 3.5mm ('headphone') jack".
    -   Then "OK".


<a id="orgbfe5967"></a>

### Bluetooth Pairing

-   could probably use gui but if that fails we can use this <https://raspberrypi.stackexchange.com/questions/53408/automatically-connect-trusted-bluetooth-speaker/76288>

