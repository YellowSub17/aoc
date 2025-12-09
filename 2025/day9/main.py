
import numpy as np
import itertools

fname = './input.prod'



def find_area(p1, p2):

    xmin = min(p1[0], p2[0])
    xmax = max(p1[0], p2[0])

    ymin = min(p1[1], p2[1])
    ymax = max(p1[1], p2[1])

    x = xmax-xmin +1
    y = ymax-ymin +1

    return x*y


points = np.loadtxt(fname, delimiter=',')
# print(points)

points = points[points[:, 1].argsort()]
points = points[points[:, 0].argsort()]
# print(points)

pairs = itertools.combinations(points, 2)



print('#####')

current_max = 0

for p1, p2 in pairs:

    # x = np.abs(p2[0]+1-p1[0])
    # y = np.abs(p2[1]+1-p1[1])
    # area = x*y
    # print(x, y, p1, p2, area)

    area = find_area(p1,p2)
    # print(p1, p2, area)

    if current_max<area:
        current_max = area


print(f'{current_max=}')








