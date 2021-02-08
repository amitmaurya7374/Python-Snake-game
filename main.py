"""Today we learn about a creating a snake game """
import time

"""To fix a catepillar effect we will use tracer() method to stop a animation and then after all the segment draw we 
will update our screen using a update mehtod """
import turtle
from snake import Snake

# created an object
screen = turtle.Screen()

'''setup a screen'''
screen.setup(width=600, height=600)  # width and height of a screen
screen.bgcolor("black")  # background color of a screen
screen.title("Snake Game")
screen.tracer(0)  # not will show on a screen until we update
screen.listen()  # listen for keybordstokes

snake = Snake()

screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)
is_game_is_on = True
while is_game_is_on:
    screen.update()  # update a screen to show a snake moving
    time.sleep(0.6)
    snake.move()
screen.exitonclick()
