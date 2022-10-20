from game_area import GameArea
from turtle import Turtle
import game_area
import time

BALL_SHAPE = "circle"
BALL_COLOR = "lightgreen"
BALL_SIZE = 1


class Ball:
    def __init__(self):
        self.ball = None

    def create_ball(self):
        self.ball = Turtle()
        self.ball.shape(BALL_SHAPE)
        self.ball.color(BALL_COLOR)
        self.ball.penup()
        self.ball.shapesize(BALL_SIZE)
        self.game_restart()

    def ball_move(self):
        self.ball.forward(5)

    def detect_LF_boundary_collision(self):
        user_comp = None
        if self.ball.xcor() < -game_area.SCREEN_WIDTH / 2 - 10:
            user_comp = 'user'
        elif self.ball.xcor() > game_area.SCREEN_WIDTH / 2 - 10:
            user_comp = 'comp'
        return user_comp

    def game_restart(self):
        self.ball.setheading(45)
        self.ball.goto(0, 0)

    def detect_TB_boundary_collision(self):
        if self.ball.ycor() > game_area.SCREEN_HEIGHT / 2 - 20:
            if self.ball.heading() == 45:
                self.ball.setheading(315)
            elif self.ball.heading() == 135:
                self.ball.setheading(225)
        elif self.ball.ycor() < -game_area.SCREEN_HEIGHT / 2 + 25:
            if self.ball.heading() == 225:
                self.ball.setheading(135)
            elif self.ball.heading() == 315:
                self.ball.setheading(45)

    def detect_fp_pedal_collision(self, fp_pedal):
        if self.ball.distance(fp_pedal) < 40:
            if self.ball.heading() == 225:
                self.ball.setheading(315)
            elif self.ball.heading() == 135:
                self.ball.setheading(45)

    def detect_sp_pedal_collision(self, sp_pedal):
        if self.ball.distance(sp_pedal) < 40:
            if self.ball.heading() == 315:
                self.ball.setheading(225)
            elif self.ball.heading() == 45:
                self.ball.setheading(135)
