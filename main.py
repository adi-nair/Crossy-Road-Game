from turtle import Screen
from scoreboard import Scoreboard
from car_manager import CarManager
from player import Player
import time

screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.tracer(0)

board = Scoreboard()

player = Player()
screen.listen()
screen.onkey(player.move, "Up")
car = CarManager()

is_game = True
while is_game:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    # if y position top of screen then go to starting position
    if player.ycor() >= 280:
        player.restart()
        board.increase_level()
        board.update()
        car.increase_speed()

    # Collision with cars
    for new_car in car.all_cars:
        if new_car.distance(player) < 20:
            is_game = False
            board.game_over()

screen.exitonclick()
