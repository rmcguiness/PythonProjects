from turtle import Turtle, Screen
from paddle import Paddle

screen= Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)
game_on = True

paddleR = Paddle()
paddleL = Paddle("LEFT")

screen.listen()
screen.onkeypress(paddleR.move_up, "Up")
screen.onkeypress(paddleR.move_down, "Down")

screen.onkeypress(paddleL.move_up, "w")
screen.onkeypress(paddleR.move_down, "s")

while game_on:
    screen.update()





screen.exitonclick()