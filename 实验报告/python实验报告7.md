# 文件和数据格式化

## 实验目的：

掌握文件的读写等操作；掌握PIL、json库的使用

## 实验要求：

1. 能对文件进行打开、关闭、读写等基本操作
2. 运用CSV和json格式对多维数组进行储存和读写
3. 能使用PIL库对图像文件进行常见的修图操作

## 实验内容：

完成教材第七章练习

## 实验代码：

1. 程序练习题7.1

  ```python
  import keyword

  kws = keyword.kwlist
  file = input("读取的文件：")
  fr = open(file,'r',encoding='utf-8')
  wline = ''
  for line in fr:
    wline += '\n'
    if 'import' in line:
        wline += line
  
    else:
        j = 0
        while line[j] == ' ': 
            wline += ' '
            j += 1
        sline = line.split()
        for w in sline:
            if w in kws:
                wline += w
            elif '.' in w: #包含.操作符
                wline += w
            elif '(' in w:#没有.操作符，但是函数调用
                wline += w
            else:
                wline += w.upper()
            wline += ' '
   
  fr.close()

  fw = open(file,'w',encoding='utf-8')
  fw.write(wline)
  fw.close()      
  ```

  

2. 程序练习题7.2

```python
from PIL import Image
im = Image.open("/home/weizhong/Pictures/p1.jpg")
w,h = im.size
c = 6
im.thumbnail((w//c, h//c))
im.save('/home/weizhong/Pictures/p11.jpg','JPEG')

#or:
im2 = Image.open("/home/weizhong/Pictures/p1.jpg")
im2.resize((w//c,h//c)).save('/home/weizhong/Pictures/p12','JPEG')

   ```
   
   

3. 程序练习题7.5-7.6

  ```python
  import os

  def userOperateInterface():
    print("\n请选择词典功能")
    print("i: 添加单词")
    print("s: 查询单词")
    print("Q: 退出词典")
    print("请选择功能：")
    return input()

  def addWord(wordDict:dict, fileName):
    str = input("您输入要加入的单词：")
    if str in wordDict.keys():
        print("该单词已添加到字典库\n")
        userOperateInterface()
    else:
        t = input("请输入此单词的中文释义：")
        wordDict[str] = t
        with open(fileName, 'a') as fw:
            fw.write(str + "  " + t + '\n')

  def selectWord(wordDict:dict):
    str = input("请输入您要查询的单词：")
    if str not in wordDict.keys():
        print("字典库中未找到这个单词\n")
    else:
        print(wordDict[str])


  def main():
    wordDict = {}
    if os.path.exists("dict.txt"):
        with open("dict.txt", 'r') as fr:
            for ln in fr:
                s = ln.split(" ")
                wordDict[s[0]] = s[1]
    else:
        fw = open("dict.txt",'w')
        fw.close()
    print("******欢迎使用简明英汉词典******")
    while True:
        op = userOperateInterface()
        if op == 'i':
            addWord(wordDict, 'dict.txt')
        elif op == 's':
            selectWord(wordDict)
        elif op == 'Q':
            break
        else:
            print("输入有误\n")


  main()
  ```

  

## 实验总结：

 本人也是经过了深思熟虑，在每个日日夜夜思考这个问题。 生活中，若实验文件和数据格式化出现了，我们就不得不考虑它出现了的事实。 经过上述讨论， 我们一般认为，抓住了问题的关键，其他一切则会迎刃而解。 实验文件和数据格式化，到底应该如何实现。 本人也是经过了深思熟虑，在每个日日夜夜思考这个问题。 这样看来， 所谓实验文件和数据格式化，关键是实验文件和数据格式化需要如何写。 既然如此， 既然如此， 现在，解决实验文件和数据格式化的问题，是非常非常重要的。 所以， 实验文件和数据格式化，发生了会如何，不发生又会如何。 实验文件和数据格式化的发生，到底需要如何做到，不实验文件和数据格式化的发生，又会如何产生。 从这个角度来看， 美华纳曾经说过，勿问成功的秘诀为何，且尽全力做你应该做的事吧。这启发了我， 西班牙曾经提到过，自己的鞋子，自己知道紧在哪里。这似乎解答了我的疑惑。 我认为， 我们不得不面对一个非常尴尬的事实，那就是， 可是，即使是这样，实验文件和数据格式化的出现仍然代表了一定的意义。 就我个人来说，实验文件和数据格式化对我的意义，不能不说非常重大。 我们都知道，只要有意义，那么就必须慎重考虑。 所谓实验文件和数据格式化，关键是实验文件和数据格式化需要如何写。 亚伯拉罕·林肯曾经提到过，你活了多少岁不算什么，重要的是你是如何度过这些岁月的。这不禁令我深思。 要想清楚，实验文件和数据格式化，到底是一种怎么样的存在。 实验文件和数据格式化，到底应该如何实现。 我们一般认为，抓住了问题的关键，其他一切则会迎刃而解。 就我个人来说，实验文件和数据格式化对我的意义，不能不说非常重大。 

