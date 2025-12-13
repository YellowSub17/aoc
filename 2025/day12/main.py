

##13:20
##13:27t



import numpy as np



with open('./input.prod') as f:
    contents = f.read().split('\n')[:-1]



n_blocks = np.array([7,7,6,7,5,7])


lines = contents[30:]

print(lines[:10])

count =0

for line in lines:
    sp = line.split(' ')


    l, w = int(sp[0].split('x')[0]), int(sp[0].split('x')[1][:-1])
    area = l*w

    npresents = list(map(int, sp[1:]))

    print(area, sum(n_blocks*npresents))

    if area> sum(npresents*n_blocks):
        count +=1

print(count)

    # print(line)
    # print(l, w)


