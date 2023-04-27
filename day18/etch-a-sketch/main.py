from turtle import Turtle, Screen
import random

t = Turtle()
screen = Screen()
t.speed('fastest')

def move_forward():
    t.forward(5)
def move_backward():
    t.backward(5)
def turn_left():
    new_heading = t.heading() + 10
    t.setheading(new_heading)
def turn_right():
    new_heading = t.heading() - 10
    t.setheading(new_heading)

screen.listen()

screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward,"s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")

screen.exitonclick()