from turtle import Turtle, Screen

BACKGROUND_COLOR = "black"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Ping Pong"
PARTITION_COLOR = "blue"
PENSIZE = 10


def create_boundary(position):
    boundary = Turtle()
    boundary.penup()
    boundary.shape('square')
    boundary.color("white")
    if position == 'top':
        boundary.shapesize(stretch_len=SCREEN_WIDTH / 20, stretch_wid=0.5)
        boundary.goto(0, SCREEN_HEIGHT / 2)
    elif position == 'bottom':
        boundary.shapesize(stretch_len=SCREEN_WIDTH / 20, stretch_wid=0.5)
        boundary.goto(0, -SCREEN_HEIGHT / 2)
    elif position == 'left':
        boundary.shapesize(stretch_len=0.5, stretch_wid=SCREEN_WIDTH / 20)
        boundary.goto(-SCREEN_WIDTH / 2, 0)
    elif position == 'right':
        boundary.shapesize(stretch_len=0.5, stretch_wid=SCREEN_WIDTH / 20)
        boundary.goto(SCREEN_WIDTH / 2, 0)
    # boundary.hideturtle()
    return boundary


class GameArea:

    def __init__(self):
        self.screen = None
        self.partition = None
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.left_boundary = None
        self.right_boundary = None
        self.top_boundary = None
        self.bottom_boundary = None

    def setup(self):
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor(BACKGROUND_COLOR)
        self.screen.title(SCREEN_TITLE)
        self.screen.tracer(0)

        self.partition = Turtle()
        self.partition.color(PARTITION_COLOR)
        self.partition.setheading(270)
        self.partition.penup()
        self.partition.goto(0, SCREEN_HEIGHT/2 - 10)
        self.partition.pensize(PENSIZE)
        is_pen_up = False
        while self.partition.distance(0, -SCREEN_HEIGHT/2) > 40:
            if is_pen_up:
                is_pen_up = False
                self.partition.pendown()
                self.partition.forward(20)
            else:
                is_pen_up = True
                self.partition.penup()
                self.partition.forward(20)
        self.partition.hideturtle()

        return self.screen

    def create_boundaries(self):
        self.top_boundary = create_boundary('top')
        self.bottom_boundary = create_boundary('bottom')
        self.left_boundary = create_boundary('left')
        self.right_boundary = create_boundary('right')
        return self.top_boundary, self.bottom_boundary, self.left_boundary, self.right_boundary




