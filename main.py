# Snake game
# Created using the turtle graphics library
# 19/06/2023

from turtle import Turtle, Screen
from snake import Snake
import time

# Screen set up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


# screen.exitonclick()
