from turtle import Turtle, Screen
import random

# Turtle drawing a square
tim = Turtle()
tim.shape("turtle")

colours = ["red", "green", "blue", "orange", "grey", "deepskyblue", "pink", "lightseagreen", "brown", "rosybrown", "wheat", "teal", "aqua", "navy", "violet", "purple", "crimson", "orchid", "lime", "khaki"]
directions = [0, 90, 180, 270]
tim.pensize(8)
tim.speed(10)

for i in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))


# To see the turtle on GUI
screen = Screen()
screen.exitonclick()

