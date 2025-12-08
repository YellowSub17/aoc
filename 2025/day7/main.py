
#18:08
#p1: 19:06

import numpy as np
import matplotlib.pyplot as plt
import time



with open('./input.test3') as f:
    contents = f.read().split('\n')[:-1]
rows = []
for row in contents:
    rows.append(list(row))

char_arr = np.array(rows)
char_arr[np.where(char_arr=='S')] = '|'






#           0 for rhs processing, 1 for lhs processing, 2 for complete tree 
#               |
#               |   number of terminations from the branch
#               |       |
## (r,c) : [visits, count]

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




    def multiverse_step(self):

        self.i_row +=1


        i_col = int(np.where(self.char_arr[self.i_row-1]=='|')[0][0])


        while self.char_arr[self.i_row, i_col] == '.':
            self.char_arr[self.i_row, i_col] = '|'
            self.i_row+=1


            if self.i_row >= self.nrows:
                last_split = self.last_splits[-1]
                splits_cache[last_split][0] +=1
                splits_cache[last_split][1] +=1

                return None


        self.last_splits.append( (self.i_row, i_col) )

        if (self.i_row, i_col) not in splits_cache:
            splits_cache[(self.i_row, i_col)] = [0,0]




        if splits_cache[(self.i_row, i_col)][0]==1:
            splits_cache[(self.i_row, i_col)][0] += 1


        elif splits_cache[(self.i_row, i_col)][0]==2:

            # self.char_arr[self.i_row, i_col] = '*'
            print(f'Cool! you found the node {(self.i_row, i_col)} where we are about to repeat the calculation')
            # print(f'This node has {splits_cache[(self.i_row, i_col)][1]} ends below it')
            add_amount = splits_cache[(self.i_row, i_col)][1]
            for split in self.last_splits:
                splits_cache[split][1] += add_amount

            print(splits_cache)

            return -1



        new_char_arrL = np.copy(self.char_arr)
        new_char_arrR = np.copy(self.char_arr)

        new_char_arrL[self.i_row, i_col-1] = '|'
        new_char_arrR[self.i_row, i_col+1] = '|'


        return [
                Sim(new_char_arrL, i_row=self.i_row, split_count = self.split_count, last_splits = list(self.last_splits)),
                Sim(new_char_arrR, i_row=self.i_row, split_count = self.split_count, last_splits = list(self.last_splits)),
                ]




    def __str__(self):
        s = ''
        s+= f'STEP: {self.i_row} \t SPLITS: {self.last_splits}\n'
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


finished_count = 0
split_count = 0

init_s = Sim(char_arr)


# x = init_s.multiverse_step()[-1] \
            # .multiverse_step()[-1]\
            # .multiverse_step()[-1]\
            # .multiverse_step()[-1]\
            # .multiverse_step()[-1]\
            # .multiverse_step()[-1]\
            # .multiverse_step()[-1]
            # # .multiverse_step()
# print(x)





# exit()

universes = init_s.multiverse_step()




t1 = time.time()



while len(universes)>0:
    print()
    print()
    print()
    print('-----------')


    this_uni = universes.pop(-1)

    print(this_uni)



    next_unis = this_uni.multiverse_step()

    if next_unis is None:


        for i_split, split in enumerate(this_uni.last_splits):
            this_uni.char_arr[split[0], split[1]] = f'{i_split}'
            # splits_cache[split][1]+=1

        for split, (visits, n) in splits_cache.items():
            if visits==2:
                this_uni.char_arr[split[0], split[1]] = f'*'

        print(this_uni)
        print('Hit rock bottom')



        for i_split, split in enumerate(this_uni.last_splits):
            print(i_split, split, splits_cache[split])
        print(splits_cache)
        # print(f'Visited this split {splits_cache[last_split][0]} times.')
        # print(f'This branch terminates {splits_cache[last_split][1]} times.')
        # time.sleep(0.01)

    elif type(next_unis) == int:

        print(this_uni)
        for i_split, split in enumerate(this_uni.last_splits):
            print(i_split, split, splits_cache[split])
        print(splits_cache)
        # print(f'Visited this split {splits_cache[last_split][0]} times.')
        # print(f'This branch terminates {splits_cache[last_split][1]} times.')
        print('-----------')
        print()
        print()
        print()
        print('-----------')
        continue

    else:
        universes += next_unis








t2 = time.time()
print(t2-t1)

print(finished_count)







