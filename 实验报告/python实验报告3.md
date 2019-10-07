# 基本数据类型

## 实验目的：

掌握数值运算操作和字符类型转换函数

## 实验要求：

1、掌握Python内置的数值运算和字符函数；

2、掌握字符串类型及其操作和格式化

## 实验内容：

完成教材93-94页练习

## 实验代码：

3.1

```python
#重量计算
weight = eval(input('输入你的体重：'))
for i in range(10):
    weight += 0.5
print('十年后你在地球上的体重：{:.2f}，你在月球上的体重是：{:.2f}。'.format(weight,weight * 0.165))


```



3.2

```python
#天天向上
abilty = 1
for i in range(365//7):
    for a in range(4):
        abilty = abilty * 1.01
print('连续学习365天后的能力值：{:.2f}'.format(abilty))
```



3.4

```python
#回文数判断
num = input('请输入一个数字：')
if num == num[::-1]:
    print(num,'是回文数')
else:
    print(num,'不是回文数')
```



3.6

```python
#文本进度条
import time
scale = 10
for i in range(scale + 1):
    a,b = '**' *i,'..' * (scale - i)
    print('\rStarting' + '{}{}'.format(a,b),end = '')
    time.sleep(0.1)
print('Done')

```



3.7

```python
#文本风格
while True:
    for i in ['/','-','|','\\','|']:
        print('%s\r' % i ,end = '')
```



3.8

```python
from tqdm import tqdm
from time import sleep
for i in tqdm(range()):
    sleep(0.01)
```



## 实验总结：

通过这次上机，我仿照教材例题写了天天向上的程序，明白了天天向上的力量，也写了文本进度条，还写了一些简单的，通过这些简单的程序可以做很多事，能够进行一些简单的计算，判断一个数是否是回文数。会使用一些简单的内置的数值运算函数和字符函数来做一些有趣的程序。此外，我也学会了第三方库的安装。

这次实验中也遇到了一些棘手的问题，进度条程序的代码与书上写的一模一样，却出现了不同的运行结果，反复检查了好几遍也没找出问题所在，后来老师解释了我们才知道了，要使用转义字符并在命令行打开才能出正确的结果。
