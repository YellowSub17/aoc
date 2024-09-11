


def run_step(inst, direction, x, y):

    visited = []
    turn, n_steps = inst[0], int(inst[1:])

    if direction=='N':
        if turn =='L':
            new_direction = 'W'
            new_x = x-n_steps
            new_y = y

            for x_prime in range(x, new_x, -1):
                visited.append( (x_prime, new_y))

        elif turn == 'R':
            new_direction = 'E'
            new_x = x+n_steps
            new_y = y

            for x_prime in range(x, new_x, +1):
                visited.append( (x_prime, new_y))

    elif direction=='S':
        if turn =='L':
            new_direction = 'E'
            new_x = x+n_steps
            new_y = y

            for x_prime in range(x, new_x, +1):
                visited.append( (x_prime, new_y))

        elif turn == 'R':
            new_direction = 'W'
            new_x = x-n_steps
            new_y = y

            for x_prime in range(x, new_x, -1):
                visited.append( (x_prime, new_y))


    if direction=='E':
        if turn =='L':
            new_direction = 'N'
            new_y = y+n_steps
            new_x = x

            for y_prime in range(y, new_y, +1):
                visited.append( (new_x, y_prime))

        elif turn == 'R':
            new_direction = 'S'
            new_y = y-n_steps
            new_x = x

            for y_prime in range(y, new_y, -1):
                visited.append( (new_x, y_prime))

    elif direction=='W':
        if turn =='L':
            new_direction = 'S'
            new_y = y-n_steps
            new_x = x

            for y_prime in range(y, new_y, -1):
                visited.append( (new_x, y_prime))

        elif turn == 'R':
            new_direction = 'N'
            new_y = y+n_steps
            new_x = x

            for y_prime in range(y, new_y, +1):
                visited.append( (new_x, y_prime))





    return new_direction, new_x, new_y, visited



DIRECTION = 'N'

X=0
Y=0
FULL_PATH = []

with open('./input.prod', 'r') as f:
    steps = f.read()[:-1].split(', ')

print(f'Starting at: {X=} {Y=} facing {DIRECTION}')



first_location_visited_twice = None
for step in steps:



    DIRECTION, X, Y, visited = run_step(step, DIRECTION, X, Y)

    for visit in visited:
        if visit in FULL_PATH:
            print(f'Found location that has been visited before!')
            print(f'Location: {visit=}')
            print(f'Distance: {abs(visit[0]) + abs(visit[1])}')

            if first_location_visited_twice is None:
                first_location_visited_twice = visit

        FULL_PATH.append(visit)



    print(f'After {step}, now at: {X=} {Y=} facing {DIRECTION}')


print(f'Ending at: {X=} {Y=} facing {DIRECTION}')
print(f'Total blocks: {abs(X)+abs(Y)}')


print(f'First Location that was visited twice: {first_location_visited_twice}')
print(f'Distance: {abs(first_location_visited_twice[0]) + abs(first_location_visited_twice[1])}')




