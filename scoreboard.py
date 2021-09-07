from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-160, 260)
        self.update()

    def increase_level(self):
        self.level += 1

    def update(self):
        self.clear()  # to prevent overight
        self.write(f"Level: {self.level} ", False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=FONT)
