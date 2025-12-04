

import numpy as np
fname = './input.prod'

with open(fname) as f:
    print(f'Loading {fname}')
    contents = f.read().split('\n')[:-1]

NY = len(contents)

jolts = np.zeros( NY)

banks =  list(map(list, contents))

digits = 12

# banks = ['111987654321111']
for i_row, bank in enumerate(banks):
    print()
    # print(f'row:\t\t{i_row}')
    row_arr = np.array( list(map(int, bank)))

    print(f'row_arr:\t\t{row_arr}')

    joltage = 0

    start = 0
    end = len(row_arr) -12


    for i_digit in range(digits, 0, -1):
        end = len(row_arr) - i_digit +1
        print(f'\t{i_digit} dig, start: {start}, end: {end}')


        row_sub_arr = row_arr[start:end]
        print(f'\trow_sub:\t', end='')
        print(f'{row_arr[:start]}//{row_arr[start:end]}//{row_arr[end:]}')


        max_of_row_sub = np.max(row_sub_arr)
        print('found next digit: ', max_of_row_sub)

        max_of_row_ind = np.where(row_sub_arr == max_of_row_sub)[0].min()

        joltage += max_of_row_sub*10**(i_digit-1)
        print(f'\tcurrent jolts: {joltage}')

        start= start+max_of_row_ind+1

    print(joltage)

    jolts[i_row]=  joltage


print(sum(jolts))



#172895362045136 too low
#172981362045136 answer



