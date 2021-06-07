from turtle import Turtle

WIDTH = 5
HEIGHT = 1
RIGHT_PADDLE = (350, 0)
LEFT_PADDLE = (-350, 0)


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        if pos == 'right':
            self.goto(RIGHT_PADDLE)
        elif pos == 'left':
            self.goto(LEFT_PADDLE)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
