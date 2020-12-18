#!/usr/bin/env python3
import sys
import os




def calc_area(l, w, h):
    x = l*w
    y = w*h
    z = h*l
    area = 2*(x+y+z) + min(x,y,z)
    return area

def calc_ribbon(l, w, h):
    v = l*w*h

    long = max(l,w,h)

    perim = 2*( l+w+h-long)

    return perim +v


def get_dims(fname):
    file = open(fname, 'r')
    cont = file.read()
    dims = cont.split('\n')[:-1]
    return dims

def get_area_and_ribbon(dims):
    sum_a = 0
    ribbon = 0
    for dim in dims:
        l,w,h = dim.split('x')
        sum_a += calc_area(float(l),float(w),float(h))
        ribbon += calc_ribbon(float(l),float(w),float(h))
    return sum_a, ribbon








if __name__=='__main__':

    fname = sys.argv[1]
    dims = get_dims(fname)
    sum_a, ribbon = get_area_and_ribbon(dims)


    print(f'From the list of present dimensions in {fname},')
    print(f'the area of wrappering paper required is {sum_a} sq. feet.')
    print(f'and the total length of ribbon required is {ribbon}.')

