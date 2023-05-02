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
        new.shapesize(1,5)
        new.setheading(90)
        new.penup()
        new.color('white')
        new.goto(PADDLE_POS[side])

        self.paddle = new

    def move_up(self):
        self.paddle.setheading(90)
        self.paddle.forward(10)

    def move_down(self):
        self.paddle.setheading(270)
        self.paddle.forward(10)