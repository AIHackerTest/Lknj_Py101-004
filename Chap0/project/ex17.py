# coding:utf-8

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s." % (from_file, to_file))

# 我们可以把这两个放在一行
raw_input = open(from_file)
indata = raw_input.read()

print("The input file is %d bytes long" % len(indata))
print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURE to continue, CTRL-C to abort.")

input()

output = open(to_file, 'w')
output.write(indata)
print("Alright,all done")

output.close()
raw_input.close()
