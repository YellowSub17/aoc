




import numpy as np



KEYPAD = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])



def parse_sqr_inst(inst, current_x, current_y):

    new_x = current_x
    new_y = current_y

    for char in inst:

        match char:
            case 'U':
                new_y = min(1, new_y+1)
            case 'D':
                new_y = max(-1, new_y-1)

            case 'R':
                new_x = min(1, new_x+1)
            case 'L':
                new_x = max(-1, new_x-1)



    key_press = KEYPAD[-new_y+1, new_x+1]

    return new_x, new_y, key_press



with open('./input.prod', 'r') as f:
    insts = f.read().split('\n')[:-1]



# X = 0
# Y = 0
# print('Square keypad key:')
# for inst in insts:
    # X, Y, key_press = parse_sqr_inst(inst, X, Y)

    # print(key_press, end='')
# print()







# * * * * * * *
# * * * 1 * * *
# * * 2 3 4 * *
# * 5 6 7 8 9 *
# * * A B C * *
# * * * D * * *
# * * * * * * *



### URDL
next_steps = {
              '1':'1131',
              '2':'2362',
              '3':'1472',
              '4':'4483',
              '5':'5655',
              '6':'27A5',
              '7':'38B6',
              '8':'49C7',
              '9':'9998',
              'A':'6BAA',
              'B':'7CDA',
              'C':'8CCB',
              'D':'BDDD',
             }



def find_next_key(current_key, direction):
    match direction:
        case 'U':
            ind = 0
        case 'R':
            ind = 1
        case 'D':
            ind = 2
        case 'L':
            ind = 3

    return next_steps[current_key][ind]




KEY = '5'

print('Larger keypad key:')
for inst in insts:

    for DIRECTION in inst:
        KEY = find_next_key(KEY, DIRECTION)

    print(KEY, end='')
print()






