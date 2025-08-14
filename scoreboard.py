from turtle import Turtle
FONT = ('Broadway', 15, 'normal')
ALIGNMENT = "left"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("olive")
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
