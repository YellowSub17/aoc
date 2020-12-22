#!/usr/bin/env python3
import sys




def create_grid(nx):

    grid = []
    for i in range(nx):
        row = []
        for j in range(nx):
            row.append(0)

        grid.append(row)

    return grid





def do_instruct(grid, inst, start, end):

    for x in range(int(start[0]), int(end[0])+1):
        for y in range(int(start[1]), int(end[1])+1):

            if inst =='off':
                grid[x][y] -=1
                if grid[x][y] <0:
                    grid[x][y] =0

            elif inst =='on':
                grid[x][y] +=1
            elif inst =='toggle':
                grid[x][y] +=2
                # grid[x][y] +=1
                # grid[x][y] = grid[x][y]%2

    return grid


def parse_line(line):
    words = line.split(' ')
    end = words[-1].split(',')

    if 'toggle' in words:
        start = words[1].split(',')
        return 'toggle', start, end

    start = words[2].split(',')
    if 'on' in words:
        return 'on', start, end
    else:
        return 'off', start, end



if __name__ == "__main__":

    fname = sys.argv[1]
    file = open(fname, 'r')
    cont = file.read()
    lines = cont.split('\n')[:-1]
    
    grid = create_grid(1000)

    for i, line in enumerate(lines):
        print(i)
        inputs = parse_line(line)

        grid = do_instruct(grid, *inputs)


    count = 0
    for i in range(1000):
        count += sum(grid[i])

    print(grid)

    print(count)
            



    # grid = create_grid(10)
    # grid = do_instruct(grid, 'on', [0, 0], [8, 8])
    # grid = do_instruct(grid, 'toggle', [0, 0], [7, 7])
    # grid = do_instruct(grid, 'off', [0, 0], [5, 5])
    # grid = do_instruct(grid, 'off', [0, 0], [5, 5])
    # grid = do_instruct(grid, 'off', [0, 0], [5, 5])
    # grid = do_instruct(grid, 'off', [0, 0], [5, 5])
    # grid = do_instruct(grid, 'off', [0, 0], [5, 5])
    # grid = do_instruct(grid, 'off', [0, 0], [5, 5])

    # for x in range(10):

        # print(grid[x])





