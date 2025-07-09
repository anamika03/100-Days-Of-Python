from turtle import Turtle, Screen

# Turtle drawing a dashed line
tim = Turtle()
tim.shape("turtle")
tim.color("red")

for i in range(10):
    tim.forward(15)
    tim.penup()
    tim.forward(15)
    tim.pendown()


# To see the turtle on GUI
screen = Screen()
screen.exitonclick()

