#!/usr/bin/env python3
import json



def recur(elem, count=0):

    if type(elem)==int:
        count +=elem

    elif type(elem)==dict:
        if 'red' in elem.values():
            return count
        for key in elem.keys():
            inner_count= recur(elem[key], count=0)
            count +=inner_count

    elif type(elem)==list:
        for a in elem:
            inner_count= recur(a, count=0)
            count +=inner_count

    return count






if __name__ == '__main__':


    fname = 'input.prod'
    file = open(fname, 'r')
    js = json.load(file)



    y = recur(js)

    print(y)




