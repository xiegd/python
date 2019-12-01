# 组合数据类型

## 实验目的：

了解列表、字典、集合、三种组合数据类型

## 实验要求：

1、能运用集合的特性对数据去重。
2、掌握运用字典概念处理复杂数据信息，及字典的排序。
3、能运用列表构建数据结构。
4、综合运用组合数据类型进行文本词频统计。


## 实验内容：

完成教材第六章练习(实验1-4：2学时，实验5-6：2学时)

## 实验代码：

1. 程序练习题6.1

```python
'''随机密码的生成'''
import random
def password():
       str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
       password = ''
       for i in range(8):
           password += random.choice(str)
       return password
   
   
   for i in range(10):
       print(password())
   ```
   
   

2. 程序练习题6.2

  ```python
  def repeat(list1):
      repeats = ''
      for i in set(list1):
          if list1.count(i) > 1:
              repeats += str(i) + ':' + str(list1.count(i)) + ','
              
      return repeats
  
  
  list = [1,2,3,4,2,1,32,3,4,4,3,2]
  print(repeat(list))
  ```

  

3. 程序练习题6.3

  ```python
  '''重复元素判定续'''
  def repeat(list1):
      set1 = set(list1)
      if len(set1) !=  list1:
          return True
      return False
  
      
  list = [1,2,3,4,2,1,32,3,4,4,3,2]
  print(repeat(list))
  ```

  

4. 程序练习题6.4

  ```python
  def repeat(str1):
      repeats = {}
      an = ''
      for i in str1:
          repeats[i] = repeats.get(i,0) + 1
  
      items = list(repeats.items())
      items.sort(key = lambda x:x[1],reverse = True)
      for i in items:
          words,count = i
          an += words
      
              
      return an
  
  
  str1 = 'dsnanoasdnadsndndaaaaadddddzaaaaaaa'
  print(repeat(str1))
  ```

  5、程序练习题6.5

```python
'''生日悖论'''
from datetime import datetime
import random

def generateSamples(n):
    birthdays = []
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    
    for i in range(n):
        month = random.randint(1,12)
        day = random.randint(1,days[month - 1])
        someday = (month,day)
        birthdays.append(someday)
        
    return birthdays

def calSameBirthdayProb(birthdays,n):
    num = 0
    for i in range(n):
        people = random.sample(birthdays,23)
        pset = set(people)
        if len(pset) != len(people):
            num += 1
    return num/n

def main():
    while True:
        n = int(input('输入一个整数:'))

        if n < 23:
            break
        birthdays = generateSamples(n)
        print('{}个随机样本数量下，23个人中至少有两人生日相同的概率是：{}'.format(n,calSameBirthdayProb(birthdays,100000)))
main()

```

6. 程序练习题6.6

  ```python
  import jieba
  with open('红楼梦.txt','r',encoding = 'utf-8') as fi:
      list1 = jieba.lcut(fi.read())
      dict = {}
      for i in list1:
          if i in '，。“”：； 不好 ？?ltgt不过的话所以出去告诉只是只得这些不敢这个东西咱们就是回来大家一面只见怎么两个没有不是不知听见这样进来什么一个我们那里如今你们说道知道起来这里出来他们众人自己':
              continue
          if len(i) >= 2:
              dict[i] = dict.get(i,0) + 1
      items = list(dict.items())
      items.sort(key = lambda x:x[1],reverse=True)
      for i in range(20):
          word,count = items[i]
          print('{:<10}{:<8}'.format(word,count))
  ```

  


## 实验总结：

 通过这次学习我熟悉了python语言的开发环境IDLE，能够编辑，运行给定的代码。完成1.1-1.6的过程中我掌握了Python语言的基本语法，比如缩进是一个对初学者来说很重要的知识，缩进的错误会导致程序无法正常运行并报出unexpected indent的错误，而语法错误是 SyntaxError。完成1.7-1.8是我们使用了turtle库进行绘图观察了绘出图形，还对程序中的数据进行了修改绘出了不同的图形。

