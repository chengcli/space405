Projects
========

This is a collection of project ideas you can work on to practice your skills.
There are computer language and difficulty labels to help you find a project.
If you have your own idea for a project, feel free to contact me!

.. |fillstar| unicode:: U+2605
.. |openstar| unicode:: U+2606

.. |uncheckedbox| unicode:: U+2610
.. |checkedbox| unicode:: U+2611

1. JunoCAM observation of Io
----------------------------

:Contributor: **Trish Murray**

:Programming Language:
  ``Python`` [``Swift``]

:Difficulty:
  |fillstar| |fillstar| |fillstar| |fillstar| |openstar|


Background
~~~~~~~~~~

The trajectory of the Juno spacecraft was modified to visit the Galilean Moons. Its
instruments were designed to study the atmosphere of Jupiter, but as there are no other spacecraft nearby,
it’s the best one around!

On December 30, 2023, Juno was close to Io, Jupiter’s volcanic moon. The images that Junocam
collected were quickly processed to make projected maps in color and those were posted on the mission’s
public website. Here is one of those pictures:

.. image:: ../images/io_from_juno.jpg
   :width: 400px
   :align: center
   :alt: Io from Juno


The JunoCam instrument is a color camera that takes pictures in red, green, and blue filters.
The raw images are transmitted to Earth and are available for anyone to download and process.
The image above is a composite of 3 raw images, one for each color filter.
It is downloaded from the Juno mission website, under the 
`Image Processing <https://www.missionjuno.swri.edu/junocam/processing>`_ tab.
You can view the composite image in the browser 
`here <https://www.missionjuno.swri.edu/junocam/processing?id=JNCE_2023364_57C00022_V01>`_.
  

Basic Goal
~~~~~~~~~~

    Replicate the color picture from the raw images that the spacecraft transmitted.

Advanced Goal
~~~~~~~~~~~~~

    Build a new UI system for processing JunoCAM images using modern UI/UX design principles.

Quests
~~~~~~

    |uncheckedbox| Download the raw images from the Juno mission website.
        There are two important links on the Juno website and similar pages for other
        Junocam images: “Metadata and Images”, each of which downloads a zip file.
        We’ll address the Metadata link later, but download both now.

    |uncheckedbox| Understand the NAIF/SPICE system for spacecraft navigation.

    |uncheckedbox| Understand the spacecraft kernel files (SPK/CK/FK)

    |uncheckedbox| Use the SPICE kernels to determine the position of the spacecraft when the images were taken.

    |uncheckedbox| More quests to come!

Questions
~~~~~~~~~

    #. How close was Juno to Io?
    #. What is the resolution of the images?
    #. Why is half of Io brightly lit?
    #. Why is the dark half visible at all?


2. Microwave Mapping of Jupiter's Polar Cyclones
------------------------------------------------

:Contributor: **Jiheng Hu**

:Programming Language:
  ``Python``

:Difficulty:
  |fillstar| |fillstar| |openstar| |openstar| |openstar|
