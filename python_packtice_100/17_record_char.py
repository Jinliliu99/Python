#!/usr/bin/python
# -*-  coding: UTF-8  -*-

'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
'''

input_string = raw_input("please input:\n" )
num_char = 0
num_space = 0
num_digit = 0
num_other = 0

for i in range(len(input_string)):
    if input_string[i].isalpha():
        num_char += 1
    elif input_string[i].isspace():
        num_space += 1
    elif input_string[i].isdigit():
        num_digit += 1
    else:
        num_other += 1

print "char = %d, space = %d, digit = %d, others = %d" % (num_char, num_space, num_digit, num_other)



