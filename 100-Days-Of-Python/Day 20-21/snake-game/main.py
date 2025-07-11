# 1. Create a snake body
# 2. Move the snake
# 3. Control the snack
# 4. Detect collision with food
# 5. create a scoreboard
# 6. Detect collision with wall
# 7. Detect collision with tail

from turtle import Screen, Turtle

snake = Turtle("square") # can provide the shape while creating an object
snake.shapesize(1, 3)
snake.color("white")


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.exitonclick()