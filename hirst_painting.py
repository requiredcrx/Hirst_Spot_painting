import random
import turtle

import colorgram
from turtle import Turtle, Screen

required = Turtle()

'''This line was initially used to extract colors from a random image found online using colorgram module. This image was generated as rgb value
represemted as turple in list........ line 13 - 23'''

# ------------------------------------------------------------------------------------------------------------------------------------
# colors = colorgram.extract("image.jpg", 30)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)
# ------------------------------------------------------------------------------------------------------------------------------------

turtle.colormode(255)

color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61), (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39), (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202), (62, 26, 45), (145, 165, 181), (6, 79, 111), (35, 44, 99), (71, 153, 84), (120, 41, 33), (170, 203, 205), (223, 178, 169)]
required.pu()

required.setpos((-190, -210))

number_of_dots = 100
rows = 0
for dots in range(1, number_of_dots +1):
    required.color(random.choice(color_list))
    required.dot(20)
    required.fd(50)
    if dots % 10 == 0:
        if rows % 2 == 0:
            required.lt(90)
            required.fd(50)
            required.lt(90)
            required.fd(50)
        else:
            required.rt(90)
            required.fd(50)
            required.rt(90)
            required.fd(50)
        rows += 1

required.hideturtle()

screen = Screen()
screen.exitonclick()
