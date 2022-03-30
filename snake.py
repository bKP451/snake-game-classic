from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POSITION = ((0, 0), (-20, 0), (-40, 0))


class Snake:
    def __init__(self):
        self.snakes_list = []
        self.create_snake()
        self.head = self.snakes_list[0]

    def create_snake(self):
        """It creates the snake at the initial state of the program"""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds individual segment to the snake list"""
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.snakes_list.append(new_segment)

    def extend_segment(self):
        """It increases the size of the snake by one square"""
        self.add_segment(self.snakes_list[-1].pos())

    def move(self):
        """move() method changes the coordinates. Head moves by 20 paces in direction of setheading()
        other squares go to preceding square's position
        """
        for segment in range(len(self.snakes_list) - 1, 0, -1):
            # here n(last item) will move to (n-1) segment's coordinates, (n-1) will move to (n-2) segment's
            # coordinates and so on (n-2)..(n-3)....2..1(first segment of the  snake which is HEAD of snake)
            x_cor_new = self.snakes_list[segment - 1].xcor()
            y_cor_new = self.snakes_list[segment - 1].ycor()
            self.snakes_list[segment].goto(x_cor_new, y_cor_new)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


