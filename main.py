# Snake game
# Created using the turtle graphics library
# 19/06/2023

from turtle import Turtle, Screen

# Screen set up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Starting postions
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# Creating the snake
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)


screen.exitonclick()
