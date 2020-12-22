#/usr/bin/env python3
import os
import sys


var_tracker = {'b': 16076}

def prep_input(fname):
    file = open(fname, 'r')
    cont = file.read()
    lines = cont.split('\n')
    return lines





def check_if_can_do(lhs, rhs):
    if lhs in var_tracker and rhs in var_tracker:
        return 1, var_tracker[lhs], var_tracker[rhs]

    elif lhs.isnumeric() and rhs.isnumeric():
        return 2, int(lhs), int(rhs)

    elif lhs in var_tracker and rhs.isnumeric():
        return 3, var_tracker[lhs], int(rhs)

    elif lhs.isnumeric() and rhs in var_tracker:
        return 4, int(lhs), var_tracker[rhs]

    else:
        return 0, 0, 0



# def OP( lhs, rhs, op, cd):
    # if 

def parse_line(line):
    eq = line.split(' ')


    ## Decleration ( a -> out)
    if len(eq)==3:
        if eq[0].isnumeric():
            var_tracker[eq[-1]] =int(eq[0])

        elif eq[0] in var_tracker:
            var_tracker[eq[-1]] = var_tracker[eq[0]]

    ## not operation (NOT a -> out)
    elif len(eq)==4:
        if eq[1].isnumeric():
            var_tracker[eq[-1]] = ~int(eq[1]) & int(65535)
        elif eq[1] in var_tracker:
            var_tracker[eq[-1]] = ~int(var_tracker[eq[1]]) & int(65535)


    elif len(eq)==5:

        can_do, lhs, rhs = check_if_can_do(eq[0], eq[2])


        if can_do > 0:

            if 'AND' in eq:
                var_tracker[eq[-1]] = lhs & rhs

            elif 'OR' in eq:
                var_tracker[eq[-1]] = lhs | rhs

            elif 'LSHIFT' in eq:
                var_tracker[eq[-1]] = lhs << rhs

            elif 'RSHIFT' in eq:
                var_tracker[eq[-1]] = lhs >> rhs











if __name__ == "__main__":

    fname = 'input.prod'

    lines = prep_input(fname)

    while not 'a' in var_tracker:

        for line in lines:
            parse_line(line)


        print(var_tracker)


    p1_answer = var_tracker['a']

    var_tracker = {}
    var_tracker['b'] = p1_answer
    
    print(var_tracker)
    
    while not 'a' in var_tracker:

        for line in lines:
            if line.split(' ')[-1] == 'b':
                continue
            else:
                parse_line(line)

        # print(var_tracker)





    


    # var_tracker = {}

    # for line in file:

        # #split terms and remove \n char
        # eq = line.split(' ')
        # eq[-1] = eq[-1][:-1]




        # if len(eq)==3:
            # ## Decleration
            # if eq[0].isnumeric():
                # var_tracker[eq[-1]] =int(eq[0])

            # elif eq[0] in var_tracker:
                # var_tracker[eq[-1]] = var_tracker[eq[0]]

        # if len(eq)==4:
            # ## not operation
            # if eq[1] in var_tracker:
                # var_tracker[eq[-1]] = ~int(var_tracker[eq[1]]) & int(65535)

            # elif eq[1].isnumeric():
                # var_tracker[eq[-1]] = ~int(eq[1]) & int(65535)

        # if len(eq)==5:
            # ## and, or, lshift rshift operation
            # lhs = eq[0]
            # rhs = eq[2]
            # pass_token =False

            # if lhs in var_tracker and rhs in var_tracker:
                # #both inputs have been declared
                # pass_token=True
            # elif lhs in var_tracker and rhs.isnumeric():
                # #one number, one declared input
                # pass_token=True
            # elif rhs in var_tracker and lhs.isnumeric():
                # pass_token=True
                # #both numbers
            # elif lhs.isnumeric() and rhs.isnumeric():
                # pass_token=True






            # if pass_token:
                # lhs = var_tracker[eq[0]] if lhs in var_tracker else int(eq[0]) 
                # if 'AND' in eq:
                    # var_tracker[eq[-1]] = int(var_tracker[eq[0]]) & int(var_tracker[eq[2]])

                # elif 'OR' in eq:
                    # var_tracker[eq[-1]] = int(var_tracker[eq[0]]) | int(var_tracker[eq[2]])

                # elif 'LSHIFT' in eq:
                    # var_tracker[eq[-1]] = int(var_tracker[eq[0]]) << int(var_tracker[eq[2]])

                # elif 'RSHIFT' in eq:
                    # var_tracker[eq[-1]] = int(var_tracker[eq[0]]) >> int(var_tracker[eq[2]])

            # else:
                # continue






    # print(var_tracker)

    # # x = convert_bin(2)
    # # y = convert_bin(3)
    # # z = x + y
    # # print(z)
    

