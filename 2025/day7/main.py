
#18:08
#p1: 19:06

import numpy as np
import matplotlib.pyplot as plt
import time



with open('./input.test2') as f:
    contents = f.read().split('\n')[:-1]
rows = []
for row in contents:
    rows.append(list(row))

char_arr = np.array(rows)
char_arr[np.where(char_arr=='S')] = '|'

# int_arr = np.zeros(char_arr.shape)
# int_arr[np.where(char_arr=='S')] =1
# int_arr[np.where(char_arr=='^')] =1

# plt.figure()
# plt.imshow(int_arr)
# plt.figure()
# plt.plot(int_arr.sum(axis=1))
# plt.show()



splits_cache = {}




class Sim:

    def __init__(self, char_arr, i_row=0, split_count=0, last_splits = [] ):
        self.char_arr = char_arr

        self.nrows = self.char_arr.shape[0]
        self.ncols = self.char_arr.shape[1]

        self.i_row = i_row
        self.split_count = split_count
        self.last_splits = last_splits




    def step(self):
        self.i_row +=1
        new_row = self.char_arr[self.i_row, :]

        for i_col in range(1, self.ncols-1):
            if self.char_arr[self.i_row, i_col] =='.':
                if self.char_arr[self.i_row-1, i_col] == '|':
                    new_row[i_col] = '|'

            if self.char_arr[self.i_row, i_col] =='^':

                if self.char_arr[self.i_row-1, i_col] == '|':
                    self.split_count +=1
                    new_row[i_col-1] = '|'
                    new_row[i_col+1] = '|'

        self.char_arr[self.i_row] = new_row




    def multiverse_step(self, last_split):

        self.i_row +=1


        i_col = np.where(self.char_arr[self.i_row-1]=='|')[0][0]


        while self.char_arr[self.i_row, i_col] == '.':
            self.char_arr[self.i_row, i_col] == '|'
            self.i_row+=1


            if self.i_row >= self.nrows:
                return 1, last_split







        # if self.char_arr[self.i_row, i_col] =='.':

            # new_char_arr = np.copy(self.char_arr)

            # new_char_arr[self.i_row, i_col] = '|'

            # return [Sim(new_char_arr, i_row=self.i_row, split_count = self.split_count)], last_split

        # if self.char_arr[self.i_row, i_col] =='^':



            # if (self.i_row, i_col) in splits_cache:
                # return splits_cache[(self.i_row, i_col)

        new_char_arrL = np.copy(self.char_arr)
        new_char_arrR = np.copy(self.char_arr)

        new_char_arrL[self.i_row, i_col-1] = '|'
        new_char_arrR[self.i_row, i_col+1] = '|'


        return [
                Sim(new_char_arrL, i_row=self.i_row, split_count = self.split_count),
                Sim(new_char_arrR, i_row=self.i_row, split_count = self.split_count),
                ], (self.i_row, i_col)

        # return 1, last_split



    def __str__(self):
        s = ''
        s+= f'STEP: {self.i_row} \t SPLITS: {self.split_count}\n'
        for row in self.char_arr:
            for val in row:
                s+= val

            s+='\n'
        return s










# s = Sim(char_arr)

# for _ in range(s.nrows-1):
    # print('\n'*25, s)
    # s.step()
    # time.sleep(0.1)

# print(s.split_count)


last_split = (-1,-1)
finished_count = 0
split_count = 0

init_s = Sim(char_arr)

universes, (last_split) = init_s.multiverse_step(last_split)




t1 = time.time()


while len(universes)>0:
    # breakpoint()
    # if finished_count>8:
        # break
    # print(len(universes))

    this_uni = universes.pop(-1)
    # print('\n'*25, this_uni)


    next_unis, (last_split) = this_uni.multiverse_step(last_split)

    if type(next_unis) == int:
        finished_count += next_unis
        print(this_uni)
        # time.sleep(0.01)
    else:
        universes += next_unis

t2 = time.time()
print(t2-t1)

print(finished_count)














# # for _ in range(s.nrows-1):
    # # print('\n'*25, s)
    # # s = s.multiverse_step()[0]
    # # time.sleep(0.1)


# # print(s.multiverse_step()[0].multiverse_step()[1].multiverse_step()[0].multiverse_step()[0])


# ## 3236 too low
# ## 1170769 too low 






