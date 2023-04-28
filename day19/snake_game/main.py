from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('Snake Game')
player_alive = True

snake = Snake()

screen.update()
screen.listen()

screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_left, "Left")
screen.onkeypress(snake.move_right, "Right")
snake.move_forward()

while player_alive:
    screen.listen()
    snake.move_forward()
    player_alive = snake.not_dead()
    screen.update()
    time.sleep(.1)

screen.exitonclick()