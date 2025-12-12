

import numpy as np
import itertools
from scipy.optimize import linprog





with open('./input.prod') as f:
    contents = f.read().split('\n')[:-1]



class Machine:


    def __init__(self, input_str):

        self.input_str = input_str

        sp = self.input_str.split(' ')

        self.target_jolts = []
        for jolt_target in sp[-1][1:-1].split(','):
            self.target_jolts.append(int(jolt_target))


        self.target_jolts = np.array(self.target_jolts, dtype=int)

        # self.current_jolts = np.zeros(self.target_jolts.shape, dtype=int)

        actions = []
        for action in sp[1:-1]:
            act = np.zeros( self.target_jolts.shape, dtype=int)
            for c in action[1:-1:2]:
                act[int(c)] = 1
            actions.append(act)

        # self.actions.sort(key=lambda s: s.sum(), reverse=True)

        self.actions_arr = np.array(actions)












    def solve(self,):


        A = self.actions_arr.copy().T

        c = np.ones(A.shape[1], dtype=int)

        b = self.target_jolts.copy()


        print(c)
        print(A)
        print(b)

        # res = linprog( c, A_eq=A, b_eq=b)
        res = linprog( c, A_eq=A, b_eq=b, integrality=1)

        return res.x






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
            









# m = Machine(contents[0])


# print(m.solve())
# print('###')
# m.solve()
# print(m.current_min)


ans=  []
for line in contents:
    m = Machine(line)
    s = m.solve()

    print(s, sum(s))

    ans.append(sum(s))

    # breakpoint()
    # ans.append(np.sum(np.round(m.solve())))

print(sum(ans))

#21004 too low





# max_button_presses = np.zeros(self.target_jolts.shape, dtype=int)


