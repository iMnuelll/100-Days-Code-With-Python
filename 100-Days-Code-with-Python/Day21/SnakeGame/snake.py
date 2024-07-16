from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        
    def add_segment(self, position) :
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_X = self.segments[seg - 1].xcor()
            new_Y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_X, new_Y)
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:  # Prevents the snake from reversing
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:  # Prevents the snake from reversing
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:  # Prevents the snake from reversing
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:  # Prevents the snake from reversing
            self.head.setheading(RIGHT)
        
    def extend(self) :
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].xcor() + MOVE_DISTANCE, self.segments[-1].ycor())
        self.segments.append(new_segment)
    
    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head.goto(0, 0)
        self.head.direction = "stop"
