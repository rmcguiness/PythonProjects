from turtle import Turtle
import random
import math

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.5, .5)
        self.color('green')
        self.speed('fastest')
        x = 5 * (random.randint(-280, 280)/5)
        y = 5 * (random.randint(-280, 280)/5)
        self.goto(x,y)

    def relocate(self, snake):
        x = 5 * (random.randint(-280, 280)/5)
        y = 5 * (random.randint(-280, 280)/5)
        self.goto(x,y)
        for i in snake.snake:
            if i.distance(self) < 20: 
                self.relocate(snake)

        
