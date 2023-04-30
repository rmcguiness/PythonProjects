from turtle import Turtle
PADDLE_POS = {
    "RIGHT" : [(280,-10),(280,0),(280,10)],
    "LEFT" : [(-280,-10),(-280,0),(-280,10)]
}



class Paddle():
    def __init__(self):
        self.create_paddle()
       

    def create_paddle(self, side = "RIGHT"):
        for i in range(3):
            new = Turtle("square")
            new.penup()
            new.color('white')
            new.goto(PADDLE_POS[side][i])
            self.paddle.append(new)