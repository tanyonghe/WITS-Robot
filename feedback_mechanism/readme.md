
# Table of Contents

1.  [Feedback Mechanism Module](#orgce8edf3)
2.  [LED](#orgc659131)
    1.  [Setup](#orga03c0e3)
        1.  [Physical Hardware](#orgd934b9f)
        2.  [Software Installation](#org57e2ad6)
3.  [Speaker](#org646a30d)
    1.  [Setup](#org4634244)
        1.  [Physical Hardware](#orga183c1c)
        2.  [Software Installation](#org36764e5)



<a id="orgce8edf3"></a>

# Feedback Mechanism Module

feedback mechanism consist of:

-   speaker
-   led


<a id="orgc659131"></a>

# LED


<a id="orga03c0e3"></a>

## Setup


<a id="orgd934b9f"></a>

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


<a id="org57e2ad6"></a>

### Software Installation

-   build tools, may be able to skip
    
        sudo apt-get install build-essential python-dev python-pip unzip wget scons swig
-   installation
    
        sudo pip install rpi_ws281x


<a id="org646a30d"></a>

# Speaker


<a id="org4634244"></a>

## Setup

We would go with the physical method first. However I have read
some blog post saying that its not possible to play music and
control the leds at the same time. This is due to the digital logic
output is based on the BCM-2835. If it cannot work then we have to
use bluetooth to pair it to the amplifier

-   might need to blacklist the BMC-2835


<a id="orga183c1c"></a>

### Physical Hardware

-   connect RCA jack on raspberrypi to TDA7492P amplifier
-   wire the speaker to the amplifier and bam.


<a id="org36764e5"></a>

### Software Installation

-   I have read some tutorials that say need to disable audio for

WS2812 to work, not sure

-   also audio might be routing through HDMI could try this to solve
    
        raspi-config
    
    -   Select 7 Advanced Options, then Audio.
    -   Select "Force 3.5mm ('headphone') jack".
    -   Then "OK".

