from turtle import Turtle


class Paddle(Turtle):  

  def __init__(self, x_pos, y_pos):
    super().__init__()    
    self.shape("square")
    self.color("white")
    # self.resizemode("user")
    self.shapesize(stretch_len=0.5, stretch_wid=2.5)
    self.penup()
    self.goto(x_pos, y_pos)
    self.speed(0)

  def up(self):     
    if self.ycor() < 270: 
      self.goto(x=self.xcor(), y=self.ycor() + 20)      
    
  def down(self):    
    if self.ycor() > -270:
      self.goto(x=self.xcor(), y=self.ycor() - 20)
      