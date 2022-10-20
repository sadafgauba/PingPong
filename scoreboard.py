from turtle import Turtle
from game_area import GameArea

SCOREBOARD_COLOR = "yellow"
ALIGNMENT = 'center'
FONT = ('Arial', 50, 'normal')
PENCOLOR = "white"

class ScoreBoard:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.score = 0
        self.scorepen = Turtle()
        self.scorepen.hideturtle()
        self.scorepen.color(PENCOLOR)
        self.scorepen.penup()
        self.scorepen.color(SCOREBOARD_COLOR)

    def display_score(self):
        self.scorepen.clear()
        self.scorepen.goto(-70, GameArea().SCREEN_HEIGHT / 2 - 100)
        self.scorepen.write(f"{self.user_score}", align=ALIGNMENT, font=FONT)
        self.scorepen.goto(70, GameArea().SCREEN_HEIGHT / 2 - 100)
        self.scorepen.write(f"{self.computer_score}", align=ALIGNMENT, font=FONT)

    def increment_user_score(self):
        self.user_score += 1

    def increment_computer_score(self):
        self.computer_score += 1

    # may not need this one
    def show_winner(self):
        if self.user_score > self.computer_score:
            pass  # display user as winner
        elif self.user_score < self.computer_score:
            pass  # display computer as winner
        else:
            pass  # show tie
