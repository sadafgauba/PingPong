from game_area import GameArea
from pedal import Pedal
from scoreboard import ScoreBoard
import time
from ball import Ball

game = GameArea()
screen = game.setup()

pedal = Pedal()
first_player_pedal = pedal.create_first_player_pedal()
second_player_pedal = pedal.create_second_player_pedal()

ball = Ball()
ball.create_ball()

scoreboard = ScoreBoard()
scoreboard.display_score()
winning_score = 7
while True:
    scoreboard.display_score()
    screen.update()
    time.sleep(0.01)
    pedal.move_first_player_pedal(screen)
    pedal.move_second_player_pedal(screen)
    ball_missed = ball.detect_LF_boundary_collision()
    if ball_missed == 'user':
        scoreboard.increment_computer_score()
        if scoreboard.computer_score == winning_score:
            print("Winner is Second Player!!")
            break
        pedal.game_restart()
        ball.game_restart()
    elif ball_missed == 'comp':
        scoreboard.increment_user_score()
        if scoreboard.user_score == winning_score:
            print("Winner is First Player!!")
            break
        pedal.game_restart()
        ball.game_restart()
    ball.ball_move()
    ball.detect_TB_boundary_collision()
    ball.detect_fp_pedal_collision(first_player_pedal)
    ball.detect_sp_pedal_collision(second_player_pedal)

screen.exitonclick()
