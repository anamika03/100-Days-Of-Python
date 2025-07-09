from turtle import Turtle, Screen, colormode
import random
from random import randint

colormode(255)

# Tuple is ordered and immutable collection of elements
my_tuple = (1, 2, 3)
print(my_tuple[2])

# Turtle drawing a square
tim = Turtle()
tim.shape("turtle")

directions = [0, 90, 180, 270]
tim.pensize(8)
tim.speed(10)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color =  (r, g, b)
    return random_color

for i in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))


# To see the turtle on GUI
screen = Screen()
screen.exitonclick()