import turtle
import time
import random

segments = []
s = 0
hs = 0

w = turtle.Screen()
w.bgcolor("blue")
w.setup(width = 600, height=600)
w.tracer(1)

h = turtle.Turtle()
h.color("red")
h.speed(3)
h.shape("square")
h.pu()
h.goto(0, 0)
h.direction = "stop"

shapes = ["square", "circle", "triangle"]

f = turtle.Turtle()
f.speed(0)
f.pu()
f.color("green")
f.shape("circle")
f.goto(0, 100)

p = turtle.Turtle()
p.color("black")
p.ht()
p.pu()
p.goto(0, 260)
p.write(f"Score : {s}, highscore : {hs}", font = ("Courier", 24, "normal"), align = "center")

def go_right():
    if h.direction != "left":
        h.direction = "right"

def go_left():
    if h.direction != "right":
        h.direction = "left"

def go_up():
    if h.direction != "down":
        h.direction = "up"

def go_down():
    if h.direction != "up":
        h.direction = "down"

def move():
    if h.direction == "up":
        y = h.ycor()
        h.sety(y + 20)
    
    if h.direction == "down":
        y = h.ycor()
        h.sety(y - 20)
    
    if h.direction == "right":
        x = h.xcor()
        h.setx(x + 20)
    
    if h.direction == "left":
        x = h.xcor()
        h.setx(x - 20)

w.listen()
w.onkeypress(go_up, "Up")
w.onkeypress(go_down, "Down")
w.onkeypress(go_left, "Left")
w.onkeypress(go_right, "Right")

while True:
    w.update()
    if h.ycor() > 290 or h.ycor() < -290 or h.xcor() > 290 or h.xcor() < -290:
        time.sleep(1)
        h.goto(0, 0)
        h.direction = "stop"
        
        for segment in segments:
            segment.goto(1000, 1000)
             
        segments.clear()
        
        s = 0
        
        p.clear()
        p.write(f"Score : {s}, highscore : {hs}", font = ("Courier", 24, "normal"), align = "center")
    
    if h.distance(f) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        f.goto(x, y)

        ns = turtle.Turtle()
        ns.color("yellow")
        ns.pu()
        ns.shape(random.choice(shapes))
        segments.append(ns)

        s += 10
        if s > hs:
            hs = s
        
        p.clear()
        p.write(f"Score : {s}, highscore : {hs}", font = ("Courier", 24, "normal"), align = "center") 
        
    for segment in segments:
        if segment.distance(h) < 20:
            time.sleep(1)
            h.goto(0, 0)
            h.direction = "stop"
        
            for segment in segments:
                segment.goto(1000, 1000)
             
            segments.clear()
        
            s = 0
        
            p.clear()
            p.write(f"Score : {s}, highscore : {hs}", font = ("Courier", 24, "normal"), align = "center")
    

    for _ in range(len(segments) - 1, 0, -1):
            x = segments[_ - 1].xcor()
            y = segments[_ - 1].ycor()
            segments[_].goto(x, y)
        
    if len(segments) > 0:
            x = h.xcor()
            y = h.ycor()
            segments[0].goto(x, y)

    move()

w.mainloop()