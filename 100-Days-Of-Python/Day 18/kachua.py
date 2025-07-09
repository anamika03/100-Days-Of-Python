from turtle import Turtle, Screen

# Turtle drawing a square
tim = Turtle()
tim.shape("turtle")
tim.color("red")

for i in range(4):
    tim.forward(100)
    tim.left(90)

# To see the turtle on GUI
screen = Screen()
screen.exitonclick()

