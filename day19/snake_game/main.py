from turtle import  Screen
import time
from snake import Snake
from food import Food

screen = Screen()
def play_snake():
    player_alive = True
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.bgcolor('black')
    screen.title('Snake Game')

    snake = Snake()
    food = Food()
    screen.listen()

    screen.onkeypress(snake.move_up, "Up")
    screen.onkeypress(snake.move_down, "Down")
    screen.onkeypress(snake.move_left, "Left")
    screen.onkeypress(snake.move_right, "Right")
    snake.move_forward()

    while player_alive:
        screen.listen()
        screen.update()
        time.sleep(.1)
        snake.move_forward()
        player_alive = snake.not_dead()
        if snake.head.distance(food) < 20:
            snake.grow()
            food.relocate()
    
    play_again = screen.textinput('GAME OVER', f'Your score was {len(snake.snake)-3}!\n Would you like to play again(y/n)?').lower()
    if play_again =='y':
        screen.clear()
        play_snake()


play_snake()


screen.exitonclick()