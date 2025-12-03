

import numpy as np
fname = './input.test'

with open(fname) as f:
    print(f'Loading {fname}')
    contents = f.read().split('\n')[:-1]

# print(contents)
NX = len(contents[0]) +1
NY = len(contents)

arr = np.zeros( (NY, NX))
jolts = np.zeros( NY)

banks =  list(map(list, contents))




digits = 3

for i_row, bank in enumerate(banks):
    print()
    print(f'row:\t\t{i_row}')
    row_arr = np.array( list(map(int, bank)) + [0])

    print(f'row_arr:\t\t{row_arr}')
    # arr[i_row] = row_arr

    joltage = 0

    start_range = 0

    end_range = -1*(digits-1)


    for i_digit in range(digits, 0, -1):
        print(f'\t{i_digit} dig, {start_range} {end_range}')


        row_sub_arr = row_arr[start_range:end_range]
        print(f'\trow_sub:\t{row_sub_arr}')


        max_of_row_sub = np.max(row_sub_arr)

        max_of_row_ind = np.where(row_sub_arr == max_of_row_sub)[0].min()

        joltage += max_of_row_sub*10**(i_digit-1)

        start_range = start_range+max_of_row_ind+1
        end_range = -1*(i_digit-1)



    print(joltage)

    jolts[i_row]=  joltage

print(sum(jolts))



# print(arr)



# def find_max_joltage(arr, current_joltage, n):
    # print()
    # print('finding max joltage: ',  arr,  current_joltage, n)

    # if n==0:
        # return current_joltage

    # max_of_row = np.max(row_arr)
    # ind = np.where(row_arr ==np.max(row_arr))[0].min()
    # print(f'{ind=}')

    # if ind > len(arr) -n:
        # print('idk')
        # return -1

    # new_joltage= current_joltage + (10**(n-1))*row_arr[ind]
    # print(new_joltage)

    # sub_arr = row_arr[ind+1:]

    # return find_max_joltage(sub_arr, new_joltage, n-1)


# print(find_max_joltage(arr[0], 0, 2))






# print(banks)

