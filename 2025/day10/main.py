

import numpy as np
import itertools





with open('./input.prod') as f:
    contents = f.read().split('\n')[:-1]






class Machine:


    def __init__(self, input_str):

        self.input_str = input_str

        sp = self.input_str.split(' ')

        self.target_lights = []
        for light in sp[0][1:-1]:
            if light == '#':
                self.target_lights.append(True)
            else:
                self.target_lights.append(False)
        self.target_lights = np.array(self.target_lights)

        self.current_lights = np.array([False]*self.target_lights.size)


        self.actions = []
        for action in sp[1:-1]:
            act = np.array( [False] * self.current_lights.size)
            for c in action[1:-1:2]:
                act[int(c)] = True

            self.actions.append(act)


    def do_action(self, i):
        self.current_lights = np.logical_xor( self.current_lights, self.actions[i])

    def generate_action_seqs(self, n):
        action_inds = np.arange(0, len(self.actions))
        return list(itertools.combinations_with_replacement(action_inds, n))

    def find_min_button_presses(self):

        count =0
        done_flag = False
        while not done_flag:
            count+=1

            for action_seq in self.generate_action_seqs(count):
                self.current_lights = np.array([False]*self.target_lights.size)
                for action_i in action_seq:
                    self.do_action(action_i)

                if np.all(self.current_lights== self.target_lights):
                    # print(f'Done! in {count} button presses')
                    # print(f'{action_seq=}')
                    # print(f'curr:\t{self.current_lights}')
                    # print(f'targ:\t{self.target_lights}')
                    # for action_i in action_seq:
                        # print(self.actions[action_i])
                    done_flag=True
                    break
        return count











ans = []
for line in contents:
    m = Machine(line)
    ans.append(m.find_min_button_presses())


print(sum(ans))
    # while True:







# print(f'{m.current_lights=}')
# print(f'{m.actions[-1]=}')
# m.do_action(m.actions[-1])

# print(f'{m.current_lights=}')
# print(f'{m.actions[-2]=}')
# m.do_action(m.actions[-2])
# print(f'{m.current_lights=}')



