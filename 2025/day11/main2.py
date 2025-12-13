






connections = {}

with open('./input.prod') as f:
    contents = f.read().split('\n')[:-1]

for line in contents:
    sp = line.split(' ')
    connections[sp[0][:-1]] = sp[1:]

connections['out'] = []






def solve(current_connection, end_connection, cache={}):

    if current_connection == end_connection:
        return 1

    else:
        if current_connection in cache:
            return cache[current_connection]

        else:
            ans = 0
            for next_connection in connections[current_connection]:
                ans += solve(next_connection, end_connection, cache=cache)
            cache[current_connection] = ans

            return ans



# print('part1:')
# c1 = {}
# count = solve('you', 'out', c1)
# print(count)

print('part2:')

# x1 = solve('svr', 'dac')*solve('dac', 'fft')*solve('fft', 'out')
# x2 = solve('svr', 'fft')*solve('fft', 'dac')*solve('dac', 'out')
# print(x1, x2)

# x2 = solve('svr', 'dac', cache=c2)
# x2 = solve('dac', 'fft', cache=c2)



c1 = {}
x1 = solve('svr', 'fft', cache=c1)
c2 = {}
x2 = solve('fft', 'dac', cache=c2)
c3 = {}
x3 = solve('dac', 'out', cache=c3)


print(x1*x2*x3)

# x2 = solve('svr', 'fft')


# print(x2)
