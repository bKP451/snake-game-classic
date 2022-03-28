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

    for segment in range(len(snakes)-1, 0, -1):
        # here n(last item) will move to (n-1) segment's coordinates, (n-1) will move to (n-2) segment's
        # coordinates and so on (n-2)..(n-3)....2..1(first segment of the  snake which is HEAD of snake)
        x_cor_new = snakes[segment-1].xcor()
        y_cor_new = snakes[segment-1].ycor()
        snakes[segment].goto(x_cor_new, y_cor_new)
    snakes[0].backward(20)
    snakes[0].right(90)


window.exitonclick()