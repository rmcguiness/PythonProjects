from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
         super().__init__()
         self.penup()
         self.shape('square')
         self.color('white')
         self.shapesize(.5, .5)

    def move(self):
        self.forward(10)
