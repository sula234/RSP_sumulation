import turtle
import os
import random


class Object(turtle.Turtle):

    def __init__(self, essence: str) -> None:
        super().__init__()
        self.essence = essence
        essence_path = os.path.join('images', essence + '.gif')
        self.shape(essence_path)
        self.penup()
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 0.1
        self.setpos(random.randint(-300, 300), random.randint(-200, 200))

    def move(self) -> None:
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self) -> None:
        self.y_move *= -1
        self.move_speed = 0.9

    def bounce_x(self) -> None:
        self.x_move *= -1
        self.move_speed = 0.9


