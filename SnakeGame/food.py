import turtle as t
import random

class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("violet")
        self.speed("fastest")
        self.goto(x=random.randint(-280,280),y=random.randint(-280,280))

    def refresh(self):
        new_x=random.randint(-280,280)
        new_y=random.randint(-280,280)
        self.goto(new_x,new_y)

