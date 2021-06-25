from turtle import Turtle

FONT = ("Arial", 20, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            high_score = file.read()
        self.high_score = int(high_score)
        self.setposition(x=0, y=260)
        self.pencolor("white")
        self.hideturtle()
        self.write(f"Scoreboard: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Scoreboard: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

