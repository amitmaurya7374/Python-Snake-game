"""This class handle a scroe of food which snake eats"""
from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 18, "normal")


class ScoreBoard(Turtle):
    """This class keep a record of score player has."""

    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=250)
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """This function write a score on a screen"""
        self.write(arg=f"Score {self.score}", align=ALIGN, font=FONT)

    def increment_score(self):
        """This function increment a score """
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """Game Over Message"""
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGN, font=FONT)
