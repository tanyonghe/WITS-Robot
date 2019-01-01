
# Table of Contents

1.  [Feedback Mechanism Module](#orgc8caa95)
2.  [LED](#org0ad4397)
    1.  [Setup](#org3e3eb25)
        1.  [Physical Hardware](#orgaaff337)
        2.  [Software Installation](#orgcb62da2)
3.  [Speaker](#orga4d5032)
    1.  [Setup](#orgd90386e)
        1.  [Physical Hardware](#org517ef9b)
        2.  [Software Installation](#orgaff3c67)



<a id="orgc8caa95"></a>

# Feedback Mechanism Module

feedback mechanism consist of:

-   speaker
-   led


<a id="org0ad4397"></a>

# LED


<a id="org3e3eb25"></a>

## Setup


<a id="orgaaff337"></a>

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


<a id="orgcb62da2"></a>

### Software Installation

-   build tools, may be able to skip
    
        sudo apt-get install build-essential python-dev python-pip unzip wget scons swig
-   installation
    
        wget https://github.com/jgarff/rpi_ws281x/archive/master.zip
        unzip master.zip
        cd rpi_ws281x-master
        sudo scons
        sudo pip install rpi_ws281x


<a id="orga4d5032"></a>

# Speaker


<a id="orgd90386e"></a>

## Setup

We would go with the physical method first. However I have read
some blog post saying that its not possible to play music and
control the leds at the same time. This is due to the digital logic
output is based on the BCM-2835. If it cannot work then we have to
use bluetooth to pair it to the amplifier

-   might need to blacklist the BMC-2835


<a id="org517ef9b"></a>

### Physical Hardware

-   connect RCA jack on raspberrypi to TDA7492P amplifier
-   wire the speaker to the amplifier and bam.


<a id="orgaff3c67"></a>

### Software Installation

-   I have read some tutorials that say need to disable audio for

WS2812 to work, not sure

-   also audio might be routing through HDMI could try this to solve
    
        raspi-config
    
    -   Select 7 Advanced Options, then Audio.
    -   Select "Force 3.5mm ('headphone') jack".
    -   Then "OK".

