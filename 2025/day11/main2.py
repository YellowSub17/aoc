






connections = {}

with open('./input.prod') as f:
    contents = f.read().split('\n')[:-1]

for line in contents:
    sp = line.split(' ')
    connections[sp[0][:-1]] = sp[1:]


reverse_connections = {}

for k, v in connections.items():
    for c in v:
        if c not in reverse_connections:
            reverse_connections[c] = []
        reverse_connections[c].append(k)

print(reverse_connections)


solved_paths = set()
def solve(current_connection=None,history=[]):


    if current_connection is None:
        current_connection = 'svr'


    # print(current_connection)
    # print(history)
    # breakpoint()


    next_history = history + [current_connection]

    if current_connection == 'out':

        if 'fft' in history and 'dac' in history:
            solved_paths.add(tuple(next_history))
        return None

    print(len(solved_paths))


    for next_connection in connections[current_connection]:

        if next_connection in next_history:
            print('History repeats!')
            return None

        x = solve(next_connection, next_history)


out = solve()

count = 0
for path in solved_paths:
    if 'fft' in path and 'dac' in path:
        count +=1
    print(path)


print(count)

