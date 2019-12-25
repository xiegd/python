# 程序设计方法

## 实验目的：

学习自顶向下的程序设计方法

## 实验要求：

1、理解计算思维
2、能运用自顶向下的程序设计方法、模块化的思想解决问题

## 实验内容：

完成教材第六章练习8.1、8.2、8.4

## 实验代码：

1. 程序练习题8.1

   ```python
    from random import random
    def printIntro():
        print("这个程序模拟两个选手A和B的某种竞技比赛")
        print("程序运行需要A和B的能力值（以0到1之间的小数表示）")
    def getInputs():
        a = eval(input("请输入选手A的能力值(0-1): "))
        b = eval(input("请输入选手B的能力值(0-1): "))
        n = eval(input("模拟比赛的场次: "))
        return a, b, n
    def simNGames(n, probA, probB):
        winsA, winsB = 0, 0
        for i in range(n):
            scoreA, scoreB = simOneGame(probA, probB)
            if scoreA > scoreB:
                winsA += 1
            else:
              winsB += 1
        return winsA, winsB
    def gameOver(a,b):
        return a==11 or b==11
    def simOneGame(probA, probB):
        scoreA, scoreB = 0, 0
        serving = 0
        t = 0
        while not gameOver(scoreA, scoreB):
            if serving == 0:
                if random() < probA:
                    scoreA += 1
                else:
                    scoreB += 1
            else:
                if random() < probB:
                    scoreB += 1
                else:
                    scoreA += 1
            t = t + 1
            if t%2 == 0:
                serving = (serving + 1)%2
        return scoreA, scoreB
    def printSummary(winsA, winsB):
        n = winsA + winsB
        print("竞技分析开始，共模拟{}场比赛".format(n))
        print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA/n))
        print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB/n))
    def main():
        printIntro()
        probA, probB, n = getInputs()
        winsA, winsB = simNGames(n, probA, probB)
        printSummary(winsA, winsB)
    main()
   ```
   
   

2. 程序练习题8.2

  ```python
  from random import random
    from random import randint
    def printIntro():
        print("这个程序模拟两个选手A和B的某种竞技比赛")
        print("程序运行需要A和B的能力值（以0到1之间的小数表示）")
    def getInputs():
        g1 = eval(input("请输入球队A的投篮能力值(0-1): "))
        b1 = eval(input("请输入球队A的篮板能力值(0-1): "))
        g2 = eval(input("请输入球队B的投篮能力值(0-1): "))
        b2 = eval(input("请输入球队B的篮板能力值(0-1): "))
        n = eval(input("模拟比赛的场次: "))
        return g1, b1, g2, b2, n
    def simNGames(n, goleA, boardA, goleB, boardB):
        winsA, winsB = 0, 0
        for i in range(n):
            scoreA, scoreB = simOneGame(goleA, boardA, goleB, boardB)
            if scoreA > scoreB:
                winsA += 1
            else:
                winsB += 1
        return winsA, winsB
    def gameOver(t):
        return t > 12*60
    def simOneGame(goleA, boardA, goleB, boardB):
        scoreA, scoreB = 0, 0
        serving = 0 #0: 代表A队发球，1：代表B队发球
        totalTime = 0
        while not gameOver(totalTime):
            t = randint(1, 24)
            totalTime += t
            if t == 24:
                serving = (serving + 1)%2
            else:
                if serving == 0:
                    if random() < goleA:
                        scoreA += 1
                        serving = 1
                    else:
                        if random() < boardA:
                            serving=0
                        else:
                            serving = 1
                else:
                    if random() < goleB:
                        scoreB += 1
                        serving = 0
                    else:
                        if random() < boardB:
                            serving = 1
                        else:
                            serving=0
        return scoreA, scoreB
    def printSummary(winsA, winsB):
        n = winsA + winsB
        print("竞技分析开始，共模拟{}场比赛".format(n))
        print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA/n))
        print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB/n))
    def main():
        printIntro()
        goleA, boardA, goleB, boardB, n = getInputs()
        winsA, winsB = simNGames(n, goleA, boardA, goleB, boardB)
        printSummary(winsA, winsB)
    main()

  ```

  

3. 程序练习题8.4

  ```python
    import jieba
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud,ImageColorGenerator
    import numpy as np
    import PIL.Image as Image

    def calWordFreqencies():
        excludes = {"将军","却说","丞相"}
        txt = open("三国演义.txt", "r", encoding='utf-8').read()
        words = jieba.lcut(txt)
        counts = {}
        for word in words:
            if len(word) == 1:
                continue
            else:
                counts[word] = counts.get(word, 0) + 1
        for word in excludes:
            del (counts[word])

        return counts

    def drawWordcloudPlot(counts):
        coloring = np.array(Image.open("E:/baidupic/alice_color.png"))
        wc = WordCloud(background_color="white",
                             max_words=2000,
                             mask=coloring,
                             max_font_size=60,
                             random_state=42,
                             scale=2,
                             font_path="c:/Windows/Fonts/SimHei.ttf")
        wc.generate_from_frequencies(counts)
        image_colors = ImageColorGenerator(coloring)

        plt.imshow(wc)
        plt.axis("off")
        plt.show()
    def main():
        counts = calWordFreqencies()
        drawWordcloudPlot(counts)

    main()
  ```

## 实验总结：

 通过这次学习我熟悉了python语言的开发环境IDLE，能够编辑，运行给定的代码。完成1.1-1.6的过程中我掌握了Python语言的基本语法，比如缩进是一个对初学者来说很重要的知识，缩进的错误会导致程序无法正常运行并报出unexpected indent的错误，而语法错误是 SyntaxError。完成1.7-1.8是我们使用了turtle库进行绘图观察了绘出图形，还对程序中的数据进行了修改绘出了不同的图形。

