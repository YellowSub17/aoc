#!/usr/bin/env python3
import os


def char_of_code(s):
    
    # count=0
    # for letter in s:
        # print(letter)

    return len(s) #+count


def char_of_str(s):
    x_count=s.count('\\x')
    hex_count=0
    hexs =['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']

    sub =str( s)
    for i in range(x_count):
        print(sub)
        pos = sub.index('\\x')
        print(sub[pos], sub[pos+1], sub[pos+2], sub[pos+3])
        print(sub[pos+3] in hexs)
        print(sub[pos+2] in hexs)
        if (sub[pos+3] in hexs) and (sub[pos+2] in hexs):
            hex_count+=1

        sub = s[pos+1:]
        # print('\n')


        




    esc_count=s.count('\\\\')
    qu_count=s.count('\\"')


    return len(s)-3*hex_count-esc_count-qu_count-2


if __name__ == '__main__':

    fname = 'input.prod'

    file = open(fname, 'r')
    cont =  file.read().split('\n')[:-1]
    

    count = 0
    for line in cont:
        print(line, char_of_code(line), char_of_str(line))

        print('\n')
        count += char_of_code(line)
        count -= char_of_str(line)

    print(count)
