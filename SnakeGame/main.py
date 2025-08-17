import turtle as t
import snake as sn
import food as f
import time
import scoreboard as sb

screen=t.Screen()
screen.setup(height=600,width=600)
screen.bgcolor("beige")
screen.title("Harshita's Snake Game")
screen.tracer(0)

snake=sn.Snake()
food=f.Food()
scoreboard=sb.ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.inc_score()

    #Detect collision with wall
    if snake.head.xcor()>285 or snake.head.xcor()<-285 or snake.head.ycor()>285 or snake.head.ycor()<-285:
        scoreboard.reset()
        scoreboard.save_highscore()
        snake.reset()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            scoreboard.save_highscore()
            snake.reset()

screen.exitonclick()

