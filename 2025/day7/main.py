
#18:08
#p1: 19:06

import numpy as np
import matplotlib.pyplot as plt
import time



with open('./input.test') as f:
    contents = f.read().split('\n')[:-1]
rows = []
for row in contents:
    rows.append(list(row))

char_arr = np.array(rows)

int_arr = np.zeros(char_arr.shape)
int_arr[np.where(char_arr=='S')] =1
int_arr[np.where(char_arr=='^')] =1

# plt.figure()
# plt.imshow(int_arr)
# plt.figure()
# plt.plot(int_arr.sum(axis=1))
# plt.show()








class Sim:

    def __init__(self, char_arr, i_row=0, split_count=0):
        self.char_arr = char_arr

        self.nrows = self.char_arr.shape[0]
        self.ncols = self.char_arr.shape[1]

        self.i_row = i_row
        self.split_count = split_count




    def step(self):
        self.i_row +=1
        new_row = self.char_arr[self.i_row, :]

        for i_col in range(1, self.ncols-1):
            if self.char_arr[self.i_row, i_col] =='.':
                if self.char_arr[self.i_row-1, i_col] == 'S' or self.char_arr[self.i_row-1, i_col] == '|':
                    new_row[i_col] = '|'

            if self.char_arr[self.i_row, i_col] =='^':

                if self.char_arr[self.i_row-1, i_col] == '|':
                    self.split_count +=1
                    new_row[i_col-1] = '|'
                    new_row[i_col+1] = '|'

        self.char_arr[self.i_row] = new_row



    def multiverse_step(self):

        self.i_row +=1
        # new_rowL = self.char_arr[self.i_row, :]
        # new_rowR = self.char_arr[self.i_row, :]
        if self.i_row >= self.nrows:
            return None

        for i_col in range(1, self.ncols-1):

            if self.char_arr[self.i_row, i_col] =='.':
                if self.char_arr[self.i_row-1, i_col] == 'S' or self.char_arr[self.i_row-1, i_col] == '|':
                    new_char_arr = np.copy(self.char_arr)

                    new_char_arr[self.i_row, i_col] = '|'

                    return [Sim(new_char_arr, i_row=self.i_row, split_count = self.split_count)]

            if self.char_arr[self.i_row, i_col] =='^':
                if self.char_arr[self.i_row-1, i_col] == '|':

                    new_char_arrL = np.copy(self.char_arr)
                    new_char_arrR = np.copy(self.char_arr)

                    self.split_count +=1
                    new_char_arrL[self.i_row, i_col-1] = '|'
                    new_char_arrR[self.i_row, i_col+1] = '|'

                    return [
                            Sim(new_char_arrL, i_row=self.i_row, split_count = self.split_count),
                            Sim(new_char_arrR, i_row=self.i_row, split_count = self.split_count),
                            ]



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


init_s = Sim(char_arr)

universes = init_s.multiverse_step()
finished_count = 0




while len(universes)>0:
    # print(len(universes))

    this_uni = universes.pop(-1)
    # print('\n'*25, this_uni)
    # time.sleep(0.05)


    next_unis = this_uni.multiverse_step()

    if next_unis is None:
        finished_count +=1
        print(this_uni)
    else:
        universes += next_unis

print(finished_count)











# for _ in range(s.nrows-1):
    # print('\n'*25, s)
    # s = s.multiverse_step()[0]
    # time.sleep(0.1)


# print(s.multiverse_step()[0].multiverse_step()[1].multiverse_step()[0].multiverse_step()[0])


## 3236 too low
## 1170769 too low 






