# What is this?
Hello, this is the space where I experiment with various openCV drawing methods to achieve an interesting / artistic result.
As of now, there are two files that you can run:
- LineToMouse.py: Draws a line from the center of the window to the current mouse position. 
- PerlinNoise.py: Draw random structures, that look interesting.

# Getting Started

## Prequisites

- Download and install Python 3 (Version 3.10.7) from python.org
<a href="https://www.python.org/">
    <img style="height: 56px; width:100px;" src="https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png" alt="Logo" width="80" height="80">
</a>

- Test which version is installed on your machine with `python --version` in the terminal
- Ensure that the correct version is used in the terminal as well as the selected interpreter
- Install pip from https://pip.pypa.io/en/stable/installation/
- Ensure that a version newer than 19.3 is installed (`pip --version`)
- As the code was developed in Visual Studio Code, download the Python extension for Visual Studio Code
- Make sure to import the modules as well:

## Modules
- OpenCV: Install by typing `pip install opencv-python` in the terminal
- numpy: Install by typing `pip install numpy` in the terminal
- noise: Install by typing `pip install noise` in the terminal (Not necessary for LineToMouse.py)

# Usage
Open the .py files and enjoy! You can also change various variables in the source code (although it is not well structured, as I didnt care enough for it to be organized).
As previously stated, these are just some fun little projects in which I tried to achieve interesting effects.

## LineToMouse.py
Play around with lines 21-23 to change the color values of the lines. Here, the lines ger lighter the closer the mouse is towards the center, but you can change this behaviour to achieve different effects.

## PerlinNoise.py
- Change lines 23 and 25 to change the shape of the drawn structure. I have not really understood what the noise function was doing based on its inputs, so it was mostly trial and error to get an interesting result.
- Line 29: Change this value to impact the spacing between the lines. The lower this number is, the closer the lines are together, which gives a ribbon effect.
- Lines 33-34: Change the color of the lines.
- Lines 50, 52, 54: These also change the shape of this structure, as well as how many lines are drawn. Just try things out if you like.
  
