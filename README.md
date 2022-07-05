## Table of contents
* [General info](#general-info)
* [Introduction](#introduction)
* [Technologies](#technologies)
* [Download](#download)
* [Run](#run)
* [Roadmap](#roadmap)

## General info
8-bit RGB (also known as 3-3-2 bit RGB and 8-8-4 bit RGB)

The 3-3-2 bit RGB use 3 bits for each of the red and green color components, and 2 bits for the blue component, due to the eyes having lesser sensitivity to blue. This results in an 8×8×4 = 256-color palette

This palette is used by

* The MSX2 series of personal computers.
* Palette 4 of the IBM PGC (palette 2 gives 2-3-3 bit RGB and palette 3 gives 3-2-3 bit RGB).
* Enterprise Computer.
* Vector-06C, a home computer from the USSR.
* VGA built-in output of the Digilent Inc. NEXYS 2, NEXYS 3 and BASYS2 FPGA boards.
* The Uzebox gaming console
* SGI Indy 8-bit XL graphics
* The Tiki 100 personal computer (only 16 colors can be displayed simultaneously)
* Wear OS smartwatches with ambient displays (only 16 colors can be displayed simultaneously)

Source: https://en.wikipedia.org/wiki/List_of_monochrome_and_RGB_color_formats

## Introduction

This is an education project, so it isn't to commercial uses. Learning programming process it isn't only to do some course from the internet, so I've decided to create this project to try use python in practice. If for someone my program will be useful that will be great! To create my program I've used external sources e.g most popular "Stack Overflow" or generally the Internet. So if you decide copy my code, feel free, you can do it with it whatever you want. As I said on the begin, project was created only for education and for a start with programming in Python.

## Technologies
Project is created with:
* Vscode: _1.67.2_
* Python version: _3.10.4_ 
* Python Imaging Library (Fork): _9.1.1_

## Download

The RGB332 (8-bit RGB) converter program in python.
It is simple program written in python, to run it you need just download project to your machine. To do that please use link below:

```
$ git clone https://github.com/Applegammer/rgb332converter-python-education.git
```
## Run

To run is required: 
* Python version: _3.x.x (recommended 3.10.4)_
* Pillow library: _9.1.1 or higher_
* tkinter library: _0.1.0_

**Linux:**
```
$ python ./converter_rgb332.py
```
**OR**
```
$ python3 ./converter_rgb332.py
```
**Windows:**
```
$ py converter_rgb332.py
```
## Roadmap

Basically information about project roadmap, what steps I want realize on the project
### Stage one
* ~~Open an image~~ 
* ~~Get image width and height~~
* ~~Take RGB (red, green, blue) values from once pixel~~
* ~~Create a loop where will be take RGB for all lines X,Y~~
* ~~Save values to file~~
### Stage two - feature #1
* ~Add to program feature which convert 24-bit RGB to 8-bit (split 3-3-2 bit red/green/blue) RGB332~
### Stage three - feature #2
* ~~Change RGB332 values to binary string~~
* ~~Marge binary values to one string (because I need 8-bit in string)~~
### Stage four - feature #3
* ~~Change binary to decimal system~~
### Additional
* Make choice to put name of your file, and choosing extenstion (e.g .txt,.pdf,.docx)
* ~~Make option to choose file from your desktop and load to the program~~