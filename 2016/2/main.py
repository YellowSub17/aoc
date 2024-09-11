




import numpy as np



KEYPAD = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])



X = np.array( [ [ -1, 0, 1],
                [ -1, 0, 1],
                [ -1, 0, 1]])

Y = np.array( [ [ 1,   1,  1],
                [ 0,   0,  0],
                [ -1, -1, -1]])

with open('./input.prod', 'r') as f:
    insts = f.read().split('\n')[:-1]




def parse_inst(inst):

    x = inst.count('R')-inst.count('L')
    y = inst.count('U')-inst.count('D')

    return x, y


print(parse_inst(insts[0]))






