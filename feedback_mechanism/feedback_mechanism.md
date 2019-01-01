
# Table of Contents

1.  [Feedback Mechanism Module](#orga336926)
2.  [LED](#org7866952)
    1.  [Setup](#orgb0902b7)
        1.  [Physical Hardware](#org513a6c7)
        2.  [Software Installation](#orgd839ae5)
3.  [Speaker](#orge3b1f50)
    1.  [setup](#orgc228541)
        1.  [Physical Hardware](#orgc1feeca)
        2.  [Software Installation](#org524ceb1)



<a id="orga336926"></a>

# Feedback Mechanism Module

feedback mechanism consist of:

-   speaker
-   led


<a id="org7866952"></a>

# LED


<a id="orgb0902b7"></a>

## Setup


<a id="org513a6c7"></a>

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


<a id="orgd839ae5"></a>

### Software Installation

-   build tools, may be able to skip
    
        sudo apt-get install build-essential python-dev python-pip unzip wget scons swig
-   installation
    
        wget https://github.com/jgarff/rpi_ws281x/archive/master.zip
        unzip master.zip
        cd rpi_ws281x-master
        sudo scons
        sudo pip install rpi_ws281x


<a id="orge3b1f50"></a>

# Speaker


<a id="orgc228541"></a>

## setup


<a id="orgc1feeca"></a>

### Physical Hardware

-   connect RCA jack on raspberrypi to TDA7492P amplifier
-   wire the speaker to the amplifier and bam.


<a id="org524ceb1"></a>

### Software Installation

-   I have read some tutorials that say need to disable audio for

WS2812 to work, not sure

-   also audio might be routing through HDMI could try this to solve
    
        raspi-config
    
    -   Select 7 Advanced Options, then Audio.
    -   Select "Force 3.5mm ('headphone') jack".
    -   Then "OK".

