from turtle import *
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.initial_score = 0
        self.hideturtle()
        self.penup()
        self.sety(270)
        self.write(f"Score: {self.initial_score}", False , align="center", font=10)
    def update_score(self):
        self.clear()
        self.initial_score+=1
        self.write(f"Score: {self.initial_score}", False, align="center", font=10)
    def game_over(self):
        self.goto(0,0)
        self.write("Game over", False, align="center", font=10)

