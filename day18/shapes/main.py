from turtle import Turtle, Screen
import random
colors = ['black' , 'red' ,  'yellow' , 'green' , 'green2' , 'cyan' , 'blue' , 'magenta', 'purple']
def print_shape(numSides=3):
    for _ in range(numSides):
        t.forward(100)
        t.right(360/numSides)


t = Turtle()
for i in range(3,12):
    t.color(colors.pop())
    print_shape(i)


screen = Screen()
screen.exitonclick()