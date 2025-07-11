from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.setheading(tim.heading() + 10)

def turn_right():
     tim.setheading(tim.heading() - 10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
# This line activates the screen's focus to start listening for keyboard events. 
# It tells the Turtle window to "start listening for key presses."
# Always use screen.listen() before setting up onkey() events.
screen.listen() 
screen.onkey(move_forwards, "w")  # on clicking the space it moves
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_screen, "c")
screen.exitonclick()
    