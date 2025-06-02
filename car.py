from turtle import Turtle
import random

COLORS = ["red", "green", "blue", "orange", "yellow", "purple"]
STEP = 5
INITIAL_POS = 300


class Car:
    def __init__(self):
        self.left_lane_cars = []
        self.right_lane_cars = []

        self.create_ltr_side_car()
        self.create_rtl_side_car()
        self.speed = STEP

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        return new_car

    def create_ltr_side_car(self):
        random_chance = random.randint(1, 10)

        if random_chance == 1:
            position_y = random.randint(20, 250)
            new_ltr_car = self.create_car()
            new_ltr_car.goto(-300, position_y)
            self.left_lane_cars.append(new_ltr_car)

    def create_rtl_side_car(self):
        random_chance = random.randint(1, 10)

        if random_chance == 1:
            position_y = random.randint(-250, -20)
            new_rtl_car = self.create_car()
            new_rtl_car.goto(300, position_y)
            self.right_lane_cars.append(new_rtl_car)

    def move_car(self):
        for car in self.left_lane_cars:
            car.forward(self.speed)

        for car in self.right_lane_cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += 5
