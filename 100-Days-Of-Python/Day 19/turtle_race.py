from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "green", "yellow", "blue", "brown", "purple"]
y_positions = [80, 50, 20, -10, -40, -70]
all_timmy = []

for i in range(6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[i])
    timmy.goto(x=-240, y=y_positions[i])
    all_timmy.append(timmy)

if user_bet:
    is_race_on = True

while is_race_on:
     
    for turtle in all_timmy:
        if turtle.xcor() > 225:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
               print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        turtle.forward(randint(0, 10))

screen.exitonclick()
    