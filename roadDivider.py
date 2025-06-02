from turtle import Turtle


class RoadDivider(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=0.2, stretch_len=1)
        self.color("orange")
        self.goto(-300, 0)
        self.create_divider()

    def create_divider(self):
        for _ in range(15):
            self.stamp()
            self.goto(self.xcor() + 40, self.ycor())
