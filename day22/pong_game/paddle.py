from turtle import Turtle
PADDLE_POS = {
    "RIGHT" : (350,0),
    "LEFT" : (-350,0)
}

class Paddle():
    def __init__(self, side = "RIGHT"):
        self.create_paddle(side)
       
    def create_paddle(self, side):
        new = Turtle("square")
        new.shapesize(5,1)
        new.penup()
        new.color('white')
        new.goto(PADDLE_POS[side])

        self.paddle = new

    def move_up(self):
        y = self.paddle.ycor() + 15
        self.paddle.goto(self.paddle.xcor(), y)

    def move_down(self):
        y = self.paddle.ycor() - 15
        self.paddle.goto(self.paddle.xcor(), y)