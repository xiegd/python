import turtle
import math
#画五角星
def star(size):
    turtle.pd()
    turtle.color('yellow','yellow')
    if size == 'big':
        length = (6 * l) /  (2 + math.sin(0.1 * 3.14)/math.sin(0.2 * 3.14))
    if size == 'small':
        length = (2 * l) /  (2 + math.sin(0.1 * 3.14)/math.sin(0.2 * 3.14))
    turtle.begin_fill()
    for i in range(5):
        turtle.fd(length)
        turtle.left(72)
        turtle.fd(length)
        turtle.left(36)
        turtle.right(180)
    turtle.end_fill()
    turtle.pu()
    
#确定小五角星位置
def weizhi(tan,sq,ud):
    turtle.goto(l * 5,-l * 5)#到大五角星中心
    turtle.seth(0)
    if ud == 'up':
        turtle.left(math.degrees(math.atan(tan)))
    if ud == 'down':
        turtle.right(math.degrees(math.atan(tan)))        
    turtle.fd(pow((sq * l**2),0.5) - l)
    turtle.left(18)
    star('small')
    
turtle.pensize(1)
turtle.color('red','red')
l = 10
turtle.goto(0,0)
turtle.pendown()
turtle.begin_fill()
#画长方形
for i in range(2):
    turtle.fd(30 * l)
    turtle.right(90)
    turtle.fd(20 * l)
    turtle.right(90)
turtle.end_fill()
turtle.pu()
turtle.goto(l * 2,-l * 4)
star('big')#画大五角星
weizhi(3/5,34,'up')#第一个小五角星
weizhi(1/7,50,'up')
weizhi(2/7,53,'down')
weizhi(4/5,41,'down')
turtle.hideturtle()
