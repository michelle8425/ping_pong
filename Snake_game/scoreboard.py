from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier', 24, 'normal')
FOT = ('Courier', 30, 'normal')
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.high_score = 0
        self.penup()
        self.goto(0, 250)
        self.ht()
        self.writing_up()

    def writing_up(self):
        self.clear()
        self.write(f"Score = {self.score} High_Score = {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.writing_up()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align= ALIGN, font= FOT)

    def scoring(self):
        self.score += 1
        self.writing_up()




