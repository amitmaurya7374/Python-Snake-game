"""Today we learn about a creating a snake game """
import time

"""To fix a catepillar effect we will use tracer() method to stop a animation and then after all the segment draw we 
will update our screen using a update mehtod """

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# created an object
screen = Screen()

'''setup a screen'''
screen.setup(width=600, height=600)  # width and height of a screen
screen.bgcolor("black")  # background color of a screen
screen.title("Snake Game")
screen.tracer(0)  # not will show on a screen until we update
screen.listen()  # listen for keybordstokes

snake = Snake()  # created an snake object
food = Food()  # created a food class object
scoreborad = ScoreBoard()

screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)
is_game_is_on = True
while is_game_is_on:
    screen.update()  # update a screen to show a snake moving
    time.sleep(0.3)
    snake.move()
    #     Detect a collosion of snake with food .we use distance method for this
    if snake.head.distance(food) < 15:
        food.food_new_location()
        snake.extend()
        scoreborad.increment_score()
    # Detect a collosion if snake with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_is_on = False
        scoreborad.game_over()
    #     Detect snake head collison
    for segment in snake.segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_game_is_on = False
            scoreborad.game_over()
screen.exitonclick()
