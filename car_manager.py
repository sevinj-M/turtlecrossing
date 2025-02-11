from turtle import Turtle 
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.shapesize(1, 2)
        self.penup()
        self.left(180)
        self.speed = speed
        y_cor = random.randint(-200, 200)
        self.goto(300, y_cor)
        

    def move(self):
        self.forward(self.speed)