# 🎨 Markov Pixel Art 🎨

Create some amazing pieces of artwork (or non-sense works of art !) using the power of Markov chains !
_________________________________________________
💡*You're currently on the version **v0.1.0** of this project. To download previous versions, please go to the Release section.*
_________________________________________________
## ❓What is it ?
The Markov Pixel Art project is a programm that allows you to generate an image made of ``50x50`` pixels with random colors.\
You choice the color of the first pixel (the top left corner) and then the other colors are built by multiplying a matrix by the previous color seen as a vector. It's basically a Markov chain operation, so the project's name.

## 🖥️ Download the project

This project runs only in Python. \
You need **at least Python 3.12** and the python module  **pygame (version 2.6.1 at least)** to run this project. \
If these requirements are satisfied, type ```git clone https://github.com/HiAbdounour/Markov-Pixel-Art``` in the terminal (cmd) to download the project.

You can also download the whole repository in the Release section *(but the project isn't actually big, a ``zip`` file just for one Python file...)*

## 🎨 Play the game

After downloading the project, type ``python markov.py`` to run the project OR use an IDE.\
Some init messages will then be displayed.\
After that, you'll be ask to put four values for your initial color, respectively for **cyan**, **magenta**, **yellow** and **black**. (The color is coded following the [CMYK color model](https://en.wikipedia.org/wiki/CMYK_color_model).) Then just watch as the window fills itself continously. \
At the end, you can take a screenshot of your fabulous artwork.

*Some examples (screenshots) will be added soon.*

Let's together dive inside Markov's secrets !

## 🛠️ Changelog
Here you can see the major changes of this project.\
To have more details about the changes or to download a previous version, [check the Release section](https://github.com/HiAbdounour/Markov-Pixel-Art/releases).\
*It is expected to create a v1 in which users can have more flexibility on color generation and Markov chains.*
