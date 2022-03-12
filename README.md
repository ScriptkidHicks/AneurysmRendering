# An Analysis of Aneurysm Data Using the VisIt Toolkit
  This is a study I did on an aneurysm data set, using the VisIt toolkit, for my scienfitic visualization final project. I focused on pressure levels, velocity, integrated velocity, and the way that the two related to one another. Initially I had intended to put a greater emphasis on camera movement, but as time went on, I found that I was considerably more interested in what could be accomplished with the isovolume, streamline, and vector field tools which VisIt provides. You can find the scripts I used in the 'Scripts' folder. I have included a sample script because it was used repeatedly with slight variations for camera movement, and file name changes. Since these were moderately small changes, I did not upload relatively similar files. Credit for that code goes both to Hank Childs, and to the VisIt tutorial. 
  
## Instillation

  Getting the VisIt toolkit installed was a considerable portion of the task in and of itself. I'm going to leave some advice here, in case anyone in the future is attempting to install VisIt for a personal / work / school project, and wants to avoid some pitfalls that I fell in.
  
#### Installing on Windows:
  I would recommend against this. I had considerable trouble with attempting to install it on windows 10. I attempted with python versions 3.72, 3.9, and 3.10.0. The consistent issue I ran into is that VisIt, once installed, had difficulty finding various path environmental variables; namely `PYTHONPATH` and `PYTHONHOME`. Initially VisIt could not import encodings. After defining PYTHONPATH it was capable of finding these encodings, but could not find other library imports which were main parts of Python (The IO and OS imports). 

#### Installing on Linux
  This is a fairly straightforward process. You're going to want to go to [this page](https://visit-dav.github.io/visit-website/releases-as-tables/#series-32) for the latest version of VisIt. There will also be a script you should download, further down the page. This script will come with a set of instructions on how to feed input to the script, including the version of Linux that you're using. I installed this on a version of Linux Mint Cinnamon, which itself is based on Ubuntu 20.
  After instillation, make sure that you have the latest version of xterm installed. VisIt is designed to use Xterm rather than bash, and many versions of linux to not come with it installed. You can install xterm by typing the lines below into bash (or you could just copy paste them).
```
sad
```


### Sources

[The tutorial I used to understand how to use VisIt](https://visit-sphinx-github-user-manual.readthedocs.io/en/develop/tutorials/VisIt_Basics.html)

[The data set I used](https://visit-dav.github.io/largedata/datarchives/aneurysm)

[The script you will need for installing VisIt on linux](https://visit-dav.github.io/visit-website/releases-as-tables/#series-32)

### Authors
Creator, editor: Tammas Hicks
Contributors: Hank Childs, Patrick Thomasma (Special thanks for giving me some ideas about which direction to go with data processing)
