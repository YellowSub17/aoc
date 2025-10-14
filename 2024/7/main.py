
import itertools

# operations = ['*', '+',]

# with open('./input.prod', 'r') as f:
    # lines = f.read().split('\n')[:-1]


# def split_input(line):
    # calib = int(line.split(':')[0])
    # inputs = list(map(int, line.split(' ')[1:]))
    # return calib, inputs


# def gen_operations(inputx):
    # return itertools.product(operations, repeat=len(inputx[1])-1)

# def gen_ans(inputx):

    # ops_sets = gen_operations(inputx)

    # reses = []
    # for op_set in ops_sets:
        # res = inputx[1][0]
        # for op, inp in zip(op_set, inputx[1][1:]):
            # res = eval(f'{res}{op}{inp}')
        # if res == inputx[0]:
            # return res

    # return 0

# def gen_ans_p2(inputx):

    # ops_sets = gen_operations(inputx)

    # reses = []
    # for op_set in ops_sets:
        # res = inputx[1][0]
        # for op, inp in zip(op_set, inputx[1][1:]):
            # res = eval(f'{res}{op}{inp}')
        # if res == inputx[0]:
            # return res

    # return 0


# lines = list(map(split_input, lines))

# anss = map(gen_ans, lines)

# out = sum(anss)

# print(out)











operations = ['*', '+', '||']

with open('./input.prod', 'r') as f:
    lines = f.read().split('\n')[:-1]


def split_input(line):
    calib = int(line.split(':')[0])
    inputs = list(map(int, line.split(' ')[1:]))
    return calib, inputs


def gen_operations(inputx):
    return itertools.product(operations, repeat=len(inputx[1])-1)

def gen_ans(inputx):

    ops_sets = gen_operations(inputx)

    reses = []
    for op_set in ops_sets:
        res = inputx[1][0]
        for op, inp in zip(op_set, inputx[1][1:]):

            # if res> inputx[0]:
                # return 0

            if op=='||':
                res = int(f'{res}{inp}')
            else:
                res = eval(f'{res}{op}{inp}')

        if res == inputx[0]:
            # print(res)
            return res

    return 0


# lines = list(map(split_input, lines))
# anss = map(gen_ans, lines)


anss = map(gen_ans, map(split_input, lines))
out = sum(anss)

print(out)



