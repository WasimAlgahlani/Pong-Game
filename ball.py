from turtle import Turtle

WIDTH = 1
HEIGHT = 1


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=WIDTH, stretch_len=HEIGHT)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1
        self.increase_speed()

    def bounce_x(self):
        self.x_move *= -1
        self.increase_speed()

    def increase_speed(self):
        self.ball_speed *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
