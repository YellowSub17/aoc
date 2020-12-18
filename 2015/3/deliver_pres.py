#!/usr/bin/env python3
import os
import sys



def read_file(fname):
    file = open(fname, 'r')
    cont =  file.read()
    return cont



def deliver(cont):

    x = 0
    y = 0
    visted = { (x,y) } 
    for direction in cont:

        if direction =="<":
            x -= 1
        elif direction == ">":
            x +=1
        elif direction == "^":
            y +=1

        elif direction == "v":
            y -=1

        visted.add( (x,y))

    return visted

def split_instructions(cont):
    
    a = ''
    b = ''
    for i,letter in enumerate(cont):

        if i%2==0:
            a+=letter
        else:
            b+=letter

    return a, b










if __name__ == "__main__":


    fname = sys.argv[1]
    cont = read_file(fname)


    visted = deliver(cont)

    print(f'After following the elfs instructions, Santa visits {len(visted)} houses')


    santa_cont, robo_cont = split_instructions(cont)

    santa_visited = deliver(santa_cont)
    robo_visted = deliver(robo_cont)

    santa_visited.update(robo_visted)

    print(f'The following year, Santa and Robo-Santa visit {len(santa_visited)} houses.')

