# 简单的python程序

## 实验目的：

熟悉Python语言基本元素，了解Python语言函数库Turtle

## 实验要求：

1. 熟悉掌握Python语言基本元素，能仿照例题温度转换程序编写汇率兑换程序。

​	2. 基本掌握Turtle库的常用函数和用法，能绘制简单的图形

## 实验内容：

完成教材第二章程序练习题56-57页

## 实验代码：

2.1

``` python
TempStr = input('请输入带有符号的温度值：')
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32) / 1.8
    print('转换后的温度是{:.0f}C'.format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print('转换后的温度是{:.0f}'.format(F))
else:
    print('输入格式错误')
```



2.2

```python
TempStr = input('请输入带有符号货币值的：')
if TempStr[-1] in ['$']:
    C = eval(TempStr[0:-1]) * 6
    print('${:} = ￥{:.2f}'.format(eval(TempStr[:-1]),C))
elif TempStr[-1] in ['￥']:
    F = 1.8 * eval(TempStr[0:-1]) / 6
    print('￥{:} = ${:.2f}'.format(eval(TempStr[:-1]),F))
else:
    print('输入格式错误')
```



2.3

```python
import turtle
turtle.setup(650,350,200,200)
turtle.pu()
turtle.fd(-250)
turtle.pd()
turtle.pensize(25)
turtle.seth(-40)
color = ['red','orange','green','purple','yellow']
for i in range(4):
    turtle.pencolor(color[i])
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
```



2.4

```python
import turtle
turtle.pensize(3)
turtle.fd(100)
turtle.left(120)
turtle.fd(100)
turtle.left(120)
turtle.fd(100)
```



2.5

```python
import turtle
def triangle():
    turtle.pd()
    turtle.pensize(3)
    turtle.seth(0)
    turtle.fd(100)
    turtle.left(120)
    turtle.fd(100)
    turtle.left(120)
    turtle.fd(100)
    turtle.pu()
turtle.goto(0,0)
triangle()
turtle.goto(100,0)
triangle()
turtle.goto(50,50 * 3 ** 0.5)
triangle()
turtle.seth(0)
```



2.6

```python
import turtle
turtle.pensize(3)
for i in range(4):
    turtle.fd(25)
    turtle.pd()
    turtle.fd(50)
    turtle.pu() 
    if i <3:
           turtle.fd(25)
           turtle.left(90)
```



2.7

```python
import turtle
def triangle(time):
    turtle.pd()
    for i in range(3):
        turtle.fd(150)
        if time == 2:
           turtle.left(120)
        if time == 1:
            turtle.right(120)
    turtle.pu()
turtle.pensize(3)
turtle.left(30)
triangle(1)
turtle.goto(25 * 3 ** 0.5,75)
turtle.seth(0)
turtle.right(90)
triangle(2)

turtle.fd(50)
turtle.left(120)
```



2.8

```python
import turtle
len = 3
a = 100
turtle.pensize(1)
turtle.left(90)
turtle.pd()
while a:
    turtle.fd(len)
    turtle.left(90)
    len +=2
    
```



## 实验总结：

通过这次实验我对python语言的语法了解的更多了，在实验中我们对书上的实例进行修改，在对书上内容的理解上书写了汇率兑换程序，掌握了从键盘输入数据到程序的方法。然后我们又模仿书上的绘图程序绘制了等边三角形、叠加等边三角形、无角正方形、六边形、正方形螺旋线、彩色蟒蛇。这次实验课我掌握了使用turtle库进行简单图形绘制的方法，掌握了turtle库中常用函数的使用方法。
