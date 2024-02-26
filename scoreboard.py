from turtle import Turtle


class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.penup()
    self.color("White")
    self.hideturtle()
    self.l_score = 0
    self.r_score = 0
    

  def score_board(self):
    self.clear()
    #For the left score board
    self.goto(x=-100, y=210)    
    self.write(self.l_score, align='center', font=('Courier', 50, 'bold'))
    #For the right score board
    self.goto(x=100, y=210)    
    self.write(self.r_score, align='center', font=('Courier', 50, 'bold'))
    

  def left_score(self):
    self.l_score += 1

  def right_score(self):
    self.r_score += 1