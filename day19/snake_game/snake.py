from turtle import Turtle
STARTING_POS = [(-22,0), (0,0), (22,0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake():
    """Snake Object That controls length and directions"""
    def __init__(self) -> None:
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    
    def create_snake(self):
        for pos in STARTING_POS:
            new = Turtle("square")
            new.penup()
            new.color('white')
            new.goto(pos)
            self.snake.append(new)
    
    def move_forward(self,distance=22):
        for i in range(len(self.snake)-1, 0, -1):
            x = self.snake[i-1].xcor()
            y = self.snake[i-1].ycor()
            self.snake[i].goto(x,y)
        self.head.forward(distance)

    def grow(self):
        new = Turtle("square")
        new.penup()
        new.color('white')
        heading = self.head.heading()
        new.setheading(heading)
        if heading == 0:
            x = self.head.xcor() + 22
            y = self.head.ycor()
            new.goto(x,y)
        elif heading == 90:
            x = self.head.xcor() 
            y = self.head.ycor() + 22
            new.goto(x,y)
        elif heading == 180:
            x = self.head.xcor() - 22
            y = self.head.ycor() 
            new.goto(x,y)
        elif heading == 270:
            x = self.head.xcor() 
            y = self.head.ycor() - 22 
            new.goto(x,y)

        self.snake.insert(0,new)
        self.head = new

    
    def move_up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(UP)
        

    def move_down(self):
        if(self.head.heading() != UP):
            self.head.setheading(DOWN)

    def move_left(self):
        if(self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def move_right(self):
        if(self.head.heading() != LEFT):
            self.snake[0].setheading(RIGHT)

    def not_dead(self):
        if(abs(self.head.pos()[0]) >= 300 or abs(self.head.pos()[1]) >= 300):
            return False
        for i in range(1,len(self.snake)):
            if self.snake[i].pos() == self.head.pos():
                return False
        return True
        

