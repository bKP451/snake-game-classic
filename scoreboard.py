from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.ink_the_board()

    def ink_the_board(self):
        """It increases the score of  the player."""
        # I must clear the screen before re-writing on otherwise the score appears blur
        self.clear()
        self.write(f"SCORE :  {self.score} ", align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        """It prints the GAME OVER tag."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)