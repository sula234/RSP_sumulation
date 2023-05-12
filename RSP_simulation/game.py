from turtle import Screen
import turtle
import os
from rsp import Object
import random
import time 


def register_images() -> None:
    for image in os.listdir('images'):
        # additional checks for Mac users
        if image == '.DS_Store':
            continue
        turtle.register_shape(os.path.join('images', image))


class Game:

    def __init__(self, object_num=None, width=800, height=566, title="RSP") -> None:
        essences = ['rock', 'paper', 'scissors']

        self.width = width
        self.height = height

        # initialize images in turtle module
        register_images()

        # set screen settings
        self.screen = Screen()
        self.screen.bgpic(os.path.join('images', 'background.gif'))
        self.screen.setup(width=width, height=height)
        self.screen.title(title)
        self.screen.tracer(0)

        # add random objects
        if object_num is None:
            self.objects = [Object(essences[random.randint(0, 2)]) for _ in range(random.randint(15, 30))]
        else:
            self.objects = [Object(essences[random.randint(0, 2)]) for _ in range(object_num)]

    # this method can be used to add objects in real time
    def add_object(self, essence: str) -> None:
        self.objects.append(Object(essence))

    def start(self) -> None:
        game_is_on = True
        while game_is_on:
            self.screen.update()
            time.sleep(0.001)

            for obj in self.objects:
                obj.move()

                # Detect collision with wall
                if obj.ycor() > (self.height/2 - 20) or obj.ycor() < -(self.height/2 - 20):
                    obj.bounce_y()

                if obj.xcor() > (self.width/2 - 20):
                    obj.bounce_x()

                if obj.xcor() < -(self.width/2 - 20):
                    obj.bounce_x()

                if self.is_collision(obj):
                    obj.bounce_x()
                    obj.bounce_y()

        self.screen.exitonclick()

    def is_collision(self, a: Object) -> bool:
        collision = False
        for b in self.objects:
            if a is b:
                continue

            if abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10:
                if a.essence == 'scissors' and b.essence == 'rock':
                    a.essence = 'rock'
                    a.shape(os.path.join('images', 'rock' + '.gif'))

                if a.essence == 'rock' and b.essence == 'paper':
                    a.essence = 'paper'
                    a.shape(os.path.join('images', 'paper' + '.gif'))

                if a.essence == 'paper' and b.essence == 'scissors':
                    a.essence = 'scissors'
                    a.shape(os.path.join('images', 'scissors' + '.gif'))

                a.move_speed = 0
                b.move_speed = 0
                collision = True

        return collision

    def set_default_bgpic(self):
        self.screen.bgcolor('white')
        self.screen.bgpic('nopic')
