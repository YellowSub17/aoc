
#18:08
#p1: 19:06

import numpy as np
import matplotlib.pyplot as plt
import time



with open('./input.prod') as f:

    contents = f.read().split('\n')[:-1]
rows = []
for row in contents:
    rows.append(list(row))

char_arr = np.array(rows)
char_arr[np.where(char_arr=='S')] = '|'






#           0 for rhs processing, 1 for lhs processing, 2 for complete tree 
#               |
#               |   number of terminations from the branch
#               |       |
## (r,c) : [visits, count]

splits_cache = {}





class Sim:

    def __init__(self, char_arr,):
        self.char_arr = char_arr
        self.nrows = self.char_arr.shape[0]
        self.ncols = self.char_arr.shape[1]
        self.total_timelines = 0


    def solve(self, start=None, history = []):


        if start is None:
            col = int(np.where(self.char_arr[0]=='|')[0][0])
            start = (0, col)

        row = start[0]
        col = start[1]

        #while there is empty space below
        while self.char_arr[row, col] == '.':
            row+=1
            if row >= self.nrows: #if you hit the bottom
                return 1

        #at this point, we hit a splitter at the end of the while loop

        #if the current split is not in the cache
        if (row, col) not in splits_cache:
            next_history = history + [(row,col)]

            #we need to solve the lhs and rhs of the branch
            lhs = self.solve(start=(row, col-1), history=next_history)
            rhs = self.solve(start=(row, col+1), history=next_history)

            #add it to the cache
            splits_cache[(row, col)] = lhs+rhs
            return lhs+rhs

        else: #if the current split is in the cache, return the precalc'd value
            return splits_cache[(row, col)]





    def __str__(self):
        s = ''
        s+= f'STEP: {self.i_row} \t SPLITS: {self.last_splits}\n'
        for row in self.char_arr:
            for val in row:
                s+= val

            s+='\n'
        return s


    def show_path(self, start,  history):

        path_map = self.char_arr.copy()
        path_map[start[0], start[1]] = '*'

        for i, split in enumerate(history):
            path_map[split[0], split[1]] = str( i%10)

        s = ''
        for row in path_map:
            for val in row:
                s+= val
            s+='\n'

        print(s)





















finished_count = 0

init_s = Sim(char_arr)

s = init_s.solve( (2, int(init_s.ncols/2)), [])
print(s)

# print(init_s.total_timelines)





