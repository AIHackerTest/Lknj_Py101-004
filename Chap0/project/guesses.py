# coding:utf-8
import random

# 生成随机4位数,
# 如果生成的数字首位为0，循环，直到首数字不为零
def Num():
    num = random.sample(range(0,10),4)
    while num[0] == 0:
        num = random.sample(range(0,10),4)
    return num


# 把键入的数字用for in 迭代为列表，为了下边的比较做铺垫
def guess():
    guesses = input("请输入你的答案（四位数字）： ")
    
    if guesses.isdigit() and len(guesses) == 4: # 是否输入为4位数字
        get_num = []
        for x in guesses:
            get_num.append(int(x))
        return get_num
    else:
        print("你输入4位数字好吧！")
    
    

# A代表数字和位置都正确，B代表数字正确，位置不正确，记录A、B的值
def comp(number,answer):
    a = c = 0
    for x in range(4):
        if number[x] == answer[x]:
            a += 1
    for y in answer:
        if y in number:
            c += 1
    b = c - a
    return a, b


def play():
    try:
        print("游戏开始")
        number = Num()
        times = 9
        
        while times >= 0:
            answer = guess()
            print("你还有%d次机会" % times)
            times -= 1
            A,B = comp(number,answer)
            print("%dA%dB" % (A,B))
            if A == 4:
                print("恭喜你答对了！")

        if times < 0:
            print("很遗憾，你机会用完了！正确答案是%r" %str(number))
    except:
        print("滴滴滴~~~")

play()

