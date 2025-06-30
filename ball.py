from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speedy = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def pad_bounce(self):
        self.x_move *= -1
        self.speedy *= 0.9  # multiply the 0.1 by 0.9 to slightly decrease and not get a negative

    def reset_position(self):
        self.goto(0, 0)
        self.speedy = 0.1
        self.pad_bounce()
        # we want it to reverse its direction.
        # This is basically for the paddle that misses it
        # Not necessarily only for the paddle but was initially used for it that why it's called pad_









