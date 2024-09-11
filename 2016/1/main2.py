


def run_step(inst, direction, x, y):

    # new_y = y
    # new_x = x
    
    turn, n_steps = inst[0], int(inst[1:])

    if direction=='N':
        if turn =='L':
            new_direction = 'W'
            new_x = x-n_steps
            new_y = y
        elif turn == 'R':
            new_direction = 'E'
            new_x = x+n_steps
            new_y = y

    elif direction=='S':
        if turn =='L':
            new_direction = 'E'
            new_x = x+n_steps
            new_y = y
        elif turn == 'R':
            new_direction = 'W'
            new_x = x-n_steps
            new_y = y


    if direction=='E':
        if turn =='L':
            new_direction = 'N'
            new_y = y+n_steps
            new_x = x
        elif turn == 'R':
            new_direction = 'S'
            new_y = y-n_steps
            new_x = x

    elif direction=='W':
        if turn =='L':
            new_direction = 'S'
            new_y = y-n_steps
            new_x = x
        elif turn == 'R':
            new_direction = 'N'
            new_y = y+n_steps
            new_x = x





    return new_direction, new_x, new_y



DIRECTION = 'N'

X=0
Y=0

with open('./input.test', 'r') as f:
    steps = f.read()[:-1].split(', ')

print(f'Starting at: {X=} {Y=} facing {DIRECTION}')


for step in steps:



    DIRECTION, X, Y = run_step(step, DIRECTION, X, Y)

    print(f'After {step}, now at: {X=} {Y=} facing {DIRECTION}')


print(f'Ending at: {X=} {Y=} facing {DIRECTION}')
print(f'Total blocks: {abs(X)+abs(Y)}')





