from turtle import Turtle
MOVE_AMOUNT = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up_r(self):
        new_y = self.ycor() + MOVE_AMOUNT
        self.goto(self.xcor(), new_y)

    def go_down_r(self):
        new_y = self.ycor() - MOVE_AMOUNT
        self.goto(self.xcor(), new_y)

    def go_up_l(self):
        new_y = self.ycor() + MOVE_AMOUNT
        self.goto(self.xcor(), new_y)

    def go_down_l(self):
        new_y = self.ycor() - MOVE_AMOUNT
        self.goto(self.xcor(), new_y)
