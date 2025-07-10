from turtle import Turtle, Screen, colormode
import random
from random import randint

colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.speed(12)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    colours =  (r, g, b)
    return colours

def draw_spirograph(gapSize):
    for _ in range(int(360 / gapSize)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gapSize)

draw_spirograph(4)

# To see the turtle on GUI
screen = Screen()
screen.exitonclick()