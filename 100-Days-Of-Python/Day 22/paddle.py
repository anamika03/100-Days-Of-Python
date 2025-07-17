from turtle import Screen, Turtle
UP = 90
DOWN = 270

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=0.7)
        self.penup()
        self.goto(position)

    def create_paddle(self):
        pass

    # def go_up(self):
    #     new_y = paddle.ycor() + 20
    #     paddle.goto(paddle.xcor(), new_y)

    # def go_down(self):
    #     new_y = paddle.ycor() - 20
    #     paddle.goto(paddle.xcor(), new_y)
