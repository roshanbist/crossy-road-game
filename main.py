from turtle import Screen
import time

from player import Player
from car import Car
from levelboard import Levelboard
from roadDivider import RoadDivider


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("gray")
screen.tracer(0)
game_player = Player()
car = Car()
levelboard = Levelboard()
divider = RoadDivider()


game_on = True
screen.listen()

screen.onkeypress(game_player.move_up, 'Up')


def is_collision(player, cars):
    for ca in cars:
        if ca.distance(player) < 25:
            return True


while game_on:
    screen.update()
    time.sleep(0.1)

    car.create_ltr_side_car()
    car.create_rtl_side_car()
    car.move_car()

    if is_collision(game_player, car.left_lane_cars) or is_collision(game_player, car.right_lane_cars):
        game_on = False
        levelboard.game_over()

    if game_player.ycor() >= 280:
        game_player.goto(0, -280)
        levelboard.score += 1
        levelboard.increase_level()
        car.increase_speed()

screen.exitonclick()
