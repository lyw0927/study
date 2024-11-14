'''
Author: Lee yeun woo
Date: 2024-11-14
'''

import turtle as t 
import random

score = 0
playing = False

t.bgcolor("black")

te = t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0)
te.penup()
te.goto(0, 200)

ts = t.Turtle()
ts.shape("circle")
ts.color("yellow")
ts.speed(0)
ts.up()
ts.goto(0, -200)

te2 = t.Turtle()
te2.shape("turtle")
te2.color("blue")
te2.speed(0)
te2.penup()
te2.goto(200, 0)

te3 = t.Turtle()
te3.shape("turtle")
te3.color("green")
te3.speed(0)
te3.penup()
te3.goto(-200, 0)

te4 = t.Turtle()
te4.shape("turtle")
te4.color("pink")
te4.speed(0)
te4.penup()
te4.goto(-100, 0)

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def start():
    global playing
    if not playing:
        playing = True
        t.clear()
        play()

def play():
    global score
    global playing
    t.forward(10)
    if random.randint(1, 5) == 3:
        ang = te.towards(t.pos())
        te.setheading(ang)
    
    speed = score + 5
    if speed > 15:
        speed = 15

    te.forward(speed)
    tr2()
    tr3()
    tr4()

    if t.distance(te) < 12 or t.distance(te2) < 12 or t.distance(te3) < 12:
        text = "Score: " + str(score)
        message("Game Over", text)
        playing = False
        score = 0

    if t.distance(ts) < 12:
        score += 1
        t.write(score)
        start_x = random.randint(-230, 230)
        start_y = random.randint(-230, 230)
        ts.goto(start_x, start_y)

    if score == 5:
        message("You Win!", "Final Score: " + str(score))
        playing = False 
        score = 0

    if playing:
        t.ontimer(play, 10)

def tr2():
    if random.randint(1, 5) == 3:
        ang = te2.towards(t.pos())
        te2.setheading(ang)

    speed = score + 5
    if speed > 15:
        speed = 15

    te2.forward(speed)

def tr3():
    if random.randint(1, 5) == 3:
        ang = te3.towards(t.pos())
        te3.setheading(ang)

    speed = score + 5
    if speed > 15:
        speed = 15

    te3.forward(speed)

def tr4():
    if random.randint(1, 5) == 3:
        ang = te3.towards(t.pos())
        te4.setheading(ang)

a    speed = score + 5
    if speed > 15:
        speed = 15

    te4.forward(speed)

def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("Consolas", 20, "italic", "bold", "underline"))
    t.goto(0, -100)
    t.write(m2, False, "center", ("Arial", 15))
    t.home()

t.title("Turtle Run")

t.shape("turtle")
t.speed(0)
t.up()
t.color("white")

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()

message("Turtle Run", "[space]")

t.mainloopa
