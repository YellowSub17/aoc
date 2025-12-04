


import numpy as np



arr = []

with open('./input.prod') as f:
    contents = f.read().split('\n')[:-1]
    for line in contents:
        line1s = line.replace('@', '1')
        line0s = line1s.replace('.', '0')
        row = list(map(int, line0s))
        arr.append(row)



arr = np.array(arr)
rolls_r, rolls_c = np.where(arr==1)


# for x,y in zip(rolls_x, rolls_y):
    # print(x,y)









neig_dirs = [
        (1,0), (-1,0), (0,1), (0, -1),
        (1,1), (-1,-1), (1,-1), (-1,1)
        ]

def can_be_removed(c, r, arr):
    # print(f'{c=}, {r=}, {arr[r,c]=}')
    neig_count = 0
    for neig_dir in neig_dirs:
        neig_c = c+neig_dir[0]
        neig_r = r+neig_dir[1]
        # print('\t', neig_dir, (neig_r, neig_c))

        if neig_c>= arr.shape[1] or neig_c<0:
            # print('\tc oob')
            continue

        if neig_r>= arr.shape[0] or neig_r <0:
            # print('\tr oob')
            continue

        # print(f'\t\t{arr[neig_r, neig_c]}')

        neig_count += arr[neig_r,neig_c]

    # print(neig_count< 4)
    return  neig_count < 4



part1_ans = 0

check = np.zeros(arr.shape)
for c,r in zip(rolls_c, rolls_r):
    if can_be_removed(c,r, arr):
        ans+=1
        check[c,r] = 1


# print(check)
print(ans)






