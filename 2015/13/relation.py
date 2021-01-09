#!/usr/bin/env python3

import pprint
import itertools

def make_dict(fname='input.prod'):

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

    return rel



def find_best_partner(p1, rel, skip=[]):
    current_points = 0
    x1 = ''
    for p2 in rel[p1].keys():
        if p2 in skip:
            continue
        pair_points = rel[p1][p2] + rel[p2][p1]
        if pair_points > current_points:
            current_points = pair_points
            x1 = str(p2)

    return x1


def find_best_match(rel):

    x1 = ''
    x2 = ''
    current_points = 0
    for p1 in rel.keys():
        for p2 in rel[p1].keys():

            if p1 ==p2:
                continue

            pair_points = rel[p1][p2] + rel[p2][p1]
            if pair_points > current_points:
                current_points = pair_points
                x1 = str(p1)
                x2 = str(p2)

    return x1,x2






if __name__ == '__main__':

    rel = make_dict()
    table = []

    names = list(rel.keys())

    x, y = find_best_match(rel)
    print('The best pairing is:', x, 'and', y)
    table.append(x)
    table.append(y)
    print('The table is now:', table)

    for i in range(len(names)-2):

        y = find_best_partner(table[-1], rel, skip=table)
        print('The two best partners for', table[-1], 'is', y)
        table.append(y)
        print('The table is now:', table)



    points  = 0
    for p1, p2 in zip(table, table[1:]):
        print(p1,p2)
        points += rel[p1][p2] + rel[p2][p1]

    points += rel[table[-1]][table[0]] + rel[table[0]][table[-1]]
    print(points)








    # print(rel)
    # print(rel[z][x] + rel[x][z])
    # print(rel[z][y] + rel[y][z])








