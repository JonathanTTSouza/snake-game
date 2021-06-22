from turtle import Turtle

FONT = ("Arial", 20, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setposition(x=0, y=260)
        self.pencolor("white")
        self.hideturtle()
        self.write(f"Scoreboard: {self.score}", align=ALIGNMENT, font=FONT)

    def on_food_get(self):
        self.score += 1
        self.clear()
        self.write(f"Scoreboard: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

