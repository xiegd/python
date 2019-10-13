# 程序控制结构

## 实验目的

掌握程序的基本结构，进行简单的程序设计

## 实验要求

1. 掌握分支结构（选择结构）基本语法，完成相应的程序练习题。

2. 掌握循环结构，完成相应的程序练习题。

3. 掌握异常处理语句。

## 实验内容

1. 程序练习题4.2

2. 程序练习题4.3

3. 程序练习题2.8（教材57页）

4. 程序练习题3.5（教材94页）

5. 程序练习题4.1。

6. 程序练习题4.4

7. 程序练习题4.5

8. 程序练习题4.6

## 实验代码

4.2

```python
str = input('请输入一串字符:')
e = num = space = other = 0
for char in str:
    if 'a' < char < 'z' or 'A' < char < 'Z':
        e += 1
    elif '0' < char < '9':
        num += 1
    elif char == ' ':
        space += 1 
    else:
        other += 1
print('英文字符数{},数字数{},空格数{},其他字符数{}'.format(e,num,space,other))
```

4.3

```python
a,b = eval(input('输入两个数字，逗号隔开：'))
if a < b:
    m,n = b,a
else:
    m,n = a,b
r = m % n
while m % n:
    m,n = n,r
    r = m % n
bei = a * b / n
print('最小公倍数{:},最大公约数{:.0f}'.format(n,bei))
```

2.8

```python
import turtle
a = 2
b = 100
while b:
    turtle.pd()
    turtle.fd(a)
    turtle.left(90)
    a += 2
    b -= 1
```



3.5

```python
for i in range(0,11):
    if i%5 == 0:
        for a in range(0,11):
            if a%5 == 0:
                print('+',end = ' ')
            else:
                print('-',end = ' ')
        print('\n')
    else:
        for b in range(0,11):
            if b%5 == 0:
                print('|',end = ' ')
            else:
                print(' ',end = ' ')
        print('\n')
```

4.1

```python
num2 = 5
time = 0
while True:
    num1 = eval(input('请输入一个数字：'))
    time += 1
    if num1 > num2:
        print('遗憾，太大了')
    elif num1 < num2:
        print('遗憾，太小了')
    else:
        print('预测{}次，你猜中了！'.format(time))
        break
```

4.4

```python
import random
num2 = random.randint(0,100)
time = 0
while True:
    num1 = eval(input('请输入一个数字：'))
    time += 1
    if num1 > num2:
        print('遗憾，太大了')
    elif num1 < num2:
        print('遗憾，太小了')
    else:
        print('预测{}次，你猜中了！'.format(time))
        break
```

4.5

```python

import random
def guess():
    while True:
        global time
        num1 = input('请输入一个数字：')
        if num1.isnumeric() == True:
            time += 1
            if eval(num1) > num2:
                print('遗憾，太大了')
            elif eval(num1) < num2:
                print('遗憾，太小了')
            else:
                print('预测{}次，你猜中了！'.format(time))
                break
        else:
            print('输入内容必须为整数！')
            continue
num2 = random.randint(0,100)
time = 0
guess()
```

4.6

```python
 
import random
a = b = c = 10000
i = j = 0
while a:
    num = random.randint(1,3)
    num_car = random.randint(1,3)
    if num == num_car:
        i += 1
    a -= 1
while b:
    num_car = random.randint(1,3)
    while True:
        num2 = random.randint(1,3)
        if num2 == num_car:
            continue
        else:
            break
    nums = [num_car,num2]
    num = random.choice(nums)
    if num == num_car:
        j += 1
    b -= 1
print('不能更换:{:.4f},能更换:{:.4f}'.format(i/c,j/c))
```



## 实验总结

在这次上机中我学会了使用分支结构，循环结构，异常处理语句。在两个小时的上机中，我一共练习了8道题目，通过练习这八道题目，复习了国庆前所学习的分支，循环结构，也学习使用了random库中的函数来生成随机数，还有randint(),choice()等函数的使用。运用random库我对羊车门问题进行了模拟，验证了参赛者更换选择后能否增加猜中汽车的机会，这是一道关于概率的问题，通过这道题我更加明白了python运用范围的广泛，学习python能够为我们的学习生活增加更多的色彩，我们也能学到一种新的思考方式。

