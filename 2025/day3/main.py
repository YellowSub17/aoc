

import numpy as np
fname = './input.prod'

with open(fname) as f:
    print(f'Loading {fname}')
    contents = f.read().split('\n')[:-1]

# print(contents)
NX = len(contents[0])
NY = len(contents)

arr = np.zeros( (NY, NX))
jolts = np.zeros( NY)

banks =  list(map(list, contents))
for i_row, bank in enumerate(banks):
    print()
    print(f'row: {i_row}')
    row_arr = np.array( list(map(int, bank)))
    arr[i_row] = row_arr


    max_of_row = np.max(row_arr)
    tens_ind = np.where(row_arr ==np.max(row_arr))[0].min()
    if tens_ind != NX-1:
        row_sub_arr = row_arr[tens_ind+1:]

        ones_ind = np.where(row_sub_arr ==np.max(row_sub_arr))[0].min()+tens_ind+1

        print(row_arr)
        print(row_sub_arr)
    else:

        print(row_arr)

        tens_ind = np.where(row_arr[:-1] ==np.max(row_arr[:-1]))[0].min()
        ones_ind = -1


    print(tens_ind, ones_ind)
    print(row_arr[tens_ind], row_arr[ones_ind])

    jolts[i_row]=  10*row_arr[tens_ind] + row_arr[ones_ind]

print(sum(jolts))








# print(banks)

