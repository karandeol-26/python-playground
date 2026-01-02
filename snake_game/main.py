import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = t.Screen()
screen.screensize(600,600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)



snake = Snake()
food = Food()
score = 0
scoreboard = ScoreBoard(score)



screen.listen()
screen.onkey(fun= snake.up, key="Up")
screen.onkey(fun= snake.down, key= "Down")
screen.onkey(fun= snake.left, key= "Left")
screen.onkey(fun= snake.right, key= "Right")

screen.update()
time.sleep(1)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score+= 1
        scoreboard.clear()
        scoreboard = ScoreBoard(score)
        snake.extend()
    if snake.head.xcor()>345 or snake.head.xcor()< -345:
        game_is_on = False
        scoreboard.game_over()
    elif snake.head.ycor()>345 or snake.head.ycor()< -345:
        game_is_on = False
        scoreboard.game_over()

    for segments in snake.segments[1:]:
        if snake.head.distance(segments)<10:
            game_is_on = False
            scoreboard.game_over()

        
screen.exitonclick()    


