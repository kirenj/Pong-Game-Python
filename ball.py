from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("circle")
    # here if the ball size is 20, we calculate it as 0.5
    self.shapesize(stretch_len=0.5, stretch_wid=0.5)
    self.penup()
    self.color("white")
    self.x_move = 10
    self.y_move = 10

  def move(self):    
    x_cor = self.xcor() + self.x_move
    y_cor = self.ycor() + self.y_move
    self.goto(x=x_cor, y=y_cor)

  def bounce(self):
    self.y_move *= -1
    