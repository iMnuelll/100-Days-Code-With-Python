from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 12, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        
    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGN, font=FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGN, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.update_score()