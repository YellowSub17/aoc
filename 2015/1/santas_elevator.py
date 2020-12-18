#!/usr/bin/env python3
import sys
import os



def read_file(fname):

    file = open(fname, 'r')
    cont = file.read()
    return cont

def count_levels(inst, find_basement=False ):
    count = 0
    for i,  level in enumerate(inst):
        if level == '(':
            count +=1
        elif level == ')':
            count -=1

        if find_basement:
            if count==-1:
                return i+1

    return count




if __name__=="__main__":


    fname = sys.argv[1]
    cont = read_file(fname)
    level = count_levels(cont)
    basement = count_levels(cont, find_basement=True)

    print(f'After following the instructions in {fname},')
    print(f'Santa will end up on level {level}.')
    print(f'Santa will enter the basement after {basement} instructions')

