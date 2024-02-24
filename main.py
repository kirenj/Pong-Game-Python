from turtle import Screen
from paddle import Right_Paddle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.listen()


rt_paddle = Right_Paddle()

#Key binding
screen.onkey(rt_paddle.up, key= "Up")
screen.onkey(rt_paddle.down, key= "Down")








screen.exitonclick()