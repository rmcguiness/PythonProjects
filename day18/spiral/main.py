from turtle import Turtle, Screen

b = Turtle()
r = Turtle()
r.shape('turtle')
r.color("red")
b.shape('turtle')
r.forward(1)
r.left(90)
r.forward(1)
for i in range(0,1000):
    r.forward(i+1)
    r.left(90)
    r.forward(i+1)
    b.forward(i)
    b.right(90)
    b.forward(i)




screen = Screen()
screen.exitonclick()