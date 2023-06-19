# Snake game
# Created using the turtle graphics library
# 19/06/2023

from turtle import Turtle, Screen
import time

# Screen set up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Starting postions
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

# Creating the snake
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(1)
    for seg in segments:
        seg.forward(20)

screen.exitonclick()
