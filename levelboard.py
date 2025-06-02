from turtle import Turtle


class Levelboard(Turtle):
    FONT = ("Courier", 10, 'normal')
    ALIGN = "center"

    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-250, 280)
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.write(f"Level: {self.score}", align=self.ALIGN, font=self.FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=self.ALIGN, font=self.FONT)
