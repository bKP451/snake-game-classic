from turtle import Screen, Turtle
import time
from snake import Snake
import turtle
window = Screen()
window.title("Classical Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600, startx=700)
game_end = False
window.tracer(0)  # Turtle animation is made off
snake = Snake()

window.listen()  # Set focuses on TurtleScreen to collect key-events
window.onkey(fun=snake.up, key="Up")
window.onkey(fun=snake.down, key="Down")
window.onkey(fun=snake.left, key="Left")
window.onkey(fun=snake.right, key="Right")
while not game_end:
    window.update()
    time.sleep(0.2)  # suspend execution of a calling thread for the requested number of seconds
    # time.sleep() is vital for this program
    snake.move()


window.exitonclick()