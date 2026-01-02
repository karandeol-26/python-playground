from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def segmemts(self):
        return self.segments

    def up(self):
        direction = self.segments[0].heading()
        if direction == 0 or direction == 180:
            self.head.setheading(90)
        else:
            pass

    def down(self):
        direction = self.segments[0].heading()
        if direction == 0 or direction == 180:
            self.head.setheading(270)
        else:
            pass

    def left(self):
        direction = self.segments[0].heading()
        if direction == 90 or direction == 270:
            self.head.setheading(180)
        else:
            pass

    def right(self):
        direction = self.segments[0].heading()
        if direction == 90 or direction == 270:
            self.head.setheading(0)
        else:
            pass

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
