# 函数

## 实验目的：

掌握函数的定义和调用方法；理解递归函数的使用

## 实验要求：

1. 能正确定义和调用函数。
2. 能使用函数解决代码复用。
3. 能编写递归函数

## 实验内容：

完成教材第五章练习

## 实验代码：

1. 程序练习题5.1

  ```python
  def tian(width,height):
      x,y = 0,0
      for i in range(height + 1):
          if i%5 == 0:
              #print(height)
              for i in range(width + 1):
                  print('+'if y%5 == 0 else '-',end = ''if i < width else '\n')
                  y += 1
              y = 0
          if i%5 != 0:
              for i in range(width + 1):
                  print('|'if y%5 == 0 else ' ',end = ''if i < width else '\n')
                  y += 1
              y = 0
  tian(20,20)
  ```

  

2. 程序练习题5.2

```python
  def isOdd(num):
       if num%2 == 0:
          return False
       else:
           return True
   print(isOdd(13))
   ```
   
   

3. 程序练习题5.3

  ```python
  def isNum(num):
      return True if type(num) == type(1) or type(num) == type(1.1) or type(num) == type(1+2j) else False
  number = eval(input())
  print(isNum(number))
  ```

  

4. 程序练习题5.4

  ```python
  def multi(num,nums):
      for n in nums:
          num *= n
      return num
  numlist = eval(input())
  print(type(numlist))
  print(multi(numlist[0],numlist[1:]))
  ```

  

5. 程序练习题5.5

  ```python
  def isPrime(num):
      for n in range(2,num):
          if num%n == 0:
              return False
              break
      else:
          return True
  number = eval(input())
  print(isPrime(number))  
  ```

  

6. 斐波拉契数列。

  ```python
  def Fabric(num1,num2):
      print(num1,num2,end = ' ')
      global n
      num1 += num2
      num2 += num1
  
  
      n += 1
      return Fabric(num1,num2) if n <10 else 'haha'
      
  n = 1
  Fabric(1,1)
  ```

  

7. 程序练习题5.7

  ```python
  def move():
      #i = 0
      column1 = list(range(1,65))
      column2 = []
      column3 = []
      for i in range(column1): 
          column3.append(column1.pop(i))
  
  
  
  def judge():
      
  move()
  
  ```

  

8. 七段数码管问题。
  在教材实例7的基础上改写代码，实现以下要求：
  1）日期的每一个数字用不同颜色表示。
  提示：0-9共有10个数字，对应10种不同颜色表示：'red', 'blue', 'yellow', 'gold', 'violet', 'purple', 'green', 'darkgreen', 'grey', 'orange'；只需要修改drawDigit()函数，添加功能使之实现每一个数字用不同颜色表示。
  2）数码管的每一段用不同颜色表示。
  提示：方法一：修改drawDigit()函数；方法二：修改drawLine()函数。

9. 修改实例代码18.1，使koch曲线反向绘制，从直线开始，中间部分向下方绘制。
  提示：参考教材实例8



## 实验总结：

 通过这次学习我熟悉了python语言的开发环境IDLE，能够编辑，运行给定的代码。完成1.1-1.6的过程中我掌握了Python语言的基本语法，比如缩进是一个对初学者来说很重要的知识，缩进的错误会导致程序无法正常运行并报出unexpected indent的错误，而语法错误是 SyntaxError。完成1.7-1.8是我们使用了turtle库进行绘图观察了绘出图形，还对程序中的数据进行了修改绘出了不同的图形。

