# coding:utf-8

from sys import argv

script, filename = argv

print("We're going to rease %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If youdo want that, hit RETURE.")

input("?")

print("Opening the file...")
target = open(filename,'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to  ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And filnally, we close it.")
target.close()
