from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
class ScoreBoard(Turtle):
    def __init__(self,score):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,300)
        self.color("white")
        self.write(f"Score: {score}",move = False, align=ALIGNMENT,  font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",move = False, align=ALIGNMENT,  font= FONT)


    
