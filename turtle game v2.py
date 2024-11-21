'''
Author: Lee yeun woo
Date: 2024-11-21
Update: 실패할 경우 오른쪽에 횟수 출력하는 기능 추가
'''

import turtle as t
import random

def turn_up():
    t.left(2)

def turn_down():
    t.right(2)

def fire():
    global isFire, cnt
    if not isFire:
        isFire = True
        ang = t.heading()
        t.forward(15)
        d = t.distance(target, 0)
        
        while t.ycor() > 0:
            t.forward(15)
            t.right(5)
            d = t.distance(target, 0)

        t.sety(random.randint(10, 100))
        if d < 25:
            t.color("blue")
            t.write("Good!", False, "center", ("", 15))
        else:
            cnt += 1
            t.color("red")
            t.write(f'Bad! {cnt}', False, "center", ("", 15))
            t.goto(-200, 10)
            t.color("black")
            t.setheading(ang)
            isFire = False
            
t.goto(-300, 0)
t.down()
t.goto(300, 0)

target = random.randint(50, 150)
t.pensize(3)
t.color("green")
t.up()
t.goto(target - 25, 2)
t.down()
t.goto(target + 25, 2)

t.color("black")
t.up()
t.goto(-200, 10)
t.setheading(20)

isFire = False
cnt = 0
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")
t.listen()

t.mainloop()
