# coding:utf-8

# 格式化字符
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"

y = "Those who know %s and those %s." % (binary, do_not)

print(x)
print(y)

# 注意print()函数后所有的内容全在括号里
print("I said: %r." % x)
print("I also said: '%s'." % y)


hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string eith a right side."

print('.' * 10)
print(w + e)
