#!/usr/bin/env python3

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def get_next(s):
    if s =='':
        return ALPHABET[0]
    pos = ALPHABET.find(s[-1])
    if pos +1 ==len(ALPHABET):
        pos = 0
        recur = get_next(s[:-1])
        s_out = recur+ALPHABET[pos]

    else:
        s_out = s[:-1]+ALPHABET[pos+1]

    return s_out


def password_check(s):

    #iol check
    if ('i' in s) or ('o' in s) or ('l' in s):
        return False

    #incrementing value check
    abc_flag = False
    for letter1, letter2, letter3 in zip( s, s[1:], s[2:]):
        pos1 = ALPHABET.find(letter1)
        pos2 = ALPHABET.find(letter2)
        pos3 = ALPHABET.find(letter3)
        if pos2-pos1==1 and pos3-pos1==2:
            abc_flag = True
            break
    if not abc_flag:
        return False



    #double letter check
    double_flag1 = None
    double_flag2 = None
    for i, (letter1, letter2) in enumerate(zip(s, s[1:])):
        # print(letter1, letter2, i)
        if letter1 == letter2:
            if not double_flag1 is None:
                double_flag2 =i
            else:
                double_flag1 =i
        # print(double_flag1, double_flag2)
        # print('\n')

    if double_flag1 is None or double_flag2 is None:
        return False

    if double_flag2 - double_flag1 ==1:
        return False







    return True






if __name__ == '__main__':

    # password = 'pizzz'
    # next_password = get_next(password)
    # print( password, next_password)


    password = 'hxbxxyzz'

    found =False
    count =0
    while not found:
        print(count)
        password = get_next(password)
        found = password_check(password)
        count+=1

    print(password)
