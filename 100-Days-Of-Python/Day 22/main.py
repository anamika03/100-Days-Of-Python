from turtle import Turtle, Screen
from paddle import Paddle
  

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-380, 0))

# screen.listen()
# screen.onkey(go_up, "Up")
# screen.onkey(go_down, "Down")


game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()
