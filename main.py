from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)


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
  time.sleep(0.1)
  ball.move()
  
  if ball.ycor() > 250:
    ball.bounce()







screen.exitonclick()