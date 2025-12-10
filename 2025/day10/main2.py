

import numpy as np
import itertools





with open('./input.prod') as f:
    contents = f.read().split('\n')[:-1]







class Machine:


    def __init__(self, input_str):

        self.input_str = input_str
        self.cache = {():0}
        self.dead_ends = set()

        sp = self.input_str.split(' ')

        self.target_jolts = []
        
        for jolt_target in sp[-1][1:-1].split(','):
            self.target_jolts.append(int(jolt_target))




        self.target_jolts = np.array(self.target_jolts, dtype=int)
        self.min_target = self.target_jolts.min()
        self.current_jolts = np.zeros(self.target_jolts.shape, dtype=int)

        self.actions = []
        for action in sp[1:-1]:
            act = np.zeros( self.current_jolts.shape, dtype=int)
            for c in action[1:-1:2]:
                act[int(c)] = 1
            self.actions.append(act)



        # print(self.target_jolts)
        # print(self.actions)




    def do_action_seq(self, seq):

        # print('Attempting to run seq:', seq)

        self.current_jolts = np.zeros(self.target_jolts.shape, dtype=int)

        if seq[:-1] in self.cache:

            # print(f'Found {seq[:-1]} in cache, loading jolts {self.cache[seq[:-1]]}')
            self.current_jolts = np.array(self.cache[seq[:-1]])
            # print(f'completing action {seq[-1]}')

            self.current_jolts = self.current_jolts + self.actions[seq[-1]]

        else:
            # print('Could not find cached result, running seq')
            for i in seq:
                self.current_jolts = self.current_jolts +  self.actions[i]

        # print(f'Adding {seq} in cache with value {self.current_jolts}')

        if np.where(self.current_jolts>self.target_jolts)[0].size>0:
            self.dead_ends.add(seq)
        else:
            self.cache[seq] = self.current_jolts.copy()

    def generate_action_seqs(self, n):
        action_inds = [i for i in range(0, len(self.actions)) ]
        all_combos = itertools.combinations_with_replacement(action_inds, n)
        filt_combos = itertools.filterfalse(lambda seq: seq[:-1] in self.dead_ends, all_combos)
        
        return list(filt_combos)

    def find_min_button_presses(self):

        count =self.min_target
        done_flag = False
        while not done_flag:
            count+=1






            action_seqs = self.generate_action_seqs(count)


            print('\t', count, len(action_seqs), len(self.dead_ends), len(self.cache))

            for action_seq in action_seqs:
                self.do_action_seq(action_seq)
                # print()

                # print('##')
                # print(action_seq)
                # print(self.current_jolts, self.target_jolts)
                # # print(np.where(self.current_jolts>self.target_jolts)[0])
                # print('##')

                # if np.all(self.current_jolts ==self.target_jolts):
                    # print(action_seq,  current_jolts, self.target_jolts)

                if np.all(self.current_jolts== self.target_jolts):

                    done_flag=True
                    break
            # breakpoint()

            # keys = list(self.cache.keys())
            # for key in keys:
                # if key not in action_seqs:
                    # del self.cache[key]

            for key in self.generate_action_seqs(count -1):
                if key in self.cache:
                    del self.cache[key]
        return count





# m = Machine(contents[0])
# print(m.actions)
# for c in range(1,15):
    # for action_seq in m.generate_action_seqs(c):
        # # print(action_seq)
        # m.do_action_seq(action_seq)
# # print(m.cache)
# print(m.dead_ends)


m = Machine(contents[0])
print(m.actions)





# ans = []
# for line in contents:

    # print()
    # print(line)
    # m = Machine(line)
    # ans.append(m.find_min_button_presses())


# print(sum(ans))

