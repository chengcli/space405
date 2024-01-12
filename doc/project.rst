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

:Owner:
  **Macarena Peralta**

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


2. Microwave Mapping of Jupiter's Vortices
------------------------------------------

:Contributor: **Jiheng Hu**

:Programming Language:
  ``Python``

:Difficulty:
  |fillstar| |fillstar| |fillstar| |openstar| |openstar|

Background
~~~~~~~~~~
Jupiter is widely known for its global widespread storms, vortices, and convective clouds that dominate its upper atmosphere. These phenomena are closely linked to the atmospheric thermal structure's instability, convective processes, and the latent heating associated with volatile condensations.  

Here is an infrared image of the Jupiter polar vortices, taken by Juno/JIRAM in the 20th flyby.

.. image:: ../images/Juno-JIRAM-polar-vortices-PJ20.jpg
   :width: 400px
   :align: center
   :alt: Jupiter’s north pole taken by JIRAM (ASI) onboard JUNO © NASA/JPL-Caltech

The Juno spacecraft is equipped with a microwave radiometer (MWR) capable of mapping Jupiter's atmosphere using six centimeter-wave channels, with frequencies ranging from 0.6 GHz (50 cm, channel 1) to 21.9 GHz (1.37 cm, channel 6). These channels are designed to detect the dynamic characteristics of Jupiter’s sub-cloud atmosphere and the presently unknown variations in the abundances of ammonia and water deep within these cloud decks.

Basic Goal
~~~~~~~~~~

Plot the images of multiband microwave brightness temperature signals observed by MWR, distinguish the individual Jovian cyclone, analyze the emission characteristics.

Advanced Goal
~~~~~~~~~~~~~

1. Derive the measurement response function (MRF) of a specific MWR footprint with provided observational parameters, including the spacecraft's altitude, antenna beamwidth and corresponding antenna pattern function. 
2. Perform the integration of high-resolution truth emission with derived MRF to simulate antenna measurements.

Quest:
~~~~~~~~~~~~~

   |uncheckedbox| Login into the workstation, find the current Juno MWR HDF file from the following directory: /nfs/nuke/chengcli/JUNOMWR/foyafuso/MWR_TA_perijove_current.h5 .  

   |uncheckedbox| Understand the mode of spinning mapping of MWR.  

   |uncheckedbox| Extract variables from the HDF file, understand the footprints and the spacecraft nadir points.  

   |uncheckedbox| Understand how the footprint forms in the context of a spinning maping mode of MWR.  


Question:
~~~~~~~~~~~~~

    #. Why is a typical MWR footprint in elliptical shape?  
    #. Why is the MWR's image down in a coarser resolution compared to JIRAM?  
    #. Amongst the images of six MWR channels, which one gives the clearest featrues of vortices, why?  
    #. How to calculate the emission angle by ourself, knowing the MWR's poistion and altitude?  

References
~~~~~~~~~~~~~

  -	S.J. Bolton et al. Microwave Observations Reveal the Deep Extent and Structure of Jupiter’s Atmospheric Vortices. Science 374, 968- 972(2021). DOI:10.1126/science.abf1015.  
  -	Janssen, M.A. et al. MWR: Microwave Radiometer for the Juno Mission to Jupiter. Space Science Review 213, 139–185 (2017). https://doi.org/10.1007/s11214-017-0349-5.  
  - Ingersoll, A.P. et al. Polygonal patterns of vortices on Jupiter: Convective forcing and large-scale shielding. Nature Astronomy (in press).  


