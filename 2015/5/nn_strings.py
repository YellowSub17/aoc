#!/usr/bin/env python3

import sys

def nn_check(s):

    if ('ab' in s) or ('cd' in s) or ('pq' in s) or ('xy' in s):
        return False

    vowels = 'aeiou'
    vowel_sum = 0

    for vowel in vowels:
        vowel_sum += s.count(vowel)

    if vowel_sum < 3:
        return False

    for i, letter in enumerate(s[:-1]):
        if letter ==s[i+1]:
            return True

    return False



def nn_check2(s):

    cond1 = False
    cond2 = False
    for i, letter in enumerate(s[:-2]):
        if letter == s[i+2]:
            cond1=True

        search = s[i:i+2]
        if s.count(search)>1:
            cond2=True

        if cond1 and cond2:
            return True

    return False
        









if __name__ == "__main__":


    file = open('input.txt', 'r')

    cont = file.read()
    names = cont.split('\n')[:-1]

    count = 0
    for name in names:
        if nn_check2(name):
            count+=1


    print(count)


