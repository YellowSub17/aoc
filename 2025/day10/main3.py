

import numpy as np
import itertools





with open('./input.test') as f:
    contents = f.read().split('\n')[:-1]



class Machine:


    def __init__(self, input_str):

        self.input_str = input_str
        # self.cache = {():0}
        # self.dead_ends = set()
        self.solved_history = [0]*10000
        self.solve_called = 0

        sp = self.input_str.split(' ')

        self.target_jolts = []
        for jolt_target in sp[-1][1:-1].split(','):
            self.target_jolts.append(int(jolt_target))


        self.target_jolts = np.array(self.target_jolts, dtype=int)

        # self.current_jolts = np.zeros(self.target_jolts.shape, dtype=int)

        self.actions = []
        for action in sp[1:-1]:
            act = np.zeros( self.target_jolts.shape, dtype=int)
            for c in action[1:-1:2]:
                act[int(c)] = 1
            self.actions.append(act)

        self.actions.sort(key=lambda s: s.sum(), reverse=True)






    # def solve(self,):



    # def solve(self,count=0, current_jolts=None, history=[]):
        # self.solve_called +=1

        # if current_jolts is None:
            # current_jolts = np.zeros(self.target_jolts.shape, dtype=int)


        # if len(history) >= len(self.solved_history):
            # return None



        # if np.all(current_jolts == self.target_jolts):
            # print('!!!')
            # print(history)
            # print(len(history))

            # self.solved_history = list(history)
            # breakpoint()
            # return len(self.solved_history)

        # if np.any(current_jolts > self.target_jolts):
            # return None


        # print('\t', len(history), self.solve_called, current_jolts, history)

        # next_jolts = [ current_jolts + i for i in self.actions]


        # for i_nj, next_jolt in enumerate(next_jolts):
            # next_history = list(history)

            # next_history.append(i_nj)


            # s = self.solve(count+1, current_jolts=next_jolt, history = next_history)

        # return s
            









m = Machine(contents[0])
print(m.actions)
# print('###')
# m.solve()
# print(m.current_min)


# ans=  []
# for line in contents:
    # m = Machine(line)
    # print(m.actions)
    # m.solve()
    # ans.append(m.current_min)
    # print(m.solve_count)

# print(ans)





# max_button_presses = np.zeros(self.target_jolts.shape, dtype=int)


