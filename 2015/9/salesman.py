#!/usr/bin/env python3





import pprint
import itertools

if __name__ == '__main__':

    file = open('input.prod', 'r')
    cont = file.read()
    lines = cont.split('\n')[:-1]

    places = {}
    max_dist = 0
    for line in lines:
        elems = line.split(' ')
        if not elems[0] in places.keys():
            places[elems[0]] = {}
        if not elems[2] in places.keys():
            places[elems[2]] = {}

        places[elems[0]][elems[2]]= int(elems[-1])
        places[elems[2]][elems[0]]= int(elems[-1])

        max_dist +=places[elems[0]][elems[2]]
        max_dist +=places[elems[2]][elems[0]]




    ##part 1
    paths = itertools.permutations(list(places.keys()))

    for path in paths:
        dist = 0
        for place_start, place_end in zip(path, path[1:]):
            dist += places[place_start][place_end]
            if dist > max_dist:
                break
        if dist < max_dist:
            max_dist = dist
            print(f'Shortest distance: {max_dist}')



    paths = itertools.permutations(list(places.keys()))
    max_dist=0
    for path in paths:
        dist = 0
        for place_start, place_end in zip(path, path[1:]):
            dist += places[place_start][place_end]
        if dist > max_dist:
            max_dist = dist
            print(f'Longest distance: {max_dist}')






        


