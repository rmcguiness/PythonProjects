from turtle import Turtle
PADDLE_POS = {
    "RIGHT" : (350,0),
    "LEFT" : (-350,0)
}

class Paddle(Turtle):
    def __init__(self, side = "RIGHT"):
        super().__init__()
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        self.color('white')
        self.goto(PADDLE_POS[side])   

    def move_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)