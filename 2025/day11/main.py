#23:59
#00:13







connections = {}

with open('./input.test2') as f:
    contents = f.read().split('\n')[:-1]

for line in contents:
    sp = line.split(' ')
    connections[sp[0][:-1]] = sp[1:]



solved_paths = set()
def solve(current_connection=None,history=[]):
    # print(current_connection, history)


    if current_connection is None:
        current_connection = 'you'

    next_history = history + [current_connection]

    if current_connection == 'out':
        solved_paths.add(tuple(next_history))
        return None



    for next_connection in connections[current_connection]:

        x = solve(next_connection, next_history)


out = solve()

print(len(solved_paths))

