from turtle import Screen, Turtle
import time
import turtle
window = Screen()
window.title("Classical Snake Game")
window.bgcolor("black")
window.setup(width=600, height=600, startx=700)
snakes = list()  # Creation of an empty list
x_cor = 0
game_end = False
window.tracer(0)  # Turtle animation is made off
for i in range(3):
    snakes.append(Turtle(shape='square'))
    snakes[i].color('white')
    snakes[i].penup()
    snakes[i].goto(x=x_cor, y=0)
    x_cor -= 20


while not game_end:
    window.update()
    time.sleep(1)  # suspend execution of a calling thread for the requested number of seconds
    # time.sleep() is vital for this program
    for segment in snakes:
        segment.forward(20)
        print(segment.xcor())
        print(f"Heading is {segment.heading()}")
    # snakes[1].right(90)
window.exitonclick()