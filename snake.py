"""This will handle all the functionality of snake related"""
from turtle import Turtle

STARTING_POSITION_OF_TURTLE = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """This snake class darw a snake and move a snake on screen.\nBy calling move() methods"""

    def __init__(self):
        # self.turtle = Turtle(shape="square")
        self.segment = []  # as soon as we create an object this code will always run
        self.create_snack()  # this method call immediately whenever we create an object from this class
        self.head = self.segment[0]

    def create_snack(self):
        """This function will create a initial snake at 0,0 position"""
        for position in STARTING_POSITION_OF_TURTLE:
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(position)
            self.segment.append(turtle)

    def move(self):
        """This function help snake to move """
        for seg_num in range(len(self.segment) - 1, 0, -1):
            """Logic a that we moving last elemnt to second and second element to first element postion"""
            new_x = self.segment[seg_num - 1].xcor()  # getting coordinates
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def move_up(self):
        """Move a snake upward direction"""
        if self.head.heading() != DOWN:
            # to prevent backward because in offical snake game we do not got backward
            self.head.setheading(UP)  # changing head of a turtle

    def move_down(self):
        """Moving a snake to downward direction"""
        if self.head.heading() != UP:
            # to prevent backward because in offical snake game we do not got backward
            self.head.setheading(DOWN)

    def move_left(self):
        """Moving a snake to left direction"""
        if self.head.heading() != RIGHT:
            # to prevent backward because in offical snake game we do not got backward
            self.head.setheading(LEFT)

    def move_right(self):
        """Moving a snake to right direction"""
        if self.head.heading() != LEFT:
            # to prevent backward because in offical snake game we do not got backward
            self.head.setheading(RIGHT)
