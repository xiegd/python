# 熟悉python语言开发环境

## 实验目的：

了解Python语言，熟悉课程所使用的Python语言开发环境

## 实验要求：

能编辑、运行给定的代码，熟练掌握集成开发环境

## 实验内容：

完成教材练习题1.1-1.8

## 实验代码：

1.1

```python
str1 = input('请输入一个人的名字：')
str2 = input('请输入一个国家的名字：')
print('世界这么大，{}想去{}看看。'.format(str1,str2))
```



1.2

```python
n = input('请输入整数N：')
sum = 0
for i in range(int(n)):
	sum += i +1
print('1到N求和结果：',sum)
```



1.3

```python
for i in range(1,10):
	for j in range(1,i + 1):
		print('{}*{}={:2}'.format(j,i,i * j),end = '')
		print(' ')
```



1.4

```python
sum,tmp = 0,1
for i in range(1,11):
    tmp *= i
    sum += tmp
print('运算结果是：{}'.format(sum))
```



1.5

```python
n = 1
for i in range(4,0,-1):
    n = (n + 1) << 1
print(n)
```



1.6

```python
diet = ['西红柿','花椰菜','黄瓜','牛排','虾仁']
for x in range(0,5):
    for y in range(0,5):
        if not(x == y):
            print('{}{}'.format(diet[x],diet[y]))
```



1.7

```python
from turtle import *
fillcolor('red')
begin_fill()
while True:
    forward(200)
    right(144)
    if abs(pos()) < 1:
        break
end_fill()        
```



1.8

```python
from turtle import *
color('red','yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
```



## 实验总结：

 通过这次学习我熟悉了python语言的开发环境IDLE，能够编辑，运行给定的代码。完成1.1-1.6的过程中我掌握了Python语言的基本语法，比如缩进是一个对初学者来说很重要的知识，缩进的错误会导致程序无法正常运行并报出unexpected indent的错误，而语法错误是 SyntaxError。完成1.7-1.8是我们使用了turtle库进行绘图观察了绘出图形，还对程序中的数据进行了修改绘出了不同的图形。

