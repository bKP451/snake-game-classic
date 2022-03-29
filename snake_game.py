from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import turtle
window = Screen()
window.title("Classical Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600, startx=700)
game_end = False
window.tracer(0)  # Turtle animation is made off
scoreboard = Scoreboard()
snake = Snake()
food = Food()

window.listen()  # Set focuses on TurtleScreen to collect key-events
window.onkey(fun=snake.up, key="Up")
window.onkey(fun=snake.down, key="Down")
window.onkey(fun=snake.left, key="Left")
window.onkey(fun=snake.right, key="Right")
while not game_end:
    window.update()
    time.sleep(0.2)  # suspend execution of a calling thread for the requested number of seconds
    # time.sleep() is vital for this program
    snake.move()  # It is just changing the coordinates
    if snake.head.distance(food) < 15:
        scoreboard.ink_the_board()
        food.refresh_food()
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 285 or snake.head.ycor() < -300:
        game_end = True
        scoreboard.game_over()


window.exitonclick()