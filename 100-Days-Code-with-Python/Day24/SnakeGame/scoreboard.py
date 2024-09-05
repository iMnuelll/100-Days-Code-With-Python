from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

# Relative Path -> Day24/100-Days-Code-With-Python/100-Days-Code-With-Python/data.txt == "../../../data.txt"
# Absolute Path -> "100-Days-Code-With-Python/data.txt"
file = "100-Days-Code-With-Python/data.txt"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        with open(file) as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def reset(self) :
        if self.score > self.high_score :
            self.high_score = self.score
            with open(file, "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)
    
    def ask_user(self) :
        self.goto(0, -20)
        self.write("Press ENTER to play again.", align=ALIGNMENT, font=FONT)
        self.write("Click the screen to leave the game!", align=ALIGNMENT, font=FONT)