from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


def colors():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.create_car()
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 7)
        if chance == 6:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.color(colors())
            car.turtlesize(stretch_wid=1, stretch_len=2, outline=None)
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
