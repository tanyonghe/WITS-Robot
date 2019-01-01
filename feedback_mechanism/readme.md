
# Table of Contents

1.  [Feedback Mechanism Module](#org1fd8bec)
2.  [LED](#org7fa24c8)
    1.  [Setup](#orge0403b8)
        1.  [Physical Hardware](#orgbce038c)
        2.  [Software Installation](#org686d2ee)
3.  [Speaker](#org727cf3c)
    1.  [Setup](#org2c6862a)
        1.  [Physical Hardware](#orgfa335d2)
        2.  [Software Installation](#org65c3dc4)



<a id="org1fd8bec"></a>

# Feedback Mechanism Module

feedback mechanism consist of:

-   speaker
-   led


<a id="org7fa24c8"></a>

# LED


<a id="orge0403b8"></a>

## Setup


<a id="orgbce038c"></a>

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


<a id="org686d2ee"></a>

### Software Installation

-   build tools, may be able to skip
    
        sudo apt-get install build-essential python-dev python-pip unzip wget scons swig
-   installation
    
        wget https://github.com/jgarff/rpi_ws281x/archive/master.zip
        unzip master.zip
        cd rpi_ws281x-master
        sudo scons
        sudo pip install rpi_ws281x


<a id="org727cf3c"></a>

# Speaker


<a id="org2c6862a"></a>

## Setup


<a id="orgfa335d2"></a>

### Physical Hardware

-   connect RCA jack on raspberrypi to TDA7492P amplifier
-   wire the speaker to the amplifier and bam.


<a id="org65c3dc4"></a>

### Software Installation

-   I have read some tutorials that say need to disable audio for

WS2812 to work, not sure

-   also audio might be routing through HDMI could try this to solve
    
        raspi-config
    
    -   Select 7 Advanced Options, then Audio.
    -   Select "Force 3.5mm ('headphone') jack".
    -   Then "OK".

