# coding:utf-8


from random import randint

num = randint(0,21)

print("来玩猜数字游戏吧！\n")
print("游戏规则是：")
print("    - 程序自动生成一个20以内的随机数，你有10次机会猜测")
print("    - 根据你的输入，给予你一定的提示")
print("    - 猜对或用完10次机会，游戏结束")

guess = int(input("> "))

guesses = 0
if guess > num:
    print("大了")
elif guess < num:
    print("小了")
else:
    print("你一次就猜对了，太强了！")
while guess != num and guesses < 9:
    times = 9 - guesses
    print("你还有%d次机会" %times)
    guesses += 1
    guess = int(input("> "))
    if guess > num:
        print("大了")
    elif guess < num: 
        print("小了")
    else:
        print("恭喜你答对了！")
if guess != num:
    print("很遗憾，你输了！")
