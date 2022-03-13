# An Analysis of Aneurysm Data Using the VisIt Toolkit


[Details](#details)

[Installation](#installation)

[Installing on Windows](#installing-on-windows)    

[Installing on Linux](#installing-on-linux)

[Making a Movie](#making-a-movie)

[Findings](#my-findings)

[Sources](#sources)

[Credits](#authors)

## Details
  This is a study I did on an aneurysm data set, using the VisIt toolkit, for my scienfitic visualization final project. I focused on pressure levels, velocity, integrated velocity, and the way that the two related to one another. Initially I had intended to put a greater emphasis on camera movement, but as time went on, I found that I was considerably more interested in what could be accomplished with the isovolume, streamline, and vector field tools which VisIt provides. You can find the scripts I used in the 'Scripts' folder. I have included a sample script because it was used repeatedly with slight variations for camera movement, and file name changes. Since these were moderately small changes, I did not upload relatively similar files. Credit for that code goes both to Hank Childs, and to the VisIt tutorial. I have not uploaded the video clips that I created, because they would easily exceed the limit that github imposes on file size.
  
## Installation

  Getting the VisIt toolkit installed was a considerable portion of the task in and of itself. I'm going to leave some advice here, in case anyone in the future is attempting to install VisIt for a personal / work / school project, and wants to avoid some pitfalls that I fell in.
  
#### Installing on Windows:
  I would recommend against this. I had considerable trouble with attempting to install it on windows 10. I attempted with python versions 3.72, 3.9, and 3.10.0. The consistent issue I ran into is that VisIt, once installed, had difficulty finding various path environmental variables; namely `PYTHONPATH` and `PYTHONHOME`. Initially VisIt could not import encodings. After defining PYTHONPATH it was capable of finding these encodings, but could not find other library imports which were main parts of Python (The IO and OS imports). 

#### Installing on Linux
  This is a fairly straightforward process. You're going to want to go to [this page](https://visit-dav.github.io/visit-website/releases-as-tables/#series-32) for the latest version of VisIt. There will also be a script you should download, further down the page. This script will come with a set of instructions on how to feed input to the script, including the version of Linux that you're using. I installed this on a version of Linux Mint Cinnamon, which itself is based on Ubuntu 20.
  After instillation, make sure that you have the latest version of xterm installed. VisIt is designed to use Xterm rather than bash, and many versions of linux to not come with it installed. You can install xterm by typing the lines below into bash (or you could just copy paste them).
```
sudo apt-get update -y
sudo apt-get install -y xterm
```
  Once installed, I would recommend creating a folder for storing the data you want to work with, and opening visit from there. Without additional direction on where to save the files that your commands create, visit will save them to the folder that it is opened from. The following command can be used to open visit:
```
~/visit/bin/visit
```
or
```
~/visit/bin/visit -cli
```
for the command line interface version. You will not necessarily need this, given that there is a command function built into VisIt.

## Making a Movie

![using Visit](https://github.com/ScriptkidHicks/AneurysmRendering/blob/main/Images/visit.png)
*A 0.03 section of pressure from the initial slide of the aneursyms data. A mesh, sliced on a bias, to demonstrate the rest of the artery*

  I used a combination of the command function in Visit, and the create movie function offered in the file dropdown. For creating movies directly from visit I would use [this script](https://github.com/ScriptkidHicks/AneurysmRendering/blob/main/Scripts/CameraRotationOnMesh.py). Special thanks to Hank Childs for information on how to use the script to make the camera fly around the body of the aneurysm while recording images. Once I had saved the images to the folder I had launched VisIt from, i used [this script](https://github.com/ScriptkidHicks/AneurysmRendering/blob/main/Scripts/ffmpegsave.py) to translate those images into a movie. The name of the movie / the name of the files could be used each time I made a different movie. It was also easy to execute these from the command function of VisIt, since it meant that I did not have to manually set up the conditions of the analysis in the code, but could instead leave that to be implicitly handled by the toolkit. 
  
  I also used the function in VisIt which allowed for saving directly to movie. This method allowed for easily taking videos of content, but limited my ability to navigate the camera around the object for the duration of the film, and also somewhat limited my ability to make videos of single index in time. 
  
  Once I had all the movie clips I needed (as well as several still images from a single point in time) I created a single ~3 minute video outlining my findings. The video was mixed together using Adobe Premier Pro (which I had access to through my job). I would estimate I put roughly 6 hours into cutting together clips, finding useful effects, and constructing a narrative.
  
## My findings
![Findings intro image](https://github.com/ScriptkidHicks/AneurysmRendering/blob/main/Images/meshless.png)

I wanted to focus my research on the way that pressure interrelated with velocity, with a focus on the body of the aneurysm. One of the first things I found was that pressure occilated on an extremely short time scale, over wide ranges, and had with tight ranges for each time section. Each time slice was roughly 0.04 seconds in length, the pressure would undergo an average change off ~100-200 between two frames, and isolating a single slice of the pressure inside aneurysm body required isovolumes with ranges on the scale of 0.3 to 1.5. 

This meant that it was difficult to isolate pressure fluctuations in the same way that I would velocity, using isovolumes. Given this, I decided to use three different approaches: tracking velocity, tracking integrated velocity, and using tight time slices to visualize pressure levels inside the aneursym during moments of high velocity / pressure.

Tracking velocity was done in two ways. Firstly I used isovolumes, clamped to both high and low velocity. The high velocity isovolume, renderred inside a mesh, allowed me to visualize concentrations of high velocity inside the aneurysm, as well as give an indicator for where high pressures would occur. Low velocity isovolumes, using a selection clip tool to slice along the bias, allowed for visualization of how velocity changed over time from a different perspective.




### Sources

[The tutorial I used to understand how to use VisIt](https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/tutorials/VisIt_Basics.html)

[The data set I used](https://visit-dav.github.io/largedata/datarchives/aneurysm)

[The script you will need for installing VisIt on linux](https://visit-dav.github.io/visit-website/releases-as-tables/#series-32)

### Authors
Creator, editor: Tammas Hicks
Contributors: Hank Childs, Patrick Thomasma (Special thanks for giving me some ideas about which direction to go with data processing)
