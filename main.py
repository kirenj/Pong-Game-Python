from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

scoreboard = Scoreboard()



rt_paddle = Paddle(x_pos=350, y_pos=0)
lt_paddle = Paddle(x_pos=-350, y_pos=0)
ball = Ball()

#Key binding
screen.listen()
screen.onkey(rt_paddle.up, key= "Up")
screen.onkey(rt_paddle.down, key= "Down")
screen.onkey(lt_paddle.up, key= "w")
screen.onkey(lt_paddle.down, key= "s")

game_on = True

while game_on is True:
  screen.update()
  time.sleep(ball.move_speed)
  ball.move()
  scoreboard.score_board()
  
  #Detect collision with top and bottom walls
  if ball.ycor() > 250 or ball.ycor() < -250:
    ball.bounce()

  #Detect collision with right paddle and left paddle
  if ball.xcor() >= 330 and ball.distance(rt_paddle) < 36 or ball.distance(lt_paddle) < 36 and ball.xcor() <= -330:    
    ball.bounce_paddle()

  #Detect if the paddles miss the ball
  if ball.xcor() >= 360:    
    ball.restart_left()
    scoreboard.left_score()
    
  
  if ball.xcor() <= -360:
    ball.restart_right()
    scoreboard.right_score()
    
    







screen.exitonclick()