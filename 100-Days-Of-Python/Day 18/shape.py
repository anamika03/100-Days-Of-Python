from turtle import Turtle, Screen
import random

# Turtle drawing a square
tim = Turtle()
tim.shape("turtle")

colours = ["red", "green", "blue", "orange", "grey", "deepskyblue", "pink", "lightseagreen", "brown", "rosybrown", "wheat", "teal", "aqua", "navy", "violet", "purple", "crimson", "orchid", "lime", "khaki"]

def shapes(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for i in range(3, 11):
    tim.color(random.choice(colours))
    shapes(i)


# To see the turtle on GUI
screen = Screen()
screen.exitonclick()

