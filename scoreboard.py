from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"SCORE: {self.score}", align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
