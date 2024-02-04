#Modules
from turtle import *
import time
from snake import Snake
from food import Food
from scoreboard import *
#Setting up screen
scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("wheat")
scr.title("Snake Game")
scr.tracer(0)
snake = Snake()
food = Food()
sb = Scoreboard()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")


game_is_on = True

while game_is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()
    #detecting collision
    if snake.head.distance(food) < 15:
        food.refresh()
        sb.update_score()
        snake.extend()
    #detecting collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        sb.game_over()
    #detecting collision with tail

    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            sb.game_over()

scr.exitonclick()
