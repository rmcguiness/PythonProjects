from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
         super().__init__()
         self.penup()
         self.shape('circle')
         self.color('white')
         self.xmove = 5
         self.ymove = 0

    def move(self):
        x = self.xcor() + self.xmove
        y = self.ycor() + self.ymove
        self.goto(x,y)
 
    def detect_collision(self, paddleL, paddleR):
        if self.ycor() > 280 or self.ycor() < -280:
            self.wall_bounce()

        left_bounce = self.xcor() < -340 and self.distance(paddleL) < 50
        right_bounce = self.xcor() > 340 and self.distance(paddleR) < 50
        
        distance_from_paddle_center = 0
        if right_bounce:
            distance_from_paddle_center = self.ycor() - paddleR.ycor()
            self.paddle_bounce(distance_from_paddle_center)

        elif left_bounce:
            distance_from_paddle_center = self.ycor() - paddleL.ycor()
            self.paddle_bounce(distance_from_paddle_center)

    def wall_bounce(self):
        self.ymove = -self.ymove

    def paddle_bounce(self, dist):
        self.xmove = -self.xmove
        self.ymove = self.ymove + (dist/15)

    def reset_ball(self, direction):
        self.goto(0,0)
        self.xmove = abs(self.xmove) * direction
        self.ymove = 0

