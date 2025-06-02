from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.setheading(90)
        self.goto(0, -280)

    def move_up(self):
        if self.ycor() < 280:
            self.forward(10)