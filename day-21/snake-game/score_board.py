from turtle import Turtle

SCORE_X_POSITION = 0
SCORE_Y_POSITION = 270
ALIGNMENT = 'center'
FONT = ('Ariel', 18, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(SCORE_X_POSITION, SCORE_Y_POSITION)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
