
import numpy as np



dirs = 'NESW'
dirs_emoji = '^>V<'






class State:

    def __init__(self, arena):


        self.arena = arena.copy()
        self.dir_log = np.ones(self.arena.shape)*9
        self.i_dir = 0

        self.loop_found = False

        self.current_x = np.where(self.arena=='^')[0][0]
        self.current_y = np.where(self.arena=='^')[1][0]

        self.last_turns =[(-1,-2), (-3,-4), (-5,-6), (-7,-8),
                          (-2,-1), (-4,-3), (-6,-5), (-8,-7),]


    @property
    def current_dir(self):
        return dirs[self.i_dir]

    @property
    def current_dir_emoji(self):
        return dirs_emoji[self.i_dir]

    @property
    def nvists(self):
        return len(np.where(self.arena=='.')[0]) +1

    def look(self):
        if self.current_dir=='N':
            return self.arena[self.current_x-1, self.current_y]
        if self.current_dir=='E':
            return self.arena[self.current_x, self.current_y+1]
        if self.current_dir=='S':
            return self.arena[self.current_x+1, self.current_y]
        if self.current_dir=='W':
            return self.arena[self.current_x, self.current_y-1]

    def move(self):
        if self.current_dir=='N':
            self.current_x -=1
        if self.current_dir=='E':
            self.current_y +=1
        if self.current_dir=='S':
            self.current_x +=1
        if self.current_dir=='W':
            self.current_y -=1




    def progress(self):
        self.arena[self.current_x, self.current_y] = '.'





        self.dir_log[self.current_x, self.current_y] = self.i_dir

        match self.look():
            case ' ' | '.':
                self.move()

            case '#':
                self.i_dir +=1
                self.i_dir = self.i_dir%4
                self.last_turns.append( (int(self.current_x), int(self.current_y)) )
                self.last_turns.pop(0)

                
        if self.dir_log[self.current_x, self.current_y] == self.i_dir:
            self.loop_found = True
        if self.last_turns[0] == self.last_turns[1] and self.last_turns[2]==self.last_turns[3]:
            self.loop_found=True

        if self.last_turns[0] == self.last_turns[4] and self.last_turns[1]==self.last_turns[5] and self.last_turns[2] == self.last_turns[6] and self.last_turns[3]==self.last_turns[7]:
            self.loop_found=True

        self.arena[self.current_x, self.current_y] = self.current_dir_emoji





    def __str__(self):
        s = ''
        s +=f'DIRECTION: {self.current_dir}\n'
        s +=f'XY: {self.current_x}, {self.current_y}\n'



        for i in self.arena:
            s+=''.join(i)+'\n'
        s+= f'{self.last_turns[:4]}\n'
        s+= f'{self.last_turns[4:]}\n'
        # for i in self.dir_log:
            # s+=''.join(str(i))+'\n'
        return s










if __name__=='__main__':

    import os
    import time


    with open('./input.prod', 'r') as f:
        cont = f.read().split('\n')[:-1]
    arena = np.array([list(line) for line in cont])
    arena = np.pad(arena, 1, 'constant', constant_values='%')


    arena[arena=='.'] = ' '



##part1

    # s = State(arena)
    # while s.look() !='%':
            # s.progress()
            # time.sleep(0.1)
            # os.system('clear')
            # print(s)

    # print( 'Part1 answer', s.nvists)


#part2


# # ###i12 j52
# # ###i34 j113
    # s = State(arena)
    # s.arena[34,113]='#'
    # counter = 0
    # while s.look() !='%' and not s.loop_found:
        # counter+=1
        # s.progress()
        # if counter % 100 == 0:
            # os.system('clear')
            # print(s)




    count = 0

    for i in range(1, arena.shape[0]-1):
        print(f'{i}\t/{arena.shape[0]-2}')
        for j in range(1, arena.shape[1]-1):
            print(i, j, end='\r')

            s = State(arena)
            if s.current_x==i and s.current_y==j:
                continue

            s.arena[i,j]='#'



            while s.look() !='%' and not s.loop_found:
                s.progress()
                # print(s.last_turns, end='\r')
                # time.sleep(0.1)

            if s.loop_found:

                count +=1


    print()
    print(f'Found {count} loops')


















