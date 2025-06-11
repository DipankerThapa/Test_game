import turtle

class GameObject(turtle.Turtle):
    def __init__(self, gmshape, color, x, y):
        turtle.Turtle.__init__(self, shape=gmshape)
        self.color(color)
        self.x = x
        self.y = y
        self.fd(0)
        self.penup()
        self.goto(x, y)
        self.speed(0)
        self.speed = 1

