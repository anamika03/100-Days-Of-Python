# colorgram.py is a Python library that lets you extract colors from images. 
# Installation: pip install colorgram.py 
# How to use: Using colorgram.py is simple. Mainly there is only one function you will need to use - colorgram.extract. 


import colorgram
from turtle import colormode

colormode(255)
rgb_colors = []
colors = colorgram.extract('/Users/anamika/Documents/100_Days_of_Python/100-Days-Of-Python/Day 18/hirst-painting-start/image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colors =  (r, g, b)
    rgb_colors.append(new_colors)

print(rgb_colors)

# Extracted colors
# color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
