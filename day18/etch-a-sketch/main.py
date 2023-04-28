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

def circle_forward_left():
    t.forward(5)
    new_heading = t.heading() + 5
    t.setheading(new_heading)

def circle_forward_right():
    t.forward(5)
    new_heading = t.heading() - 5
    t.setheading(new_heading)

def circle_backward_left():
    t.backward(5)
    new_heading = t.heading() - 5
    t.setheading(new_heading)

def circle_backward_right():
    t.backward(5)
    new_heading = t.heading() + 5
    t.setheading(new_heading)

def pen_size_up():
    og_pen = t.pensize() 
    t.pensize(og_pen+1)

def pen_size_down():
    og_pen =   t.pensize() if t.pensize()>0 else 1  
    t.pensize(og_pen-1)

def reset_screen():
    t.home()
    t.clear()

screen.listen()

screen.onkey(move_forward, "Up")
screen.onkey(move_backward,"Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkeypress(t.penup, 'u')
screen.onkeypress(t.pendown, 'd')
screen.onkeypress(pen_size_up , '1')
screen.onkeypress(pen_size_down, '2')
screen.onkeypress(reset_screen, 'r')

screen.exitonclick()