from turtle import Turtle


class Right_Paddle(Turtle):  

  def __init__(self):
    super().__init__()    
    self.shape("square")
    self.color("white")
    # self.resizemode("user")
    self.shapesize(stretch_len=0.5, stretch_wid=2.5)
    self.penup()
    self.goto(x=350, y=0)
    self.speed(0)

  def up(self):     
    if self.ycor() < 270: 
      self.goto(x=350, y=self.ycor() + 20)      
    
  def down(self):    
    if self.ycor() > -270:
      self.goto(x=350, y=self.ycor() - 20)
      