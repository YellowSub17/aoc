

import numpy as np


with open('./input.prod', 'r') as f:
    cont = f.read().split('\n')[:-1]


ws = np.array( [list(line) for line in cont])

NROWS, NCOLS = ws.shape

print('\t[ ', end='')
for i in range(NCOLS):
    print(f'{i}   ', end='')
print(']c')

print('r')

for j, line in enumerate(ws):
    print(f'{j}\t{line}')

ws[ws=='X'] = 0
ws[ws=='M'] = 1
ws[ws=='A'] = 2
ws[ws=='S'] = 3
ws[ws=='.'] = 9
ws = ws.astype(int)

print(f'{NROWS=},{NCOLS=} ')




def search_S(r,c):
    # sli = ws[c:c+4, r]
    sli = ws[r:r+4, c]
    if len(sli) <4:
        return 0
    if np.all(sli == [0,1,2,3]):
        return 1
    else:
        return 0



def search_N(r,c):
    # sli = ws[c-3:c+1, r]
    sli = ws[r-3:r+1, c]
    if len(sli) <4:
        return 0
    if np.all(sli == [3,2,1,0]):
        return 1
    else:
        return 0




def search_E(r,c):
    # sli = ws[c, r:r+4]
    sli = ws[r, c:c+4]
    if len(sli) <4:
        return 0
    if np.all(sli == [0,1,2,3]):
        return 1
    else:
        return 0



def search_W(r,c):
    # sli = ws[c, r-3:r+1]
    sli = ws[r, c-3:c+1]
    if len(sli) <4:
        return 0
    if np.all(sli == [3,2,1,0]):
        return 1
    else:
        return 0



def search_NW(r,c):
    if r <= 2 or c <= 2:
        return 0

    MAS = ws[r-1, c-1], ws[r-2, c-2], ws[r-3,c-3]

    if MAS == (1,2,3):
        return 1
    else:
        return 0


def search_SE(r,c):
    if r >= NROWS -3 or c >= NCOLS-3:
        return 0

    MAS = ws[r+1, c+1], ws[r+2, c+2], ws[r+3,c+3]

    # print(MAS)

    if MAS == (1,2,3):
        return 1
    else:
        return 0



def search_NE(r,c):
    if r <= 2 or c >= NCOLS -3:
        return 0
    MAS = ws[r-1, c+1], ws[r-2, c+2], ws[r-3,c+3]

    if MAS == (1,2,3):
        return 1
    else:
        return 0

def search_SW(r,c):
    if c <= 2 or r >= NROWS-3:
        return 0

    MAS = ws[r+1, c-1], ws[r+2, c-2], ws[r+3,c-3]

    if MAS == (1,2,3):
        return 1
    else:
        return 0


def search_cross(r,c):

    #mm sm ss ms
    #ss sm mm ms

    if r==0 or r==NROWS-1 or c==0 or c==NCOLS-1:
        return 0

    print(r,c)
    NW, NE, SE, SW= ws[r-1,c-1], ws[r-1,c+1], ws[r+1,c+1], ws[r+1,c-1]

    if 0 in [NW, NE, SE, SW] or 2 in [NW, NE, SE, SW]: # X or A
        return 0

    if NW != SE and SW != NE:
        return 1

    return 0






def search_all(r,c):
    found = 0
    for fn in [search_N, search_S, search_E, search_W, search_NE, search_SE, search_NW, search_SW]:
        found += fn(r,c)

    return found




X_loc = np.where(ws==0)
founds = map(search_all, X_loc[0], X_loc[1])
print(sum(founds))


A_loc = np.where(ws==2)
founds = map(search_cross, A_loc[0], A_loc[1])
print(sum(founds))





