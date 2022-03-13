# An Analysis of Aneurysm Data Using the VisIt Toolkit


[Details](#details)

[Installation](#installation)

[Installing on Windows](#installing-on-windows)    

[Installing on Linux](#installing-on-linux)

[Making a Movie](#making-a-movie)

[Findings](#my-findings)

[Sources](#sources)

[Credits](#authors)

You can find the final video I made [here](https://www.youtube.com/watch?v=rGB3E8xr6Ug&ab_channel=TammasHicks)

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

Tracking velocity was done in two ways. Firstly I used isovolumes, clamped to both high and low velocity. The high velocity isovolume, renderred inside a mesh, allowed me to visualize concentrations of high velocity inside the aneurysm, as well as give an indicator for where high pressures would occur. Low velocity isovolumes, using a selection clip tool to slice along the bias, allowed for visualization of how velocity changed over time from a different perspective. This also gave me an opportunity to work with visualizations that involved doing different selections on overlapping renderings, to create a complete image, each part of which conveys different types of information.

The second way I tracked velocity was by using a vector field focused on velocity. This ended up being a relatively small part of my final presented findings, but it was an interesting way to observe velocity from an eulerian perspective. I ended up choosing the eliptical shape for the vector indicators, feeling that the soft shape of them gave an interesting indication of where the walls of the aneurysm were. The technique of visualizing data inside the body of the field, without visualizing the matrix itself, was a method I found rendered very interesting looking results, and one I applied several times.

![A streamline image](https://github.com/ScriptkidHicks/AneurysmRendering/blob/main/Images/Streamline0008.png)
Tracking integrated velocity was useful for visually rendering information about how velicity influenced the flow of objects through the artery and aneurysm. I generated my main visualization of this information through the streamline operator. The VisIt tutorial had a good guide on where to place the origin of the streamlines, though they used a very different style for the streamlines. I increased the number of streamlines for the video I created to ~4000, which caused the renderer to chug horribly, but did create a video which clearly indicated how particles would travel through the cell at each step of time, and how they would travel through the cell generall. I attempted to create a visualization of read or white blood cells traveling through the aneurysm, but the length of the streamline could not be clamped to anything below 0.3, and anything close to that range simply looked like a short line, which moved the point of its destination around at a pace difficult to comprehend for the viewer.

The integrated streamline visualization did give some important information about the movement of objects wthin the aneurysm though. As I note in [the video](https://www.youtube.com/watch?v=rGB3E8xr6Ug&ab_channel=TammasHicks) the particles accelerate as they approach the top of the aneurysm, and circle towards the center. This resulted in VisIt throwing an error, refering to particles in the advection field circling endlessly around the same point, and entering an endless loop. This is interesting because I think it draws attention to the ways in which our massless, volume-less particles differ from real particles. Obviously this is not a phenomena that would occur in real life, given that particles would jostle and push one another out of the way.

In my visualization of streamlines, as you can see above, I clamped the range between 0 and 2.0. The velocity scale, over the time of the simulation, ranges from 0 to 40, and most of the values occur from 0 to 5. For the integrated velocity values, we see most of the values occuring between 0 and 2, or slightly above. Clamping the display increases color contrast, which better allows us to visualize differences in speed, but also allows us to focus on where most of the information is. Similarly, if we wanted to study outliers, we could clamp the range to the highest levels. This focus on clamping the range is something I will revisit in the next part about visualization of pressure.

![Tracking pressure](https://github.com/ScriptkidHicks/AneurysmRendering/blob/main/Images/visit0200.png)
Tracking pressure was, as mentioned at the start, made difficult by the high variation of pressure levels, combined with the tight range of pressure that would occur, and the high rate at which the pressure levels would change. Consequently I decided to focus on single slices of time, and small ranges of pressure to give the viewer an idea of how waves of pressure entered the cell. This meant using the script I mentioned above, but removing the function within it that advanced time, instead setting the time slice to the desired initial 175, then rotating around the object a few times. I ended up cutting most of that video, and only using part of it in the final product, but it was nice to have a selection to work from.

The range of pressure, from minimum to maximum, across the course of the entire time slice, was from -400, to 3000. Despite this, most pressures inside the aneurysm body, did not occur above 1500. The only place that pressures above 2000, roughly 1/3 of the entire range, occured was in the entry to the artery section we were observing, and then only for between 0.04 and 0.08 seconds. This is a good example of how considering the entire range of your data can be detrimental to accurately visualizing the important parts. A big takeaway from this project for me was that clamping data to ranges which dialated focus in on essential activity important for good visualization.

#### a few final thoughts
  Throughout the course of making this video I found that it was useful to use pseudocolors with high contrast, or attractive colors. I found that clamping the values that the pseudocolor adressed created greater differentiation between high and low areas of pressure / velocity / integrated velocity, in a way that allowed the viewer to more accurately identify areas of high activity or low activity. I found that generating beautiful images was an important component of creating visualizations that I wanted to look at longer, and gather more information from. I think we don't always consider the importance of aesthetic in scientific visualization. Keeping the viewers attention, rendering the data in an acessible way, these are both important in our attempt to convey ideas to our observeers.
  
  There were also some ways that I failed in making this project, which I did not think about until it was too late to fix. Namely, I did not consider color blind individuals when making these videos. About 8% of assigned male at birth individuals have color blindess, and of them about 60% have Deuteranomaly, which impinges their ability to see colors on the green portion of the spectrum. The majority of my visualizations rely on some form of green to convey information about their content; and those are likely inaccessible to people with the most common form of color blindess. It can be difficult to reduce the range of colors we have to work with, and still create visualizations that are aesthetic and high contrast, but it is important that we work to be inclusive as we make this type of content. It's something I would like to do differently if I do a project like this in the future.

### Sources

[The tutorial I used to understand how to use VisIt](https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/tutorials/VisIt_Basics.html)

[The data set I used](https://visit-dav.github.io/largedata/datarchives/aneurysm)

[The script you will need for installing VisIt on linux](https://visit-dav.github.io/visit-website/releases-as-tables/#series-32)

### Authors
Creator, editor: Tammas Hicks

Contributors: Hank Childs, Patrick Thomasma (Special thanks for giving me some ideas about which direction to go with data processing)
