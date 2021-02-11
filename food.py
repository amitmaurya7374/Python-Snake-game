"""This class handle a food of a snake all about a food """
import random
from turtle import Turtle


# Inherit a Turtle class
class Food(Turtle):
    """This class generate a food for snake.That change a position everytime a snake hit a food randomly"""

    def __init__(self):
        """All this things come from a turtle class and this will initilize automatically as soon as a New object is
        created """
        super(Food, self).__init__()
        #         Now I can used Turtle class attributes and methods
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # change a size of shape
        self.color("blue")
        self.speed("fastest")
        rand_x_coor = random.randint(-280, 280)  # generate random coordinates
        rand_y_coor = random.randint(-280, 280)
        self.goto(rand_x_coor, rand_y_coor)
        self.food_new_location()

    def food_new_location(self):
        """This will set a turtle on new location randomly."""
        rand_x_coor = random.randint(-280, 280)  # generate random coordinates
        rand_y_coor = random.randint(-280, 280)
        self.goto(rand_x_coor, rand_y_coor)