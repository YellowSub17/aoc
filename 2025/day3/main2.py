

import numpy as np
fname = './input.test2'

with open(fname) as f:
    print(f'Loading {fname}')
    contents = f.read().split('\n')[:-1]

NY = len(contents)

jolts = np.zeros( NY)

banks =  list(map(list, contents))

digits = 12

banks = ['987654321111119']

for i_row, bank in enumerate(banks):
    print()
    # print(f'row:\t\t{i_row}')
    row_arr = np.array( list(map(int, bank)))

    print(f'row_arr:\t\t{row_arr}')

    joltage = 0

    start_range = 0

    end_range = len(row_arr) - digits


    for i_digit in range(digits, 0, -1):
        print(f'\t{i_digit} dig, start: {start_range} end: {end_range}')


        row_sub_arr = row_arr[start_range:end_range]
        print(f'\trow_sub:\t', end='')
        print(f'{row_arr[:start_range]}//{row_arr[start_range:end_range]}//{row_arr[end_range:]}')


        max_of_row_sub = np.max(row_sub_arr)
        print('found next digit: ', max_of_row_sub)

        max_of_row_ind = np.where(row_sub_arr == max_of_row_sub)[0].min()

        joltage += max_of_row_sub*10**(i_digit-1)
        print(f'\tcurrent jolts: {joltage}')

        start_range = start_range+max_of_row_ind+1

        end_range = len(row_arr) - i_digit +2



    print(joltage)

    jolts[i_row]=  joltage


print(sum(jolts))



#172895362045136 too low


