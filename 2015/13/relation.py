#!/usr/bin/env python3

import pprint
import itertools

def make_dict(fname='input.prod', add_me=False):

    rel = {}

    file = open(fname, 'r')
    cont = file.read()
    file.close()

    for line in cont.split('\n')[:-1]:
        sentance = line.split()
        p1 = sentance[0]
        p2 = sentance[-1][:-1]
        if sentance[2]=='gain':
            points = int(sentance[3])
        else:
            points = -1*int(sentance[3])


        if not p1 in rel.keys():
            rel[p1]={}
        if not p2 in rel[p1].keys():
            rel[p1][p2] = {}

        rel[p1][p2] = points

    if add_me:

        rel['me'] = {}
        for p1 in rel.keys():
            rel[p1]['me'] = 0
            rel['me'][p1] = 0



    return rel



def calc_table_happy(table, rel):

    happy = 0
    for p1, p2 in zip(table, table[1:]):
        happy += rel[p1][p2] + rel[p2][p1]

    happy +=  rel[table[0]][table[-1]] + rel[table[-1]][table[0]]

    return happy






if __name__ == '__main__':

    rel = make_dict()


    names = list(rel.keys())

    tables = itertools.permutations(names)

    current_happy = 0
    for table in tables:
        happy = calc_table_happy(list(table), rel)
        if happy > current_happy:
            current_happy = happy

    print(current_happy)




    rel = make_dict(add_me=True)


    names = list(rel.keys())

    tables = itertools.permutations(names)

    current_happy2= 0
    for table in tables:
        happy = calc_table_happy(list(table), rel)
        if happy > current_happy2:
            current_happy2 = happy

    print(current_happy2)


    print(current_happy2 - current_happy)










