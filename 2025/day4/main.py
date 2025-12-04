


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




neig_dirs = [
        (1,0), (-1,0), (0,1), (0, -1),
        (1,1), (-1,-1), (1,-1), (-1,1)
        ]

def can_be_removed(c, r, arr):
    neig_count = 0
    for neig_dir in neig_dirs:
        neig_c = c+neig_dir[0]
        neig_r = r+neig_dir[1]

        if neig_c>= arr.shape[1] or neig_c<0:
            continue

        if neig_r>= arr.shape[0] or neig_r <0:
            continue


        neig_count += arr[neig_r,neig_c]

    return  neig_count < 4



# part1_ans = 0
# marked = np.zeros(arr.shape)

# for c,r in zip(rolls_c, rolls_r):
    # if can_be_removed(c,r, arr):
        # part1_ans+=1
        # marked[r,c] = 1
# print(part1_ans)
# print(marked)





part2_ans = 0
arr = np.array(arr)
rolls_r, rolls_c = np.where(arr==1)

rolls_r_len = len(rolls_r)

while True:
    marked = np.zeros(arr.shape)
    for c,r in zip(rolls_c, rolls_r):
        if can_be_removed(c,r, arr):
            part2_ans+=1
            marked[r,c] = 1

    arr[marked==1] = 0

    rolls_r, rolls_c = np.where(arr==1)

    if len(rolls_r) == rolls_r_len:
        break
    else:
        rolls_r_len = len(rolls_r)


print(part2_ans)










