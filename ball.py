import turtle as t
import random
import time

speed = random.randint(1, 20)
angle = random.randint(0, 359)

r=random.randint(0, 254)
g=random.randint(0, 254)
b=random.randint(0, 254)

radius = random.randint(1, 300)

x=random.randint(-500+radius, 500-radius)
y=random.randint(-300+2*radius, 300)

t.setup(1000, 600)
t.hideturtle()
t.speed(0)
t.colormode(255)
t.color((r, g, b))

t.pu()
t.goto(x, y)
t.pd()

def circle():
    t.seth(180)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

try:
    while True:
        t.tracer(False)
        t.clear()
        t.pu()
        if t.ycor() >= 300:
            angle=360-angle
        elif t.ycor() <= -300+2*radius:
            angle=360-angle
        if t.xcor() <= -500+radius:
            if angle <= 180:
                angle=180-angle
            elif angle > 180:
                angle=540-angle
        elif t.xcor() >= 500-radius:
            if angle <= 180:
                angle = 180-angle
            elif angle > 180:
                angle=540-angle
        t.seth(angle)
        t.forward(speed)
        t.pd()
        circle()
        time.sleep(0.01)
        t.tracer(True)
except:
    pass
