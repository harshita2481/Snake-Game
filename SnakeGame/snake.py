import turtle as t
Starting_pos=[(0,0),(-20,0),(-40,0)]
move_distance=20
up=90
down=270
left=180
right=0

class Snake:
    def __init__(self):
       self.segments=[]
       self.create_snake()
       self.head=self.segments[0]
       
    def create_snake(self):
        for position in Starting_pos:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment=t.Turtle("square")
        new_segment.color("red")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
        pass

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg-1].xcor()
            new_y=self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.segments[0].forward(move_distance)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

    def up(self):
        if self.head.heading()!=down:
            self.head.setheading(up)
        pass
    def down(self):
        if self.head.heading()!=up:
            self.head.setheading(down)
        pass
    def left(self):
        if self.head.heading()!=right:
            self.head.setheading(left)
        pass
    def right(self):
        if self.head.heading()!=left:   
            self.head.setheading(right)
        pass