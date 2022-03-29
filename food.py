from turtle import Turtle
import random
# We are going to make food subclass of Turtle class


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('yellow')
        self.penup()
        self.refresh_food()

    def refresh_food(self):
        coor_x = random.randrange(-280, 280)
        coor_y = random.randrange(-280, 280)
        self.goto(coor_x, coor_y)
