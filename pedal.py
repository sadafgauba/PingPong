from turtle import Turtle
import time
import game_area
from game_area import GameArea

FILL_COLOR = "orange"
SHAPE = "square"


def create_pedal():
    pedal = Turtle()
    pedal.color(FILL_COLOR)
    pedal.shape(SHAPE)
    pedal.penup()
    pedal.speed(10)
    pedal.shapesize(stretch_len=5, stretch_wid=2)
    pedal.setheading(90)

    return pedal


class Pedal:

    def __init__(self):
        self.screen = None
        self.first_player_pedal = None
        self.second_player_pedal = None
        self.first_player_top_border = None
        self.first_player_bottom_border = None
        self.second_player_top_border = None
        self.second_player_bottom_border = None
        self.second_player_going_up = True

    def create_first_player_pedal(self):
        self.first_player_pedal = create_pedal()
        self.first_player_pedal.goto(-game_area.SCREEN_WIDTH / 2, 0)
        self.first_player_pedal.speed(10)
        return self.first_player_pedal

    def create_second_player_pedal(self):
        self.second_player_pedal = create_pedal()
        self.second_player_pedal.goto(game_area.SCREEN_WIDTH / 2 - 5, 0)
        self.second_player_pedal.speed(10)
        return self.second_player_pedal

    def game_restart(self):
        self.first_player_pedal.goto(-game_area.SCREEN_WIDTH / 2, 0)
        self.second_player_pedal.goto(game_area.SCREEN_WIDTH / 2 - 5, 0)

    def fp_up(self):
        if self.first_player_pedal.ycor() < game_area.SCREEN_HEIGHT/2 - 50:
            self.first_player_pedal.forward(50)

    def fp_down(self):
        if self.first_player_pedal.ycor() > -game_area.SCREEN_HEIGHT/2 + 50:
            self.first_player_pedal.backward(50)

    def sp_up(self):
        if self.second_player_pedal.ycor() < game_area.SCREEN_HEIGHT/2 - 50:
            self.second_player_pedal.forward(50)

    def sp_down(self):
        if self.second_player_pedal.ycor() > -game_area.SCREEN_HEIGHT/2 + 50:
            self.second_player_pedal.backward(50)

    def move_first_player_pedal(self, screen):
        self.screen = screen
        self.screen.listen()
        self.screen.onkey(self.fp_up, "w")
        self.screen.onkey(self.fp_down, "s")

    def move_second_player_pedal(self, screen):
        self.screen = screen
        self.screen.listen()
        self.screen.onkey(self.sp_up, "Up")
        self.screen.onkey(self.sp_down, "Down")